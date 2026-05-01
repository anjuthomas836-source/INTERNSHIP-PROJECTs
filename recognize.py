import cv2
import pandas as pd
from datetime import datetime

def mark_attendance(name):
    file = "attendance.csv"

    try:
        df = pd.read_csv(file)
    except:
        df = pd.DataFrame(columns=["Name", "Time", "Date"])

    # Avoid duplicate
    if name in df["Name"].values:
        return

    now = datetime.now()
    new_row = {
        "Name": name,
        "Time": now.strftime("%H:%M:%S"),
        "Date": now.strftime("%Y-%m-%d")
    }

    df = df.append(new_row, ignore_index=True)
    df.to_csv(file, index=False)


def recognize_faces(label_map):
    model = cv2.face.LBPHFaceRecognizer_create()
    model.read("model/face_model.xml")

    cam = cv2.VideoCapture(0)

    while True:
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        label, confidence = model.predict(gray)

        if confidence < 100:
            name = label_map[label]
            mark_attendance(name)

            cv2.putText(frame, name, (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Attendance", frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
    
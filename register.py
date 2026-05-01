import cv2
import os

def capture_images(name):
    path = f"dataset/{name}"
    os.makedirs(path, exist_ok=True)

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cam.isOpened():
        print("❌ Camera not opening. Try index 1 or check webcam.")
        return

    detector = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    count = 0
    MAX_IMAGES = 5

    while True:
        ret, frame = cam.read()
        if not ret:
            print("❌ Failed to read frame")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            if count < MAX_IMAGES:
                count += 1
                face = gray[y:y+h, x:x+w]
                cv2.imwrite(f"{path}/{count}.jpg", face)

        cv2.imshow("Capture", frame)

        if count >= MAX_IMAGES:
            break

        if cv2.waitKey(1) == 27:
            break

    cam.release()
    cv2.destroyAllWindows()
    print("✅ Done capturing images")


if __name__ == "__main__":
    name = input("Enter student name: ")
    capture_images(name)
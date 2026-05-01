import streamlit as st
from register import capture_images
from train import train_model
from recognize import recognize_faces
import pandas as pd

st.title("📷 Face Detection Attendance System")

menu = ["Register Face", "Train Model", "Take Attendance", "View Report"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Register Face":
    name = st.text_input("Enter Student Name")

    if st.button("Capture Images"):
        capture_images(name)
        st.success("Images captured!")

elif choice == "Train Model":
    if st.button("Train"):
        label_map = train_model()
        st.success("Model trained!")

elif choice == "Take Attendance":
    if st.button("Start Camera"):
        label_map = train_model()
        recognize_faces(label_map)

elif choice == "View Report":
    try:
        df = pd.read_csv("attendance.csv")
        st.dataframe(df)
    except:
        st.warning("No attendance yet!")
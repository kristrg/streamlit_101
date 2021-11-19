import streamlit as st
import pandas as pd
import cv2

st.header("First WebApp MDFK")
st.write("Hello world yoooooo!")

menu = ["Home", "About Us", "Read Data", "Camera"]

choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.image("media/dog-beach-lifesaver.png")

    col1, col2 = st.columns(2)

    with col1:
        dog_name = st.text_input("What is your dog name?")
        st.write("Your dog name:", dog_name)

    with col2:
        dog_age = st.slider("Your dog age?", min_value = 1, max_value=100)
        st.write("Your dog age:", dog_age)

    st.image("media/isle_of_dog.gif")
    
    
elif choice == "Read Data":
    st.header("My table")
    st.write("haha")
    df = pd.read_csv("media/AB_NYC_2019.csv")
    st.dataframe(df)

elif choice == "About Us":
    st.audio("media/Loi_nho.mp3")
    st.video("media/dogs.mp4")
    fileUp = st.file_uploader("Upload file", type = ["jpg","png","jpeg"])
    st.image(fileUp)

elif choice == "Camera":
    st.title('Open your webcam')
    st.warning('Webcam show on local computer ONLY')
    show = st.checkbox('Show!')
    FRAME_WINDOW = st.image([])
    camera = cv2.VideoCapture(0) # device 1/2

    while show:
        _, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)
    else:
        camera.release()

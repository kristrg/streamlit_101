import streamlit as st
import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf

menu = ['Capture from webcam','Upload from computer']

choice = st.sidebar.selectbox('Please choose your uploaded options', menu)


#Load your model and check create the class_names list
Model_Path = 'Saved_model_Xception'
class_names = ["1,000","10,000","100,000","2,000","20,000","200,000","5,000","50,000","500,000"]
model = tf.keras.models.load_model(Model_Path)


if choice == 'Capture from webcam':
    st.title('Capture photo from your webcam')
    cap = cv2.VideoCapture(0)  # device 0
    run = st.checkbox('Show Webcam')
    capture_button = st.checkbox('Capture')

    captured_image = np.array(None)


    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    FRAME_WINDOW = st.image([])
    while run:
        ret, frame = cap.read()        
        # Display Webcam
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB ) #Convert color
        FRAME_WINDOW.image(frame)

        if capture_button:      
            captured_image = frame
            break

    cap.release()

    if  captured_image.all() != None:
        st.image(captured_image)
        st.success('Image is captured')

        #Resize the Image according with your model
        captured_image = cv2.resize(captured_image,(299,299),interpolation = cv2.INTER_AREA)
        #Expand dim to make sure your img_array is (1, Height, Width , Channel ) before plugging into the model
        img_array  = np.expand_dims(captured_image, axis=0)
        #Check the img_array here
        #st.write(img_array)

        prediction = model.predict(img_array)
        a = np.argmax(prediction,axis=1)
        result = class_names[int(a)]
        if a>=0.5:
            st.write("The prediction is: ",result)
            st.write(prediction)
        else:
            st.write("Please try again")
        
        # Preprocess your prediction , How are we going to get the label name out from the prediction
        # Now it's your turn to solve the rest of the code
if choice == "Upload from computer":
    st.title("Upload your own photo")
    photo_uploaded = st.file_uploader('Upload your photo here', ['png', 'jpeg', 'jpg'])
    if photo_uploaded!=None:
        file_details = {"FileName":photo_uploaded.name,"FileType":photo_uploaded.type}
        # st.write(file_details)
        st.success("Photo uploaded")
        image_np = np.asarray(bytearray(photo_uploaded.read()), dtype=np.uint8)
        image = cv2.imdecode(image_np, 1)
        st.image(image, channels='BGR')

        # st.write(photo_uploaded.size)
        # st.write(photo_uploaded.type)

        #Resize the Image according with your model
        image = cv2.resize(image,(299,299),interpolation = cv2.INTER_AREA)
        #Expand dim to make sure your img_array is (1, Height, Width , Channel ) before plugging into the model
        img_array  = np.expand_dims(image, axis=0)
        #Check the img_array here
        #st.write(img_array)
        if(st.button("Predict")):
            prediction = model.predict(img_array)
            a = np.argmax(prediction,axis=1)
            result = class_names[int(a)]
            if a>=0.5:
                st.write("The prediction is: ",result)
                st.write(prediction)
                st.write("Is it correct?")
                if st.checkbox("Yes"):
                    st.text("Thank you!")
                elif st.checkbox("Nope"):
                    user_label = st.selectbox("Correct label: ",class_names)
                    st.write("Thank you! We recorded your label: ",user_label)
            else:
                st.write("Please try again")

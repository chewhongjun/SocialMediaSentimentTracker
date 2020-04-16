import streamlit as st

#General displaying
st.title("streamlit tutorials")

st.header("This is a header")

st.subheader("this is a subheader")

st.text("Hello streamlit")

st.markdown("### this is a markdown")

st.success("successful")

st.info("information")

st.warning("This is a warning")

st.error("This is a error danger")

st.exception("NameError('name three is not defined')")

#get help info about python
st.help(range)

#Writing text
st.write("text with write")

st.write(range(10))

#Images
from PIL import Image
img = Image.open("download.png")
st.image(img, width=300,caption="Simple Image")

#Videos
vid_file = open("1280.mp4","rb").read()
st.video(vid_file)

#Audio
# audio_file = open("example.mp3","rb").read()
# st.audio(audio_file,format='audio/mp3')

#Widges

#checkboxes
if st.checkbox("Show/Hide"):
    st.text("showing or hiding widget")

#radio button
status = st.radio("What is your status",("Active","Inactive","hungry"))
if status == "hungry":
    st.success("You want sushi?")

else:
    st.warning("Not Hungry")

#SelectBox
occupation = st.selectbox("Your Occupation", ["Programmer","Data Scientist","Student"])
st.write("You have selected",occupation)

#MultiSelect
location = st.multiselect("Where do you want to work",["London","New York","Singapore","Hong Kong","Canada"])
st.write(location)
st.write("You have selected",len(location),"locations")

#Slider
level = st.slider("Whats you level",1,5)
st.write("You're at",level)

#Button
st.button("Simple Button")

if st.button("About"):
    st.text("Streamlit is cool")

#Text
firstname = st.text_input("Enter Your Firstname","Type here..")
if st.button("submit"):
    result = firstname.title()
    st.success(result)
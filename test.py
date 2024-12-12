import streamlit as st

left, right = st.columns(2)

with left:
    st.write("hallo")

with right:
    st.write("hii")

left, right = st.columns(2)

with left:
    st.title("hallo")

with right:
    st.title("hii")

left, right = st.columns(2)

with left:
    st.header("hallo")

with right:
    st.header("hii")

left, right = st.columns(2)

with left:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQr34neQZPaKQ13Gt9Cpobht_C07qttsJOtWw&s")

with right:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSkGGYkd6sRsHNOMvn3NpC1LQf1sjFjuGZLXw&s")

left, right = st.columns(2)

with left:
    st.video("https://www.youtube.com/watch?v=3MT5Yy6VvHU")

with right:
    st.video("https://www.youtube.com/watch?v=pxmy0nAzSiE")

left, right = st.columns(2)

left.header("Neu Links")
right.header("Neu Rechts")






st.title("Positives Hallo" , anchor=False)
st.header("Smoll", anchor=False, divider="violet")
st.subheader("Smoller" , anchor=False, divider="violet")
st.write("Hallo!!")
st.image("https://cdn.britannica.com/42/233842-050-E64243D7/Pomeranian-dog.jpg")
st.video("https://www.youtube.com/watch?v=AaKcpaVGCjQ")

st.title("Noch mehr positives Hallo" , anchor=False)
st.header("Small", anchor=False, divider="green")
st.subheader("Smaller" , anchor=False, divider="green")
st.write("Hii!!")
st.image("https://media.tenor.com/G0OBtQPRa40AAAAM/cat-funny-looking-camera-cat-smurf.gif")
st.video("https://www.youtube.com/watch?v=HMTKMWHLbdQ")

st.title("Playful hallo" , anchor=False)
st.header("Tiny", anchor=False, divider="rainbow")
st.subheader("very tiny" , anchor=False, divider="rainbow")
st.write("yoo!!")
st.image("https://i.redd.it/sjusjrmpazh81.jpg")
st.video("https://www.youtube.com/watch?v=kG7d_4LeP48")

st.title("Espanol Hallo" , anchor=False)
st.header("Pocketsize", anchor=False, divider="blue")
st.subheader("even smaller" , anchor=False, divider="blue")
st.write("Hola!!")
st.image("https://i.pinimg.com/564x/98/a0/9e/98a09ed13b0640a10d9fba126208864a.jpg")
st.video("https://www.youtube.com/watch?v=SMoXHjVBJ4c")

st.title("Lmfao" , anchor=False)
st.header("Lmfao", anchor=False, divider="red")
st.subheader("Lmfao" , anchor=False, divider="red")
st.write("Lmfao")
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqwcs5BJsHGEx8_6WAMCZXvU5OYZ4qq5rquQ&s")
st.video("https://www.youtube.com/watch?v=gPHAZlKW3zw")
from pathlib import WindowsPath
import streamlit as st


name = st.sidebar.text_input("Enter your name", "")


job = st.sidebar.text_area("What do you do ?")

age = st.sidebar.number_input(
    "Enter a number value", min_value=0, max_value=100, step=1
)


is_available_for_work = st.sidebar.checkbox("Available for work")

threshold = st.sidebar.slider(
    "Pick a threshold", min_value=1.0, max_value=100.0, value=50.0, step=0.1
)


selected_element = st.sidebar.selectbox("Pick", ("item1", "item2", "item3"))


columns = st.beta_columns((2, 1))


with columns[0]:
    st.markdown(f"Name : {name}")
    st.markdown(f"Job : {job}")
    st.markdown(f"Age: {age}")

with columns[1]:
    st.markdown(f"Available for work : {is_available_for_work}")


st.markdown("---")

container = st.beta_container()


with container:
    st.markdown(
        "Deserunt ea commodo laboris do et duis consequat tempor qui sint deserunt dolor. Enim adipisicing amet et velit ullamco do non duis laborum Lorem anim irure. Aliqua aliqua veniam exercitation deserunt dolor irure reprehenderit adipisicing voluptate quis irure occaecat sit."
    )


expander = st.beta_expander("Learn more", expanded=True)

with expander:
    st.info("Some information here")
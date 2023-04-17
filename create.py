import streamlit as st
from database import add_data


def create():
    col1, col2 = st.columns(2)
    with col1:
        train_no = st.text_input("Train No:")
        train_name = st.text_input("Name:")
    with col2:
        train_type = st.text_input("Train_Type:")
        train_source = st.text_input("Source:")
    train_destination = st.text_input("Destination:")
    train_availability = st.text_input("Availability:")
    if st.button("Add Train"):
        add_data(train_no, train_name, train_type, train_source, train_destination,train_availability)
        st.success("Successfully added Train: {}".format(train_no))

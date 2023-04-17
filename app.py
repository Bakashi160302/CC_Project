# Importing pakages
import streamlit as st
import mysql.connector

from create import create
from database import create_table
from delete import delete
from read import read
from update import update

mydb = mysql.connector.connect(
    host="cc-project.cv2rz4kihl7u.us-east-1.rds.amazonaws.com",
    user="admin",
    password="password123",
    port = "3306",
    database="PES2UG20CS370_Train_Lab10"
)
c = mydb.cursor()

#c.execute("CREATE DATABASE PES2UG20CS370_Train_Lab10")


def main():
    st.title("Train App")
    menu = ["Add", "View", "Edit", "Remove"]
    choice = st.sidebar.selectbox("Menu", menu)

    create_table()
    if choice == "Add":
        st.subheader("Enter Train Details:")
        create()

    elif choice == "View":
        st.subheader("View created tasks")
        read()

    elif choice == "Edit":
        st.subheader("Update created tasks")
        update()

    elif choice == "Remove":
        st.subheader("Delete created tasks")
        delete()

    else:
        st.subheader("About tasks")


if __name__ == '__main__':
    main()

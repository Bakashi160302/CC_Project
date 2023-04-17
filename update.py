import datetime

import pandas as pd
import streamlit as st
from database import view_all_data, view_only_dealer_names, get_dealer, edit_dealer_data


def update():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['train_no', 'train_name', 'train_type', 'train_source', 'train_destination','train_availability'])
    with st.expander("Current Trains"):
        st.dataframe(df)
    list_of_dealers = [i[0] for i in view_only_dealer_names()]
    selected_dealer = st.selectbox("Train to Edit", list_of_dealers)
    selected_result = get_dealer(selected_dealer)
    # st.write(selected_result)
    if selected_result:
        train_no = selected_result[0][0]
        train_name = selected_result[0][1]
        train_type = selected_result[0][2]
        train_source = selected_result[0][3]
        train_destination = selected_result[0][4]
        train_availability = selected_result[0][5]

        # Layout of Create

        col1, col2, col3 = st.columns(3)
        with col1:
            new_train_no = st.text_input("No:", train_no)
            new_train_name = st.text_input("Name:", train_name)
        with col2:
            new_train_type = st.selectbox("train_source",train_type)
            new_train_source = st.text_input("Train Source:", train_source)
        with col3:
            new_train_destination = st.text_input("Train Destination:", train_destination)
            new_train_availability = st.text_input("Train Availability",train_availability)
        if st.button("Update Train"):
            edit_dealer_data(new_train_no, new_train_name, new_train_type, new_train_source, new_train_destination,new_train_availability, train_no, train_name, train_type, train_source, train_destination,train_availability)
            st.success("Successfully updated:: {} to ::{}".format(train_name, new_train_name))

    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=['train_no', 'train_name', 'train_type', 'train_source',' train_destination','train_availability'])
    with st.expander("Updated data"):
        st.dataframe(df2)

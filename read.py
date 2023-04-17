import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_all_data


def read():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['train_no', 'train_name', 'train_type', 'train_source', 'train_destination','train_availability'])
    with st.expander("View all Trains"):
        st.dataframe(df)
    with st.expander("Train Location"):
        task_df = df['train_source'].value_counts().to_frame()
        task_df = task_df.reset_index()
        st.dataframe(task_df)
        p1 = px.pie(task_df, names='index', values='train_source')
        st.plotly_chart(p1)
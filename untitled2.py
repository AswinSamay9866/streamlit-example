import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

st.set_page_config(page_title = "Sales Dashboard", page_icon=":cake:", layout="wide")

file = pd.read_excel(r"D:\Masala Box\TABLES\Report_June 13.xlsx", sheet_name =['Master_table','Details table'])
master = file.get('Master_table')
details = file.get('Details table')
test = master.astype(str)
st.dataframe(test)
st.sidebar.header("Please Filter Here:")
city = st.sidebar.multiselect(
    "Select the City:",
    options=master["city"].unique(),
    default=master["city"].unique()
)

Order_status = st.sidebar.multiselect(
    "Select order_status:",
    options=master["status"].unique(),
    default=master["status"].unique(),
)
comment='''Create start and end date for filter'''

start_date=master['Invoice_Date_'].iloc[0]
end_date=master['Invoice_Date_'].iloc[len(master['Invoice_Date_'])-1]
start_date = st.sidebar.date_input('Start date', start_date)
end_date = st.sidebar.date_input('End date', end_date)
if start_date < end_date:
    st.sidebar.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
else:
    st.sidebar.error('Error: End date must fall after start date.')
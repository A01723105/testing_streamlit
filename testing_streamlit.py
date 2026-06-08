import streamlit as st     
import pandas as pd        
df = pd.read_excel("sellers.xlsx")

# display the table by region
st.header("table by region :")

regions = ["All"] + list(df["REGION"].unique())
region = st.selectbox("Choose a region:", regions)

if region == "All":
    table = df
else:
    table = df[df["REGION"] == region]

st.dataframe(table)

# displays the 3 graphs in bar charts
st.header("the 3 graphs : ")

data = table.set_index("NAME")

st.subheader("Units Sold")
st.bar_chart(data["SOLD UNITS"])

st.subheader("Total Sales")
st.bar_chart(data["TOTAL SALES"])

st.subheader("Average Sales")
st.bar_chart(data["SALES AVERAGE"])

# displays the data for a specific vendor
st.header("Data Display for Specific Vendor")

vendor = st.selectbox("Choose a vendor:", df["NAME"].unique())
vendor_data = df[df["NAME"] == vendor]
st.dataframe(vendor_data)
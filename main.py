import pandas as pd
import streamlit as st

#read csv file
data = pd.read_csv("car_data.csv")

# store our input results from the user (with defualt values)
filters = {
    'Car_Name': '',
    'Transmission': ['Automatic', 'Manual'],
    'selling_price': [0.0, data['Selling_Price'].max()],
    'year': [2000, 2024]
}

#sidebar
with st.sidebar:
    #a. text box (st.text_input) to input the car_name (optional)
    car_name_filter = st.text_input("Car Name (optional)")
    filters['Car_Name'] = car_name_filter
    #b. multiselect (st.multiselect) to choose between Manual and/or Automatic (default option is both)
    transmission_filter = st.multiselect("Transmission", options=data['Transmission'].unique(), default=filters['Transmission'])
    filters['Transmission'] = transmission_filter
    #c. slider (st.slider) to choose a range of selling_price (default: 0 to 20)
    selling_price_filter = st.slider("Selling Price Range", min_value=0.0, max_value=20.0, value=filters['selling_price'], format="%d")
    filters['selling_price'] = selling_price_filter
    #d. slider (st.slider) to choose a range of year (default: 2000 to 2024)
    year_filter = st.slider("Year Range", min_value=2000, max_value=2024, value=filters['year'], format="%d")
    filters['year'] = year_filter
    #e. submit button (st.button)
    st.button("Apply Filters")

# we filter our cars dataset with the corresponding filter values from "filters" object
filtered_data = data.loc[
    data['Car_Name'].str.contains(filters['Car_Name'], case=False) &
    data['Transmission'].isin(filters['Transmission']) &
    (data['Selling_Price'] >= filters['selling_price'][0]) & (data['Selling_Price'] <= filters['selling_price'][1]) &
    (data['Year'] >= filters['year'][0]) & (data['Year'] <= filters['year'][1])
]


st.header("Filtered Cars")
if filtered_data.empty:
    st.write("No cars match the current filters.")
else:
    # show dataframe onto page
    st.dataframe(filtered_data)

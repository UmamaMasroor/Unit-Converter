import streamlit as st

def length_converter(value, from_unit, to_unit):
    conversion_factors = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Miles": 0.000621371,
        "Feet": 3.28084
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    return value

st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")
st.title("🔄 Unit Converter App")

category = st.selectbox("Choose a category:", ["Length", "Temperature"])

if category == "Length":
    st.subheader("Length Converter")
    length_units = ["Meters", "Kilometers", "Miles", "Feet"]
    value = st.number_input("Enter the value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit:", length_units)
    to_unit = st.selectbox("To Unit:", length_units)
    if st.button("Convert"):
        result = length_converter(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Temperature":
    st.subheader("Temperature Converter")
    temp_units = ["Celsius", "Fahrenheit"]
    value = st.number_input("Enter the temperature:", format="%.2f")
    from_unit = st.selectbox("From Unit:", temp_units)
    to_unit = st.selectbox("To Unit:", temp_units)
    if st.button("Convert"):
        result = temperature_converter(value, from_unit, to_unit)
        st.success(f"{value}° {from_unit} = {result:.2f}° {to_unit}")


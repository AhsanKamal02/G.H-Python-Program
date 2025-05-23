import streamlit as st

def convert_length(value, from_unit, to_unit):
    length_units = {
        'meters': 1,
        'kilometers': 1000,
        'miles': 1609.34,
        'feet': 0.3048,
        'inches': 0.0254
    }
    
    value_in_meters = value * length_units[from_unit]

    return value_in_meters / length_units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'Kelvin':
            return value + 273.15
        else:
            return value

    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
        else:
            return value

    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return value - 273.15
        elif to_unit == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32
        else:
            return value


st.title("Unit Converter")

value = st.number_input("Enter the value to convert:", value=0.0)

conversion_category = st.selectbox("Select conversion category:", ["Length", "Temperature"])

if conversion_category == "Length":
    length_units = ['meters', 'kilometers', 'miles', 'feet', 'inches']
    from_unit = st.selectbox("Select input unit:", length_units)
    to_unit = st.selectbox("Select output unit:", length_units)
    
    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")

elif conversion_category == "Temperature":
    temperature_units = ['Celsius', 'Fahrenheit', 'Kelvin']
    from_unit = st.selectbox("Select input unit:", temperature_units)
    to_unit = st.selectbox("Select output unit:", temperature_units)
    
    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")
import streamlit as st
import pandas as pd

st.title('Question 2: ')


def check_level(level):
    try:
        level = int(level)  # Attempt to convert level to integer
    except ValueError:  # Handle cases where level is not a valid integer
        if level.upper() in ('A', 'B', 'C', 'D', 'E', 'F'):
            st.success('Good job!')
        else:
            st.error(f'Invalid level: {level}')
    else:  # Execute only if conversion to integer was successful
        if level < 10:
            st.error(f'Level {level} for Dulce is too low.')
        elif level >= 10:
            st.error(f'Level {level} for Dulce is too high.')


def get_file(file):
    file_path = file

    # Load data from Excel file
    data = pd.read_csv(file_path)

    st.write(data)

    level = data['level'][0]
    check_level(level)


uploaded_file = st.file_uploader("Upload Excel file", type=["csv"])
if not uploaded_file:
    get_file('file.csv')
else:

    get_file(uploaded_file)



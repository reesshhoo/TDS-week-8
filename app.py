import streamlit as st

def find_largest(x, y, z):
    largest = x
    if y > largest:
        largest = y
    if z > largest:
        largest = z
    return largest

st.title("Find the largest among three numbers")

x = st.number_input("Enter the first number:")
y = st.number_input("Enter the second number:")
z = st.number_input("Enter the third number:")

if st.button("Find the largest"):
    result = find_largest(x, y, z)
    st.write("The largest number is:", result)

import streamlit as st

st.title("simple calaculator by pda college")

num1 = st.number_input("enter the first number")
num2 = st.number_input("enter the second number")

operation = st.selectbox("select the operation" , ["add" , "subtract" , "multiply" , "divide"])

if st.button("calculate"):
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero is not allowed."
    st.write("the result is" , result)

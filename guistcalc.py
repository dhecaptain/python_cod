import streamlit as st

def simple_calculator():
    st.title("simple calculator")
    
    num1=st.number_input("enter the first number ",format='%g')
    operation=st.selectbox("choose an operation ",["Addition","Subtraction","Multiplication","Division"])
    num2=st.number_input("enter the second number ",format='%g')
    
    result=0.0
    
    if operation=="Addition":
        result=num1+num2
    elif operation=="Subtraction":
        result=num1-num2
    elif operation=="Multiplication":
        result=num1*num2
    else:
        if num2!=0:
            result=num1/num2
        else:
            st.error("zero division error")
    st.write(f"results={result}")
    
if __name__=="__main__":
    simple_calculator()
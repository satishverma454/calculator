import streamlit as st

if "result" not in st.session_state:
    st.session_state["result"]=""
def number_call(num):
    st.session_state["result"]+=str(num)

def operator_click(operator):
    if operator=="cls":
        st.session_state["result"]=""
    elif operator=="X":
        exp=[]
        for ch in st.session_state["result"]:
            exp.append(ch)

        exp.pop()
        st.session_state["result"]="".join(exp)
    else:
        st.session_state["result"]+=operator
def calculate():

    expression = st.session_state["result"]

    try:
        answer = eval(expression)
        st.session_state["result"] = str(answer)

    except ZeroDivisionError:
        st.session_state["result"]="Cannot divide by zero."
        

    except SyntaxError:
        st.sesion_state["result"]="Invalid expression!"

    except Exception:
        st.session_state["result"]="Something Wrong!"

with st.container(border=True, width=300,height=470,autoscroll=False):

    with st.container(border=True, height=70):
        st.write(st.session_state["result"])

    col1, col2, col3 = st.columns(3,gap="xxsmall")

    with col1:
        st.button("1", on_click=number_call, args=(1,))
        st.button("4", on_click=number_call, args=(4,))
        st.button("7", on_click=number_call, args=(7,))
        st.button("0", on_click=number_call, args=(0,))
        st.button("-", on_click=operator_click, args=("-",))
        st.button("*", on_click=operator_click, args=("*",))
    with col2:
        st.button("2", on_click=number_call, args=(2,))
        st.button("5", on_click=number_call, args=(5,))
        st.button("8", on_click=number_call, args=(8,))
        st.button(".", on_click=operator_click, args=(".",))
        st.button("/", on_click=operator_click, args=("/",))
        st.button("X", on_click=operator_click, args=("X",))

    with col3:
        st.button("3", on_click=number_call, args=(3,))
        st.button("6", on_click=number_call, args=(6,))
        st.button("9", on_click=number_call, args=(9,))
        st.button("+", on_click=operator_click, args=("+",))
        st.button("=", on_click=calculate)
        st.button("cls", on_click=operator_click, args=("cls",))
        
       
        

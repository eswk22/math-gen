import streamlit as st
import llm_helper
from streamlit_javascript import st_javascript


def load_html():
    # Create Streamlit app layout
    st.title("Math Problem Generator")
    with st.sidebar:
        # User input for problem type and difficulty
        problem_type = st.selectbox("Problem Type", ["Addition", "Subtraction", "Multiplication", "Division"])
        difficulty_level = st.selectbox("Difficulty Level", ["Easy", "Medium", "Hard"])
        word_problem = st.checkbox("Word Problem?")
        # Generate and display math problem
        if st.button("Generate Problem"):
            st.session_state["problem"] = llm_helper.generate_math_problem(problem_type, difficulty_level, word_problem)
        if st.button("Print"):
           st_javascript("function print(){window.print();return false;} print();")
    result_container = st.container()
    with result_container:
        if "problem" in st.session_state:
            st.write(st.session_state["problem"])
    add_css()
    
def add_css():
    css = """
   <style type="text/css">
    @media print {
        [data-testid="stSidebarContent"] {display: none;}
        .main, .main > * {
            display: block !important;
        }
    }
    """
    st.markdown(css, unsafe_allow_html=True)

if __name__ == "__main__":
    load_html()
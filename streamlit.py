import streamlit as st
from questions import questions  # ייבוא השאלות מקובץ חיצוני

# פונקציה להוספת עיצוב מותאם ב-CSS
def local_css(css):
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# יישור לימין בעזרת CSS
local_css("""
    .stRadio > div, .stTextInput > div {
        direction: rtl;
        text-align: right;
    }
    .stMarkdown {
        direction: rtl;
        text-align: right;
    }
""")

# אתחול מצב הסשן אם לא קיים
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0
if 'answers' not in st.session_state:
    st.session_state.answers = []

# פונקציה להתקדמות לשאלה הבאה
def next_question():
    st.session_state.question_index += 1

# הצגת השאלה הנוכחית
if st.session_state.question_index < len(questions):
    current_q = questions[st.session_state.question_index]
    st.write(current_q["question"])
    
    if current_q["options"]:
        answer = st.radio("", current_q["options"], key=st.session_state.question_index)
        if answer:
            st.session_state.answers.append(answer)
            next_question()
    else:
        answer = st.text_input("", key=st.session_state.question_index)
        if answer:
            st.session_state.answers.append(answer)
            next_question()
else:
    st.write("תודה על ההשתתפות בצ'אט!")
    st.write("התשובות שלך:")
    for idx, ans in enumerate(st.session_state.answers):
        st.write(f"שאלה {idx+1}: {ans}")

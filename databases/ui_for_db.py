#streamlit run databases/ui_for_db.py  OR
# py -m streamlit run databases/ui_for_db.py
import streamlit as st
from db_example1 import open_db
from db_example1 import Student,Grade

def show_student_form():
    with st.form('f1'):
        name=st.text_input("enter student name")
        c1,c2=st.columns(2)
        klass=c1.text_input("enter student class")
        section=c2.text_input("enter student section")
        is_online=st.checkbox("is student attending online?")
        btn=st.form_submit_button("add student")

    if btn and name and klass and section:
        db=open_db()
        db.add(Student(name=name,section=section,klass=klass)) 
        db.commit()
        db.close()
        st.success("saved student details")   
def show_grading_form():
    pass


st.title("Database Example for Newbies😎😎")

options=["View students","view grades","add students","add grades"]
choice=st.sidebar.radio("select any option",options)

if choice==options[0]:
    pass
elif choice==options[1]:
    pass
elif choice==options[2]:
    show_student_form()
elif choice==options[3]:
    show_grading_form()

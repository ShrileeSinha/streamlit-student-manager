import streamlit as st
import mysql.connector
import pandas as pd
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Student Management System",
    page_icon="👨‍💻",
)
# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="shrilee",
    password="shrilee",
    database="student_management"
)

# Create a cursor to execute SQL queries
cursor = conn.cursor()

# Create a table to store student information if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    address VARCHAR(255) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    email VARCHAR(255) NOT NULL,
    college VARCHAR(255) NOT NULL,
    course VARCHAR(255) NOT NULL
)
"""
cursor.execute(create_table_query)
conn.commit()

# Page 1: Add a student
def add_student():
    st.title("Add a Student")
    name = st.text_input("Name")
    age = st.number_input("Age", step=1)
    address = st.text_input("Address")
    phone = st.text_input("Phone Number")
    email = st.text_input("Email ID")
    college = st.text_input("College Name")
    course = st.text_input("Course Name")

    if st.button("Add"):
        insert_query = """
        INSERT INTO students (name, age, address, phone, email, college, course)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (name, age, address, phone, email, college, course)
        cursor.execute(insert_query, values)
        conn.commit()
        st.success("Student added successfully.")

# Page 2: Delete a student
def delete_student():
    st.title("Delete a Student")
    student_id = st.number_input("Enter Student ID",step=1)

    if st.button("Delete"):
        delete_query = "DELETE FROM students WHERE id = %s"
        values = (student_id,)
        cursor.execute(delete_query, values)
        conn.commit()
        st.success("Student deleted successfully.")

# Page 3: View students by name
def view_students_by_name():
    st.title("View Students by Name")
    name = st.text_input("Enter Name")
    query = "SELECT * FROM students WHERE name LIKE %s"
    values = (f"%{name}%",)

    cursor.execute(query, values)
    students = cursor.fetchall()

    if students:
        df = pd.DataFrame(students, columns=["ID", "Name", "Age", "Address", "Phone", "Email", "College", "Course"])
        st.dataframe(df)
    else:
        st.warning("No students found.")

# Page 4: Show all students
def show_all_students():
    st.title("All Students")
    query = "SELECT * FROM students"
    cursor.execute(query)
    students = cursor.fetchall()

    if students:
        df = pd.DataFrame(students, columns=["ID", "Name", "Age", "Address", "Phone", "Email", "College", "Course"])
        st.dataframe(df)
    else:
        st.warning("No students found.")

# Page 5: Modify student details
def modify_student():
    st.title("Modify Student Details")
    student_id = st.number_input("Enter Student ID",step=1)

    # Retrieve the student details from the database
    query = "SELECT * FROM students WHERE id = %s"
    values = (student_id,)
    cursor.execute(query, values)
    student = cursor.fetchone()

    if student:
        name = st.text_input("Name", value=student[1])
        age = st.number_input("Age", value=student[2])
        address = st.text_input("Address", value=student[3])
        phone = st.text_input("Phone Number", value=student[4])
        email = st.text_input("Email ID", value=student[5])
        college = st.text_input("College Name", value=student[6])
        course = st.text_input("Course Name", value=student[7])
        if st.button("Update"):
            update_query = """
            UPDATE students
            SET name = %s, age = %s, address = %s, phone = %s, email = %s, college = %s, course = %s
            WHERE id = %s
            """
            values = (name, age, address, phone, email, college, course, student_id)
            cursor.execute(update_query, values)
            conn.commit()
            st.success("Student details updated successfully.")
    else:
        st.warning("Student not found.")


def streamlit_menu():
    with st.sidebar:
        selected = option_menu(
            menu_title="Student Management System ",
            options=["Add a Student", "Delete a Student", "Modify Student Details", "View Students by Name","Show all Students"], 
            default_index=0, 
            )
        return selected

# Main function to run the Streamlit application
def main():
    selected_page = streamlit_menu()
    if selected_page == "Add a Student":
        add_student()
    elif selected_page == "Delete a Student":
        delete_student()
    elif selected_page == "Modify Student Details":
        modify_student()
    elif selected_page == "View Students by Name":
        view_students_by_name()
    elif selected_page == "Show all Students":
        show_all_students()
if __name__ == '__main__':
    main()


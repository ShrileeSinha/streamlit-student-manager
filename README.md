# Student Management System

This is a simple Student Management System implemented using Streamlit, MySQL, and Pandas.

## Requirements

Make sure to install the required packages by running:

```bash
pip install -r requirements.txt
```

- streamlit_option_menu==0.3.2
- streamlit==1.22.0
- pandas==2.0.2
- mysql-connector-python==8.0.33pi

## Usage

### Setup

1. Install the required packages using the command mentioned in the Requirements section.
2. Make sure you have a MySQL database running locally, and update the connection details in the `student.py` file.

### Running the Application

```bash
streamlit run student.py
```

## Code Overview

### Database Setup

- The system uses a MySQL database named `student_management`.
- A table named `students` is created to store student information.

### Pages

1. **Add a Student**: Allows you to add a new student to the database.

2. **Delete a Student**: Enables you to delete a student by providing the student's ID.

3. **View Students by Name**: Displays a list of students whose names match the provided input.

4. **Show all Students**: Shows all students present in the database.

5. **Modify Student Details**: Allows you to update the details of a specific student.

### Streamlit Menu

- A sidebar menu is implemented using the `streamlit_option_menu` package, providing easy navigation between different pages.

## How to Run

1. Run the Streamlit application using the command mentioned in the "Running the Application" section.
2. Use the sidebar menu to navigate through different functionalities.
3. Follow the on-screen instructions for each operation.

Feel free to explore and customize the code as needed for your specific use case. If you encounter any issues or have suggestions for improvements, please feel free to reach out to the author, Shrilee Sinha.

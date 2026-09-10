import gradio as gr
import requests

# FastAPI backend URL
BASE_URL = "http://127.0.0.1:8000"


# ==========================================
# CREATE STUDENT
# ==========================================

def create_student(student_id, name, course, marks):

    try:
        response = requests.post(
            f"{BASE_URL}/students",
            params={
                "id": int(student_id),
                "name": name,
                "course": course,
                "marks": int(marks)
            }
        )

        return response.json()

    except Exception as e:
        return {"error": str(e)}


# ==========================================
# READ ALL STUDENTS
# ==========================================

def get_students():

    try:
        response = requests.get(
            f"{BASE_URL}/students"
        )

        return response.json()

    except Exception as e:
        return {"error": str(e)}


# ==========================================
# READ ONE STUDENT
# ==========================================

def get_student(student_id):

    try:
        response = requests.get(
            f"{BASE_URL}/students/{int(student_id)}"
        )

        return response.json()

    except Exception as e:
        return {"error": str(e)}


# ==========================================
# UPDATE STUDENT
# ==========================================

def update_student(student_id, marks):

    try:
        response = requests.put(
            f"{BASE_URL}/students/{int(student_id)}",
            params={
                "marks": int(marks)
            }
        )

        return response.json()

    except Exception as e:
        return {"error": str(e)}


# ==========================================
# DELETE STUDENT
# ==========================================

def delete_student(student_id):

    try:
        response = requests.delete(
            f"{BASE_URL}/students/{int(student_id)}"
        )

        return response.json()

    except Exception as e:
        return {"error": str(e)}


# ==========================================
# GRADIO INTERFACE
# ==========================================

with gr.Blocks(title="Student Management System") as app:

    gr.Markdown("# 🎓 Student Management System")
    gr.Markdown("### FastAPI + Supabase + Gradio")


    # ======================================
    # CREATE
    # ======================================

    with gr.Tab("Create Student"):

        gr.Markdown("## Add New Student")

        student_id = gr.Number(
            label="Student ID",
            precision=0
        )

        name = gr.Textbox(
            label="Name",
            placeholder="Enter student name"
        )

        course = gr.Textbox(
            label="Course",
            placeholder="Enter course"
        )

        marks = gr.Number(
            label="Marks",
            precision=0
        )

        create_button = gr.Button(
            "Create Student"
        )

        create_result = gr.JSON(
            label="Result"
        )

        create_button.click(
            fn=create_student,
            inputs=[
                student_id,
                name,
                course,
                marks
            ],
            outputs=create_result
        )


    # ======================================
    # READ ALL
    # ======================================

    with gr.Tab("All Students"):

        gr.Markdown("## All Students")

        get_button = gr.Button(
            "Get All Students"
        )

        students_result = gr.JSON(
            label="Students"
        )

        get_button.click(
            fn=get_students,
            inputs=[],
            outputs=students_result
        )


    # ======================================
    # READ ONE
    # ======================================

    with gr.Tab("Find Student"):

        gr.Markdown("## Find Student")

        find_id = gr.Number(
            label="Student ID",
            precision=0
        )

        find_button = gr.Button(
            "Find Student"
        )

        find_result = gr.JSON(
            label="Student"
        )

        find_button.click(
            fn=get_student,
            inputs=find_id,
            outputs=find_result
        )


    # ======================================
    # UPDATE
    # ======================================

    with gr.Tab("Update Student"):

        gr.Markdown("## Update Student Marks")

        update_id = gr.Number(
            label="Student ID",
            precision=0
        )

        new_marks = gr.Number(
            label="New Marks",
            precision=0
        )

        update_button = gr.Button(
            "Update Marks"
        )

        update_result = gr.JSON(
            label="Result"
        )

        update_button.click(
            fn=update_student,
            inputs=[
                update_id,
                new_marks
            ],
            outputs=update_result
        )


    # ======================================
    # DELETE
    # ======================================

    with gr.Tab("Delete Student"):

        gr.Markdown("## Delete Student")

        delete_id = gr.Number(
            label="Student ID",
            precision=0
        )

        delete_button = gr.Button(
            "Delete Student"
        )

        delete_result = gr.JSON(
            label="Result"
        )

        delete_button.click(
            fn=delete_student,
            inputs=delete_id,
            outputs=delete_result
        )


# ==========================================
# START GRADIO
# ==========================================

app.launch()
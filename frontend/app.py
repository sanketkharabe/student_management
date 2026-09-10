import gradio as gr
import requests

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
# GET ALL STUDENTS
# ==========================================

def get_all_students():

    try:
        response = requests.get(
            f"{BASE_URL}/students"
        )

        return response.json()

    except Exception as e:
        return {"error": str(e)}


# ==========================================
# GET ONE STUDENT
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
# GRADIO UI
# ==========================================

with gr.Blocks(title="Student Management System") as app:

    gr.Markdown("# 🎓 Student Management System")

    # ======================================
    # CREATE
    # ======================================

    gr.Markdown("## Create Student")

    student_id = gr.Number(
        label="Student ID",
        precision=0
    )

    name = gr.Textbox(
        label="Name"
    )

    course = gr.Textbox(
        label="Course"
    )

    marks = gr.Number(
        label="Marks",
        precision=0
    )

    create_button = gr.Button(
        "Create Student"
    )

    create_output = gr.JSON(
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
        outputs=create_output
    )


    # ======================================
    # GET ALL
    # ======================================

    gr.Markdown("## View All Students")

    get_all_button = gr.Button(
        "Get All Students"
    )

    all_students_output = gr.JSON(
        label="Students"
    )

    get_all_button.click(
        fn=get_all_students,
        inputs=[],
        outputs=all_students_output
    )


    # ======================================
    # GET ONE
    # ======================================

    gr.Markdown("## Find Student")

    find_id = gr.Number(
        label="Student ID",
        precision=0
    )

    find_button = gr.Button(
        "Find Student"
    )

    find_output = gr.JSON(
        label="Student"
    )

    find_button.click(
        fn=get_student,
        inputs=find_id,
        outputs=find_output
    )


    # ======================================
    # UPDATE
    # ======================================

    gr.Markdown("## Update Marks")

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

    update_output = gr.JSON(
        label="Result"
    )

    update_button.click(
        fn=update_student,
        inputs=[
            update_id,
            new_marks
        ],
        outputs=update_output
    )


    # ======================================
    # DELETE
    # ======================================

    gr.Markdown("## Delete Student")

    delete_id = gr.Number(
        label="Student ID",
        precision=0
    )

    delete_button = gr.Button(
        "Delete Student"
    )

    delete_output = gr.JSON(
        label="Result"
    )

    delete_button.click(
        fn=delete_student,
        inputs=delete_id,
        outputs=delete_output
    )


# ==========================================
# START APP
# ==========================================

app.launch()
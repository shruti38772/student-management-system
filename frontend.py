import gradio as gr
import requests

API_URL = "http://127.0.0.1:8000"


# -------------------------
# ADD STUDENT
# -------------------------
def add_student(name, course, marks):

    if not name or not course or marks == "":
        return "Please enter all details."

    try:
        response = requests.post(
            f"{API_URL}/students",
            params={
                "name": name,
                "course": course,
                "marks": int(marks)
            }
        )

        if response.status_code == 200:
            return "Student added successfully!\n\n" + str(response.json())

        return "Error: " + response.text

    except Exception as e:
        return "Backend connection error: " + str(e)


# -------------------------
# VIEW ALL STUDENTS
# -------------------------
def get_students():

    try:
        response = requests.get(
            f"{API_URL}/students"
        )

        if response.status_code == 200:
            return response.json()

        return "Error: " + response.text

    except Exception as e:
        return "Backend connection error: " + str(e)


# -------------------------
# GET ONE STUDENT
# -------------------------
def get_student(student_id):

    try:
        response = requests.get(
            f"{API_URL}/students/{int(student_id)}"
        )

        if response.status_code == 200:
            return response.json()

        return "Error: " + response.text

    except Exception as e:
        return "Backend connection error: " + str(e)


# -------------------------
# UPDATE STUDENT
# -------------------------
def update_student(student_id, marks):

    try:
        response = requests.put(
            f"{API_URL}/students/{int(student_id)}",
            params={
                "marks": int(marks)
            }
        )

        if response.status_code == 200:
            return "Student updated successfully!\n\n" + str(response.json())

        return "Error: " + response.text

    except Exception as e:
        return "Backend connection error: " + str(e)


# -------------------------
# DELETE STUDENT
# -------------------------
def delete_student(student_id):

    try:
        response = requests.delete(
            f"{API_URL}/students/{int(student_id)}"
        )

        if response.status_code == 200:
            return "Student deleted successfully!\n\n" + str(response.json())

        return "Error: " + response.text

    except Exception as e:
        return "Backend connection error: " + str(e)


# =====================================================
# GRADIO FRONTEND
# =====================================================

with gr.Blocks(title="Student Management System") as app:

    gr.Markdown(
        """
        # 🎓 Student Management System

        **Frontend:** Gradio  
        **Backend:** FastAPI  
        **Database:** Supabase
        """
    )

    # =========================
    # ADD STUDENT
    # =========================

    with gr.Tab("Add Student"):

        name = gr.Textbox(
            label="Student Name",
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

        add_btn = gr.Button("Add Student")

        add_result = gr.Textbox(
            label="Result"
        )

        add_btn.click(
            add_student,
            inputs=[name, course, marks],
            outputs=add_result
        )

    # =========================
    # VIEW STUDENTS
    # =========================

    with gr.Tab("View Students"):

        view_btn = gr.Button("View All Students")

        view_result = gr.JSON(
            label="Students"
        )

        view_btn.click(
            get_students,
            inputs=[],
            outputs=view_result
        )

    # =========================
    # FIND STUDENT
    # =========================

    with gr.Tab("Find Student"):

        student_id = gr.Number(
            label="Student ID",
            precision=0
        )

        find_btn = gr.Button("Find Student")

        find_result = gr.JSON(
            label="Student Details"
        )

        find_btn.click(
            get_student,
            inputs=student_id,
            outputs=find_result
        )

    # =========================
    # UPDATE STUDENT
    # =========================

    with gr.Tab("Update Student"):

        update_id = gr.Number(
            label="Student ID",
            precision=0
        )

        new_marks = gr.Number(
            label="New Marks",
            precision=0
        )

        update_btn = gr.Button("Update Marks")

        update_result = gr.Textbox(
            label="Result"
        )

        update_btn.click(
            update_student,
            inputs=[update_id, new_marks],
            outputs=update_result
        )

    # =========================
    # DELETE STUDENT
    # =========================

    with gr.Tab("Delete Student"):

        delete_id = gr.Number(
            label="Student ID",
            precision=0
        )

        delete_btn = gr.Button("Delete Student")

        delete_result = gr.Textbox(
            label="Result"
        )

        delete_btn.click(
            delete_student,
            inputs=delete_id,
            outputs=delete_result
        )


# =========================
# START GRADIO
# =========================

app.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))

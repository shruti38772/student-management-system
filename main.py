from fastapi import FastAPI
from supabase import create_client
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

# Create FastAPI application
app = FastAPI()

# -------------------------
# SUPABASE CONNECTION
# -------------------------

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Check credentials
if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("SUPABASE_URL or SUPABASE_KEY is missing in .env file")

# Connect Python to Supabase
supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)


# -------------------------
# HOME
# -------------------------

@app.get("/")
def home():
    return {
        "message": "FastAPI and Supabase connected successfully!"
    }


# -------------------------
# CREATE
# -------------------------

@app.post("/students")
def create_student(name: str, course: str, marks: int):

    student = {
        "name": name,
        "course": course,
        "marks": marks
    }

    response = (
        supabase
        .table("students")
        .insert(student)
        .execute()
    )

    return {
        "message": "Student created successfully",
        "data": response.data
    }


# -------------------------
# READ ALL
# -------------------------

@app.get("/students")
def get_students():

    response = (
        supabase
        .table("students")
        .select("*")
        .execute()
    )

    return {
        "message": "Students fetched successfully",
        "data": response.data
    }


# -------------------------
# READ ONE
# -------------------------

@app.get("/students/{student_id}")
def get_student(student_id: int):

    response = (
        supabase
        .table("students")
        .select("*")
        .eq("id", student_id)
        .execute()
    )

    return {
        "message": "Student fetched successfully",
        "data": response.data
    }


# -------------------------
# UPDATE
# -------------------------

@app.put("/students/{student_id}")
def update_student(student_id: int, marks: int):

    updated_data = {
        "marks": marks
    }

    response = (
        supabase
        .table("students")
        .update(updated_data)
        .eq("id", student_id)
        .execute()
    )

    return {
        "message": "Student updated successfully",
        "data": response.data
    }


# -------------------------
# DELETE
# -------------------------

@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    response = (
        supabase
        .table("students")
        .delete()
        .eq("id", student_id)
        .execute()
    )

    return {
        "message": "Student deleted successfully",
        "data": response.data
    }
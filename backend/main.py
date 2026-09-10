from fastapi import FastAPI, HTTPException
from supabase import create_client
from pydantic import BaseModel
from dotenv import load_dotenv
import os

class StudentCreate(BaseModel):
    id: int
    name: str
    course: str
    marks: int

class StudentUpdate(BaseModel):
    marks: int

# Load variables from .env
load_dotenv()

# Create FastAPI application
app = FastAPI()

# Get Supabase credentials
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

print("SUPABASE_URL:", SUPABASE_URL)
print("SUPABASE_KEY:", "Loaded" if SUPABASE_KEY else "Not Loaded")

# Check credentials
if not SUPABASE_URL:
    raise ValueError("SUPABASE_URL is missing from .env")

if not SUPABASE_KEY:
    raise ValueError("SUPABASE_KEY is missing from .env")

# Connect to Supabase
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

print("Supabase connected successfully!")


# ==========================================
# CREATE STUDENT
# ==========================================

@app.post("/students")
def create_student(student: StudentCreate):

    try:
        response = (
            supabase
            .table("students")
            .insert(student.model_dump())
            .execute()
        )

        print("SUPABASE RESPONSE:", response.data)

        return {
            "message": "Student created successfully",
            "data": response.data
        }

    except Exception as e:
        print("SUPABASE ERROR:", repr(e))

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# ==========================================
# GET ALL STUDENTS
# ==========================================

@app.get("/students")
def get_students():

    try:
        # Read all records from students table
        response = (
            supabase
            .table("students")
            .select("*")
            .execute()
        )

        # Send database records as API response
        return {
            "message": "Students fetched successfully",
            "data": response.data
        }

    except Exception as e:
        print("SUPABASE ERROR:", repr(e))

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    # -------------------------
# READ ONE
# -------------------------

@app.get("/students/{student_id}")
def get_student(student_id: int):

    try:
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

    except Exception as e:
        print("SUPABASE ERROR:", repr(e))
        raise HTTPException(status_code=500, detail=str(e))


# -------------------------
# UPDATE
# -------------------------

@app.put("/students/{student_id}")
def update_student(student_id: int, student_update: StudentUpdate):

    try:
        response = (
            supabase
            .table("students")
            .update(student_update.model_dump())
            .eq("id", student_id)
            .execute()
        )

        return {
            "message": "Student updated successfully",
            "data": response.data
        }

    except Exception as e:
        print("SUPABASE ERROR:", repr(e))
        raise HTTPException(status_code=500, detail=str(e))


# -------------------------
# DELETE
# -------------------------

@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    try:
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

    except Exception as e:
        print("SUPABASE ERROR:", repr(e))
        raise HTTPException(status_code=500, detail=str(e))



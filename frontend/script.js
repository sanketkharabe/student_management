const BASE_URL = "http://127.0.0.1:8000";

// ==================================================
// CREATE STUDENT
// ==================================================

async function createStudent() {

    const id = document.getElementById("studentId").value;
    const name = document.getElementById("name").value;
    const course = document.getElementById("course").value;
    const marks = document.getElementById("marks").value;

    if (!id || !name || !course || !marks) {
        showResult("createResult", {
            error: "Please fill all fields"
        });
        return;
    }

    try {

        const url =
            `${BASE_URL}/students?id=${id}` +
            `&name=${encodeURIComponent(name)}` +
            `&course=${encodeURIComponent(course)}` +
            `&marks=${marks}`;

        const response = await fetch(url, {
            method: "POST"
        });

        const data = await response.json();

        showResult("createResult", data);

    } catch (error) {

        showResult("createResult", {
            error: error.message
        });

    }
}


// ==================================================
// GET ALL STUDENTS
// ==================================================

async function getStudents() {

    try {

        const response = await fetch(
            `${BASE_URL}/students`
        );

        const data = await response.json();

        displayStudents(data);

    } catch (error) {

        showResult("studentsResult", {
            error: error.message
        });

    }
}


// ==================================================
// GET ONE STUDENT
// ==================================================

async function getStudent() {

    const id = document.getElementById("findId").value;

    if (!id) {

        showResult("findResult", {
            error: "Please enter student ID"
        });

        return;
    }

    try {

        const response = await fetch(
            `${BASE_URL}/students/${id}`
        );

        const data = await response.json();

        showResult("findResult", data);

    } catch (error) {

        showResult("findResult", {
            error: error.message
        });

    }
}


// ==================================================
// UPDATE STUDENT
// ==================================================

async function updateStudent() {

    const id = document.getElementById("updateId").value;
    const marks = document.getElementById("newMarks").value;

    if (!id || !marks) {

        showResult("updateResult", {
            error: "Please enter ID and marks"
        });

        return;
    }

    try {

        const url =
            `${BASE_URL}/students/${id}?marks=${marks}`;

        const response = await fetch(url, {
            method: "PUT"
        });

        const data = await response.json();

        showResult("updateResult", data);

    } catch (error) {

        showResult("updateResult", {
            error: error.message
        });

    }
}


// ==================================================
// DELETE STUDENT
// ==================================================

async function deleteStudent() {

    const id = document.getElementById("deleteId").value;

    if (!id) {

        showResult("deleteResult", {
            error: "Please enter student ID"
        });

        return;
    }

    try {

        const response = await fetch(
            `${BASE_URL}/students/${id}`,
            {
                method: "DELETE"
            }
        );

        const data = await response.json();

        showResult("deleteResult", data);

    } catch (error) {

        showResult("deleteResult", {
            error: error.message
        });

    }
}


// ==================================================
// DISPLAY JSON RESULT
// ==================================================

function showResult(elementId, data) {

    const element = document.getElementById(elementId);

    element.innerHTML = "";

    const pre = document.createElement("pre");

    pre.textContent = JSON.stringify(data, null, 2);

    element.appendChild(pre);
}


// ==================================================
// DISPLAY ALL STUDENTS AS TABLE
// ==================================================

function displayStudents(data) {

    const container =
        document.getElementById("studentsResult");

    container.innerHTML = "";

    if (!data.data || data.data.length === 0) {

        container.innerHTML =
            "<p>No students found.</p>";

        return;
    }

    const table = document.createElement("table");

    table.innerHTML = `
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Course</th>
                <th>Marks</th>
            </tr>
        </thead>

        <tbody></tbody>
    `;

    const tbody = table.querySelector("tbody");

    data.data.forEach(student => {

        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${student.id}</td>
            <td>${student.name}</td>
            <td>${student.course}</td>
            <td>${student.marks}</td>
        `;

        tbody.appendChild(row);

    });

    container.appendChild(table);
}
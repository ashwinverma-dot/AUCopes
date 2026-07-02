from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

DEPARTMENTS = [
    {
        "name": "Computer Science and Engineering",
        "code": "CSE",
        "description": "Focuses on programming, data structures, cloud computing, AI, cybersecurity, and software development."
    },
    {
        "name": "Information Technology",
        "code": "IT",
        "description": "Covers web technologies, databases, networking, software engineering, and enterprise applications."
    },
    {
        "name": "Electronics and Communication Engineering",
        "code": "ECE",
        "description": "Deals with embedded systems, communication networks, VLSI, signal processing, and IoT."
    },
    {
        "name": "Mechanical Engineering",
        "code": "ME",
        "description": "Includes design, manufacturing, thermodynamics, robotics, and industrial engineering."
    },
    {
        "name": "Civil Engineering",
        "code": "CE",
        "description": "Covers structural engineering, transportation, surveying, construction, and environmental engineering."
    }
]

COURSES = [
    {
        "name": "B.Tech",
        "duration": "4 Years",
        "level": "Undergraduate",
        "details": "Engineering degree program offered across multiple technical departments."
    },
    {
        "name": "M.Tech",
        "duration": "2 Years",
        "level": "Postgraduate",
        "details": "Advanced technical program with specialization and research-oriented learning."
    },
    {
        "name": "BCA",
        "duration": "3 Years",
        "level": "Undergraduate",
        "details": "Computer applications program focused on programming, databases, and web development."
    },
    {
        "name": "MCA",
        "duration": "2 Years",
        "level": "Postgraduate",
        "details": "Professional program focused on software development, application design, and IT systems."
    },
    {
        "name": "Ph.D.",
        "duration": "Minimum 3 Years",
        "level": "Doctoral",
        "details": "Research program for advanced academic and industry-oriented research."
    }
]

FACULTY = [
    {
        "name": "Dr. Anil Sharma",
        "designation": "Professor and Head",
        "department": "Computer Science and Engineering",
        "specialization": "Cloud Computing, Distributed Systems"
    },
    {
        "name": "Dr. Neha Patel",
        "designation": "Associate Professor",
        "department": "Information Technology",
        "specialization": "Database Systems, Web Technologies"
    },
    {
        "name": "Prof. Rahul Verma",
        "designation": "Assistant Professor",
        "department": "Electronics and Communication Engineering",
        "specialization": "IoT, Embedded Systems"
    },
    {
        "name": "Dr. Priya Singh",
        "designation": "Associate Professor",
        "department": "Mechanical Engineering",
        "specialization": "Robotics, Manufacturing Systems"
    },
    {
        "name": "Prof. Meera Joshi",
        "designation": "Assistant Professor",
        "department": "Civil Engineering",
        "specialization": "Structural Engineering, Construction Management"
    }
]


@app.route("/")
def home():
    return render_template(
        "index.html",
        title="Cloud-Based College Information Portal"
    )


@app.route("/academics")
def academics():
    return render_template(
        "academics.html",
        title="Departments and Courses",
        departments=DEPARTMENTS,
        courses=COURSES
    )


@app.route("/faculty-contact", methods=["GET", "POST"])
def faculty_contact():
    success_message = None

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        if name and email and message:
            success_message = "Thank you. Your enquiry has been submitted successfully."
        else:
            success_message = "Please fill all fields before submitting the enquiry."

    return render_template(
        "faculty_contact.html",
        title="Faculty and Contact",
        faculty=FACULTY,
        success_message=success_message
    )


@app.route("/health")
def health():
    return jsonify({
        "service": "college-info-portal-cicd",
        "health": "ok"
    }), 200


@app.route("/api/college")
def college_api():
    return jsonify({
        "project_title": "Cloud-Based College Information Portal with CI/CD Pipeline",
        "pages": ["Home", "Departments and Courses", "Faculty and Contact"],
        "technology_stack": ["Python Flask", "HTML", "CSS", "Docker", "GitHub Actions"],
        "deployment": "Cloud deployment using CI/CD pipeline"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

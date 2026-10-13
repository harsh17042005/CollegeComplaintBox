
import streamlit as st
from datetime import date

# Page configuration
st.set_page_config(
    page_title="College Complaint Box",
    page_icon="🎓",
    layout="centered"
)

# Application title
st.title("🎓 College Complaint Box")
st.write("Welcome to the College Complaint Box Management System.")
st.write("Submit your college-related complaints using the form below.")

st.divider()

# Complaint form
st.subheader("📝 Submit a Complaint")

with st.form("complaint_form"):
    student_id = st.text_input("Student ID (optional)")

    title = st.text_input("Complaint Title")

    category = st.selectbox(
        "Select Complaint Category",
        [
            "Hostel",
            "Classroom",
            "Faculty",
            "Infrastructure",
            "Transport",
            "Sanitation",
            "Other"
        ]
    )

    description = st.text_area(
        "Describe Your Complaint",
        placeholder="Explain your problem here..."
    )

    anonymous = st.checkbox("Submit anonymously")

    submitted = st.form_submit_button(
        "Submit Complaint",
        use_container_width=True
    )

# Process form submission
if submitted:
    if not title.strip() or not description.strip():
        st.error("Please enter both the complaint title and description.")

    else:
        complaint = {
            "student_id": "" if anonymous else student_id.strip(),
            "title": title.strip(),
            "category": category,
            "description": description.strip(),
            "anonymous": anonymous,
            "status": "Pending",
            "created_at": str(date.today())
        }

        st.success("Complaint form submitted successfully!")
        st.write("### Complaint Summary")
        st.write("**Title:**", complaint["title"])
        st.write("**Category:**", complaint["category"])
        st.write("**Status:**", complaint["status"])

        if anonymous:
            st.info("Your complaint is marked as anonymous.")

        st.caption(
            "Demo version: this complaint is not yet saved to MongoDB."
        )

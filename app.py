from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import os

app = Flask(__name__)

# Ensure the "resumes" directory exists
if not os.path.exists("resumes"):
    os.makedirs("resumes")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_resume():
    data = request.form
    filename = f"resumes/{data['name'].replace(' ', '_')}_resume.pdf"
    
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", style='B', size=16)
    pdf.cell(200, 10, "Professional Resume", ln=True, align='C')
    pdf.ln(10)
    
    pdf.set_font("Arial", size=12)
    
    # Personal Information
    pdf.cell(200, 10, f"Name: {data['name']}", ln=True)
    pdf.cell(200, 10, f"Email: {data['email']}", ln=True)
    pdf.cell(200, 10, f"Phone: {data['phone']}", ln=True)
    pdf.cell(200, 10, f"LinkedIn: {data['linkedin']}", ln=True)
    pdf.cell(200, 10, f"Address: {data['address']}", ln=True)
    pdf.ln(5)
    
    sections = [
        ("Professional Summary", "summary"),
        ("Work Experience", "experience"),
        ("Education", "education"),
        ("Skills", "skills"),
        ("Certifications", "certifications"),
        ("Projects", "projects"),
        ("Languages", "languages"),
        ("Volunteer Experience", "volunteer"),
        ("Publications", "publications"),
        ("Awards", "awards"),
        ("References", "references")
    ]
    
    for title, key in sections:
        if data[key].strip():
            pdf.set_font("Arial", style='B', size=14)
            pdf.cell(200, 10, title, ln=True)
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, data[key])
            pdf.ln(5)
    
    pdf.output(filename)
    
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

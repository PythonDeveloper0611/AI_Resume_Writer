from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import os

app = Flask(__name__)

# Resume Generator Function
def generate_resume(name, email, phone, skills, experience):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Resume", ln=True, align="C")
    pdf.ln(10)
    
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, f"Name: {name}", ln=True)
    pdf.cell(200, 10, f"Email: {email}", ln=True)
    pdf.cell(200, 10, f"Phone: {phone}", ln=True)
    pdf.ln(5)
    
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, "Skills:", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, skills)
    pdf.ln(5)
    
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, "Experience:", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, experience)
    
    filename = "resume.pdf"
    pdf.output(filename)
    return filename

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AI Resume Generator</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; background-color: #f4f4f4; padding: 20px; }
            .container { max-width: 500px; margin: auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }
            h1 { color: #333; }
            label, input, textarea { display: block; width: 100%; margin: 10px 0; }
            textarea { height: 100px; }
            .btn { padding: 10px 20px; font-size: 18px; color: white; background: #28a745; border: none; border-radius: 5px; cursor: pointer; }
            .btn:hover { background: #218838; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>AI Resume Generator</h1>
            <form action="/generate" method="post">
                <label for="name">Full Name:</label>
                <input type="text" id="name" name="name" required>
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                
                <label for="phone">Phone:</label>
                <input type="text" id="phone" name="phone" required>
                
                <label for="skills">Skills:</label>
                <textarea id="skills" name="skills" required></textarea>
                
                <label for="experience">Experience:</label>
                <textarea id="experience" name="experience" required></textarea>
                
                <button type="submit" class="btn">Generate Resume</button>
            </form>
        </div>
    </body>
    </html>
    '''

@app.route('/generate', methods=['POST'])
def generate():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    skills = request.form["skills"]
    experience = request.form["experience"]
    
    resume_file = generate_resume(name, email, phone, skills, experience)
    
    return send_file(resume_file, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)

import streamlit as st
import os
import re
from pdf2image import convert_from_path
import pytesseract
import subprocess
from langchain_nvidia_ai_endpoints import ChatNVIDIA
import tempfile


# Set up Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Text cleaning function
def clean_text(text):
    text = text.strip()  # Remove unnecessary spaces at the start and end
    text = re.sub(r'\s+', ' ', text)  # Reduce multiple spaces to one
    text = text.lower()  # Convert text to lowercase
    text = re.sub(r'\n\s*\n', '\n', text)  # Remove blank lines
    return text

def generate_cv_pdf_from_latex(latex_code):
    output_dir = "generated_files"
    os.makedirs(output_dir, exist_ok=True)
    tex_file_path = os.path.join(output_dir, "generated_cv.tex")
    pdf_file_path = os.path.join(output_dir, "generated_cv.pdf")
    log_file_path = os.path.join(output_dir, "generated_cv.log")

    # Prepend \UseRawInputEncoding to handle encoding issues
    latex_code = "\\UseRawInputEncoding\n" + latex_code

    with open(tex_file_path, "w", encoding="utf-8") as tex_file:
        tex_file.write(latex_code)

    try:
        # Run pdflatex twice to resolve cross-references
        subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", tex_file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True
        )
        subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", tex_file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True
        )

        # Check if the PDF was created
        if not os.path.exists(pdf_file_path):
            raise FileNotFoundError(f"PDF file not found: {pdf_file_path}")

    except subprocess.CalledProcessError as e:
        st.error("PDF generation failed. See log details below.")
        if os.path.exists(log_file_path):
            with open(log_file_path, "r", encoding="utf-8") as log_file:
                log_content = log_file.read()
            st.text_area("LaTeX Log File", log_content, height=300)
        return None
    except FileNotFoundError as e:
        st.error(str(e))
        return None

    return pdf_file_path





# Streamlit app starts
st.title("CV Normalizer")
st.write("Upload your CV in PDF format, and we will generate a professional CV for you.")

# File upload
uploaded_file = st.file_uploader("Upload your PDF CV", type=["pdf"])

if uploaded_file is not None:
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        temp_pdf.write(uploaded_file.read())
        pdf_path = temp_pdf.name

    st.write("Extracting text from the PDF...")
    images = convert_from_path(pdf_path)
    text = ""

    for i, image in enumerate(images):
        page_text = pytesseract.image_to_string(image, lang='eng')
        text += page_text

    # Clean the extracted text
    cleaned_text = clean_text(text)
    st.write("Text extraction and cleaning completed.")

    # Prompt construction
    prompt1 = f"""
    Here is the cleaned text extracted from a CV:

    {cleaned_text}

    Based on this cleaned text, generate a structured JSON representation of the CV. Follow this exact JSON format:

    {{
      "Name": "",
      "Contact": {{
        "Email": "",
        "Phone": "",
        "Address": "",
        "LinkedIn": "",
        "GitHub": ""
      }},
      "Profile": "",
      "Skills": [],
      "Languages": {{}},
      "Professional_Experience": [
        {{
          "Position": "",
          "Company": "",
          "Dates": "",
          "Description": ""
        }}
      ],
      "Education": [
        {{
          "Degree": "",
          "Institution": "",
          "Dates": ""
        }}
      ],
      "Projects": [
        {{
          "Name": "",
          "Description": "",
          "Dates": ""
        }}
      ],
      "References": [
        {{
          "Name": "",
          "Position": "",
          "Contact": ""
        }}
      ],
      "Hobbies": [
        {{
          "Hobby": ""
        }}
      ]
    }}
    Make sure the output is exactly only a JSON representation of the CV.
    """

    st.write("Generating structured JSON...")
    client = ChatNVIDIA(
      model="meta/llama-3.1-70b-instruct",
      api_key="YOUR_API_KEY", 
      temperature=0.2,
      top_p=0.7,
      max_tokens=4096,
    )

    response = client.invoke([{"role":"user","content":f"{prompt1}"}])
    structured_json = response.content
    print(structured_json)
    st.write("Structured JSON generated successfully.")

# Load LaTeX template
    with open("TEMPLATE.tex", "r") as file:
       latex_template = file.read()

    with open("EXAMPLE.tex", "r") as file:
       latex_example = file.read()

    with open("J_exa.json", "r") as file:
       Jason_exa = file.read()
    
    # Construct the second prompt
    prompt2 = f"""
    Hello, you are an expert programmer that writes simple and concise LaTeX code. We are working on an AI project that involves extracting information from CVs in PDF format as input and generating a professional CV in PDF format using a specific LaTeX template.

    Your task is as follows:
    1. Take the structured JSON data provided here: {structured_json}.
    2. Use the structured JSON data to populate the given LaTeX template: {latex_template}.
    3. Ensure the output strictly adheres to the provided LaTeX template format.

    To clarify, here is an example:
    - Structured information: {Jason_exa}
    - Corresponding desired LaTeX output: {latex_example}

    You must generate a LaTeX document that follows the same given LaTeX format, filled with the provided data. Feel free to delete any section from the latex code if the information doesn't exist in the structured json data. Please ensure the output is accurate, clean, and directly compatible with LaTeX.

    Remember, your role is to output only the populated LaTeX code, nothing more. Don't add "  ```, latex, ``` " in your output.
    """

    st.write("Generating LaTeX code...")
    client = ChatNVIDIA(
       model="meta/llama-3.3-70b-instruct",
      api_key="your_api_key", 
      temperature=0.2,
      top_p=0.7,
      max_tokens=4096,
    )

    response2 = client.invoke([{"role":"user","content":f"{prompt2}"}])
    latex_code = response2.content
    print(latex_code)
    st.write("LaTeX code generated successfully.")
    

    # Compile LaTeX to PDF
    st.write("Generating PDF from LaTeX...")
    pdf_path = generate_cv_pdf_from_latex(latex_code)
    if pdf_path:
        st.success("CV generated successfully!")
        with open(pdf_path, "rb") as pdf_file:
            st.download_button(
                label="Download Your CV",
                data=pdf_file,
                file_name="generated_cv.pdf",
                mime="application/pdf"
            )
    else:
        st.error("PDF generation failed. Please check the LaTeX code and logs for more details.")

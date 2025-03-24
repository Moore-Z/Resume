import pymupdf
import pdfplumber
import os
from openai import OpenAI
from dotenv import load_dotenv

def readpdf(path):
    doc = pymupdf.open(path)  # open a document
    for page in doc:  # iterate the document pages
        text = page.get_text()  # get plain text encoded as UTF-8





# 2. Read PDF content
def extract_text_from_pdf(pdf_path):
    full_text = ''
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text += text + '\n\n'
    return full_text

# 3. Call OpenAI to convert to Markdown
def convert_to_markdown_with_openai(pdf_text):
    prompt = f"""You are a helpful assistant. Convert the following PDF content to clean, properly formatted Markdown:

            --- START OF PDF CONTENT ---
            {pdf_text}
            --- END OF PDF CONTENT ---
            
            Only return the Markdown output, no explanation.
            """

    response = client.chat.completions.create(model='gpt-4o-mini',
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0.3)
    return response.choices[0].message.content

# 4. Save Markdown to file
def save_markdown(md_text, output_dir='.', filename='converted_output.md'):
    # Ensure output_dir is a valid folder
    if not os.path.isdir(output_dir):
        raise ValueError(f"The output path {output_dir} is not a directory.")

    full_path = os.path.join(output_dir, filename)

    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(md_text)

    print(f"✅ Markdown saved to: {full_path}")

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Example usage
pdf_path = '/Users/henry/Documents/Project/PracticeProject/Resume/data/CV_Ruijie_Zhu_2025.pdf'
output_md = '/Users/henry/Documents/Project/PracticeProject/Resume/data'
output_mdFile_name = 'ResumeOutput.md'

pdf_text = extract_text_from_pdf(pdf_path)
markdown_result = convert_to_markdown_with_openai(pdf_text)
save_markdown(markdown_result, output_md,output_mdFile_name)

print("✅ PDF converted to Markdown and saved to", output_md)


# # Example usage
# pdf_file = "data/CV_Ruijie_Zhu_2025.pdf"
# markdown_file = "data"
# pdf_to_markdown(pdf_file, markdown_file)
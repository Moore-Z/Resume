import os


# 1. Create a markdown version of your resume (Note: ChatGPT can do this for you).
# 2. Experiment with different prompt templates that take your markdown resume and
# a job description and output a new resume in markdown.
# 3. Use OpenAI’s Python API to prompt GPT-4o-mini to rewrite your resume dynamically.
# 4. Convert the markdown file to HTML and then to PDF with the markdown and pdfkit libraries,
# respectively.

import pymupdf  # imports the pymupdf library
import openai
from dotenv import load_dotenv

from src.core import save_markdown
from src.readMarkdown import readfile




if __name__ == "__main__":
    load_dotenv()
    resume_md = '/Users/henry/Documents/Project/PracticeProject/Resume/data/ResumeOutput.md'
    jobdescription = '/Users/henry/Documents/Project/PracticeProject/Resume/data/JobDescription.txt'

    md_resume = readfile(resume_md)
    job_desciption = readfile(jobdescription)
    # prompt (assuming md_resume and job_desciption have been defined)
    prompt = f"""
    I have a resume formatted in Markdown and a job description. \
    Please adapt my resume to better align with the job requirements while \
    maintaining a professional tone. Tailor my skills, experiences, and \
    achievements to highlight the most relevant points for the position. \
    Ensure that my resume still reflects my unique qualifications and strengths \
    but emphasizes the skills and experiences that match the job description.

    ### Here is my resume in Markdown:
    {md_resume}

    ### Here is the job description:
    {job_desciption}

    Please modify the resume to:
    - Use keywords and phrases from the job description.
    - Adjust the bullet points under each role to emphasize relevant skills and achievements.
    - Make sure my experiences are presented in a way that matches the required qualifications.
    - If my experience does not have curtain requirement, add the experience with some make up experience and work story to my work experience area
    - Maintain clarity, conciseness, and professionalism throughout.

    Return the updated resume in Markdown format.

    """

    # make api call
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature = 0.25
    )

    print("This is full respond: \n \n", response)

    # extract response
    resume = response.choices[0].message.content

    # Example usage
    output_md = '/Users/henry/Documents/Project/PracticeProject/Resume/data'
    output_mdFile_name = 'modifiedResume.md'

    save_markdown(resume, output_md, output_mdFile_name)

    print("✅ JD based Optimized Resume to Markdown and saved to", output_md)



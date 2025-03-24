import markdown

# resume_md = '/Users/henry/Documents/Project/PracticeProject/Resume/data/ResumeOutput.md'
# jobDescription = '/Users/henry/Documents/Project/PracticeProject/Resume/data/JobDescription.txt'
# f = open(jobDescription, 'r')
# resumeMarkdown = markdown.markdown(f.read())
#
# print(type(resumeMarkdown))

def readfile(path):
    f = open(path, 'r')
    resume_markdown = markdown.markdown(f.read())
    return resume_markdown
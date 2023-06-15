import re

resume_text = ""

# Read resume text from a text file
file_path = 'static/uploads/Resumewords.txt'
try:
    with open(file_path, 'r') as file:
        resume_text = file.read()
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
    exit()

phone_regex = re.compile(r'\b(?:\+\d{1,3}\s+)?\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})\b')
email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

phone_number = re.search(phone_regex, resume_text)
email = re.search(email_regex, resume_text)  # Using re.I flag for case-insensitive matching

phone_number = phone_number.group(0) if phone_number else None
email = email.group(0) if email else None

if phone_number:
    print("Phone number:", phone_number)
else:
    print("Phone number not found in the resume.")

if email:
    print("Email:", email)
else:
    print("Email not found in the resume.")

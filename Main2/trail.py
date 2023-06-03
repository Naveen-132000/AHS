import re

file_list = ["static/uploads/Rmerged.txt", "static/uploads/JDmerged.txt"]
resume_text = ""
skills_set1 = set()

for file_name in file_list:
    with open(file_name, 'r') as file:
        if file_name == "static/uploads/Rmerged.txt":
            resume_text = file.read()
        else:
            skills_list = [line.strip() for line in file.readlines()]
            pattern = re.compile("|".join(map(re.escape, skills_list)), re.IGNORECASE)
            matches = re.findall(pattern, resume_text.upper())
            skills_set1.update(matches)

with open("static/uploads/Common.txt", "w") as f:
    for skill in skills_set1:
        f.write(skill + "\n")

total_skills_file1 = len(set([line.strip() for line in open(file_list[0], 'r')]))
match_rate = len(skills_set1) / total_skills_file1 * 100
match_rate = round(match_rate)

print("Match Rate: ", match_rate)
print("Extracted Skills: ", skills_set1)

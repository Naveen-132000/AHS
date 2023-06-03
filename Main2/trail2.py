import re
hfile_list = ["static/uploads/Rskills.txt", "static/uploads/Jskills.txt"]
hresume_text = ""
hskills_set1 = set()

for hfile_name in hfile_list:
    with open(hfile_name, 'r') as hfile:
        if hfile_name == "static/uploads/Rskills.txt":
            hresume_text = hfile.read()
        else:
            hskills_list = [line.strip() for line in hfile.readlines()]
            hpattern = re.compile("|".join(map(re.escape, hskills_list)), re.IGNORECASE)
            hmatches = re.findall(hpattern, hresume_text.upper())
            hskills_set1.update(hmatches)

htotal_skills_file1 = len(set([line.strip() for line in open(hfile_list[0], 'r')]))
hmatch_rate = len(hskills_set1) / htotal_skills_file1 * 100
hmatch_rate = round(hmatch_rate)

print("Match Rate: ", hmatch_rate)
print("Extracted Skills: ", hskills_set1)

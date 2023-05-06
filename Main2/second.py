from flask import Blueprint,render_template
from serpapi import GoogleSearch

second = Blueprint("second",__name__,static_folder="static",template_folder="templates")
@second.route("/",methods=["POST","GET"])


def home():
    file2 = open('static/uploads/TandL.txt','w',encoding="utf-8")
    file1=open('static/uploads/Rskills.txt','r')
    lines=file1.readlines()
    count=0
    for line in lines:
        count+=1
        params = {
    "api_key": "f9efcd58e8de137f2122cc2f86e66e786fa3b1ab247fafedba4e440b3b9ee7c1",
    #"api_key": "9998b610e8e9fe2032ab34da16f4639cd13d17e2b30d01e9835d25983afa321c",
 
    "engine": "google",
    "q": line+" jobs india",
    "location": "Austin, Texas, United States",
    "google_domain": "google.com",
    "gl": "us",
    "hl": "en",
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        try:
            for result in results["jobs_results"]["jobs"]:
                title=result["title"]   
                link=result["link"]
                print(title)
                print(link)
                #file2.write(title,end=",")
                #file2.write(link,end="\n")
                print(title,file=file2,end=", ")
                print(link,file=file2,end="\n")
        except:
           pass
    titles_and_links = []
    with open('static/uploads/TandL.txt', 'r') as f:
        for line in f:
            try:
                title, link = line.strip().split(',',1)
                titles_and_links.append((title, link))
            except ValueError:
                pass
                
    return render_template('scraped.html',titles_and_links=titles_and_links)
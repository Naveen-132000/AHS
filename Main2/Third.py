from flask import Blueprint, render_template

third=Blueprint("third",__name__,static_folder="static",template_folder="templates")
@third.route("/",methods=["POST","GET"])

def home():
    return render_template("compare.html")
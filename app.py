from flask import Flask,render_template,request,redirect, url_for

app=Flask(__name__)



@app.route("/search") 
def search():
    return render_template("search.html")


@app.route("/display",methods=["POST"])
def display():
    name=request.form.get("name")
    print(name)
    data=search(name)
    print(data)
    return render_template("display.html",data=data)


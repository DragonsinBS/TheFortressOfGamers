from flask import Flask,render_template,request,redirect, url_for
from functions import basicfunction
from properties import file_info

tables={}
for table_info in file_info:
    tables[table_info["name"]]=basicfunction(table_info)



app=Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
@app.route("/search") 
def search():
    return render_template("search.html")


@app.route("/display",methods=["POST","GET"])
def display():
    if request.method=="GET":
        name=request.args.get("pkey")
        table_name=request.args.get("table_name")
    elif request.method=="POST":    
        name=request.form.get("name")
        table_name=request.form.get("table_name")
    
    data=tables[table_name].search(name)
    if data is False:
        return "file not found"
    data["table_name"]=table_name
    return render_template("display.html",data=data)

@app.route("/<string:table_name>/update/<string:pkey>", methods=['GET','POST'])
def update(pkey,table_name):
    if request.method=="GET":
        return render_template("update.html",pkey=pkey,table_name=table_name)
    data={}
    data["genre"]=request.form.get("genre")
    data["writter"]=request.form.get("writter")
    data["name"]=pkey
    print(data)
    tables[table_name].update(pkey,data)
    
    print(pkey)
    return redirect(url_for("display",table_name=table_name,pkey=pkey))
    
@app.route("/<string:table_name>/delete/<string:pkey>", methods=['GET','POST'])
def delete(pkey,table_name):
    if request.method=="GET":
        if tables[table_name].delete(pkey):
            return redirect(url_for("index"))
        else:
            return " record not found"

@app.route("/insert", methods=['GET','POST'])
def insert():
    if request.method=="GET":
        return render_template("insert.html")
    data=request.form.to_dict()
    table_name = request.form["table_name"]
    tables[table_name].insert(data)
    return redirect(url_for("display",table_name=table_name,pkey=data["name"]))

if __name__=="__main__":
    app.run(debug=True)
    

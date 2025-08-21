from flask import Flask, render_template, render_template_string, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///rs_data.db"
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////home/RealityStudios/App/rs_data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

CORRECT_PASSWORD = "c793f8a09df6465e9faf2625a978af7e617928c01911141a5250dbe162b24469"

class Data(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  text = db.Column(db.String(255), nullable=False)
  date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
  
with app.app_context():
  db.create_all()

@app.route("/", methods=["POST", "GET"])
def index():
  data = request.form.get("data") 
  
  if request.method == "POST":
    if data:
      new_data = Data(text=data)
      db.session.add(new_data)
      db.session.commit()
    
  return render_template("index.html")

@app.route("/data", methods=["GET"])
def data():
  getData = None
  password = request.args.get("p", "")
  
  try:
    getData = Data.query.all()
    if getData:
      ReverseData(getData)
  except:
    pass
  
  if (CORRECT_PASSWORD == password):
    return render_template("data.html", data=getData)
  else:
    return render_template_string("<h1 style='font-family: monospace'> <a href='/'>Incorrect password, go back</a> </h1>")

def ReverseData(getData):
  sort = True
  while sort:
    sort = False
    
    for i in range(len(getData) - 1):
      if (getData[i].id < getData[i + 1].id):
        temp = getData[i]
        getData[i] = getData[i + 1]
        getData[i + 1] = temp

        sort = True
        
@app.route("/clear", methods=["POST"])
def clear():
  db.drop_all()
  
  return render_template_string("<h1 style='font-family: monospace'> <a href='/'>data cleared, back</a> </h1>")

@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
  deleteRow = Data.query.get_or_404(id)
  db.session.delete(deleteRow)
  db.session.commit()
  
  return redirect("/")

if __name__ == "__main__":
  app.run(debug=True)
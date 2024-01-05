import shutil
import os
from flask import *
from flask import render_template, redirect, send_file
import datetime

def verify(customerid,passcode,password,dob):
	if (customerid in os.listdir("accounts")):
		if (open("accounts/"+customerid+"/data","r").read().split("\n") == [passcode,password,dob] and open("accounts/"+customerid+"/status","r").read() == "unlocked"):
			return True
		else:
			open("accounts/"+customerid+"/attempts/data","a").write(str(datetime.datetime.now()).split(".")[0]+"\n")
			r = open("accounts/"+customerid+"/attempts/data","r").read().split("\n")
			t=[]
			for i in r:
				t.append(i.split(" ")[0])
			if (t[0] == t[1] and t[1] == t[2]):
				open("accounts/"+customerid+"/status","w").write("locked")
			return False
	else:
		return False

app = Flask(__name__, template_folder=os.getcwd(), static_folder="static")

@app.route("/", methods=["GET","POST"])
def a():
	if request.method == "GET":
		return render_template("index.html", msg="none")
	else:
		w = [request.form["customerid"], request.form["passcode"], request.form["password"], request.form["dob"]]
		if verify(w[0],w[1],w[2],w[3]):
			return render_template("check.html",msg="y")
		else:
			return render_template("index.html", msg="Either Wrong crendential or your customer id is locked")

@app.route("/second_auth")
def b():
		return render_template("second_auth.html")

@app.route("/get_secure_image/<customerid>/<passcode>/<password>/<dob>", methods=["GET","POST"])
def c(customerid, passcode,password,dob):
	if verify(customerid, passcode,password,dob):
		img = os.listdir(f"accounts/{customerid}/secure/")[0]
		return send_file(f"accounts/{customerid}/secure/"+img)
	else:
		return "static/image-1.jpg"

@app.route("/dashboard")
def d():
	return render_template("dashboard.html")

if __name__ == '__main__':
	app.run()
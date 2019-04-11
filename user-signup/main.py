from flask import Flask, request, redirect, render_template 
import urllib.parse
import cgi 
import os 


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    username_error= request.args.get("username_error")
    password_error= request.args.get("password_error")
    password_error2= request.args.get("password_error2")
    email_error= request.args.get("email_error")
    #encoded_error = request.args.get("error")
    return render_template("form.html", username_error=username_error, password_error=password_error, password_error2=password_error2, email_error=email_error)

#username_error = False
#password_error = False
#email_error = False

@app.route("/welcome", methods=["POST"])
def welcome():
    username = request.form["username"]
    password = request.form["password"]
    email = request.form["email"]
    verify_password = request.form["verify_password"]
    no_error = True
    #username_error = ""
    #password_error = ""
    #password_error2 = ""
    #email_error = ""
    #errors = ""
    params = {
        "username_error": "",
        "password_error": "",
        "password_error2": "",
        "email_error": "",
    }
    if (len(username) < 3 or len(username) > 20) or ((not username) or username.strip() == "") or " " in username: 
        params["username_error"] = "Username MUST be between 3-20 characters long and cannot have any spaces."
        #errors += username_error
        no_error = False
    if (len(password) > 20 or len(password) < 3) or (" " in password) or ((not password) or password.strip() == ""):
        params["password_error"] = "Password MUST be between 3-20 characters long and cannot have any spaces."
        #errors += password_error
        no_error = False
    if verify_password != password:
        params["password_error2"] = "Make sure password is the same in both boxes."
        #errors += password_error2
        #password = ""
        no_error = False
    if len(email)>0 and ("@" and ".") not in email:
        params["email_error"] = "Please enter a valid email address."
        #errors += email_error
        no_error = False

    if not no_error:
        query_string = urllib.parse.urlencode(params)
        return redirect("/?" + query_string)
        #return render_template("form.html", username_error=username_error, password_error=password_error, password_error2=password_error2, email_error=email_error)
    else:
        return render_template("welcome_page.html", username=username)

@app.route("/?error=", methods=["POST", "GET"])
def error_display():
    username_error= request.args.get("username_error")
    password_error= request.args.get("password_error")
    password_error2= request.args.get("password_error2")
    email_error= request.args.get("email_error")

    return render_template("form.html", username_error=username_error, password_error=password_error, password_error2=password_error2, email_error=email_error)
app.run()
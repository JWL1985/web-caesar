from flask import Flask, request, redirect, render_template 
import urllib.parse
import cgi 
import os 


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/", methods=["GET", "POST"])
def index():
    errors = ""
    if request.method == "POST":
        if request.form:
            errors = validate_form()
            if errors:
                return render_template("form.html", error=errors)
            else:    
                return render_template("welcome_page.html", username=request.form["username"])    

    else:
        return render_template("form.html", error=errors)

def validate_form():
    username = request.form["username"]
    password = request.form["password"]
    email = request.form["email"]
    verify_password = request.form["verify_password"]

    errors = {}

    if (len(username) < 3 or len(username) > 20) or ((not username) or username.strip() == "") or " " in username: 
        errors["username_error"] = "Username must be between 3-20 characters and cannot contain any spaces"
    if (len(password) > 20 or len(password) < 3) or (" " in password) or ((not password) or password.strip() == ""):
        errors["password_error"] = "Password must be between 3-20 characters and cannot have any spaces."
    if verify_password != password:
        errors["password_error2"] = "Make sure password is the same in both boxes."
    if len(email)>0 and ("@" and ".") not in email:
        errors["email_error"] = "Please enter a valid email address."
    if errors:
        return errors



app.run()
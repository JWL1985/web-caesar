from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
    <style>
        body {
            background-color: #F5F5F5;
        }
        div.main_form {
            margin-top: 100px;
            display: block;
            background-color: #00FF7F;
            padding: 20px;                margin: 0 auto;
            width: 540px;
            font: 16px sans-serif;
            border-radius: 20px;
            }
        .main_form label {
            font-size: 18px;
            margin: 10px 0;
            width: 540px;
            height: 120px;
            }
        .main_form form {
            text-align: left;
        }

        .main_form input {
            width: 80%;
            height: 25px;
            display: block;
            background-color: #F0FFF0;
        }

        #sub_button {
            text-align: center;
            margin: 0px auto;
            width: 200px;
            height: 50px;
            font-size: 30px;
            font-weight: bold;
            border-radius: 15px;
            box-shadow: 4px 4px 4px 4px;
        }

        .main_form .submit {
            margin-top: 20px;
            margin-left: 20px;
            margin-right: 20px;
            width: 50%;
            text-align: center;
        }

        .main_form h1 {
            text-align: center;
            text-shadow: -1px 0 white, 0 1px white, 1px 0 white, 0 -1px white;
            text-transform: uppercase;
            font-size: 40px;
        }

    </style>
    </head>
    <body>
    <div class= "main_form">
        <h1>Sign-Up Form</h1>
        <form action= "/" method= "POST">            
            <label for= "username" value= "">Username:</label>
            <input id= "username" type= "text" name= "username" /><br>
            <label for= "password" value= "">Password:</label>
            <input type= "password" name= "password" /><br>
            <label for= "email" value= "">E-Mail:</label>
            <input type= "email" name= "email" /><br>           
            <input id="sub_button" type= "submit"/>
        </form>
    </div>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

app.run()
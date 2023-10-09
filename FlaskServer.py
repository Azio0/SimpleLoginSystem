#Imports of external modules
import secrets
from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)

#Really unsecured method of handling logins, would recommend this is updated to what ever handling system you use
users = {
    "Root" : "Root"
}

#Handles the user logging into the website
@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == "POST":
        if request.form.get("username") != None: #Stops the error notice being returned on the logout page. Temporary fix.
            if request.form.get("username") in users and request.form.get("password") == str(users[request.form.get("username")]):
                return Dashboard()
            else:
                flash('error_notify')

    return render_template('Login.html')

#Main page after login
@app.route("/dashboard/", methods = ['POST'])
def Dashboard():
    return render_template('Dashboard.html')

#Logs the user out
@app.route("/logout/", methods=['GET', 'POST'])
def return_to_login():
    return redirect("/", code=301)

#Error Handling
@app.errorhandler(404)
def page_not_found(e):
    return redirect("/", code=301)

@app.errorhandler(405)
def method_not_allowed(e):
    return redirect("/", code=301)

#Launches App
if __name__ == "__main__":
    app.secret_key = secrets.token_urlsafe(32) # Enables the flash command
    app.run(port=80,host='0.0.0.0', debug=True)
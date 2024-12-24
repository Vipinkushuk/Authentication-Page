from flask import Blueprint,render_template,redirect,url_for,Request
auth = Blueprint("auth",__name__)


@auth.route('/login', methods=['GET','POST'])
def login():

    email = Request.user.get("email")
    password = Request.user.get("password")
    return render_template("login.html")
    
@auth.route('/sign_up', methods=['GET','POST'])
def sign_up():

    email = Request.user.get("email")
    username = Request.user.get("username")
    password1 = Request.user.get("password1")
    password2 = Request.user.get("password2")
    return render_template("sign_up.html")
    
@auth.route('/logout')
def logout():
    return redirect(url_for("views.home"))

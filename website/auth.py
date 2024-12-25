from flask import Blueprint,render_template,redirect,url_for,request,flash
auth = Blueprint("auth",__name__)


@auth.route('/login', methods=['GET','POST'])
def login():
    email = request.form.get("email")
    password1 = request.form.get("password1")
    return render_template("login.html")
    
@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        user_name = request.form.get('user_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(user_name) < 2:
            flash('Username must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            flash('Account created successfully!', category='success')
            # You can redirect after successful action
            return redirect(url_for('auth.login'))  # assuming you have a login route

    return render_template('sign_up.html')

    
@auth.route('/logout')
def logout():
    return redirect(url_for("auth.login"))

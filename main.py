from flask import Flask, redirect, url_for, render_template, request, session
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = 'your-secret-key'

app.config['MYSQL_HOST'] = 'tpm-tool-db.cp7vhrqeultj.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'nMatexaMaciN8'
app.config['MYSQL_DB'] = 'qmiprocess'


bcrypt = Bcrypt()

# login_manager = LoginManager()

# @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)
# login_manager.init_app(app)

# Define your User class here if needed
# login_manager.init_app(app)

# class User(UserMixin):
#     def __init__(self, user_id):
#         self.id = user_id

# @login_manager.user_loader
# def load_user(user_id):
#     return User(user_id)

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    submit = SubmitField('Login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        # Check username and password against your database here
        if username == 'admin' and password == 'admin':  # Example authentication
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html', form=form)

@app.route('/', methods=['GET', 'POST'])
@login_required
def dashboard():
   return render_template('index.html')

@app.route('/questions/general')
def general():
   return render_template('general.html')

@app.route('/questions/process')
def process():
   return render_template('process.html')

@app.route('/questions/delivery')
def delivery():
   return render_template('delivery.html')

@app.route('/questions/compliants')
def compliants():
   return render_template('compliants.html')

@app.route('/auditor')
@login_required
def auditor():
   return render_template('auditor.html')

@app.route('/auditor/audits')
@login_required
def audits():
   return render_template('audits.html')

@app.route('/auditor/auditorreview')
@login_required
def auditorreview():
   return render_template('auditorreview.html')

@app.route('/admin')
@login_required
def admin():
   return render_template('admin.html')

@app.route('/admin/qmanage')
@login_required
def qmanage():
   return render_template('qmanage.html')

@app.route('/admin/pmanage')
@login_required
def pmanage():
   return render_template('pmanage.html')

if __name__ == "__main__":
    app.run(debug=True)

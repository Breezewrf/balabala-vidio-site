from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import StringField, SubmitField, PasswordField


# 这里不能用Form，会报错，必须from flask_wtf import FlaskForm

class LoginForm(FlaskForm):
    name = StringField('用户名',
                       validators=[Length(min=6, max=12, message='用户名长度为6~12位'), DataRequired(message='用户名不能为空')])
    password = PasswordField('密码',
                             validators=[Length(min=6, max=12, message='密码长度为6~12位'), DataRequired(message='密码不能为空')])
    submit = SubmitField('登录')


app = Flask(__name__)
app1 = Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess'


@app.errorhandler(404)
# 这个e不能少！
def page_not_found(e):
    return render_template('404.html')


@app.route('/', methods=['GET', 'POST'])
def base():
    name = None
    myform = LoginForm()
    if myform.validate_on_submit():
        name = myform.name.data
        myform.name.data = ''
    return render_template('login.html', form=myform, name=name)


@app.route('/user/<name>', methods=['GET', 'POST'])
def index(name):
    # name = None
    print("@@@")
    # form = LoginForm()
    # if form.validate_on_submit():
    #    name = form.name.data
    #    form.name.data = ''
    return render_template('base.html')


if __name__ == '__main__':
    app.run()
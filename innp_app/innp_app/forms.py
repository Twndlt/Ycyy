from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, BooleanField, SubmitField)
from wtforms.validators import (DataRequired, length)


class LoginForm(FlaskForm):
    """
    用户登录
    author：吴有为
    time：2018-4-26
    """
    username = StringField(
        validators=[
            DataRequired(u"用户名不存在"),
            length(1, 20)
        ]
    )
    password = PasswordField(
        validators=[
            DataRequired(u"密码错误"),
            length(1, 20)
        ]
    )
    remember_me = BooleanField('记住我')

    submit = SubmitField('登录')


class RegisterForm(FlaskForm):
    """
    注册表单
    """
    pass

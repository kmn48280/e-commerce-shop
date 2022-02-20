from .import bp as auth
from .forms import LoginForm, RegisterForm, EditProfileForm
from flask import render_template, request, flash, redirect, url_for
from app.models import User 
from flask_login import login_user, current_user, logout_user, login_required 

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = request.form.get('email').lower()
        password = request.form.get('password')
        u = User.query.filter_by(email=email).first()
        if u and u.check_hashed_password(password):
            login_user(u)
            flash('Welcome to my store!', 'success')
            return redirect(url_for('main.index'))
        flash('Sorry, your email/password combo is incorrect', 'danger')
        return render_template('login.html.j2', form = form)
    # flash('meow', 'danger')
    return render_template('login.html.j2', form = form)

@auth.route('/logout')
@login_required
def logout():
    if current_user:
        logout_user()
        flash('You have successfully logged out! See you soon!', 'warning')
        return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        new_user_data = {
            'first_name': form.first_name.data.title(),
            'last_name': form.last_name.data.title(),
            'email': form.email.data.lower(),
            'password': form.password.data
        }
        new_user_object = User()
        new_user_object.from_dict(new_user_data)
        new_user_object.save()
        flash('You have successfully registered! Please Login', 'success')
        return redirect(url_for('auth.login'))
    else:
        flash('Sorry, there was an unexpected error creating your account. Please try again!', 'danger')
        return render_template('register.html.j2', form = form)

@auth.route('/edit_profile', methods = ['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if request.method == 'POST' and form.validate_on_submit():
        new_user_data={
            'first_name': form.first_name.data.title(),
            'last_name': form.last_name.data.title(),
            'email': form.email.data.lower(), 
            'password': form.email.data
        }
        u = User.query.filter_by(email = form.email.data.lower()).first()
        if u and u.email != current_user.email:
            flash('Sorry, that email is taken. Please use another email address', 'danger')
            return render_template('register.html.j2', form = form)
        else:
            current_user.from_dict(new_user_data)
            current_user.save()
            flash('Your profile has been updated!', 'success')
            return redirect(url_for('main.index'))
    return render_template('register.html.j2', form=form)







from .import bp as main 
from flask_login import login_required
from .forms import SearchForm
from flask import request, flash, render_template, redirect, url_for
from app.models import *



@main.route('/', methods =['GET', 'POST'])
@login_required
def index():
    form = SearchForm()
    if request.method == 'POST' and form.validate_on_submit():
        char_name = request.form.get('character_name')
        category = Category.query.filter_by(name = char_name).first()
        if category:
            items_in_category = category.products
            flash('Here are the items we currently carry', 'success')
            return render_template('show_items.html.j2', items_in_category = items_in_category)
        else:
            flash('Sorry, we do not have any more items of that character!', 'danger')
            return render_template('index.html.j2', form = form)
    return render_template('index.html.j2', form=form)

@main.route('/about')
def about():
    return render_template('about.html.j2')


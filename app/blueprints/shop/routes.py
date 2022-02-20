from .import bp as shop
from flask_login import login_required, current_user
from flask import render_template, redirect, url_for, flash
from app.models import *


@shop.route('/show_all_items')
@login_required
def show_all_items():
    all_items = Item.query.all()
    return render_template('show_items.html.j2', all_items = all_items)


    #    category = Category.query.filter_by(name = char_name).first()
    #     if category:
    #         items_in_category = category.products

@shop.route('/select_item/<int:id>', methods=['GET','POST'])
@login_required
def select_item(id):
    item = Item.query.get(id)
    if item in current_user.user_cart:
        flash('You can only purchase each item once (1x)! Take a look at our other items!', 'danger')
        return redirect(url_for('shop.show_all_items'))
    else:
        current_user.add_item(id)
        flash('You have successfully added this item to your cart!', 'success')
        return redirect(url_for('shop.view_cart'))
 
        # print('meow')
        # return redirect(url_for('shop.show_all_items'))

@shop.route('/view_cart')
@login_required
def view_cart():
    shopping_cart = current_user.user_cart
    if len(list(shopping_cart)) == 0:
        flash('Your cart is empty! Add some items on our search page!')
        return redirect(url_for('main.index'))
    else:
        return render_template('cart.html.j2', shopping_cart = shopping_cart)

@shop.route('/remove_item/<int:id>')
@login_required
def remove_item(id):
    current_user.delete_item(id)
    flash('You have removed this item', 'warning')
    return redirect(url_for('shop.view_cart'))

@shop.route('/checkout')
@login_required
def checkout():
    if len(list(current_user.user_cart)) == 0:
        flash('Your cart is empty! Add some items on our search page!')
        return redirect(url_for('main.index'))
    shopping_cart = current_user.user_cart
    return render_template('checkout.html.j2', shopping_cart = shopping_cart)

@shop.route('/pay')
@login_required
def pay():
    current_user.clear_cart()
    flash('Thank you for shopping with us!', 'success')
    return render_template('about.html.j2')



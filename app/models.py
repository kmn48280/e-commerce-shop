from app import db, login
from flask_login import UserMixin
from datetime import datetime as dt 
from werkzeug.security import generate_password_hash, check_password_hash
from flask import flash


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    desc = db.Column(db.Text)
    price = db.Column(db.Float) 
    img = db.Column(db.String(200))
    created_on = db.Column(db.DateTime, index=True, default =dt.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
  

    def __repr__(self):
        return f'<Item: {self.id} | {self.name}>'

    def from_dict(self, data):
        for field in ['name', 'desc', 'price', 'img', 'category_id']:
            setattr(self, field, data[field])
        
    def save(self):
        db.session.save(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(200))
    created_on = db.Column(db.DateTime, default = dt.utcnow)
    user_cart = db.relationship(
        'Item', 
        secondary = 'cart', #needs to be 'cart' NOT 'Cart'--b/c ref SQL
        backref= 'purchaser', #optional b/c it will return a list of user's that have items in cart
        lazy='dynamic')

    def __repr__(self):
        return f'<User: {self.id} | {self.email}>'
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def from_dict(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = self.hash_password(data['password'])
    
    def hash_password(self, original_password):
        return generate_password_hash(original_password)
    
    def check_hashed_password(self, login_password):
        return check_password_hash(self.password, login_password)
    
    def add_item(self, id):
        item = Item.query.get(id)
        self.user_cart.append(item)
        db.session.commit()
        return flash("f'You have added {item.name} to your cart. Your total is: ${self.total()}.'", "success")
        
    def delete_item(self, id):
        item = Item.query.get(id)
        self.user_cart.remove(item)
        db.session.commit()
        return flash("f'You have removed {item.name} from your cart, your total is now: ${self.total()}.'", "success")
    
    def clear_cart(self):
        while len(list(self.user_cart)) >0:
            for item in self.user_cart:
                self.user_cart.remove(item)
        db.session.commit()
        return flash('You have cleared your cart', 'warning')

    def total(self):
        total = 0
        for item in self.user_cart:
            total += item.price
        return total 
    
    def tax(self):
        serv_tax = self.total() * .20
        return serv_tax
    
    def final_total(self):
        final_total = self.total() + self.tax()
        return final_total
    




@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    level = db.Column(db.Integer)
    products = db.relationship('Item', cascade='all, delete-orphan', backref='cat', lazy='dynamic')

    def __repr__(self):
        return f'<Category: {self.id} | {self.name}>'
    
    # def char_category_items(self, id):
    #     char_id = Category.query.filter_by(id = char_id).first()
    #     char_products = char_id.products
    #     render_template()


class Cart(db.Model):
    user_id = db.Column(db.ForeignKey('user.id'), primary_key = True)
    item_id = db.Column(db.ForeignKey('item.id'), primary_key = True)
    created_on = db.Column(db.DateTime, default= dt.utcnow)

   



















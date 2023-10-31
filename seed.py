from models import Cupcake
from app import app
from init import db 


with app.app_context():
    db.drop_all()
    db.create_all()


cupcakes = [
    Cupcake(flavor="Red Velvet", size="large", rating=7.3, image="https://sallysbakingaddiction.com/wp-content/uploads/2014/10/Red-Velvet-Cupcakes-6.jpg"),
    Cupcake(flavor="Super Moist Chocolate", size="large", rating=8.7, image="https://sallysbakingaddiction.com/wp-content/uploads/2017/06/moist-chocolate-cupcakes-5.jpg"),
    Cupcake(flavor="Pumpkin Spice Cupcakes with Marshmallow Frosting", size="medium", rating=7.8, image="https://sallysbakingaddiction.com/wp-content/uploads/2014/11/Spiced-Pumpkin-Cupcakes-with-fluffy-marshmallow-frosting.jpg"),
    Cupcake(flavor="Banana Cupcakes with Cinnamon Cream Cheese Frosting", size="small", rating=8.5, image="https://sallysbakingaddiction.com/wp-content/uploads/2017/08/banana-cupcakes-cinnamon-cream-cheese-frosting.jpg"),
    Cupcake(flavor="Brown Sugar Butterscotch Cupcakes", size="medium", rating=6.3, image="https://sallysbakingaddiction.com/wp-content/uploads/2013/11/Butterscotch-Filled-Brown-Sugar-Cupcakes-by-sallysbakingaddiction.com_.jpg"),
    Cupcake(flavor="Peppermint Mocha Cupcakes", size="large", rating=7.4, image="https://sallysbakingaddiction.com/wp-content/uploads/2013/11/delicious-peppermint-mocha-cupcakes.jpg"),
    Cupcake(flavor="Strawberry Cupcakes with Strawberry Buttercream", size="large", rating=9.4, image="https://sallysbakingaddiction.com/wp-content/uploads/2015/04/Strawberry-Cupcakes-with-Creamy-Strawberry-Frosting-2.jpg"),
    Cupcake(flavor="Lemon Cupcakes with Vanilla Frosting", size="small", rating=6.9, image="https://sallysbakingaddiction.com/wp-content/uploads/2013/04/the-best-lemon-cupcakes-2.jpg"),
    Cupcake(flavor="S’mores Brownie Cupcakes", size="medium", rating=3.5, image="https://sallysbakingaddiction.com/wp-content/uploads/2017/08/smores-brownie-cupcakes-2.jpg"),
    Cupcake(flavor="Cookies & Cream Cupcakes with Chocolate Frosting", size="small", rating=3.6, image="https://sallysbakingaddiction.com/wp-content/uploads/2013/05/Cookies-n-Cream-Milk-Chocolate-Cupcakes.jpg"),
]

with app.app_context():
    db.session.add_all(cupcakes)
    db.session.commit()

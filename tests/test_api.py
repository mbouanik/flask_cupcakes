from unittest import TestCase
from init import create_app, db
from models import Cupcake
import os

app = create_app()
app.config['SQLALCHEMY_DATABASE_URI']= os.getenv("URI_TEST")
app.config["SQLALCHEMY_ECHO"] = False
app.config["TESTING"] = True

db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

cupcake_one = {
    "flavor":"Chocolate Fudge",
    "size":"large",
    "rating":8.7,
    "image":None
}

cupcake_two = {
    "flavor":"Strawberry Pineapple",
    "size":"medium",
    "rating":8.9,
    "image":"https://www.yourcupofcake.com/wp-content/uploads/2014/03/Strawberry-Pineapple-Greek-Yogurt-Cupcakes.jpg"
}

class ApiTest(TestCase):
    def setUp(self):
        with app.app_context():
            Cupcake.query.delete()
            cupcake = Cupcake(**cupcake_one)
            db.session.add(cupcake)
            db.session.commit()
            self.client = app.test_client()
            self.cupcake_id = cupcake.id
            self.cupcake = cupcake

    def tearDown(self):
        with app.app_context():
            db.session.rollback()
    
    def test_list_cupcakes(self):
        res =  self.client.get("/api/cupcakes")
        data = res.json

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data, {
            "cupcakes": [
                {
                "id": self.cupcake.id,
                "flavor": "Chocolate Fudge",
                "size": "large",
                "rating": 8.7,
                "image": "https://tinyurl.com/demo-cupcake"
                },
            ]
        })
    

    def test_get_cupcake(self):
        res = self.client.get(f"/api/cupcakes/{self.cupcake.id}")
        data = res.json

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data, {
            "cupcake": 
                {
                "id": self.cupcake.id,
                "flavor": "Chocolate Fudge",
                "size": "large",
                "rating": 8.7,
                "image": "https://tinyurl.com/demo-cupcake"
                }
            
        })

    def test_create_cupcake(self):
        res = self.client.post('/api/cupcakes', json=cupcake_two)
        data = res.json

        self.assertEqual(res.status_code, 201)
        if data:
            self.assertIsInstance(data['cupcake']['id'], int)
            del data['cupcake']['id']
        self.assertEqual(data, {
            "cupcake":{
                "flavor":"Strawberry Pineapple",
                "size":"medium",
                "rating":8.9,
                "image":"https://www.yourcupofcake.com/wp-content/uploads/2014/03/Strawberry-Pineapple-Greek-Yogurt-Cupcakes.jpg"
            }
        })



    def test_update_cupcake(self):
        cupcake_one['flavor'] = "Strawberry"
        cupcake_one['image']= self.cupcake.image
        res = self.client.patch(f"/api/cupcakes/{self.cupcake.id}", json=cupcake_one)
        data = res.json

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data, {
            "cupcake": cupcake_one
        })

    def test_delete_cupcake(self):
        res = self.client.delete(f"/api/cupcakes/{self.cupcake.id}")
        data = res.json
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data, {"message": "Deleted"})

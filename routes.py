from flask import Blueprint, jsonify, render_template, request
from werkzeug.wrappers import response
from init import db
from models import Cupcake


app_routes = Blueprint("app_routes", __name__, template_folder="templates", static_folder='static', static_url_path="/app_routes/static")

@app_routes.route("/")
def home():
    cupcakes = db.session.execute(db.select(Cupcake)).scalars()
    return render_template('home.html', cupcakes=cupcakes)

@app_routes.route('/api/cupcakes')
def all_cupcakes():
    cupcakes = db.session.execute(db.select(Cupcake)).scalars()
    serialized = [cupcake.serialize() for cupcake in cupcakes]
    print(serialized)
    return jsonify(cupcakes=serialized)


@app_routes.route('/api/cupcakes/<int:cupcake_id>')
def get_cupcake(cupcake_id):
    cupcake = db.get_or_404(Cupcake, cupcake_id)
    return jsonify(cupcake=cupcake.serialize())


@app_routes.route('/api/cupcakes', methods=['POST'])
def add_cupcake():
    if request.json:
        cupcake = Cupcake(
            flavor=request.json['flavor'],
            size=request.json['size'],
            rating=request.json['rating'],
            image=request.json["image"]
        )
        cupcake.image = cupcake.image if cupcake.image else None

        db.session.add(cupcake)
        db.session.commit()
        response = jsonify(cupcake=cupcake.serialize())
        return (response, 201)
    return ({}, 403)


@app_routes.route('/api/cupcakes/<int:cupcake_id>',methods=["PATCH"])
def update_cupcake(cupcake_id):
    cupcake = db.get_or_404(Cupcake, cupcake_id)
    if request.json:
        cupcake.flavor = request.json.get("flavor", cupcake.flavor)
        cupcake.size = request.json.get("size", cupcake.size)
        cupcake.rating = request.json.get("rating", cupcake.rating)
        cupcake.image = request.json.get("image", None)
        response = request.json
        db.session.add(cupcake)
        db.session.commit()
        return jsonify(cupcake=response)
    return jsonify({})


@app_routes.route('/api/cupcakes/<int:cupcake_id>', methods=["DELETE"])
def delete_cupcake(cupcake_id):
    cupcake = db.get_or_404(Cupcake, cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify({"message": "Deleted"})


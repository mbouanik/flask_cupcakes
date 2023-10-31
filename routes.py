from flask import Blueprint, render_template


app_routes = Blueprint("app_routes", __name__, template_folder="templates", static_folder='static', static_url_path="/app_routes/static")

@app_routes.route("/")
def home():
    return render_template('home.html')

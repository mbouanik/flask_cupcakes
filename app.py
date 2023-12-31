from init import create_app, db

app = create_app()
db.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)

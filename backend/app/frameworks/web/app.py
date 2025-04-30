from flask import Flask
from app.interfaces.controllers.insert_user_controller import insert_user_controller
from app.interfaces.controllers.get_users_controller import get_users_controller
from app.interfaces.controllers.delete_user_controller import delete_user_controller
from app.interfaces.controllers.login_controller import login_controller

app = Flask(__name__)
SECRET_KEY = "super-secret-key"

app.add_url_rule("/insert", view_func=insert_user_controller, methods=["POST"])
app.add_url_rule("/users", view_func=get_users_controller, methods=["GET"])
app.add_url_rule("/delete", view_func=delete_user_controller, methods=["DELETE"])
app.add_url_rule("/login", view_func=login_controller(SECRET_KEY), methods=["POST"])

if __name__ == "__main__":
    app.run(debug=True)

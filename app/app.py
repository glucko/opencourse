from flask import Flask
from .login import login, current_user
from .cli import create_db, print_db
from .config import Config
from .courses import courses

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(login)
app.register_blueprint(courses)

app.cli.add_command(print_db)
app.cli.add_command(create_db)

if __name__ == "__main__":
    app.run(ssl_context="adhoc")

@app.route("/")
def index():
    if current_user.is_authenticated:
        return (
            "<p>Hello, {}! You're logged in! Email: {}</p>"
            "<div><p>Google Profile Picture:</p>"
            '<img src="{}" alt="Google profile pic"></img></div>'
            '<a class="button" href="/logout">Logout</a>'.format(
                current_user.name, current_user.email, current_user.profile_pic
            )
        )
    else:
        return '<a class="button" href="/login">Google Login</a>'
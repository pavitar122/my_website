from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
# from flask_ckeditor import CKEditor

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

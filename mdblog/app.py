from flask import Flask
from flask import render_template

from .database import articles

flask_app = Flask(__name__)

@flask_app.route("/")
def view_home():
	return render_template("home.jinja")

@flask_app.route("/about/")
def view_about():
	return render_template("about.jinja")

@flask_app.route("/articles/")
def view_articles():
	return render_template("articles.jinja", articles=articles.items())

@flask_app.route("/admin/")
def view_admin():
	return render_template("admin.jinja")

@flask_app.route("/articles/<int:article_id>")
def view_article(article_id):
	article = articles.get(article_id)
	if article:
		return render_template("article.jinja", article=article)
	return render_template("article_not_found.jinja", article_id=article_id)
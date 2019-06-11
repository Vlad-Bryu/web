from flask import Flask, render_template
from webapp.weather import weather_in_city
from webapp.model import db, News


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://postgres:Dkfl09071995bryu@localhost/news"
    db.init_app(app)

    @app.route("/")
    def hello():
        page_title = "Новости Python"
        weather = weather_in_city(app.config['WEATHER_DEFAULT_CITY'])
        news_list = News.query.order_by(News.published.desc()).all()
        return render_template('index.html', page_title=page_title, weather=weather, news_list=news_list)

    return app


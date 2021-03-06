from flask import Flask
import time
import os
import telepot
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, PickleType, String
from sqlalchemy.orm import sessionmaker
from flask.ext.heroku import Heroku

app = Flask(__name__)
app.config['SECRET_KEY'] = "random string"
heroku = Heroku(app)

@app.route('/')  # the requests handled successfully!
def hello_world():
    return 'Hello World!'

# the bot code deleted to simplify

uri = os.environ.get('postgres://ktpkryydfoopqw:24gVoST3zpAWPDWv7f5nmPvf1u@ec2-54-75-238-7.eu-west-1.compute.amazonaws.com:5432/d7ev4d45afhalo')
engine = create_engine(uri)
Base = declarative_base()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    global session
    Session = sessionmaker(bind=engine)
    session = Session()

    TOKEN = '222115522:AAFQGKb1h78PP1y0TvVwg-HCkd0X8U84kVg'

    bot = MyBot(TOKEN)  # the bot stuff here
    bot.message_loop()  # but the bot stuff just doesn't work

    # i also removed incoming 2 lines and let it be the default but has no effect
    port = int(os.environ.get("PORT", 5000))

    app.run(host='0.0.0.0', port=port)
    while 1:
        time.sleep(10)

    engine.dispose()

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

uri = os.environ.get('DATABASE_URL')
engine = create_engine(uri)
Base = declarative_base()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    global session
    Session = sessionmaker(bind=engine)
    session = Session()

    TOKEN = 'token'

    bot = MyBot(TOKEN)  # the bot stuff here
    bot.message_loop()  # but the bot stuff just doesn't work

    # i also removed incoming 2 lines and let it be the default but has no effect
    port = int(os.environ.get("PORT", 5000))

    app.run(host='0.0.0.0', port=port)
    while 1:
        time.sleep(10)

    engine.dispose()

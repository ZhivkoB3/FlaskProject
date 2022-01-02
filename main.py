from config import create_app
from db import db
from scripts.update_database import scheduler

app = create_app()
scheduler.start()


@app.before_first_request
def init_request():
    db.init_app(app)
    db.create_all()


if __name__ == "__main__":
    app.run()

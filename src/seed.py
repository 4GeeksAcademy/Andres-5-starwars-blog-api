from app import app
from models import db, User, People, Planet

with app.app_context():
    print("ANTES:", People.query.all())

    user = User(email="johan@example.com", username="johan",
                password="123456", is_active=True)

    luke = People(name="Luke Skywalker")
    leia = People(name="Leia Organa")

    tatooine = Planet(name="Tatooine")
    alderaan = Planet(name="Alderaan")

    db.session.add_all([user, luke, leia, tatooine, alderaan])
    db.session.commit()

    print("DESPUES:", People.query.all())

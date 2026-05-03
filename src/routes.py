from flask import Blueprint, jsonify
from models import db, User, People, Planet, Favorite

api = Blueprint("api", __name__)

# ✅ Endpoint de prueba


@api.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Star Wars API funcionando correctamente"}), 200


# ✅ USERS
@api.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([user.serialize() for user in users]), 200


# ✅ PEOPLE
@api.route("/people", methods=["GET"])
def get_all_people():
    people = People.query.all()
    return jsonify([person.serialize() for person in people]), 200


@api.route("/people/<int:people_id>", methods=["GET"])
def get_one_people(people_id):
    person = People.query.get(people_id)

    if person is None:
        return jsonify({"error": "Personaje no encontrado"}), 404

    return jsonify(person.serialize()), 200


# ✅ PLANETS
@api.route("/planets", methods=["GET"])
def get_all_planets():
    planets = Planet.query.all()
    return jsonify([planet.serialize() for planet in planets]), 200


@api.route("/planets/<int:planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = Planet.query.get(planet_id)

    if planet is None:
        return jsonify({"error": "Planeta no encontrado"}), 404

    return jsonify(planet.serialize()), 200


# ✅ FAVORITES
CURRENT_USER_ID = 1


@api.route("/users/favorites", methods=["GET"])
def get_user_favorites():
    favorites = Favorite.query.filter_by(user_id=CURRENT_USER_ID).all()
    return jsonify([favorite.serialize() for favorite in favorites]), 200


@api.route("/favorite/people/<int:people_id>", methods=["POST"])
def add_people_favorite(people_id):
    favorite = Favorite(
        user_id=CURRENT_USER_ID,
        people_id=people_id
    )
    db.session.add(favorite)
    db.session.commit()

    return jsonify({"message": "Personaje agregado a favoritos"}), 201


@api.route("/favorite/planet/<int:planet_id>", methods=["POST"])
def add_planet_favorite(planet_id):
    favorite = Favorite(
        user_id=CURRENT_USER_ID,
        planet_id=planet_id
    )
    db.session.add(favorite)
    db.session.commit()

    return jsonify({"message": "Planeta agregado a favoritos"}), 201


@api.route("/favorite/people/<int:people_id>", methods=["DELETE"])
def delete_people_favorite(people_id):
    favorite = Favorite.query.filter_by(
        user_id=CURRENT_USER_ID,
        people_id=people_id
    ).first()

    if favorite is None:
        return jsonify({"error": "Favorito no encontrado"}), 404

    db.session.delete(favorite)
    db.session.commit()

    return jsonify({"message": "Personaje eliminado de favoritos"}), 200


@api.route("/favorite/planet/<int:planet_id>", methods=["DELETE"])
def delete_planet_favorite(planet_id):
    favorite = Favorite.query.filter_by(
        user_id=CURRENT_USER_ID,
        planet_id=planet_id
    ).first()

    if favorite is None:
        return jsonify({"error": "Favorito no encontrado"}), 404

    db.session.delete(favorite)
    db.session.commit()

    return jsonify({"message": "Planeta eliminado de favoritos"}), 200

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.user

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "is_active": self.is_active,
            # do not serialize the password, its a security breach
        }


class Star_Systems(db.Model):
    __tablename__ = 'star_systems'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    galactic_coordinates = db.Column(db.String(50))

    def __repr__(self):
        return '<Starystems %r>' % self.starsystems

    def serialize(self):
        return {
            "id":  self.id,
            "name": self.name,
            "galactic_coordiantes": self.galactic_coordinates
        }

class Factions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    leader = db.Column(db.String, unique=True, nullable=False)
    organization_type = db.Column(db.String)
    capital = db.Column(db.String)
    affiliation = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return '<Factions %r>' % self.factions
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "leader": self.leader,
            "organization_type": self.organization_type,
            "capital": self.capital,
            "affiliation": self.affiliation,
        }
    
class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    population = db.Column(db.Integer, nullable=False)
    terrain = db.Column(db.String(100))
    climate = db.Column(db.String(100))

    def __repr__(self):
        return '<Planets %r>' % self.planets

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "terrain": self.terrain,
            "climate": self.climate,
        }

class Species(db.Model):
    __tablename__ = 'species'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    classification = db.Column(db.String(100), unique=True, nullable=False)
    lifespan = db.Column(db.Integer)
    language = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Species %r>' % self.species
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "classification": self.classification,
            "lifespan": self.lifespan,
            "language": self.language,
        }

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    birthdate = db.Column(db.Date)
    gender = db.Column(db.String)
    occupation = db.Column(db.String(50))


    def __repr__(self):
        return '<Characters %r>' % self.characters
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "weight": self.weight,
            "birthdate": self.birthdate,
            "gender": self.gender,
            "occupation": self.occupation
        }
    
    
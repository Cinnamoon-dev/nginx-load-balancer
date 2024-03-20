import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

load_dotenv()

SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "postgresql://postgres:1234@localhost:5432/loadtest")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["DEBUG"] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
server = Server(host="0.0.0.0", port=int(os.getenv('PORT', 5000)))

manager.add_command("runserver", server)
manager.add_command("db", MigrateCommand)

class Cidade(db.Model):
    __tablename__ = "cidade"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    sigla = db.Column(db.String(2), nullable=False)

    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        
    def to_dict(self):
        data = {
            "id": self.id,
            "nome": self.nome,
            "sigla": self.sigla
        }

        return data

    def __repr__(self):
        return f"<Cidade {self.id} {self.nome} {self.sigla}>"

@app.route("/cidade/all", methods=["GET"])
def cidadeAll():
    cities = db.query(Cidade).all()
    response = {
        "error": True,
        "cities": []
    }

    for i in cities:
        response["cities"].append(i.to_dict())

    return response, 200
    
@app.route("/cidade/view/{id:int}")
def cidadeView(id: int):
    city = db.query(Cidade).get(id)

    if not city:
        return {"error": True, "message": "Not Found"}, 404
    
    response = {
        "error": False,
        "data": city.to_dict()
    }

    return response

if __name__ == "__main__":
    manager.run()
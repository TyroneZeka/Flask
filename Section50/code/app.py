from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from user import UserRegister
from items import Item,ItemList


app = Flask(__name__)
app.secret_key = 'Chama'
api = Api(app)

jwt = JWT(app,authenticate,identity) #creates endpoint /auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = "5000", debug=True)

import pymongo
connection_string = "mongodb+srv://cyblogerz:pranav123@cluster0.hg1rd.mongodb.net/test"
import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)



from flask import Flask
app = Flask(__name__)

#Setting up connection with mongodb
client = pymongo.MongoClient(connection_string)
    
#Creating a Database for a grocery store   
db = client['emart-database']

#Accessing products collection
products = db.products

#Function to retrieve product data with product id
def retrieve_product(id):
    return products.find_one({"pid" : id})

#Defining api routes
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/product/<int:n>')
def product_data(n):
    result = JSONEncoder().encode(retrieve_product(n))
    return  result

if __name__ == "__main__":
    app.run(debug=True)





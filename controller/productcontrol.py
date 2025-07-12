from app import app  
from model import product
from flask import request
from model.product import product_management
# object for using class project management
obj=product_management()
@app.route("/getall")
def getall():
    return obj.getall()
@app.route("/add",methods=["POST"])
def addone():
   return obj.add(request.form)
@app.route("/delete",methods=["DELETE"])
def delete():
    return obj.delete(request.form)
@app.route("/update",methods=["PUT"])
def updateone():
    return obj.update(request.form)

if __name__ == '__main__':
    app.run(debug=True)
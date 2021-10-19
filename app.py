from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from connection import DatabaseConn

con = DatabaseConn()

app = Flask(__name__)
CORS(app)


@app.route("/customer/<string:name>/<string:lname>", methods=['GET', 'POST', 'DELETE', 'PATCH'])
def handle_person(name, lname):
    if request.method == 'POST':  # we can understand what type of request we are handling using a conditiozxnal
        con.addCustomer(name, lname, request.args.get('company'), request.args.get('email'), request.args.get('adress'),
                        request.args.get('city'), request.args.get('country'), request.args.get('postal'),
                        request.args.get('phone'))
        return 'success adding customer'
    elif request.method == 'DELETE':
        con.deleteCustomer(name, lname)
        return 'Deleted ' + name + " " + lname
    elif request.method == 'PATCH':
        con.patchCustomer(request.args.get('id'), request.args.get('collumn'), request.args.get('value'))
        return 'Values changed ---> at id:' + request.args.get('id') + " value : " + request.args.get('collumn') + " to: "+request.args.get('value')
    else:
        return jsonify(con.getCustInfo(name, lname))


@app.route("/customers/")
def getAllCustomers():
    return jsonify(con.getAllCustomers())


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)

from flask import Flask, request, jsonify
from cliente import bucarCliente

app = Flask(__name__);

@app.route('/cliente', methods=['POST'])
def obtener_cliente():
    data=request.get_json()
    ci=data.get("ci")
    resultado = bucarCliente(ci)
    return jsonify(resultado)
if __name__ == '__main__':
    app.run(host='localhost',port=5003, debug=True)
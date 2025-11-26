from flask import Flask, jsonify, request  # pyright: ignore[reportUnknownVariableType, reportMissingImports] # Убедитесь что импортирован request

app = Flask(__name__) # type: ignore

@app.route('/') # type: ignore
def hello():
    return "Hello, Serverless! 🚀\n", 200, {'Content-Type': 'text/plain'}
    
@app.route('/echo', methods=['POST']) # type: ignore
def echo(): # type: ignore
    data = request.get_json(silent=True)  # type: ignore # Теперь request должен быть доступен
    if data is None:
        return jsonify({"status": "error", "message": "Invalid or missing JSON data"}), 400 # type: ignore
    
    return jsonify({
        "status": "received",
        "you_sent": data,
        "length": len(str(data)) if data else 0 # type: ignore
    }) # type: ignore

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) # type: ignore
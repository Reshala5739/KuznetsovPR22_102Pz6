from flask import Flask, jsonify, request

app = Flask(__name__)

# Простейший маршрут "Hello World"
@app.route('/hello_world', methods=['GET'])
def hello_world():
    return jsonify({"message": "Hello World"})

# Данные пользователей для демонстрации работы API
users = {
    1: {"name": "Alice", "age": 25},
    2: {"name": "Bob", "age": 30}
}

# Маршрут для получения информации о пользователе по ID
@app.route('/users', methods=['GET'])
def get_user():
    user_id = request.args.get("id")
    if user_id and user_id.isdigit():
        user = users.get(int(user_id), "User not found")
        return jsonify(user)
    else:
        return jsonify({"error": "Invalid or missing 'id' parameter"}), 400

# Запуск сервера
if __name__ == "__main__":
    app.run(debug=True)

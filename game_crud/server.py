from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint
import mysql.connector

app = Flask(__name__)

# Koneksi ke database MySQL
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Ganti dengan username MySQL Anda
        password="",  # Ganti dengan password MySQL Anda
        database="game_db"
    )

# Swagger UI
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# API Endpoint untuk mendapatkan semua data karakter
@app.route('/characters', methods=['GET'])
def get_characters():
    db = connect_to_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM characters")
    characters = cursor.fetchall()
    db.close()
    return jsonify(characters)

# API Endpoint untuk menambahkan karakter baru
@app.route('/characters', methods=['POST'])
def add_character():
    data = request.json
    db = connect_to_db()
    cursor = db.cursor()
    sql = "INSERT INTO characters (name, level, strength, health, mana, agility) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (data['name'], data['level'], data['strength'], data['health'], data['mana'], data['agility']))
    db.commit()
    db.close()
    return jsonify({"message": "Character added successfully"}), 201

# API Endpoint untuk memperbarui data karakter
@app.route('/characters/<int:id>', methods=['PUT'])
def update_character(id):
    data = request.json
    db = connect_to_db()
    cursor = db.cursor()
    sql = "UPDATE characters SET name=%s, level=%s, strength=%s, health=%s, mana=%s, agility=%s WHERE id=%s"
    cursor.execute(sql, (data['name'], data['level'], data['strength'], data['health'], data['mana'], data['agility'], id))
    db.commit()
    db.close()
    return jsonify({"message": "Character updated successfully"})

# API Endpoint untuk menghapus karakter
@app.route('/characters/<int:id>', methods=['DELETE'])
def delete_character(id):
    db = connect_to_db()
    cursor = db.cursor()
    sql = "DELETE FROM characters WHERE id=%s"
    cursor.execute(sql, (id,))
    db.commit()
    db.close()
    return jsonify({"message": "Character deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)

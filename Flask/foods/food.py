from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample food data
foods = [
    {
        'id': 1,
        'name': 'Pizza',
        'category': 'Fast Food'
    },
    {
        'id': 2,
        'name': 'Salad',
        'category': 'Healthy'
    }
]

# Get all foods
@app.route('/foods', methods=['GET'])
def get_foods():
    return jsonify(foods)

# Get a specific food by ID
@app.route('/foods/<int:food_id>', methods=['GET'])
def get_food(food_id):
    food = next((food for food in foods if food['id'] == food_id), None)
    if food:
        return jsonify(food)
    return jsonify({'message': 'Food not found'}), 404

# Add a new food
@app.route('/foods', methods=['POST'])
def add_food():
    new_food = {
        'id': len(foods) + 1,
        'name': request.json['name'],
        'category': request.json['category']
    }
    foods.append(new_food)
    return jsonify(new_food), 201

# Update an existing food
@app.route('/foods/<int:food_id>', methods=['PUT'])
def update_food(food_id):
    food = next((food for food in foods if food['id'] == food_id), None)
    if not food:
        return jsonify({'message': 'Food not found'}), 404

    food['name'] = request.json['name']
    food['category'] = request.json['category']
    return jsonify(food)

# Delete a food
@app.route('/foods/<int:food_id>', methods=['DELETE'])
def delete_food(food_id):
    food = next((food for food in foods if food['id'] == food_id), None)
    if not food:
        return jsonify({'message': 'Food not found'}), 404

    foods.remove(food)
    return jsonify({'message': 'Food deleted'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8070,debug=True)
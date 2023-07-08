from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample animal data
animals = [
    {
        'id': 1,
        'name': 'Lion',
        'species': 'Panthera leo'
    },
    {
        'id': 2,
        'name': 'Elephant',
        'species': 'Loxodonta africana'
    }
]

# Get all animals
@app.route('/animals', methods=['GET'])
def get_animals():
    return jsonify(animals)

# Get a specific animal by ID
@app.route('/animals/<int:animal_id>', methods=['GET'])
def get_animal(animal_id):
    animal = next((animal for animal in animals if animal['id'] == animal_id), None)
    if animal:
        return jsonify(animal)
    return jsonify({'message': 'Animal not found'}), 404

# Add a new animal
@app.route('/animals', methods=['POST'])
def add_animal():
    new_animal = {
        'id': len(animals) + 1,
        'name': request.json['name'],
        'species': request.json['species']
    }
    animals.append(new_animal)
    return jsonify(new_animal), 201

# Update an existing animal
@app.route('/animals/<int:animal_id>', methods=['PUT'])
def update_animal(animal_id):
    animal = next((animal for animal in animals if animal['id'] == animal_id), None)
    if not animal:
        return jsonify({'message': 'Animal not found'}), 404

    animal['name'] = request.json['name']
    animal['species'] = request.json['species']
    return jsonify(animal)

# Delete an animal
@app.route('/animals/<int:animal_id>', methods=['DELETE'])
def delete_animal(animal_id):
    animal = next((animal for animal in animals if animal['id'] == animal_id), None)
    if not animal:
        return jsonify({'message': 'Animal not found'}), 404

    animals.remove(animal)
    return jsonify({'message': 'Animal deleted'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090,debug=True)

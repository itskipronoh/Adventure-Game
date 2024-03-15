from flask import Flask, render_template, request, redirect, session
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Load the game map from game.json
with open('game.json', 'r') as f:
    game_map = json.load(f)

# Initialize player's inventory in session within a request context
@app.before_request
def before_request():
    if 'inventory' not in session:
        session['inventory'] = []

@app.route('/')
def index():
    current_room_name = session.get('current_room', 'START')
    current_room = game_map[current_room_name]
    return render_template('index.html', room=current_room, room_name=current_room_name, inventory=session['inventory'])

@app.route('/move', methods=['POST'])
def move():
    direction = request.form['direction']
    current_room_name = session.get('current_room', 'START')

    current_room = game_map[current_room_name]

    for exit in current_room['exits']:
        if exit['exit'] == direction:
            next_room_name = exit['target']
            next_room = game_map[next_room_name]
            session['current_room'] = next_room_name
            return render_template('index.html', room=next_room, room_name=next_room_name, inventory=session['inventory'])
    
    # If direction not valid, stay in the current room
    return render_template('index.html', room=current_room, room_name=current_room_name, inventory=session['inventory'])

@app.route('/take_item', methods=['POST'])
def take_item():
    item_name = request.form['item']
    session['inventory'].append(item_name)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
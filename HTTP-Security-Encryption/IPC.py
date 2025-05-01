from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

IP_ADDRESS = '127.0.0.1'
PORT = 5000
APP_ADDRESS = f'http://{IP_ADDRESS}:{PORT}'
messages = []

@app.route('/get_messages', methods=['GET'])
def get_messages():
    receiver = request.args.get('receiver')
    received_messages = [msg for msg in messages if msg['receiver'] == receiver]
    return jsonify({'messages': received_messages})


@app.route('/')
def index():
    return app.render_template('message_send.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    sender = data['sender']
    receiver = data['receiver']
    message = data['message']
    messages.append({'sender': sender, 'receiver': receiver, 'message': message})
    return jsonify({'status': 'success', 'message': 'Message sent'})

if __name__ == '__main__':
    # send_message()
    print(f'Click to start a send App: {APP_ADDRESS}/send_message')
    print(f'Click to start a send App: {APP_ADDRESS}/get_message')
    app.run() 
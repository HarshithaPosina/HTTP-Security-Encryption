from flask import Flask, render_template,request,jsonify

app = Flask(__name__)

messages =[]

@app.route('/send_message', methods=['POST'])
def send_message():
     # Access the data from the form
    message = request.form['message']
    messages.append(message)
    # Now you can work with the message
    print(message)

    # Return a simple response or redirect, etc.
    return render_template('receive.html', messages=messages)

@app.route('/get_messages', methods=['GET'])
def get_messages():
    receiver = request.args.get('receiver')
    received_messages = [msg for msg in messages if msg['receiver'] == receiver]
    return render_template('receive.html', messages=received_messages)
    #return jsonify({'messages': received_messages})

@app.route('/')
def index():
    return render_template('sender.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
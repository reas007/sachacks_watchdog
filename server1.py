CLIENT_ID = '4743ffac-e371-46eb-9597-97c7db22b80d'
CLIENT_SECRET = '09e392e1-d837-4d3c-83ec-d05af653fc7f'

import smartcar
from flask import Flask, request, jsonify

app = Flask(__name__)

client = smartcar.AuthClient(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri='http://localhost:8000/callback',
    scope=['read_vehicle_info', 'read_location', 'read_odometer', 'control_security'],
    test_mode=True
)

@app.route('/', methods=['GET'])
def index():
    auth_url = client.get_auth_url(force=True)
    return '''
        <h1><center>Hello, SacHacks!</h1>
        <a href=%s>
          <button>Connect Car</button>
        </a>
    ''' % auth_url

@app.route('/callback', methods=['GET'])
def callback():
    code = request.args.get('code')
    access = client.exchange_code(code)
    
    print(access)

    return jsonify(access)

if __name__ == '__main__':
    app.run(port=8000)
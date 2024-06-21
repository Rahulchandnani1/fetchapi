from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your actual client ID and secret
CLIENT_ID = '5HSICYA44CLRZIE77JT37NCC2RFFQ7U6'
CLIENT_SECRET = '691oualvsg2m2tdxki9gmfl474dsqdh4'

@app.route('/verify-token', methods=['POST'])
def verify_token():
    data = request.get_json()
    token = data.get('token')
    if not token:
        return jsonify({'error': 'Token is required'}), 400

    # Prepare the data for the POST request
    post_data = {
        'token': token,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }

    # Make the request to the OTPless API
    response = requests.post(
        'https://auth.otpless.app/auth/userInfo',
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
        data=post_data
    )

    if response.status_code != 200:
        return jsonify({'error': 'Failed to verify token', 'details': response.text}), response.status_code

    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, Response
from Utils import wol

app = Flask(__name__)
secret = 'Ur Secret'  # Secret key


@app.route('/wol', methods=['POST'])
def wakeOnLan():
    key = request.json
    if key['key'] == secret:
        wol.sendWOL('Ur PC MAC')  # Example: AA:AA:AA:AA:AA:AA
    else:
        return Response('', status=403)

    return ''


if __name__ == '__main__':
    app.run(ssl_context=('Certs/cert.pem', 'Certs/key.pem'), host='0.0.0.0', port=5000, debug=False)

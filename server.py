from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    try:
        # Get JSON data from the request
        json_data = request.get_json()

        # Access JSON values using keys
        first_no = int(json_data['first'])
        second_no = int(json_data['second'])
        result = first_no + second_no

        # Return a response
        return jsonify({'result: ' + str(result)}), 200

    except KeyError:
        return jsonify({'error': 'Invalid JSON data or missing fields.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    try:
        # Get JSON data from the request
        json_data = request.get_json()

        # Access JSON values using keys
        first_no = int(json_data['first'])
        second_no = int(json_data['second'])
        result = first_no - second_no

        # Return a response
        return jsonify({'result: ' + str(result)}), 200

    except KeyError:
        return jsonify({'error': 'Invalid JSON data or missing fields.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')

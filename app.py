from flask import Flask, request
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return {'error': 'No file part'}, 400
    print("files being uploaded")
    file = request.files['file']

    if file.filename == '':
        return {'error': 'No file selected'}, 400

    filename = secure_filename(file.filename)
    filepath = 'files/' + filename  # Replace with your desired path

    file.save(filepath)

    return {'message': 'File uploaded successfully!'}, 200
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


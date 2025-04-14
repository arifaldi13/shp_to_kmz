from flask import Flask, render_template, request, send_file, after_this_request
import os
import glob
import time
from werkzeug.utils import secure_filename
from shptokmz import shp_to_kmz

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    files = request.files.getlist("files")
    filenames = {}
    for file in files:
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        ext = filename.split('.')[-1].lower()
        filenames[ext] = filepath
    if not all(ext in filenames for ext in ['shp', 'shx', 'dbf']):
        return "Error: Missing required shapefile components (shp, shx, dbf)", 400
    kmz_output = os.path.join(OUTPUT_FOLDER, "output.kmz")
    shp_to_kmz(filenames['shp'], kmz_output)
    
    @after_this_request
    def cleanup(response):
        try:
            time.sleep(1)
            for folder in [UPLOAD_FOLDER, OUTPUT_FOLDER]:
                for file in glob.glob(os.path.join(folder, "*")):
                    os.remove(file)
        except Exception as e:
            print("Cleanup error:", e)
        return response
    return send_file(kmz_output, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

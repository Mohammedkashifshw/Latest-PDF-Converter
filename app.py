from flask import Flask, request, send_file
from pdf2image import convert_from_path
from PIL import Image
import os

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_pdf_to_jpg():
    if 'pdf' not in request.files:
        return "No PDF uploaded", 400

    pdf = request.files['pdf']
    pdf.save("temp.pdf")

    images = convert_from_path("temp.pdf")
    image_paths = []

    for i, image in enumerate(images):
        image_path = f"page_{i + 1}.jpg"
        image.save(image_path, 'JPEG')
        image_paths.append(image_path)

    os.remove("temp.pdf")
    return send_file(image_paths[0], mimetype='image/jpeg')  # Just return first image for demo

if __name__ == '__main__':
    import os
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
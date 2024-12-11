from flask import Flask, request, send_file, render_template
import cv2
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'app/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def lanczos_resampling(image, scale):
    height, width = image.shape[:2]
    new_width, new_height = int(width * scale), int(height * scale)
    return cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LANCZOS4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return {"error": "No image file provided"}, 400

    image_file = request.files['image']
    input_path = os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded_image.jpg')
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'enhanced_image.jpg')
    image_file.save(input_path)

    # Process image
    image = cv2.imread(input_path)
    enhanced_image = lanczos_resampling(image, 2.0)
    cv2.imwrite(output_path, enhanced_image)

    return send_file(output_path, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)

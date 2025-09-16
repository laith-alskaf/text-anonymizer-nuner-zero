"""
api.py - خادم REST API
"""

from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename
import os
import tempfile
import json
import threading
import time
from pyngrok import ngrok
from file_handlers import FileHandler
from dotenv import load_dotenv  

app = Flask(__name__)
UPLOAD_FOLDER = tempfile.mkdtemp()
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/health', methods=['GET'])
def health_check():
    """نقطة نهاية للتحقق من صحة الخادم."""
    return jsonify({"status": "healthy"}), 200

@app.route('/anonymize', methods=['POST'])
def anonymize_document():
    """نقطة نهاية لإخفاء هوية المستندات."""
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        
        entity_types = json.loads(request.form.get('entity_types', '[]'))
        replacement_mode = request.form.get('replacement_mode', 'fake')
        
        filename = secure_filename(file.filename)
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(input_path)
        
        output_path, _ = FileHandler.process_file(
            input_path=input_path,
            entity_types=entity_types,
            replacement_mode=replacement_mode,
            output_dir=app.config['UPLOAD_FOLDER']
        )
        
        return send_file(output_path, as_attachment=True)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def run_ngrok():
    """تشغيل ngrok لإنشاء نفق عام."""
    NGROK_AUTH_TOKEN =  os.getenv("NGROK_AUTH_TOKEN")
    ngrok.set_auth_token(NGROK_AUTH_TOKEN)
    ngrok.kill()
    public_url = ngrok.connect(5000)
    print(f"✅ تم إنشاء نفق ngrok!")
    print(f"🌍 رابط API العام: {public_url}")
    print(f"🧪 جرب الآن: {public_url}/health")
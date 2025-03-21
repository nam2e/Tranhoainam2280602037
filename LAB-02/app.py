from flask import Flask, render_template, request, jsonify
from cipher.caesar import CaesarCipher

app = Flask(__name__)

# Router route for home page
@app.route("/")
def home():
    return render_template('index.html')

# Router route for Caesar cipher page
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

# Route for Caesar cipher encryption
@app.route("/encrypt", methods=["POST"])
def caesar_encrypt():
    # Kiểm tra dữ liệu đầu vào
    if "inputPlainText" not in request.form or "inputKeyPlain" not in request.form:
        return "Missing inputPlainText or inputKeyPlain", 400

    # Lấy dữ liệu từ form
    text = request.form["inputPlainText"]
    key = int(request.form["inputKeyPlain"])

    # Khởi tạo đối tượng CaesarCipher
    caesar = CaesarCipher()

    # Mã hóa văn bản
    encrypted_text = caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

# Route for Caesar cipher decryption
@app.route("/decrypt", methods=["POST"])
def caesar_decrypt():
    # Kiểm tra dữ liệu đầu vào
    if "inputCipherText" not in request.form or "inputKeyCipher" not in request.form:
        return "Missing inputCipherText or inputKeyCipher", 400

    # Lấy dữ liệu từ form
    text = request.form["inputCipherText"]
    key = int(request.form["inputKeyCipher"])

    # Khởi tạo đối tượng CaesarCipher
    caesar = CaesarCipher()

    # Giải mã văn bản
    decrypted_text = caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# Main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
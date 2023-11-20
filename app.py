from flask import Flask, request, render_template, send_file
import qrcode
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def generate_qr():
    if request.method == 'POST':
        data = request.form['data']
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')

        img_io = io.BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)
        return send_file(img_io, mimetype='image/png')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

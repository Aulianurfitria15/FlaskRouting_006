from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

# Route untuk halaman sukses
@app.route('/success/<name>')
def success(name):
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Welcome Page</title>
        <link rel="stylesheet" type="text/css" href="{{{{ url_for('static', filename='styles.css') }}}}">
    </head>
    <body>
        <div class="container">
            <h1>Welcome, {name}!</h1>
            <p>We are glad to have you here.</p>
            <a href="{{{{ url_for('login') }}}}" class="btn">Back to Login</a>
        </div>
    </body>
    </html>
    """

# Route untuk login
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form.get('nm', '').strip()  # Ambil data dari form input 'nm'
        if user:  # Validasi input tidak kosong
            return redirect(url_for('success', name=user))  # Redirect ke halaman sukses
        else:
            error = "Name cannot be empty!"  # Pesan error jika kosong
            return render_template('login.html', error=error)
    return render_template('login.html')  # Tampilkan form login

if __name__ == '__main__':
    app.run(debug=True)

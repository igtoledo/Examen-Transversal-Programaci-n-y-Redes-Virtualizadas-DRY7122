from flask import Flask, request, render_template_string
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['PORT'] = 5800

# Configuración de la base de datos
DATABASE = 'users.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template_string('''
        <h1>Gestión de Usuarios</h1>
        <form action="/register" method="post">
            <h2>Registrar Usuario</h2>
            <label for="username">Nombre de Usuario:</label><br>
            <input type="text" id="username" name="username"><br>
            <label for="password">Contraseña:</label><br>
            <input type="password" id="password" name="password"><br><br>
            <input type="submit" value="Registrar">
        </form>
        <form action="/login" method="post">
            <h2>Iniciar Sesión</h2>
            <label for="username">Nombre de Usuario:</label><br>
            <input type="text" id="username" name="username"><br>
            <label for="password">Contraseña:</label><br>
            <input type="password" id="password" name="password"><br><br>
            <input type="submit" value="Iniciar Sesión">
        </form>
    ''')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    password_hash = generate_password_hash(password)
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, password_hash))
    conn.commit()
    conn.close()
    
    return 'Usuario registrado con éxito.'

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT password_hash FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    
    if user and check_password_hash(user[0], password):
        return 'Inicio de sesión exitoso.'
    else:
        return 'Nombre de usuario o contraseña incorrectos.'

if __name__ == '__main__':
    init_db()
    app.run(port=app.config['PORT'])

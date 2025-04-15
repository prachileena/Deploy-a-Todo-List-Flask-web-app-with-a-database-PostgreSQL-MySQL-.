from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        conn = psycopg2.connect(
            dbname="todo",
            user="postgres",
            password="postgres",
            host="db"
        )
        return "Connected to the database!"
    except Exception as e:
        return f"Database connection failed: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0')

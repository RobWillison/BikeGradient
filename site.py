from flask import Flask
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <button onclick='down()'>Down</button>
    <button onclick='up()'>Up</button>

    <script>
        function up() {
            fetch('up')
        }

        function down() {
            fetch('down')
        }
    </script>
    """

@app.route('/down')
def down():
    current = int(r.get('foo'))
    r.set('foo', current - 1)
    return 'Down'

@app.route('/up')
def up():
    current = int(r.get('foo'))
    r.set('foo', current + 1)
    return 'Up'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

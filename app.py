from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/proxy')
def proxy():
    url = request.args.get('url')
    if not url:
        return 'Missing url param', 400
    try:
        r = requests.get(url, timeout=5)
        return Response(r.content, status=r.status_code, content_type=r.headers.get('Content-Type', 'text/plain'))
    except Exception as e:
        return f'Error: {str(e)}', 500

# 🟢 Ось тут має бути — ЗА МЕЖАМИ функції!
if __name__ == "__main__":
    app.run(debug=True, port=5000)

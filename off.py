from urllib.request import Request, urlopen
BASE_URL = "http://127.0.0.1:5000"
SHUTDOWN = "/shutdown"

def request_shutdown(url=BASE_URL + SHUTDOWN):
    req = Request(url, method="POST")
    res = urlopen(req)
    content = res.read()
    print(content)
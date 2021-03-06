
def runonce():
    # This is only ran when OSIRIS is restarted, unlike normal live updates
    return {}


def depends():
    # this is list of modules to import from app
    return ['testmodule', 'osirisd']


def reply(msg):
    """
    code, header, and template are optional
    header is another json dict thing
    template is another, but entries in the msg called (or in the file passed) {{ something }} will get replaced with the value
    If you don't pass msg you can pass the path to a file with file:, if you do both file has higher priority

    'runonce':1 being added causes it to re-run the runonce function
    'reload':1 being added causes the current app to be reloaded
    'modload':[list] being added causes it to import the modules listed
    'type' optionally accepts a mimetype used in the Content-Type header
    If no type is passed it logically figures it out based on path or falls back to text/html

    Passes object with the body and headers
    headers come in an object called header, keys are names
    body is the posted data
    IP is the IP, (X-Real-IP is proxy = 1 in osiris.conf)
    TYPE is the type (get, post, etc)
    PATH is the requested path, the /

        DNT support: If <tracker></tracker> tags are used in the sent data and the browser enables DNT that data will be removed from the request
        Also, dht is passed in the payload sent to reply

    A sample dict passed:
    {'body': '', 'header': {'Accept-Language': 'en-US,en;q=0.8', 'Accept-Encoding': 'gzip,deflate,sdch', 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36', 'DNT': '1', 'Host': 'localhost:8000', 'Cache-Control': 'max-age=0', 'PATH': '/', 'TYPE': 'GET'}, 'ip': '127.0.0.1'}
    """
    ip = msg['ip']
    try:
        msg['runonce'][ip] += 1
    except:
        msg['runonce'][ip] = 0

    # Starts searching in app/{module name}/
    if msg['header']['PATH'] == '/ip_stats':
        dat = "<p>"
        for ip in msg['runonce']:
            dat = dat + \
                '%s has visited this page %s times<br>' % (
                    ip, msg['runonce'][ip])
        dat += "</p>"
        return {"code": 200, "msg": dat}
    elif msg['header']['PATH'].startswith('/code'):
        request = int(msg['header']['PATH'].split('/')[2])

        return {"code": request, "msg": str(msg['depends']['osirisd'].app().code(request))}

    elif msg['header']['PATH'] == '/test.html':
        return {"code": 200, "file": "test.html", "template": {"name.first": "Test", "name.last": "user"}}

    else:
        msg2srv = "Hello, {0}!\r\nYour IP is {1}\r\nYour name is {{name.first}} {{ name.last }}!\r\nYour key is '{2}'<br><br><tracker>Botnet mode is enabled</tracker>".format(
            msg['header']['User-Agent'], msg['ip'], msg['depends']['testmodule'].test())

        send = {"code": 200, "msg": msg2srv, "template": {"name.first": "Test",
                                                          "name.last": "user"}, 'modload': ['testmodule'], 'reload': 1, 'type': 'text/html'}

        return send

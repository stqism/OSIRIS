
def reply(msg):
	"""
	code, header, and template are optional
	header is another json dict thing
	template is another, but entries in the msg called (or in the file passed) {{ something }} will get replaced with the value
	If you don't pass msg you can pass the path to a file with file:, if you do both file has higher priority
	Passes object with the body and headers
	headers come in an object called header, keys are names
	body is the posted data
	IP is the IP, (X-Real-IP is proxy = 1 in osiris.conf)
	TYPE is the type (get, post, etc)
	PATH is the requested path, the /

	A sample dict passed:
	{'body': '', 'header': {'Accept-Language': 'en-US,en;q=0.8', 'Accept-Encoding': 'gzip,deflate,sdch', 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36', 'DNT': '1', 'Host': 'localhost:8000', 'Cache-Control': 'max-age=0', 'PATH': '/', 'TYPE': 'GET'}, 'ip': '127.0.0.1'}
	"""
	if msg['header']['PATH'] == '/test.html':
		return { "code": 200, "file": "test.html", "template": {"name.first": "Test", "name.last": "user"} }
	else:
		msg2srv = "Hello, {0}!\r\nYour IP is {1}\r\nYour name is {{name.first}} {{ name.last }}!".format(msg['header']['User-Agent'],msg['ip'])
		send = { "code": 200, "msg": msg2srv, "template": {"name.first": "Test", "name.last": "user"} }

		return send
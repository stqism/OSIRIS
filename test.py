def reply(msg):
	"""
	code and header are optional
	header is another json dict thing
	Passes object with the body and headers
	headers come in an object called header, keys are names
	body is the posted data
	IP is the IP, (X-Real-IP is proxy = 1 in osiris.conf)
	TYPE is the type (get, post, etc)
	PATH is the requested path, the /
	"""

	msg2srv = "Hello, {0}!\r\nYour IP is {1}\r\n".format(msg['header']['User-Agent'],msg['ip'])
	send = { "code": 200, "msg": msg2srv, "header": {"Generic-header": "test"} }
	return send
def reply(msg):
	"""
	code and header are optional
	header is another json dict thing
	Passes object with the body and headers
	headers come in an object called header, keys are names
	body is the posted data
	TYPE is the type (get, post, etc)
	"""

	msg2srv = "Hello, {0}!\r\n".format(msg['header']['User-Agent'])
	send = { "code": 200, "msg": msg2srv, "header": {"Server": "OSIRIS"} }
	return send
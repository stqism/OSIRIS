def reply(msg):
	"""
	code and header are optional
	header is another json dict thing
	"""

	send = { "code": 200, "msg": msg, "header": {"Server": "OSIRIS"} }
	return send
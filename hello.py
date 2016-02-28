import urlparse

def wsgi_application(environ, start_response):

	status = '200 OK'

	param = parse_qs(environ['QUERY_STRING'],1)	

	headers = [
	('Content-Type' , 'text/plain')
	]
	#body = 'Hello world'
	start_response(status,headers)
	return [param]

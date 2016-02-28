import urlparse

def wsgi_application(environ, start_response):

	status = '200 OK'

	param = urlparse.parse_qs(environ['QUERY_STRING'],1)
	paramr = urlparse.parse_qs(environ['QUERY_STRING'],0)

	for i, param in enumerate(param):
    print i, '-->', param
	
	for i, param in enumerate(param):
    print i, '-->', paramr
	
	
	headers = [
	('Content-Type' , 'text/plain')
	]

	start_response(status,headers)
	return [param]

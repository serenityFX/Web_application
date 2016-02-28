import urlparse

def wsgi_application(environ, start_response):

	status = '200 OK'

	param = urlparse.parse_qsl(environ['QUERY_STRING'],1)

	str = ''
	
	for i in param:
			str += i[0] + '=' + i[1] + '\r\n'
	
	
	
	headers = [
	('Content-Type' , 'text/plain')
	]

	start_response(status,headers)
	return [str]

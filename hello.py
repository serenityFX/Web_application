import urlparse

def wsgi_application(environ, start_response):

	status = '200 OK'

	param = urlparse.parse_qs(environ['QUERY_STRING'],1)	

	#for i in range(len(param)):
	#	param[i] += '\r\n'
	
	
	headers = [
	('Content-Type' , 'text/plain')
	]

	start_response(status,headers)
	return [param]

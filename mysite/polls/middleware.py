import logging
from django.http import HttpResponse
logging.basicConfig(filename='log.txt')
logger = logging.getLogger(__name__)

class LogMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		logger.info(f'''Method: {request.method}, 
			            Path: {request.path}, 
						User Agent: {request.META.get('HTTP_USER_AGENT')}, 
						IP: {request.META.get('REMOTE_ADDR')}''')
		response = self.get_response(request)
		logger.info(f"Status Code: {response.status_code}")
		return response

class UserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_agent = request.META.get('HTTP_USER_AGENT', '') 
		
        if "unknown" in user_agent.lower():
            return HttpResponse("Unknown User is not allowed", status=403)
		
        return self.get_response(request)


class RestrictIPMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response
		self.restricted_ips = ['127.0.0.1']
	def __call__(self, request):
		ip_address = request.META.get('REMOTE_ADDR')
		if ip_address in self.restricted_ips:
			return HttpResponse("Forbidden: Your IP is restricted", status=403)
		response = self.get_response(request)
		return response

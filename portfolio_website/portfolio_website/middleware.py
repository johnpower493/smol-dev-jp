```python
from django.utils.deprecation import MiddlewareMixin

class SimpleMiddleware(MiddlewareMixin):

    def process_request(self, request):
        pass

    def process_response(self, request, response):
        return response
```
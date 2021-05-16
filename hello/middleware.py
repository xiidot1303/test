  from django.http import HttpResponseForbidden
  from whitenoise.middleware import WhiteNoiseMiddleware
  # this is a sample code, you can change for your use case
  class ProtectedStaticFileMiddleware(WhiteNoiseMiddleware):
        def process_request(self, request):
            # check user authentication
            if condition_met(request):
               return super(WhiteNoiseMiddleware, self).process_request(request)
            # condition false
            return HttpResponseForbidden("you are not authorized")
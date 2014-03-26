from django.conf import settings
from django.http import HttpResponseRedirect
import re
from django.http.request import HttpRequest


def secure_required(view_func):
    """Decorator makes sure URL is accessed over https."""
    print("Raul")
    def _wrapped_view_func(self, request, *args, **kwargs):
        print("Raul2")
        print('request ==> %s' %(request))
        print('request url ==> %s' %(request.build_absolute_uri(request.get_full_path())))

        print("request.is_secure() ==> %s" %(request.is_secure()))

        regex = re.compile('^HTTP_')
        all_headers = dict((regex.sub('', header), value) for (header, value)
        in request.META.items() if header.startswith('HTTP_'))
        # print('ra')
        print('headers == > %s' %(all_headers.values()))



        if not request.is_secure():
            if getattr(settings, 'HTTPS_SUPPORT', True):
                request_url = request.build_absolute_uri(request.get_full_path())
                secure_url = request_url.replace('http://', 'https://')

                print('secure url ==> %s' %(secure_url))
                
                # return HttpResponseRedirect(secure_url)
        return view_func(self, request, *args, **kwargs)
    return _wrapped_view_func
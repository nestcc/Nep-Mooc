from django.http import HttpResponseRedirect, HttpResponse
from django.utils.deprecation import MiddlewareMixin

class UserAuthMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        if '/student/' == request.path[0:9]:
            if 'stu_id' not in request.COOKIES:
                return HttpResponseRedirect('/')
            elif 'my_course' in request.path:
                if request.get_full_path().split('/')[3] != request.COOKIES['stu_id']:
                    return HttpResponse('error')

        elif '/teacher/' == request.path[0:9]:
            if 'tch_id' not in request.COOKIES:
                return HttpResponseRedirect('/')

from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest
from .models import CustomUser

DEGREE_SALARY_MAPPING = {
        "bachelor": ("Библиотекарь", 40000),
        "master": ("Главный библиотекарь", 50000),
        "docent": ("Директор", 55000),
        "college": ("Помощник библиотекаря", 10000),
    }


class DiplomaMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            diploma = request.POST.get('diploma')
            if not diploma:
                return HttpResponseBadRequest('Вы должны указать диплом')

            salary = DEGREE_SALARY_MAPPING.get(diploma)
            if salary:
                request.salary = salary

            degree_data = DEGREE_SALARY_MAPPING.get(diploma)
            if degree_data:
                request.position, request.salary = degree_data
            else:
                request.position = "none"
                request.salary = 0

        elif request.path == '/register/' and request.method == 'GET':
             setattr(request, 'salary', 0)
             setattr(request, 'position', 'none')

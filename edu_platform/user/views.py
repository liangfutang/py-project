from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from mapper import views

@csrf_exempt
def orm_select(request):
    result = views.index()
    print(result)
    return HttpResponse("ok")

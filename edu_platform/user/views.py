from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def orm_select(request):

    return HttpResponse("ok")

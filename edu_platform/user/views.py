from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

from mapper import views
from mapper.models import Book
from rest_framework import generics

from mapper.serializers import BookSerializer


@csrf_exempt
def orm_select(request):
    result = views.index()
    print(result)
    return HttpResponse("ok")

class BookView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Book.objects.all()

        serializer = BookSerializer(queryset, many=True)
        return JsonResponse({
            "status": 200,
            "data": serializer.data
        }, safe=False)

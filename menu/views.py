from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from menu.models import Menu
from menu.serializer import MenuSerializer
from common.json_response import JSONResponse

# Create your views here.
def get(request):
    if request.method == 'GET':
        menu = Menu.objects.all()

        serializer = MenuSerializer(menu, many=True)
        return JSONResponse(serializer.data)
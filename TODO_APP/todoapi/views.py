from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TODOSERIALIZER
from django.http import HttpResponse,QueryDict,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import TODOTABLE
from json import loads


# HTTP METHODS  = POST, GET, PATCH, DELETE, PUT,
# user body = JSON, TEXT/PLAIN , FILE, XML
# params = /user/atuhorname/6/ 
# query = /user? url.com/query?=djhfsdhgfhdgfhsdghgdshgfdgs 
# /user?mail=praveencattie@gmail.com
#eg url = http://domainname.com/user/3



@api_view(["GET"])
def GET_ALLTODO(request):
    try:
        Tabledata = TODOTABLE.objects.all()
        serializerdata = TODOSERIALIZER(Tabledata,many=True)
        return JsonResponse({"tododata":serializerdata.data})
    except Exception as err:
        print(err)
        return HttpResponse("Error")



@api_view(["POST"])
def INSERT_TODO(request):
    try:
        # request.method HTTP = POST, GET, PUT, DELETE ---->string
        if request.method == "POST":
            userdata = request.body
            jsondata = QueryDict(userdata)
            todo = TODOTABLE(todovalue=jsondata.get("value"),todostatus=False)
            todo.save()
            serializercurrentvalue = TODOSERIALIZER(todo)
            return JsonResponse({"tododata":serializercurrentvalue.data})
        else:
            return Response({"status":"error"})    
    except Exception as err:
        print(err)
        return Response({"status":"error"})
        

@csrf_exempt
def MANIDATA(request,id):

    if request.method == "DELETE":
        todo = TODOTABLE.objects.get(id=id)
        todo.delete()
        return HttpResponse("delete")
    elif request.method == "PUT":
        todo = TODOTABLE.objects.get(id=id)
        todo.todostatus = True
        todo.save()
        return HttpResponse("complete")











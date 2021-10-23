from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import status 
class ResponseHandler:
    def response_ok(self,data=None,message=None):
        context = {
            'data':data,
            'message':message,
            'status':'success'
        }
        return Response(context,status=status.HTTP_200_OK)
    def response_created(self,data,message):
        context = {
            'data':data,
            'message':message,
            'status':'success'
        }
        return Response(context,status=status.HTTP_201_CREATED)
    def response_updated(self,data,message):
        context = {
            'data':data,
            'message':message,
            'status':'success'
        }
        return Response(context,status=status.HTTP_200_OK)
    def response_archived(self,model):
        context = {
            'message':f'{model} was deleted',
            'status':'success'
        }
        return Response(context,status=status.HTTP_200_OK)
    def response_notfound(self,model):
        context = {
            'message':f'{model} not found',
            'status':'error'
        }
        return Response(context,status=status.HTTP_404_NOT_FOUND)

    def response_validation_client(self,error):
        return JsonResponse(error,safe=False)


    def response_unexpected(self,error):
        context = {
            'message':error,
            'status':'error'
        }
        return Response(context,status=status.HTTP_417_EXPECTATION_FAILED)
    def response_server_error(self,error):
        print(error)
        context = {
            'message':error,
            'status':'error'
        }
        return Response(context,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
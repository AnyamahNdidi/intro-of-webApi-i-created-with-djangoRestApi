
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

@api_view(['GET','POST'])
def index(request):
    print(request.auth)
    print(request.user)
    if request.method == 'GET':
        return Response(data={"message":"hello from django"}, status=status.HTTP_200_OK)
    elif request.method == "POST":
        return Response(data=request.data, status=status.HTTP_200_OK)
    else:
        return Response(data="request not found", status=status.HTTP_200_OK)

class message(APIView):

    def post(self, request):
        return Response(data="this is class based hit by post request", status=status.HTTP_200_OK)

    def get(self, request):
        print(request.data)
        return Response(data="this is a class based view hit by Get request", status=status.HTTP_200_OK)





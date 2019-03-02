from rest_framework.views import APIView
from rest_framework.response import Response


class ActivitiesApi(APIView):

    def get(self, request, format=None):
    	code=request.GET['country']
    	year=request.GET['year']
    	result= {

    	}
    	return Response(result)
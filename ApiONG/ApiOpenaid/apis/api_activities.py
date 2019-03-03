from rest_framework.views import APIView
from rest_framework.response import Response
from ApiOpenaid.utils.activities_data import ActivitiesData


class ActivitiesApi(APIView):

	def get(self, request, format=None):
		code=request.GET['country']
		year=request.GET['year']
		result = ActivitiesData().get_data(code, year)
		return Response(result)
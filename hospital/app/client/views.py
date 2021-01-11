from rest_framework import status
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from hospital.app.client.models import Shift
from hospital.app.user.serializers import ShiftCreationSerializer



class ShiftRegisterationView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    serializer_class = ShiftCreationSerializer


    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        response = {
            'success' : 'True',
             'status code' : status.HTTP_200_OK,
             'message' : 'Shift created Successfully',

        }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)






class ShiftListView(RetrieveAPIView):

    permission_classes = (IsAuthenticated,)
    #authentication_class = JSONWebTokenAuthentication

    def get(self, request):  
        try:

            shift_data = Shift.objects.all()          
          
            dt = [{
                    'Start time': shift_data.start,                    
                    'Start date': shift_data.start_date,
                    'arrival time': shift_data.arrival_time,
                    'departure_time': shift_data.departure_time,
                    'repeat':   shift_data.repeat,
                    'shift_availability' : shift_data.shift_availability,

                    }]

            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'Shift data fetched successfully',
                'data': dt,
                }

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'Data does not exist',
                'error': str(e)
                }
        return Response(response, status=status_code)




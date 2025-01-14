from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from out_come.models import OutCome
from shared.utils import response_data
from shared.messages import ResponseMessage
from out_come.serializers import CreateOutComeSerializer,ListOutComeSerializer
# Create your views here.
class CreateAndListOutComeView(generics.ListCreateAPIView):
    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = CreateOutComeSerializer(data = data, context = {'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response = response_data(
            success = True,
            statusCode=status.HTTP_201_CREATED,
            message=ResponseMessage.CREATE_SUCCESS_MESSAGE,
            data = serializer.data
        )
        else:
            response = response_data(
                success = False,
                statusCode=status.HTTP_400_BAD_REQUEST,
                message=ResponseMessage.CREATE_FAILURE_MESSAGE
            )
        return Response(response, status=response.get('statusCode'))

    def list(self, request, *args, **kwargs):
        queryset = OutCome.objects.filter(user = request.user)
        if len(queryset) > 0:
            serializer = ListOutComeSerializer(queryset, many = True)
            response = response_data(
                success = True,
                statusCode=status.HTTP_200_OK,
                message= ResponseMessage.GET_SUCCESS_MESSAGE,
                data = serializer.data
            )
        else:
            response = response_data(
                success = False,
                statusCode=status.HTTP_400_BAD_REQUEST,
                message=ResponseMessage.GET_FAILURE_MESSAGE
            )
        return Response(response, status= response.get('statusCode'))
class GetDetailUpdateOutComeView(generics.RetrieveUpdateAPIView):
    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.pop('pk')
        queryset = OutCome.objects.get(pk = pk)
        if queryset is not None:
            serializer = ListOutComeSerializer(queryset)
            response = response_data(
                success = True,
                statusCode=status.HTTP_200_OK,
                message= ResponseMessage.GET_SUCCESS_MESSAGE,
                data = serializer.data
            )
        else:
            response = response_data(
                success = False,
                statusCode=status.HTTP_400_BAD_REQUEST,
                message=ResponseMessage.GET_FAILURE_MESSAGE
            )
        return Response(response, status= response.get('statusCode'))
    
    def update(self, request, *args, **kwargs):
        id = kwargs.pop('pk')
        partial = kwargs.pop('partial', False)
        outcome = OutCome.objects.get(
            pk = id,
        )
        serializer = ListOutComeSerializer(outcome, data=request.data, partial = partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if getattr(outcome, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            outcome._prefetched_objects_cache = {}
        response = response_data(
            success = True,
            statusCode = status.HTTP_200_OK,
            message = ResponseMessage.UPDATE_SUCCESS_MESSAGE,
            data = serializer.data
        )
        return Response(response, status = response.get('statusCode'))

class GetlistOutcomeEnableAddtoJar(generics.ListAPIView):
    def list(self, request, *args, **kwargs):
        queryset = OutCome.objects.filter(user = request.user).exclude(jars__outcome__user = request.user)
        if len(queryset) > 0:
            serializer = ListOutComeSerializer(queryset, many = True)
            response = response_data(
                success = True,
                statusCode = status.HTTP_200_OK,
                message = ResponseMessage.UPDATE_SUCCESS_MESSAGE,
                data = serializer.data
            )
        else:
            response = response_data(
                success = True,
                statusCode = status.HTTP_200_OK,
                message = ResponseMessage.UPDATE_SUCCESS_MESSAGE,
                data = serializer.data
            )
        return Response(response, status = response.get('statusCode'))
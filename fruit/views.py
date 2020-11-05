from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Classify
from rest_framework import status
from .serializers import ClassifySerializers
from rest_framework.viewsets import ModelViewSet
# Create your views here.


class ClassifyControl(APIView):
    def get(self,request,format=None):
        print('请求:'+str(request))
        dict1 = self.request.query_params
        #print(dict1['classifyName'])
        #Classify.objects.create(classifyName='热带水果',createdTime='2020-10-1 10:30:00',updateTime='2020-10-1 10:30:00')
        classify = Classify.objects.all()
        serializer = ClassifySerializers(classify, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        print(request)
        print(self.request.data)
        serializer = ClassifySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ClassifyObject(APIView):

    def delete(self,request,uid):
        print(request)
        Classify.objects.get(pk=uid).delete()
        return Response('success')
    def get(self,request,uid):
        print(request)
        classify=Classify.objects.get(pk=uid)
        serializer = ClassifySerializers(classify, many=False)
        return Response(serializer.data)

class ClassifyList(ModelViewSet):
    queryset = Classify.objects.all()
    serializer_class = ClassifySerializers





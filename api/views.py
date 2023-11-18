from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.decorators import APIView


class ListProduct(APIView):
    queryset = {
        "data": "hello",
        "malumot": "true"
    }
    def __init__(self,  yosh,  query):
        self.query = query
        
        

        

class ListAPi(ListProduct):
    def __init__(self, query, age, *args, **kwargs):
        super().__init__(query, *args, **kwargs)
        self.age = age

    def get(self, request, format=None):
        data = {
            "product": "product",
            "name": self.query
        }
        return Response(data)
    
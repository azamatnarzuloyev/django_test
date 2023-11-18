from rest_framework.response import Response
from pprint import pprint
# from rest_framework.generics import ListAPIView
# from rest_framework.decorators import APIView
# from api.models import Product

# class ListProduct(APIView):
#     def __init__(self, query):
#         self.query = query
        

#     @staticmethod
#     def run(yosh):
#       return yosh
        

# class ListAPi(ListProduct, ListAPIView):
#     queryset = Product.objects.all()
#     def __init__(self, query, age, *args, **kwargs):
#         super().__init__(query, *args, **kwargs)
#         self.age = age

#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
 


#     def get(self, request , format=None):

#         data = {
#             "product": "product",
#             "name": self.query
#         }
#         return data

# list  = ListAPi(age=11, query="salom")


# print(list.queryset)
def run():
    pprint(Response.__dict__)

    
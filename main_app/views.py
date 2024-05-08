from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
class LibraryApiView(APIView):
    serializer_library=LibrarySerializer
    def get(self,request):
        info  = Library.objects.all().values()
        return Response({"Your Booking Info": info})

    def post(self,request):
        serializer_post_library=LibrarySerializer(data=request.data)
        if(serializer_post_library.is_valid()):
            Library.objects.create(bookid=serializer_post_library.data.get("bookid"),
                            bookname=serializer_post_library.data.get("bookname"),
                            customername=serializer_post_library.data.get("customername"),
                            address=serializer_post_library.data.get("address"),
                            phonenumber=serializer_post_library.data.get("phonenumber"),
                            )

        library = Library.objects.all().filter(id=request.data["bookid"]).values()
        return Response({"Notification": "New Booking is Added!", "Library": library})

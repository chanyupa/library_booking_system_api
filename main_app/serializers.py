from rest_framework import serializers

class LibrarySerializer(serializers.Serializer):
    bookid=serializers.IntegerField(label="Enter Book ID")
    bookname=serializers.CharField(label="Enter Book Name")
    customername =serializers.CharField(label="Enter Your Name")
    address=serializers.CharField(label="Enter Your Address")
    phonenumber=serializers.CharField(label="Enter Your Phone Number")
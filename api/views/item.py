from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models.items import Item
from ..serializers import ItemSerializer

@api_view(['GET'])
def get_items(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_item(request):
    # Parse the request data with the serializer
    serializer = ItemSerializer(data=request.data)
    # Check if the data is valid
    if serializer.is_valid():
        # Save the new object to the database
        serializer.save()
        # Return a response with the created object data
        return Response(serializer.data, status=201)
    # If the data is not valid, return an error response
    return Response(serializer.errors, status=400)
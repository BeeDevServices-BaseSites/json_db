from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from base.models.honeycombs import Honeycombs
from ..serializers import HoneycombsSerializer


# CREATE
@api_view(['POST'])
def create(request):
    # Parse the request data with the serializer
    serializer = HoneycombsSerializer(data=request.data)
    # Check if the data is valid
    if serializer.is_valid():
        # Save the new object to the database
        serializer.save()
        # Return a response with the created object data
        return Response(serializer.data, status=201)
    # If the data is not valid, return an error response
    return Response(serializer.errors, status=400)

# READ
@api_view(['GET'])
def get_all(request):
    # Get all the course_card objs
    honeycombs = Honeycombs.objects.all()
    # Run the course_card objs throught the serializer
    serializer = HoneycombsSerializer(honeycombs, many=True)
    # return the data on from the serialized response
    return Response(serializer.data)

@api_view(['GET'])
def get_one(request, id):
    try:
        # Get the course_card object with the specified ID
        course_card = Honeycombs.objects.get(id=id)
    except Honeycombs.DoesNotExist:
        # Handle the case where the object doesn't exist (e.g., return an error response)
        return Response({"error": "Honeycombs not found"}, status=status.HTTP_404_NOT_FOUND)

    # Run the course_card object through the serializer
    serializer = HoneycombsSerializer(course_card)
    # Return the serialized data in the response
    return Response(serializer.data)


# UPDATE
@api_view(['PATCH'])
def update_one(request, id):
    try:
        # Get the course_card object with the specified ID
        course_card = Honeycombs.objects.get(id=id)
        for key in request.data:
            setattr(course_card, key, request.data[key])

        course_card.save()
    except Honeycombs.DoesNotExist:
        # Handle the case where the object doesn't exist (e.g., return an error response)
        return Response({"error": "Honeycombs not found"}, status=status.HTTP_404_NOT_FOUND)

    # Run the course_card object through the serializer
    serializer = HoneycombsSerializer(course_card)
    # Return the serialized data in the response
    return Response(serializer.data)

# DELETE
@api_view(['DELETE'])
def delete_one(request, id):
    try:
        # Get the course_card object with the specified ID
        course_card = Honeycombs.objects.get(id=id)
        course_card.delete()

    except Honeycombs.DoesNotExist:
        # Handle the case where the object doesn't exist (e.g., return an error response)
        return Response({"error": "Honeycombs not found"}, status=status.HTTP_404_NOT_FOUND)

    # Run the course_card object through the serializer
    serializer = HoneycombsSerializer(course_card)
    # Return the serialized data in the response
    return Response(serializer.data)
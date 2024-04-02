from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from base.models.careers import Career
from ..serializers import CareerSerializer


# CREATE
@api_view(['POST', 'PUT'])
def create(request):
    # Parse the request data with the serializer
    serializer = CareerSerializer(data=request.data)
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
    # Get all the career objs
    careers = Career.objects.all()
    # Run the career objs throught the serializer
    serializer = CareerSerializer(careers, many=True)
    # return the data on from the serialized response
    return Response(serializer.data)

@api_view(['GET'])
def get_one(request, id):
    try:
        # Get the career object with the specified ID
        career = Career.objects.get(id=id)
    except Career.DoesNotExist:
        # Handle the case where the object doesn't exist (e.g., return an error response)
        return Response({"error": "Career not found"}, status=status.HTTP_404_NOT_FOUND)

    # Run the career object through the serializer
    serializer = CareerSerializer(career)
    # Return the serialized data in the response
    return Response(serializer.data)


# UPDATE
@api_view(['PATCH'])
def update_one(request, id):
    try:
        # Get the career object with the specified ID
        career = Career.objects.get(id=id)
        for key in request.data:
            setattr(career, key, request.data[key])

        career.save()
    except Career.DoesNotExist:
        # Handle the case where the object doesn't exist (e.g., return an error response)
        return Response({"error": "Career not found"}, status=status.HTTP_404_NOT_FOUND)

    # Run the career object through the serializer
    serializer = CareerSerializer(career)
    # Return the serialized data in the response
    return Response(serializer.data)

# DELETE
@api_view(['DELETE'])
def delete_one(request, id):
    try:
        # Get the career object with the specified ID
        career = Career.objects.get(id=id)
        career.delete()

    except Career.DoesNotExist:
        # Handle the case where the object doesn't exist (e.g., return an error response)
        return Response({"error": "Career not found"}, status=status.HTTP_404_NOT_FOUND)

    # Run the career object through the serializer
    serializer = CareerSerializer(career)
    # Return the serialized data in the response
    return Response(serializer.data)
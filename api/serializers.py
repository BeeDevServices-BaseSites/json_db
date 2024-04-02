from rest_framework import serializers

from base.models.careers import Career
from base.models.course_cards import CourseCard
from base.models.employees import Employee
from base.models.honeycombs import Honeycombs


class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'

class CourseCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCard
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class HoneycombsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Honeycombs
        fields = '__all__'
from rest_framework import serializers

from base.models.items import Item
from base.models.careers import Career
from base.models.course_cards import CourseCard

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'

class CourseCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCard
        fields = '__all__'
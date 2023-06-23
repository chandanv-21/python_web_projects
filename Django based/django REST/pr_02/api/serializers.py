from rest_framework import serializers
from .models import Student

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['name','roll', 'city']

# Field Level validation
    def validate_roll(self,value):
        if value>200:
            raise serializers.ValidationError("Seat full")
        return value
    
# Object level Validation
def validate(self, data):
    nm=data.get('name')
    ct=data.get('city')
    if nm.lower()=='manish' and ct.lower()!='ranchi':
        raise serializers.ValidationError("City name should be Ranchi!!")
    return data




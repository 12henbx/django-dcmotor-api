from rest_framework import serializers
from .models import All_Status

# class FaultPredictSerializer(serializers.HyperlinkedModelSerializer):
    
#     class Meta:
#         model = Fault_Predict
#         fields = ('timestamp', 'faultPredictval')

class AllStatusSerializer(serializers.ModelSerializer):
    # faultPredict = FaultPredictSerializer(many=True)
    class Meta:
        model = All_Status
        fields = ('createdStr', 'faultval', 'faultPredict', 'speedVal', 'currentVal')
        # fields = '__all__'


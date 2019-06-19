from rest_framework import serializers
from .models import Banks, Branches

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banks
        fields = '__all__'

class BranchesSerializer(serializers.ModelSerializer):
    bank = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Branches
        fields = '__all__'

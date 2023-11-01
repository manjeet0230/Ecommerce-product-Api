from rest_framework import serializers

from .models import Product,QuantityVariant,Category,ColorVariant,SizeVariant

class QuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuantityVariant
        fields = '__all__' 
        # exclude = ['id']

        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        # exclude = ['id']


class color_serializers(serializers.ModelSerializer):
    class Meta:
        model=ColorVariant
        fields='__all__'

class size_serializers(serializers.ModelSerializer):
    class Meta:
        model=SizeVariant
        fields='__all__'




class Product_serializers(serializers.ModelSerializer):
    category = CategorySerializer()
    quantity_type = QuantitySerializer()
    color_type=color_serializers()
    size_type=size_serializers()

    class Meta:
        model = Product
        fields = [field.name for field in Product._meta.fields if field.name != 'id']




    
from .models import Classify
from rest_framework_mongoengine import serializers

# 序列化模型


class ClassifySerializers(serializers.DocumentSerializer):
    class Meta:
        model = Classify
        fields = ('classifyName', 'createdTime', 'updateTime', 'uid')

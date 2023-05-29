from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from men.models import Men


# class MenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class MenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault())  # by default, the current user name is used

    class Meta:
        model = Men
        fields = '__all__'

# def encode():
#     model = MenModel('Face', 'Raper')
#     model_sr = MenSerializer(model)
#     print(model_sr.data)
#     json = JSONRenderer().render(model_sr.data)
#     print(json)

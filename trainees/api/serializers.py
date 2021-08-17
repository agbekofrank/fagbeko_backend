from rest_framework import serializers
from trainees.models import Trainee

class TraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainee
        fields = '__all__'


class TraineeEditSerializer(serializers.ModelSerializer):
    # image = ImageField(max_length=None, use_url=True, required=False)
    class Meta:
        model = Trainee
        fields = '__all__'
    

class TraineeDetailSerializer(serializers.ModelSerializer):
    # user = SerializerMethodField()
    # user = UserSerializer(read_only=True)
    # image = SerializerMethodField()
    class Meta:
        model = Trainee
        fields = '__all__'
    
    # def get_user(self, obj):
    #     return str(obj.user.username)

    # def get_image(self, img):
    #     try:
    #         image = 'http://localhost:8000' + img.image.url
    #     except:
    #         image = None
    #     return image

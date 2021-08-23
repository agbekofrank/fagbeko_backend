from utils.models import Education
from rest_framework import serializers
from trainees.models import Trainee
from utils.api.serializers import EducationSerializer
from skills.api.serializers import SkillSerializer

class TraineeSerializer(serializers.ModelSerializer):
    # child = RelatedFieldAlternative(queryset=Child.objects.all(), serializer=ChildSerializer)
    # education = EducationSerializer(many=True)
    skills = SkillSerializer(many=True)
    class Meta:
        model = Trainee
        fields = '__all__'
        depth = 2

class TraineeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainee
        fields = '__all__'
        depth = 2

class TraineeEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainee
        fields = '__all__'
        depth = 2
    

class TraineeDetailSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)
    class Meta:
        model = Trainee
        fields = '__all__'
        depth = 2
    
    # def get_user(self, obj):
    #     return str(obj.user.username)

    # def get_image(self, img):
    #     try:
    #         image = 'http://localhost:8000' + img.image.url
    #     except:
    #         image = None
    #     return image

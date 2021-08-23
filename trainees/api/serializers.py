from rest_framework import serializers

from trainees.models import *

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__'

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

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class FieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fields
        fields = '__all__'


class EstablishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Establishment
        fields = '__all__'
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from django.db.models import Q

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(label='Password') #PasswordField(label='Password')
    password2 = serializers.CharField(label='Confirm password')#.PasswordField(label='Confirm password')
    class  Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_password2(self, value):
        data = self.get_initial()
        password1 = data.get('password')
        password2 = value
        if password1 != password2:
            raise serializers.ValidationError('Passwords Must match!!')
        return value
    def create(self, validated_data):
        print(validated_data)
        username = validated_data['username']
        email = validated_data['email']
        # email2 = validated_data['email2']
        password = validated_data['password']
        user_obj = User(username=username, password=password, email=email)
        user_obj.set_password(password)
        user_obj.save()
        UserLoginSerializer.validate(user_obj, validated_data)
        return validated_data


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
        )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            'username', 'password', 'password2', 'email', 'first_name', 'last_name'
            )
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
                )

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )        
        user.set_password(validated_data['password'])
        user.save()

        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            # update_last_login(None, user)
        except User.DoesNotExist:
            pass
        validated_data['token'] = jwt_token

        return user



class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(label='Email Address',required=False, allow_blank=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'token']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        user_obj = None
        email = data.get('email')
        username = data.get('username')
        password = data['password']
        if not email and not username:
            raise serializers.ValidationError('You need an email or username to login!!')
        user = User.objects.filter(
            Q(username=username)|
            Q(email=email)
        ).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise serializers.ValidationError('This username/email is already there!')
        if user_obj:
            if not user_obj.check_password(password):
                raise serializers.ValidationError('Incorrect credentials, try again!!')
        try:
            payload = JWT_PAYLOAD_HANDLER(user_obj)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            # update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        data['token'] = jwt_token
        return data
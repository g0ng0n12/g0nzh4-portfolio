from rest_framework import serializers
from app.models import Job, Technology


class TechnologySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)

    class Meta:
        model = Technology
        fields = ('name',)


class JobSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=2, max_length=200)
    company = serializers.CharField(min_length=2, max_length=200)
    project = serializers.CharField(min_length=2, max_length=200)
    location = serializers.CharField(min_length=2, max_length=200)
    employment_type = serializers.CharField(min_length=2, max_length=200)
    url_company = serializers.URLField()
    description = serializers.CharField(min_length=2, max_length=200)
    image = serializers.ImageField(default=None)
    start_date = serializers.DateTimeField(
        required=False,
        input_formats=['%B %Y'], format=None, allow_null=True,
        help_text='Accepted format is "12:01 PM 16 April 2019"',
        style={'input_type': 'text', 'placeholder': '12:01 AM 28 July 2019'}
    )
    end_date = serializers.DateTimeField(
        required=False,
        input_formats=['%B %Y'], format=None, allow_null=True,
        help_text='Accepted format is "12:01 PM 16 April 2019"',
        style={'input_type': 'text', 'placeholder': '12:01 AM 28 July 2019'}
    )
    technologies = TechnologySerializer(many=True, read_only=True)

    class Meta:
        model = Job
        fields = ('title', 'company', 'description', 'url_company', 'project', 'location', 'employment_type', 'image',
                  'start_date', 'end_date', 'technologies')

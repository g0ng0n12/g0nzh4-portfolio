from rest_framework.generics import RetrieveAPIView, get_object_or_404
from rest_framework.views import Response
from .models import Job
from .serializers import JobSerializer


class JobList(RetrieveAPIView):
    queryset = Job.objects.all()
    lookup_field = 'id'
    serializer_class = JobSerializer

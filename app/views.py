from django.shortcuts import render, get_object_or_404
from .models import Job, Certification


# Create your views here.
def get_jobs(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/jobs_list.html', {'jobs': jobs})


def get_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})


def get_certifications(request):
    certifications = Certification.objects.all()
    return render(request, 'certifications/list.html', {'jobs': certifications})


def get_certification(request, certification_id):
    certification = get_object_or_404(Certification, pk=certification_id)
    return render(request, 'certifications/detail.html', {'certification': certification})

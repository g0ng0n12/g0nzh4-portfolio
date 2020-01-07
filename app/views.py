from django.shortcuts import render, get_object_or_404
from .models import Job, Certification, Project, Technology, Reading
from django.http import JsonResponse, HttpResponse
import json


# Create your views here.
def home(request):
    return render(request, 'index.html')


def get_jobs(request):
    jobs = Job.objects.order_by('-end_date')
    return render(request, 'jobs/jobs_list.html', {'jobs': jobs})


def get_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})


def get_certifications(request):
    certifications = Certification.objects.all()
    technologies = Technology.objects.filter(has_certification=True)
    return render(request, 'certifications/certifications_list.html',
                  {'certifications': certifications, 'technologies': technologies})


def get_certification(request, certification_id):
    certification = get_object_or_404(Certification, pk=certification_id)
    return render(request, 'certifications/certification_detail.html', {'certification': certification})


def get_projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})


def get_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/project_details.html', {'project': project})


def get_readings(request):
    readings = Reading.objects.all()
    return render(request, 'readings/readings_list.html', {'readings': readings})



def handler404(request, exception):
    return render(request, '404.html')


def handler500(request, exception):
    return render(request, '500.html')

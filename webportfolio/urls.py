"""webportfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('jobs', views.get_jobs, name='jobs_list'),
    path('job/<int:job_id>', views.get_job, name='job_detail'),
    path('certifications', views.get_certifications, name='certifications'),
    path('certifications/<int:certification_id>', views.get_certification, name='certification_detail'),
    path('projects', views.get_projects, name='projects'),
    path('projects/<int:project_id>', views.get_project, name='project_details')
]

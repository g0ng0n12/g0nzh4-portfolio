from django.contrib import admin
from .models import Job, Certification, Project, Technology
from django.contrib.admin.views.main import ChangeList
from app.models import Job
from app.forms import JobChangeListForm

admin.site.register(Job)
admin.site.register(Certification)
admin.site.register(Project)
admin.site.register(Technology)


class JobChangeList(ChangeList):
    def __init__(self, request, model, list_display,
                 list_display_links, list_filter, date_hierarchy,
                 search_fields, list_select_related, list_per_page,
                 list_max_show_all, list_editable, model_admin):
        super(JobChangeList, self).__init__(request, model,
                                              list_display, list_display_links, list_filter,
                                              date_hierarchy, search_fields, list_select_related,
                                              list_per_page, list_max_show_all, list_editable,
                                              model_admin)

        # these need to be defined here, and not in JobAdmin
        self.list_display = ['action_checkbox', 'name', 'technology']
        self.list_display_links = ['name']
        self.list_editable = ['technology']


class JobAdmin(admin.ModelAdmin):

    def get_changelist(self, request, **kwargs):
        return JobChangeList

    def get_changelist_form(self, request, **kwargs):
        return JobChangeListForm


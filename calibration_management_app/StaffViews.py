from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse,reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import get_list_or_404, get_object_or_404
from django.forms import modelformset_factory
from django.db import transaction, IntegrityError
import csv
import datetime
import xlwt
from io import BytesIO
from reportlab.pdfgen import canvas
from django.db.models import Q

import os
from django.conf import settings
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa


from calibration_management_app.models import CustomUser, Staffs,LeaveReportStaff, FeedBackStaffs
from calibration_management_app.models import *
from calibration_management_app.forms import *




def staff_home(request):

    # Fetch All Approve Leave
    staff = Staffs.objects.get(admin=request.user.id)
    leave_count = LeaveReportStaff.objects.filter(staff_id=staff.id, leave_status=1).count()

    total_task = Todo.objects.all().count()
    latest_job = AddNewJob.objects.all().order_by('-created_at')[0:3]
    new_task =Todo.objects.all().order_by('-created_at')[0:3]


    pending_task = Todo.objects.filter(status=False).count()

    pending_cert = Finalcert.objects.filter(check=False).count()



    labels = []
    data = []

    context={
        "leave_count": leave_count,
        "total_task": total_task,
        "latest_job": latest_job,
        "new_task": new_task,
        'pending_task': pending_task,
        'pending_cert': pending_cert,
        'labels': labels,
        'data': data,
    }

    return render(request, "staff_template/staff_home_template.html", context)





def staff_apply_leave(request):
    staff_obj = Staffs.objects.get(admin=request.user.id)
    leave_data = LeaveReportStaff.objects.filter(staff_id=staff_obj)
    context = {
        "leave_data": leave_data
    }
    return render(request, "staff_template/staff_apply_leave_template.html", context)


def staff_apply_leave_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('staff_apply_leave')
    else:
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')

        staff_obj = Staffs.objects.get(admin=request.user.id)
        try:
            leave_report = LeaveReportStaff(staff_id=staff_obj, leave_date=leave_date, leave_message=leave_message, leave_status=0)
            leave_report.save()
            messages.success(request, "Applied for Leave.")
            return redirect('staff_apply_leave')
        except:
            messages.error(request, "Failed to Apply Leave")
            return redirect('staff_apply_leave')


def staff_feedback(request):
    staff_obj = Staffs.objects.get(admin=request.user.id)
    feedback_data = FeedBackStaffs.objects.filter(staff_id=staff_obj)
    context = {
        "feedback_data":feedback_data
    }
    return render(request, "staff_template/staff_feedback_template.html", context)


def staff_feedback_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method.")
        return redirect('staff_feedback')
    else:
        feedback = request.POST.get('feedback_message')
        staff_obj = Staffs.objects.get(admin=request.user.id)

        try:
            add_feedback = FeedBackStaffs(staff_id=staff_obj, feedback=feedback, feedback_reply="")
            add_feedback.save()
            messages.success(request, "Feedback Sent.")
            return redirect('staff_feedback')
        except:
            messages.error(request, "Failed to Send Feedback.")
            return redirect('staff_feedback')







def staff_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    staff = Staffs.objects.get(admin=user)

    context={
        "user": user,
        "staff": staff
    }
    return render(request, 'staff_template/staff_profile.html', context)


def staff_profile_update(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('staff_profile')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        address = request.POST.get('address')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()

            staff = Staffs.objects.get(admin=customuser.id)
            staff.address = address
            staff.save()

            messages.success(request, "Profile Updated Successfully")
            return redirect('staff_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('staff_profile')



##################  CALIBRATION DASHBOARD ####################################################################

def calibration_dashboard(request):
    return render(request, 'staff_template/calibration_dashboard.html')



##################   ADD NEW JOB #########################################################################

class JobListView(ListView):
    context_object_name = 'job_list'
    model = AddNewJob
    template_name = 'staff_template/add_new_job/job_list.html'


class CreateNewJobView(CreateView):
	model = AddNewJob
	form_class = AddNewJobForm
	template_name = 'staff_template/add_new_job/add_new_job.html'
	success_url = reverse_lazy('job_list')


class UpdateJobView(UpdateView):
	model = AddNewJob
	form_class = AddNewJobForm
	template_name = 'staff_template/add_new_job/add_new_job.html'
	success_url = reverse_lazy('job_list')


class DeleteJobView(DeleteView):
	model = AddNewJob
	template_name = 'staff_template/add_new_job/job_confirm_delete.html'
	success_url = reverse_lazy('job_list')




############################ PARTY INFO ############################################################

class PartyListView(ListView):
    context_object_name = 'party_list'
    model = Party
    template_name = 'staff_template/party/party_list.html'


class CreatePartyView(CreateView):
	model = Party
	form_class = PartyForm
	template_name = 'staff_template/party/create_party.html'
	success_url = reverse_lazy('party_list')


class UpdatePartyView(UpdateView):
	model = Party
	form_class = PartyForm
	template_name = 'staff_template/party/create_party.html'
	success_url = reverse_lazy('party_list')


class DeletePartyView(DeleteView):
	model = Party
	template_name = 'staff_template/party/party_confirm_delete.html'
	success_url = reverse_lazy('party_list')




########################### INSTRUMENT INFO #########################################################

class InstrumentList(ListView):
    context_object_name = 'inst_list'
    model = InstrumentInfo
    template_name = 'staff_template/instrument/instrument_list.html'



class CreateInstrumentView(CreateView):
	model = InstrumentInfo
	form_class = InstrumentInfoForm
	success_url = reverse_lazy('inst_list')
	template_name = 'staff_template/instrument/instrumentinfo_form.html'


class UpdateInstrumentView(UpdateView):
	model = InstrumentInfo
	form_class = InstrumentInfoForm
	success_url = reverse_lazy('inst_list')
	template_name = 'staff_template/instrument/instrumentinfo_form.html'


class DeleteInstrumentView(DeleteView):
	model = InstrumentInfo
	success_url = reverse_lazy('inst_list')
	template_name = 'staff_template/instrument/instrumentinfo_confirm_delete.html'



#############################  MAKE ############################################

class MakeList(ListView):
    context_object_name = 'make_list'
    model = Make
    template_name = 'staff_template/make_model/make_list.html'



class CreateMakeView(CreateView):
	model = Make
	form_class = MakeForm
	success_url = reverse_lazy('make_list')
	template_name = 'staff_template/make_model/make_form.html'


class UpdateMakeView(UpdateView):
	model = Make
	form_class = MakeForm
	success_url = reverse_lazy('make_list')
	template_name = 'staff_template/make_model/make_form.html'


class DeleteMakeView(DeleteView):
	model = Make
	success_url = reverse_lazy('make_list')
	template_name = 'staff_template/make_model/make_confirm_delete.html'




####################### MODEL ################################################

class ModelList(ListView):
    context_object_name = 'model_list'
    model = Model
    template_name = 'staff_template/make_model/model_list.html'



class CreateModelView(CreateView):
	model = Model
	form_class = ModelForm
	success_url = reverse_lazy('model_list')
	template_name = 'staff_template/make_model/model_form.html'


class UpdateModelView(UpdateView):
	model = Model
	form_class = ModelForm
	success_url = reverse_lazy('model_list')
	template_name = 'staff_template/make_model/model_form.html'


class DeleteModelView(DeleteView):
	model = Model
	success_url = reverse_lazy('model_list')
	template_name = 'staff_template/make_model/model_confirm_delete.html'




######################### UUC ###############################################

class UUCListView(ListView):
    context_object_name = 'uuc_list'
    model = UUC
    template_name = 'staff_template/uuc/uuc_list.html'


class UUCCreateView(CreateView):
    model = UUC
    form_class = UUCForm
    template_name = 'staff_template/uuc/uuc_form.html'
    success_url = reverse_lazy('uuc_list')


class UUCUpdateView(UpdateView):
	model = UUC
	form_class = UUCForm
	template_name = 'staff_template/uuc/uuc_form.html'
	success_url = reverse_lazy('uuc_list')


class UUCDeleteView(DeleteView):
	model = UUC
	template_name = 'staff_template/uuc/uuc_confirm_delete.html'
	success_url = reverse_lazy('uuc_list')




###########################   # TODO  ####################################

class TodoListView(ListView):
    context_object_name = 'todo_list'
    model = Todo
    template_name = 'staff_template/todo/todo_list.html'


class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'staff_template/todo/todo_form.html'
    success_url = reverse_lazy('todo_list')


class TodoUpdateView(UpdateView):
	model = Todo
	form_class = TodoForm
	template_name = 'staff_template/todo/todo_form.html'
	success_url = reverse_lazy('todo_list')


class TodoDeleteView(DeleteView):
	model = Todo
	template_name = 'staff_template/todo/todo_confirm_delete.html'
	success_url = reverse_lazy('todo_list')



##################### MASTER INSTRUMENT ######################################

class MasterinstrumentListView(ListView):
    context_object_name = 'master_list'
    model = MasterInstrument
    template_name = 'staff_template/masterinst/master_list.html'


class CreateMasterinstrumentView(CreateView):
	model = MasterInstrument
	form_class = MasterInstrumentForm
	template_name = 'staff_template/masterinst/master_form.html'
	success_url = reverse_lazy('master_list')



class UpdateMasterinstrumentView(UpdateView):
	model = MasterInstrument
	form_class = MasterInstrumentForm
	template_name = 'staff_template/masterinst/master_form.html'
	success_url = reverse_lazy('master_list')



class DeleteMasterinstrumentView(DeleteView):
	model = MasterInstrument
	template_name = 'staff_template/masterinst/master_confirm_delete.html'
	success_url = reverse_lazy('master_list')



###################  Certificate Info #################################


class CertInfoListView(ListView):
    context_object_name = 'cert_list'
    model = Certificate_info
    template_name = 'staff_template/readings/cert_list.html'


class UpdateCertInfoView(UpdateView):
	model = Certificate_info
	form_class = CertInfoForm
	template_name = 'staff_template/readings/certificate_info_form.html'
	success_url = reverse_lazy('cert_list')



class DeleteCertInfoView(DeleteView):
	model = Certificate_info
	template_name = 'staff_template/readings/certificate_info_confirm_delete.html'
	success_url = reverse_lazy('cert_list')

class CreateCertInfoView(CreateView):
    context_object_name = 'c'
    model = Certificate_info
    form_class = CertInfoForm
    template_name = 'staff_template/readings/certificate_info_form.html'
    success_url = reverse_lazy('cert_list')



####################    FINAL Certificate   ###################################

class FinalcertListView(ListView):
    context_object_name = 'fcert_list'
    model = Finalcert
    template_name = 'staff_template/finalcert/fcert_list.html'


class CreateFinalcertView(CreateView):
	model = Finalcert
	form_class = FinalcertForm
	template_name = 'staff_template/finalcert/finalcert_form.html'
	success_url = reverse_lazy('fcert_list')



class UpdateFinalcertView(UpdateView):
	model = Finalcert
	form_class = FinalcertForm
	template_name = 'staff_template/finalcert/finalcert_form.html'
	success_url = reverse_lazy('fcert_list')



class DeleteFinalcertView(DeleteView):
	model = Finalcert
	template_name = 'staff_template/finalcert/finalcert_confirm_delete.html'
	success_url = reverse_lazy('fcert_list')


class FinalcertDetailView(DetailView):
    context_object_name = 'f'
    model = Finalcert
    template_name = 'staff_template/finalcert/finalcert_detail.html'



####################### CHECKED CERT LIST VIEW ###############################

class CheckedcertListView(ListView):
    context_object_name = 'checked_list'
    model = Finalcert
    template_name = 'staff_template/checkedcert/checkedcert_list.html'

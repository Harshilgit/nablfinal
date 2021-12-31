from django.urls import path, include
from django.conf.urls import url
from . import views
from .import HodViews, StaffViews
from django.views.generic import RedirectView



urlpatterns = [
    path('', views.loginPage, name="login"),
    path('doLogin/', views.doLogin, name="doLogin"),
    path('get_user_details/', views.get_user_details, name="get_user_details"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('admin_home/', HodViews.admin_home, name="admin_home"),
    path('add_staff/', HodViews.add_staff, name="add_staff"),
    path('add_staff_save/', HodViews.add_staff_save, name="add_staff_save"),
    path('manage_staff/', HodViews.manage_staff, name="manage_staff"),
    path('edit_staff/<staff_id>/', HodViews.edit_staff, name="edit_staff"),
    path('edit_staff_save/', HodViews.edit_staff_save, name="edit_staff_save"),
    path('delete_staff/<staff_id>/', HodViews.delete_staff, name="delete_staff"),
    path('admin_profile/', HodViews.admin_profile, name="admin_profile"),
    path('admin_profile_update/', HodViews.admin_profile_update, name="admin_profile_update"),
    path('check_email_exist/', HodViews.check_email_exist, name="check_email_exist"),
    path('check_username_exist/', HodViews.check_username_exist, name="check_username_exist"),
    path('staff_leave_view/', HodViews.staff_leave_view, name="staff_leave_view"),
    path('staff_leave_approve/<leave_id>/', HodViews.staff_leave_approve, name="staff_leave_approve"),
    path('staff_leave_reject/<leave_id>/', HodViews.staff_leave_reject, name="staff_leave_reject"),
    path('staff_feedback_message/', HodViews.staff_feedback_message, name="staff_feedback_message"),
    path('staff_feedback_message_reply/', HodViews.staff_feedback_message_reply, name="staff_feedback_message_reply"),



    path('staff_home/', StaffViews.staff_home, name="staff_home"),
    path('staff_apply_leave/', StaffViews.staff_apply_leave, name="staff_apply_leave"),
    path('staff_apply_leave_save/', StaffViews.staff_apply_leave_save, name="staff_apply_leave_save"),
    path('staff_feedback/', StaffViews.staff_feedback, name="staff_feedback"),
    path('staff_feedback_save/', StaffViews.staff_feedback_save, name="staff_feedback_save"),
    path('staff_profile/', StaffViews.staff_profile, name="staff_profile"),
    path('staff_profile_update/', StaffViews.staff_profile_update, name="staff_profile_update"),



    path('calibration_dashboard/', StaffViews.calibration_dashboard, name="calibration_dashboard"),


    path('job_list', StaffViews.JobListView.as_view(), name='job_list' ),
    path('add_new_job_create', StaffViews.CreateNewJobView.as_view(), name= 'add_new_job_create' ),
    path('job_update/<int:pk>', StaffViews.UpdateJobView.as_view(), name= 'job_update'),
    path('job_delete/<int:pk>', StaffViews.DeleteJobView.as_view(), name='job_delete'),


    path('party_list', StaffViews.PartyListView.as_view(), name='party_list' ),
    path('create_party', StaffViews.CreatePartyView.as_view(), name= 'create_party' ),
    path('party_update/<int:pk>', StaffViews.UpdatePartyView.as_view(), name= 'party_update'),
    path('party_delete/<int:pk>', StaffViews.DeletePartyView.as_view(), name='party_delete'),


    path('inst_list', StaffViews.InstrumentList.as_view(), name='inst_list' ),
    path('create_inst', StaffViews.CreateInstrumentView.as_view(), name= 'create_inst' ),
    path('inst_update/<int:pk>', StaffViews.UpdateInstrumentView.as_view(), name= 'inst_update'),
    path('inst_delete/<int:pk>', StaffViews.DeleteInstrumentView.as_view(), name='inst_delete'),


    path('make_list', StaffViews.MakeList.as_view(), name='make_list' ),
    path('create_make', StaffViews.CreateMakeView.as_view(), name= 'create_make' ),
    path('make_update/<int:pk>', StaffViews.UpdateMakeView.as_view(), name= 'make_update'),
    path('make_delete/<int:pk>', StaffViews.DeleteMakeView.as_view(), name='make_delete'),


    path('model_list', StaffViews.ModelList.as_view(), name='model_list' ),
    path('create_model', StaffViews.CreateModelView.as_view(), name= 'create_model' ),
    path('model_update/<int:pk>', StaffViews.UpdateModelView.as_view(), name= 'model_update'),
    path('model_delete/<int:pk>', StaffViews.DeleteModelView.as_view(), name='model_delete'),


    path('uuc_list', StaffViews.UUCListView.as_view(), name='uuc_list' ),
    path('uuc_create', StaffViews.UUCCreateView.as_view(), name= 'uuc_create' ),
    path('uuc_update/<int:pk>', StaffViews.UUCUpdateView.as_view(), name= 'uuc_update'),
    path('uuc_delete/<int:pk>', StaffViews.UUCDeleteView.as_view(), name='uuc_delete'),


    path('todo_list', StaffViews.TodoListView.as_view(), name='todo_list' ),
    path('create_todo', StaffViews.TodoCreateView.as_view(), name= 'create_todo' ),
    path('todo_update/<int:pk>', StaffViews.TodoUpdateView.as_view(), name= 'todo_update'),
    path('todo_delete/<int:pk>', StaffViews.TodoDeleteView.as_view(), name='todo_delete'),
    url(r'^todosearch/$', StaffViews.Todosearch, name='todosearch'),


    path('master_list', StaffViews.MasterinstrumentListView.as_view(), name='master_list' ),
    path('master_create', StaffViews.CreateMasterinstrumentView.as_view(), name= 'master_create' ),
    path('master_update/<int:pk>', StaffViews.UpdateMasterinstrumentView.as_view(), name= 'master_update'),
    path('master_delete/<int:pk>', StaffViews.DeleteMasterinstrumentView.as_view(), name='master_delete'),


    path('cert_list', StaffViews.CertInfoListView.as_view(), name='cert_list' ),
    path('certinfo_create', StaffViews.CreateCertInfoView.as_view(), name= 'certinfo_create' ),
    path('certinfo_update/<int:pk>', StaffViews.UpdateCertInfoView.as_view(), name= 'certinfo_update'),
    path('certinfo_delete/<int:pk>', StaffViews.DeleteCertInfoView.as_view(), name='certinfo_delete'),


    path('fcert_list', StaffViews.FinalcertListView.as_view(), name='fcert_list' ),
    path('fcert_detail/<int:pk>', StaffViews.FinalcertDetailView.as_view(), name='fcert_detail' ),
    path('fcert_create', StaffViews.CreateFinalcertView.as_view(), name= 'fcert_create' ),
    path('fcert_update/<int:pk>', StaffViews.UpdateFinalcertView.as_view(), name= 'fcert_update'),
    path('fcert_delete/<int:pk>', StaffViews.DeleteFinalcertView.as_view(), name='fcert_delete'),


    path('checked_list', StaffViews.CheckedcertListView.as_view(), name='checked_list' ),




    ]

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from datetime import datetime
from django.utils import timezone



class CustomUser(AbstractUser):
    user_type_data = ((1, "HOD"), (2, "Staff"), (3, "Student"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)

class LoggedInUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='logged_in_user', on_delete=models.CASCADE)
    session_key = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return self.user.username


class AdminHOD(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class Staffs(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.admin)


class LeaveReportStaff(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class FeedBackStaffs(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


#########################  PARTY INFO #########################################################
class Party(models.Model):
    id = models.AutoField(primary_key=True)
    party_name = models.CharField(max_length=200, blank=False)
    address = models.CharField(max_length=500)
    email = models.CharField(max_length=200)
    contact = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.party_name)


######################## ADD NEW JOB ###########################################################

class AddNewJob(models.Model):
    id = models.AutoField(primary_key=True)
    Job_Choices = (
    ("LAB NABL", 'LAB NABL'),
    ("LAB TRAC", 'LAB TRAC'),
    ("ONSITE NABL", 'ONSITE NABL'),
    ("ONSITE TRAC", 'ONSITE TRAC')
    )
    job_choices = models.CharField(max_length=50, choices=Job_Choices, default="LAB NABL")
    job_number = models.CharField(max_length=50, blank=False)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    party_address = models.CharField(max_length=200, blank=False)
    party_email = models.CharField(max_length=200)
    party_contact = models.CharField(max_length=15)
    party_gatepass = models.CharField(max_length=200)
    party_instrument = models.IntegerField()
    inward_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.job_number)



###################### Instrument Info ##################################################


class InstrumentInfo(models.Model):
    id = models.AutoField(primary_key=True)
    job_number = models.ForeignKey('AddNewJob', on_delete=models.CASCADE)
    inst_job_id = models.CharField(max_length=200,null=True)
    inst_name = models.ForeignKey('UUC', on_delete=models.CASCADE, related_name='inst_name')
    cust_spec_name = models.CharField(max_length=200, null=True)
    Location_Choices = (
    ("DIMENSION_LAB", 'Dimension Lab'),
    ("PRESSURE_LAB", 'Pressure Lab'),
    ("THERMAL_LAB", 'Thermal Lab'),
    ("ELECTRICAL_LAB", 'Electrical Lab'),
    ("ONSITE", 'On Site')
    )
    location = models.CharField(max_length=50, choices=Location_Choices, default="DIMENSION_LAB")
    make = models.ForeignKey('Make', on_delete=models.CASCADE)
    model = models.ForeignKey('Model', on_delete=models.CASCADE)
    sr_no = models.CharField(max_length=200)
    id_no = models.CharField(max_length=200)
    least_count = models.FloatField(max_length=200,default="")
    accuracy = models.FloatField()
    low_range = models.FloatField()
    high_range = models.FloatField()
    unit = models.CharField(max_length=100)
    inst_location = models.CharField(max_length=200)
    Condition_Choices = (
    ("OK", 'OK'),
    ("NOT_GOOD", 'NOT GOOD')
    )
    condition = models.CharField(max_length=50, choices=Condition_Choices, default="OK")
    nabl = models.BooleanField()
    Frequency_Choices = (
    ("3_MONTHS", '3 Months'),
    ("6_MONTHS", '6 Months'),
    ("1_YEAR", '1 Year'),
    ("2_YEAR", '2 Year'),
    ("3_YEAR", '3 Year')
    )
    cal_frequency = models.CharField(max_length=50, choices=Frequency_Choices, default="1_YEAR")
    sp_req = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


    def __str__(self):
        return str(self.inst_job_id)



########################  MAKE  ######################################################

class Make(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.name)


########################  MODEL  #####################################################

class Model(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.name)



#######################  UUC  ##################################################

class UUC(models.Model):
    uuc_name = models.CharField(max_length=200)
    workinstruction = models.CharField(max_length=200)
    Is_Standard = models.CharField(max_length=200)
    uncertainity = models.FloatField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.uuc_name)



###################### TODO ####################################################

class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=200)
    assigned_to = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    deadline = models.DateTimeField()
    now = models.DateTimeField(default=timezone.now, blank=True, editable = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.task_name)




#################  Master Instrument ##########################################


class MasterInstrument(models.Model):
    id = models.AutoField(primary_key=True)
    masterinstrument = models.CharField(max_length=200)
    master_serialno = models.CharField(max_length=200,null=True)
    master_idno = models.CharField(max_length=200,null=True)
    range = models.CharField(max_length=200,null=True)
    inservice_date = models.DateField(max_length=100, null=True)
    inservice = models.BooleanField(max_length=100)
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    least_count = models.FloatField(max_length=200,default="")
    resolution = models.FloatField(max_length=200,default="")
    initial_trac = models.CharField(max_length=200,default="")
    acceptance_criteria = models.CharField(max_length=200,default="")
    purchase_from = models.CharField(max_length=200,default="")
    purchase_order = models.CharField(max_length=200,default="")
    purchase_date = models.DateField(max_length=100, null=True)
    date_of_receipt = models.DateField(max_length=100, null=True)
    condition_of_receipt = models.CharField(max_length=200, null=True)
    date_of_inspection = models.DateField(max_length=100, null=True)
    software_details = models.CharField(max_length=200,default="")
    software_idno = models.CharField(max_length=200,default="")
    software_inservice = models.CharField(max_length=200,default="")
    manufacture_instruction = models.CharField(max_length=200,default="")
    national_international_standerd = models.CharField(max_length=200,default="")
    accuracy = models.FloatField(max_length=200,null=True)
    current_inst_condition = models.CharField(max_length=200)
    amount = models.FloatField(max_length=200,null=True)
    parameter_calibrated = models.CharField(max_length=200)
    referance_standard = models.CharField(max_length=200, null=True)
    ext_calibration_agency = models.CharField(max_length=200, null=True)
    cal_frequency = models.CharField(max_length=200)
    certificate_no = models.CharField(max_length=200)
    ulr_no = models.CharField(max_length=200,null=True)
    uncertainity = models.FloatField(blank=True,default=1)
    issue_date = models.DateField(max_length=100)
    exp_date = models.DateField(max_length=100)
    review_of_record = models.BooleanField(max_length=100)
    active_status = models.BooleanField(max_length=100)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


    def __str__(self):
        return str(self.masterinstrument)







####################### CERTIFICATE INFO #######################################

class Certificate_info(models.Model):
    inst_job_id = models.ForeignKey(InstrumentInfo, on_delete=models.CASCADE)
    cert_no = models.CharField(max_length=100)
    ulr_no = models.CharField(max_length=100)
    cal_date = models.DateField()
    due_date = models.DateField()

    r1_1 = models.CharField(max_length=256, null=True, default="0")
    r1_2 = models.CharField(max_length=256,null=True, default="0")
    r1_3 = models.CharField(max_length=256,null=True, default="0")
    r1_4 = models.CharField(max_length=256,null=True, default="0")
    r1_5 = models.CharField(max_length=256,null=True, default="0")
    r1_6 = models.CharField(max_length=256,null=True, default="0")
    r1_7 = models.CharField(max_length=256,null=True, default="0")
    r1_8 = models.CharField(max_length=256,null=True, default="0")
    r1_9 = models.CharField(max_length=256,null=True, default="0")
    r1_10 = models.CharField(max_length=256,null=True, default="0")

    r2_1 = models.CharField(max_length=256,null=True, default="0")
    r2_2 = models.CharField(max_length=256,null=True,default="0")
    r2_3 = models.CharField(max_length=256,null=True, default="0")
    r2_4 = models.CharField(max_length=256,null=True, default="0")
    r2_5 = models.CharField(max_length=256,null=True, default="0")
    r2_6 = models.CharField(max_length=256,null=True, default="0")
    r2_7 = models.CharField(max_length=256,null=True,default="0")
    r2_8 = models.CharField(max_length=256,null=True,default="0")
    r2_9 = models.CharField(max_length=256,null=True, default="0")
    r2_10 = models.CharField(max_length=256,null=True, default="0")

    r3_1 = models.CharField(max_length=256,null=True, default="0")
    r3_2 = models.CharField(max_length=256,null=True, default="0")
    r3_3 = models.CharField(max_length=256,null=True, default="0")
    r3_4 = models.CharField(max_length=256,null=True, default="0")
    r3_5 = models.CharField(max_length=256,null=True, default="0")
    r3_6 = models.CharField(max_length=256,null=True, default="0")
    r3_7 = models.CharField(max_length=256,null=True, default="0")
    r3_8 = models.CharField(max_length=256,null=True, default="0")
    r3_9 = models.CharField(max_length=256,null=True, default="0")
    r3_10 = models.CharField(max_length=256,null=True, default="0")

    r4_1 = models.CharField(max_length=256,null=True, default="0")
    r4_2 = models.CharField(max_length=256,null=True, default="0")
    r4_3 = models.CharField(max_length=256,null=True, default="0")
    r4_4 = models.CharField(max_length=256,null=True,default="0")
    r4_5 = models.CharField(max_length=256,null=True, default="0")
    r4_6 = models.CharField(max_length=256,null=True, default="0")
    r4_7 = models.CharField(max_length=256,null=True, default="0")
    r4_8 = models.CharField(max_length=256,null=True, default="0")
    r4_9 = models.CharField(max_length=256,null=True, default="0")
    r4_10 = models.CharField(max_length=256,null=True, default="0")

    r5_1 = models.CharField(max_length=256,null=True, default="0")
    r5_2 = models.CharField(max_length=256,null=True, default="0")
    r5_3 = models.CharField(max_length=256,null=True, default="0")
    r5_4 = models.CharField(max_length=256,null=True, default="0")
    r5_5 = models.CharField(max_length=256,null=True, default="0")
    r5_6 = models.CharField(max_length=256,null=True,default="0")
    r5_7 = models.CharField(max_length=256,null=True, default="0")
    r5_8 = models.CharField(max_length=256,null=True, default="0")
    r5_9 = models.CharField(max_length=256,null=True, default="0")
    r5_10 = models.CharField(max_length=256,null=True,default="0")


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
    	return self.cert_no



class Finalcert(models.Model):
    cert_no = models.OneToOneField('Certificate_info', on_delete=models.CASCADE)
    master = models.ForeignKey('MasterInstrument', on_delete=models.CASCADE)
    inst_name = models.ForeignKey('InstrumentInfo', on_delete=models.CASCADE)
    check = models.BooleanField(default=False)
    comment = models.CharField(max_length=500, default='In Process')
    qr_code = models.ImageField(upload_to='qr_codes', blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
    	return self.cert_no

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.cert_no)
        canvas = Image.new('RGB',(300,300), 'black')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.cert_no}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)



#Creating Django Signals

# It's like trigger in database. It will run only when Data is Added in CustomUser model

@receiver(post_save, sender=CustomUser)
# Now Creating a Function which will automatically insert data in HOD, Staff or Student
def create_user_profile(sender, instance, created, **kwargs):
    # if Created is true (Means Data Inserted)
    if created:
        # Check the user_type and insert the data in respective tables
        if instance.user_type == 1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type == 2:
            Staffs.objects.create(admin=instance)
        if instance.user_type == 3:
            Students.objects.create(admin=instance, course_id=Courses.objects.get(id=1), session_year_id=SessionYearModel.objects.get(id=1), address="", profile_pic="", gender="")


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.adminhod.save()
    if instance.user_type == 2:
        instance.staffs.save()
    if instance.user_type == 3:
        instance.students.save()

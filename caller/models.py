from django.db import models


class PhoneNumbersModel(models.Model):
    phone_number = models.BigIntegerField(unique=True, db_index=True, default=None, null=False)
    has_processed = models.BooleanField(default=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        db_table = 'tbl_phone_numbers'

    def __str__(self):
        return str(self.phone_number)


class CnicNumbersModel(models.Model):
    cnic_number = models.BigIntegerField(unique=True, db_index=True, default=None, null=False)
    cnic_teleem_pk = models.BooleanField(default=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = 'tbl_cnic_numbers'

    def __str__(self):
        return str(self.cnic_number)


class NumberDetailModel(models.Model):
    phone_number = models.ForeignKey(PhoneNumbersModel, on_delete=models.CASCADE)
    cnic = models.ForeignKey(CnicNumbersModel, on_delete=models.CASCADE)
    date = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, db_index=True, null=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    address1 = models.CharField(max_length=200, null=True)
    address2 = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    other_phone = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        db_table = 'tbl_number_details'
        unique_together = ('phone_number', 'cnic')

    def __str__(self):
        return self.name


class HavingErrorNumberModel(models.Model):
    phone_number = models.OneToOneField(PhoneNumbersModel, on_delete=models.CASCADE)
    has_processed = models.BooleanField(default=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = 'tbl_failed_numbers'

    def __str__(self):
        return str(self.phone_number)


class NetworkInformationModel(models.Model):
    phone_number = models.OneToOneField(PhoneNumbersModel, on_delete=models.CASCADE)
    city = models.CharField(max_length=200, null=True)
    network = models.CharField(max_length=45, null=True)
    province = models.CharField(max_length=60, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        db_table = 'tbl_network_information'

    def __str__(self):
        return str(self.phone_number)


class LocationGenderModel(models.Model):
    cnic = models.OneToOneField(CnicNumbersModel, on_delete=models.CASCADE)
    tehsil = models.CharField(max_length=200, db_index=True, null=True)
    division = models.CharField(max_length=200, db_index=True, null=True)
    province = models.CharField(max_length=50, db_index=True, null=True)
    gander = models.CharField(max_length=10, db_index=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        db_table = 'tbl_teleem_pk_data'

    def __str__(self):
        return self.gander


class CharaghSharedNumber(models.Model):
    phone_number = models.OneToOneField(PhoneNumbersModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    facebook_user_image = models.CharField(max_length=400, blank=True, null=True, default=None)
    facebook_user_profile_link = models.CharField(max_length=250, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        db_table = 'tbl_charagh_shared_number'

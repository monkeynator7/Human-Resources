# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Department(models.Model):
    departmentid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    groupname = models.CharField(max_length=50, blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'

class Employee(models.Model):
    businessentityid = models.OneToOneField('Person', models.DO_NOTHING, db_column='businessentityid', primary_key=True)
    nationalidnumber = models.CharField(max_length=15, blank=True, null=True)
    loginid = models.CharField(max_length=256, blank=True, null=True)
    jobtitle = models.CharField(max_length=50, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    maritalstatus = models.CharField(max_length=1, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    hiredate = models.DateField(blank=True, null=True)
    salariedflag = models.BooleanField(blank=True, null=True)
    vacationhours = models.SmallIntegerField(blank=True, null=True)
    sickleavehours = models.SmallIntegerField(blank=True, null=True)
    currentflag = models.BooleanField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    organizationnode = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class Employeedepartmenthistory(models.Model):
    employeedepartmenthistoryid = models.AutoField(primary_key=True)
    businessentityid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='businessentityid', blank=True, null=True)
    departmentid = models.ForeignKey(Department, models.DO_NOTHING, db_column='departmentid', blank=True, null=True)
    shiftid = models.ForeignKey('Shift', models.DO_NOTHING, db_column='shiftid', blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employeedepartmenthistory'


class Employeepayhistory(models.Model):
    employeepayhistoryid = models.AutoField(primary_key=True)
    businessentityid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='businessentityid', blank=True, null=True)
    ratechangedate = models.DateTimeField(blank=True, null=True)
    rate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    payfrequency = models.SmallIntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employeepayhistory'


class Person(models.Model):
    businessentityid = models.IntegerField(primary_key=True)
    persontype = models.CharField(max_length=2, blank=True, null=True)
    namestyle = models.BooleanField(blank=True, null=True)
    title = models.CharField(max_length=8, blank=True, null=True)
    firstname = models.CharField(max_length=50, blank=True, null=True)
    middlename = models.CharField(max_length=50, blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    suffix = models.CharField(max_length=10, blank=True, null=True)
    emailpromotion = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person'


class Shift(models.Model):
    shiftid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    starttime = models.TimeField(blank=True, null=True)
    endtime = models.TimeField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shift'

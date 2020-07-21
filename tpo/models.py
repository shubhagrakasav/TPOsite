from django.contrib.auth.models import *
from django.db import models
from django import forms

class CompanyProfile(models.Model):
    #TYPE = (("government","government"),("Private","Private"),("Semi-Governamet", "Semi-Governamet"),("Public", "Public"))
    GD = (("YES","YES"),("NO","NO"))
    Name_Of_the_Company = models.CharField(max_length=100,blank=True,null=True)
    Address = models.TextField()
    Type = models.CharField(max_length=20,blank=True,null=True)
    Indstry_sctr_Core = models.CharField(max_length=10,blank=True,null=True)
    Indstry_sctr_consulting = models.CharField(max_length=10,blank=True,null=True)
    Indstry_sctr_IT = models.CharField(max_length=10,blank=True,null=True)
    Indstry_sctr_Finanace = models.CharField(max_length=10,blank=True,null=True)
    Indstry_sctr_Govrnt = models.CharField(max_length=10,blank=True,null=True)
    Indstry_sctr_Other = models.CharField(max_length=100,blank=True,null=True)
    req_functional_areas_Red = models.CharField(max_length=10,blank=True,null=True)
    req_functional_areas_Maintenance = models.CharField(max_length=10,blank=True,null=True)
    req_functional_areas_Design = models.CharField(max_length=10,blank=True,null=True)
    req_functional_areas_Production = models.CharField(max_length=10,blank=True,null=True)
    req_functional_areas_RD = models.CharField(max_length=10,blank=True,null=True)
    req_functional_areas_Others = models.CharField(max_length=200,blank=True,null=True)
    req_functional_areas_Finance = models.CharField(max_length=10,blank=True,null=True)
    VsnandInterest = models.CharField(max_length=10,blank=True,null=True)
    PrsnName = models.CharField(max_length=200,blank=True,null=True)
    PrsnDesignation = models.CharField(max_length=200,blank=True,null=True)
    PrsnPhone = models.CharField(max_length=200,blank=True,null=True)
    PrsnEmail = models.CharField(max_length=200,blank=True,null=True)
    CGPA = models.CharField(max_length=10,blank=True,null=True)
    XII_perc = models.CharField(max_length=10,blank=True,null=True)
    X_perc = models.CharField(max_length=200,blank=True,null=True)
    SpecialisationPG = models.CharField(max_length=200,blank=True,null=True)
    Age_limits = models.CharField(max_length=200,blank=True,null=True)
    Test_Written = models.CharField(max_length=10,blank=True,null=True)
    Test_Aptitude = models.CharField(max_length=10,blank=True,null=True)
    Test_Online = models.CharField(max_length=10,blank=True,null=True)
    Test_Technical = models.CharField(max_length=10,blank=True,null=True)
    Test_Others = models.CharField(max_length=10,blank=True,null=True)
    GD = models.CharField(max_length=20,blank=True,null=True)
    PITechnical = models.CharField(max_length=10,blank=True,null=True)
    PIHR = models.CharField(max_length=10,blank=True,null=True)
    PIOthers = models.CharField(max_length=100,blank=True,null=True)
    ServiceAgreement = models.CharField(max_length=100,blank=True,null=True)
    TrainingPeriod = models.CharField(max_length=100,blank=True,null=True)
    AllStreamsBtech = models.CharField(max_length=10,blank=True,null=True)
    AllStreamsIDD = models.CharField(max_length=10,blank=True,null=True)
    AllStreamsMTech = models.CharField(max_length=10,blank=True,null=True)
    AllStreamsIMD = models.CharField(max_length=10,blank=True,null=True)
    CeraBtech = models.CharField(max_length=10,blank=True,null=True)
    CeraMTech = models.CharField(max_length=10,blank=True,null=True)
    CeraIDD = models.CharField(max_length=10,blank=True,null=True)
    ChemBTech = models.CharField(max_length=10,blank=True,null=True)
    ChemMTech = models.CharField(max_length=10,blank=True,null=True)
    CivilBtech = models.CharField(max_length=10,blank=True,null=True)
    CivilIDD = models.CharField(max_length=10,blank=True,null=True)
    CivilMtech = models.CharField(max_length=10,blank=True,null=True)
    ComputerBtech = models.CharField(max_length=10,blank=True,null=True)
    ComputerIDD = models.CharField(max_length=10,blank=True,null=True)
    TricalBtech = models.CharField(max_length=10,blank=True,null=True)
    TricalMTech = models.CharField(max_length=10,blank=True,null=True)
    TricalIDD = models.CharField(max_length=10,blank=True,null=True)
    TronicsBtech = models.CharField(max_length=10,blank=True,null=True)
    TronicsMTech = models.CharField(max_length=10,blank=True,null=True)
    TronicsIDD = models.CharField(max_length=10,blank=True,null=True)
    MechBtech = models.CharField(max_length=10,blank=True,null=True)
    MechMTech = models.CharField(max_length=10,blank=True,null=True)
    MechIDD = models.CharField(max_length=10,blank=True,null=True)
    MetaBtech = models.CharField(max_length=10,blank=True,null=True)
    MetaMTech = models.CharField(max_length=10,blank=True,null=True)
    MetaIDD = models.CharField(max_length=10,blank=True,null=True)
    MinBtech = models.CharField(max_length=10,blank=True,null=True)
    MinMTech = models.CharField(max_length=10,blank=True,null=True)
    MinIDD = models.CharField(max_length=10,blank=True,null=True)
    BioChemMTech = models.CharField(max_length=10,blank=True,null=True)
    BioChemIDD = models.CharField(max_length=10,blank=True,null=True)
    BioMedMTech = models.CharField(max_length=10,blank=True,null=True)
    BioMedIDD = models.CharField(max_length=10,blank=True,null=True)
    MSTMTech = models.CharField(max_length=10,blank=True,null=True)
    MSTIDD = models.CharField(max_length=10,blank=True,null=True)
    PharmaBtech = models.CharField(max_length=10,blank=True,null=True)
    PharmaMTech = models.CharField(max_length=10,blank=True,null=True)
    PharmaIDD = models.CharField(max_length=10,blank=True,null=True)
    EngPhy = models.CharField(max_length=10,blank=True,null=True)
    MNC = models.CharField(max_length=10,blank=True,null=True)
    InC = models.CharField(max_length=10,blank=True,null=True)
    CTC = models.CharField(max_length=20,blank=True,null=True)
    In_Hand = models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return self.Name_Of_the_Company
class LeavePage(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Phone = models.CharField(max_length=20)
    Subject = models.CharField(max_length=20)
    Message = models.TextField()

    def __str__(self):
        return self.Name
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Sector(models.Model):
    SECTOR = (("Core_Engineering", "Core_Engineering"), ("Consulting", "Consulting"), ("IT", "IT"), ("Finanace", "Finanace"))


class Choices(models.Model):
    description = models.CharField(max_length=300)


class Profile(models.Model):
   user = models.ForeignKey(User, blank=True, unique=True, on_delete=models.CASCADE)
   the_choices = models.ManyToManyField(Choices)
class Feedback(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Phone = models.CharField(max_length=20)
    Subject = models.CharField(max_length=20)
    Message = models.TextField()

    def __str__(self):
        return self.Name
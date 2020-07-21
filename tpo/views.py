from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext
from .forms import *
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
#from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from django.core.mail import send_mail, mail_admins
from django.contrib import messages
from .models import CompanyProfile
import re

def Home(request):
    return render(request, 'tpo/home.html')
    
def Contact_Us(request):
    return render(request, 'tpo/ContactUs.html')

def Procedure_And_Policy(request):
    return render(request, 'tpo/Procedure&Policy.html')

def CompanyResponseSheet(request):
    context = {}
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # check whether it's valid:
        if True:
            Name_Of_the_Company = request.POST.get('Name_Of_the_Company')


            #f.Name_Of_the_Company = Name_Of_the_Company
            Address = request.POST.get('Address')
            #f.Address = Address
            Type = request.POST.get('Type')
            #f.Type = Type
            Indstry_sctr_Core = request.POST.get('Indstry_sctr_Core')
            print(Indstry_sctr_Core)
            #f.Indstry_sctr_Core = Indstry_sctr_Core
            Indstry_sctr_consulting = request.POST.get('Indstry_sctr_consulting')
            #f.Indstry_sctr_consulting = Indstry_sctr_consulting
            Indstry_sctr_IT = request.POST.get('Indstry_sctr_IT')
            #f.some_field = Indstry_sctr_IT
            Indstry_sctr_Finanace = request.POST.get('Indstry_sctr_Finanace')
            #f.Indstry_sctr_Finanace = Indstry_sctr_Finanace
            Indstry_sctr_Govrnt = request.POST.get('Indstry_sctr_Govrnt')
            #f.Indstry_sctr_Govrnt = Indstry_sctr_Govrnt
            Indstry_sctr_Other = request.POST.get('Indstry_sctr_Other')
            #f.Indstry_sctr_Other = Indstry_sctr_Other
            req_functional_areas_Red = request.POST.get('req_functional_areas_Red')
            #f.req_functional_areas_Red = req_functional_areas_Red
            req_functional_areas_Maintenance = request.POST.get('req_functional_areas_Maintenance')
            #f.req_functional_areas_Maintenance = req_functional_areas_Maintenance
            req_functional_areas_Design = request.POST.get('req_functional_areas_Design')
            #f.req_functional_areas_Design = req_functional_areas_Design
            req_functional_areas_Production = request.POST.get('req_functional_areas_Production')
            #f.req_functional_areas_Production = req_functional_areas_Production
            req_functional_areas_RD = request.POST.get('req_functional_areas_RD')
            #f.req_functional_areas_RD = req_functional_areas_RD
            req_functional_areas_Others = request.POST.get('req_functional_areas_Others')
            #f.req_functional_areas_Others = req_functional_areas_Others
            req_functional_areas_Finance = request.POST.get('req_functional_areas_Finance')
            #f.req_functional_areas_Finance = req_functional_areas_Finance
            VsnandInterest = request.POST.get('VsnandInterest')
            #f.VsnandInterest = VsnandInterest
            PrsnName = request.POST.get('PrsnName')
            #f.PrsnName = PrsnName
            PrsnDesignation = request.POST.get('PrsnDesignation')
            #f.PrsnDesignation = PrsnDesignation
            PrsnPhone = request.POST.get('PrsnPhone')
            #f.PrsnPhone = PrsnPhone
            PrsnEmail = request.POST.get('PrsnEmail')
            #f.PrsnEmail = PrsnEmail
            CGPA = request.POST.get('CGPA')
            #f.CGPA = CGPA
            XII_perc = request.POST.get('XII_perc ')
            #f.XII_perc  = XII_perc
            X_perc = request.POST.get('X_perc')
            #f.X_perc = X_perc
            SpecialisationPG = request.POST.get('SpecialisationPG')
            #f.SpecialisationPG = SpecialisationPG
            Age_limits = request.POST.get('Age_limits')
            #f.Age_limits = Age_limits
            Test_Written = request.POST.get('Test_Written')
            #f.Test_Written = Test_Written
            Test_Aptitude = request.POST.get('Test_Aptitude')
            #f.Test_Aptitude = Test_Aptitude
            Test_Online = request.POST.get('Test_Online')
            #f.Test_Online = Test_Online
            Test_Technical = request.POST.get('Test_Technical')
            #f.Test_Technical = Test_Technical
            Test_Others = request.POST.get('Test_Others')
            #f.Test_Others = Test_Others
            GD = request.POST.get('GD')
            #f.GD =GD
            PITechnical = request.POST.get('PITechnical')
            #f.PITechnical = PITechnical
            PIHR = request.POST.get('PIHR')
            #f.PIHR = PIHR
            PIOthers = request.POST.get('PIOthers')
            #f.PIOthers = PIOthers
            ServiceAgreement = request.POST.get('ServiceAgreement')
            #f.ServiceAgreement = ServiceAgreement
            TrainingPeriod = request.POST.get('TrainingPeriod')
            #f.TrainingPeriod = TrainingPeriod
            AllStreamsBtech = request.POST.get('AllStreamsBtech')
            #f.AllStreamsBtech = AllStreamsBtech
            AllStreamsIDD = request.POST.get(' AllStreamsIDD')
            #f. AllStreamsIDD =  AllStreamsIDD
            AllStreamsMTech = request.POST.get('AllStreamsMTech')
            #f.AllStreamsMTech = AllStreamsMTech
            AllStreamsIMD = request.POST.get('AllStreamsIMD')
            #f.AllStreamsIMD = AllStreamsIMD
            CeraBtech = request.POST.get('CeraBtech')
            #f.CeraBtech = CeraBtech
            CeraMTech = request.POST.get('CeraMTech')
            #f.CeraMTech = CeraMTech
            CeraIDD = request.POST.get('CeraIDD')
            #f.CeraIDD = CeraIDD
            ChemBTech = request.POST.get('ChemBTech')
            #f.ChemBTech = ChemBTech
            ChemMTech = request.POST.get('ChemMTech')
            #f.ChemMTech = ChemMTech
            CivilBtech = request.POST.get('CivilBtech')
            #f.CivilBtech = CivilBtech
            CivilIDD = request.POST.get('CivilIDD')
            #f.CivilIDD = CivilIDD
            CivilMtech = request.POST.get('CivilMtech')
            #f.CivilMtech = CivilMtech
            ComputerBtech = request.POST.get('ComputerBtech')
            #f.ComputerBtech = ComputerBtech
            ComputerIDD = request.POST.get('ComputerIDD')
            #f.ComputerIDD = ComputerIDD
            TricalBtech = request.POST.get('TricalBtech')
            #f.TricalBtech = TricalBtech
            TricalMTech = request.POST.get('TricalMTech')
            #f.TricalMTech = TricalMTech
            TricalIDD = request.POST.get('TricalIDD')
            #f.TricalIDD = TricalIDD
            TronicsBtech = request.POST.get('TronicsBtech')
            #f.TronicsBtech = TronicsBtech
            TronicsMTech = request.POST.get('TronicsMTech')
            #f.TronicsMTech = TronicsMTech
            TronicsIDD = request.POST.get('TronicsIDD')
            #f.TronicsIDD = TronicsIDD
            MechBtech = request.POST.get('MechBtech')
            #f.MechBtech = MechBtech
            MechMTech = request.POST.get('MechMTech')
            #f.MechMTech = MechMTech
            MechIDD = request.POST.get('MechIDD')
            #f.MechIDD = MechIDD
            MetaBtech = request.POST.get('MetaBtech')
            #f.MetaBtech = MetaBtech
            MetaMTech = request.POST.get('MetaMTech')
            #f.MetaMTech = MetaMTech
            MetaIDD = request.POST.get('MetaIDD')
            #f.MetaIDD = MetaIDD
            MinBtech = request.POST.get('MinBtech')
            #f.MinBtech = MinBtech
            MinMTech = request.POST.get('MinMTech')
            #f.MinMTech = MinMTech
            MinIDD = request.POST.get('MinIDD')
            #f.MinIDD = MinIDD
            BioChemMTech = request.POST.get('BioChemMTech')
            #f.BioChemMTech = BioChemMTech
            BioChemIDD = request.POST.get('BioChemIDD')
            #f.BioChemIDD = BioChemIDD
            BioMedMTech = request.POST.get('BioMedMTech')
            #f.BioMedMTech = BioMedMTech
            BioMedIDD = request.POST.get('BioMedIDD')
            #f.BioMedIDD = BioMedIDD
            MSTMTech = request.POST.get('MSTMTech')
            #f.MSTMTech = MSTMTech
            MSTIDD = request.POST.get('MSTIDD')
            #f.MSTIDD = MSTIDD
            PharmaBtech = request.POST.get('PharmaBtech')
            #f.PharmaBtech = PharmaBtech
            PharmaMTech = request.POST.get('PharmaMTech')
            #f.PharmaMTech = PharmaMTech
            PharmaIDD = request.POST.get('PharmaIDD')
            #f.PharmaIDD =PharmaIDD
            EngPhy = request.POST.get('EngPhy')
            #f.EngPhy = EngPhy
            MNC = request.POST.get('MNC ')
            #f.MNC = MNC
            InC = request.POST.get('InC')
            #f.InC = InC
            CTC = request.POST.get('CTC')
            #.CTC = CTC
            In_Hand = request.POST.get('In_Hand')
            #f.In_Hand = In_Hand
            '''context = [Name_Of_the_Company= Name_Of_the_Company,'Address': Address,'Type': Type,
                       'Indstry_sctr_Core': Indstry_sctr_Core,'Indstry_sctr_consulting': Indstry_sctr_consulting,
                       'Indstry_sctr_IT': Indstry_sctr_IT,
                       'Indstry_sctr_Finanace':Indstry_sctr_Finanace,'Indstry_sctr_Govrnt': Indstry_sctr_Govrnt,
                       'Indstry_sctr_Other':Indstry_sctr_Other,
                       'req_functional_areas_Red': req_functional_areas_Red,
                       'req_functional_areas_Maintenance': req_functional_areas_Maintenance,
                       'req_functional_areas_Design': req_functional_areas_Design,
                       'req_functional_areas_Production': req_functional_areas_Production,
                       'req_functional_areas_RD': req_functional_areas_RD,
                       'req_functional_areas_Others': req_functional_areas_Others,
                       'req_functional_areas_Finance': req_functional_areas_Finance, 'VsnandInterest': VsnandInterest,
                       'PrsnName': PrsnName,
                       'PrsnDesignation': PrsnDesignation, 'PrsnPhone': PrsnPhone, 'PrsnEmail': PrsnEmail,
                       'CGPA': CGPA, 'XII_perc': XII_perc, 'X_perc': X_perc,
                       'SpecialisationPG': SpecialisationPG, 'Age_limits': Age_limits, 'Test_Written': Test_Written,
                       'Test_Aptitude': Test_Aptitude, 'Test_Online': Test_Online, 'Test_Technical': Test_Technical,
                       'Test_Others': Test_Others, 'GD': GD, 'PITechnical': PITechnical,
                       'PIHR':PIHR,'PIOthers': PIOthers, 'ServiceAgreement': ServiceAgreement,
                       'TrainingPeriod': TrainingPeriod,
                       'AllStreamsBtech': AllStreamsBtech, ' AllStreamsIDD': AllStreamsIDD,
                       'AllStreamsMTech': AllStreamsMTech, 'AllStreamsIMD': AllStreamsIMD,'CeraBtech': CeraBtech,
                       'CeraMTech': CeraMTech,'CeraIDD': CeraIDD, 'ChemBTech': ChemBTech,
                       'ChemMTech': ChemMTech, 'CivilBtech': CivilBtech,'CivilIDD': CivilIDD,'CivilMtech': CivilMtech,
                       'ComputerBtech': ComputerBtech,'ComputerIDD': ComputerIDD,'TricalBtech': TricalBtech,
                        'TricalMTech': TricalMTech, 'TricalIDD': TricalIDD, 'TronicsBtech':'TronicsBtech',
                       'TronicsMTech':TronicsMTech, 'TronicsIDD': TronicsIDD, 'MechBtech': MechBtech, 'MechMTech': MechMTech,
                       'MechIDD': MechIDD, 'MetaBtech':MetaBtech, 'MetaMTech':MetaMTech, 'MetaIDD':MetaIDD,
                       'MinBtech': MinBtech, 'MinMTech': MinMTech, 'MinIDD': MinIDD,
                       'BioChemMTech':BioChemMTech, 'BioChemIDD':BioChemIDD, 'BioMedMTech':BioMedMTech,
                       'BioMedIDD':BioMedIDD, 'MSTMTech':MSTMTech, 'MSTIDD': MSTIDD, 'PharmaBtech': PharmaBtech,
                       'PharmaMTech': PharmaMTech, 'PharmaIDD': PharmaIDD, 'EngPhy': EngPhy,
                       'MNC': MNC, 'InC': InC, 'CTC': CTC, 'In_Hand': In_Hand}'''
            objects = CompanyProfile(
                Name_Of_the_Company=Name_Of_the_Company,
                Address= Address,
                Type= Type,
                Indstry_sctr_Core= Indstry_sctr_Core,
                Indstry_sctr_consulting= Indstry_sctr_consulting,
                Indstry_sctr_IT= Indstry_sctr_IT,
                Indstry_sctr_Finanace=Indstry_sctr_Finanace,
                Indstry_sctr_Govrnt= Indstry_sctr_Govrnt,
                Indstry_sctr_Other=Indstry_sctr_Other,
                req_functional_areas_Red=req_functional_areas_Red,
                req_functional_areas_Maintenance= req_functional_areas_Maintenance,
                req_functional_areas_Design= req_functional_areas_Design,
                req_functional_areas_RD =req_functional_areas_RD,
                req_functional_areas_Others= req_functional_areas_Others,
                req_functional_areas_Finance= req_functional_areas_Finance,
                VsnandInterest= VsnandInterest,
                PrsnName=PrsnName,
                PrsnDesignation=PrsnDesignation,
                PrsnPhone= PrsnPhone,
                PrsnEmail=PrsnEmail,
                CGPA=CGPA,
                XII_perc= XII_perc,
                X_perc=X_perc,
                SpecialisationPG=SpecialisationPG,
                Age_limits=Age_limits,
                Test_Written=Test_Written,
                Test_Aptitude=Test_Aptitude,
                Test_Online=Test_Online,
                Test_Technical=Test_Technical,
                Test_Others=Test_Others,
                GD=GD,
                PITechnical= PITechnical,
                PIHR=PIHR,
                PIOthers=PIOthers,
                ServiceAgreement=ServiceAgreement,
                TrainingPeriod=TrainingPeriod,
                AllStreamsBtech= AllStreamsBtech,
                AllStreamsIDD=AllStreamsIDD,
                AllStreamsMTech=AllStreamsMTech,
                AllStreamsIMD= AllStreamsIMD,
                CeraBtech=CeraBtech,
                CeraMTech=CeraMTech,
                CeraIDD=CeraIDD,
                ChemBTech=ChemBTech,
                ChemMTech=ChemMTech,
                CivilBtech=CivilBtech,
                CivilIDD=CivilIDD,
                CivilMtech=CivilMtech,
                ComputerBtech=ComputerBtech,
                ComputerIDD=ComputerIDD,
                TricalBtech=TricalBtech,
                TricalMTech=TricalMTech,
                TricalIDD=TricalIDD,
                TronicsBtech=TronicsBtech,
                TronicsMTech=TronicsMTech,
                TronicsIDD=TronicsIDD,
                MechBtech=MechBtech,
                MechMTech=MechMTech,
                MechIDD=MechIDD,
                MetaBtech=MetaBtech,
                MetaMTech=MetaMTech,
                MetaIDD=MetaIDD,
                MinBtech=MinBtech,
                MinMTech=MinMTech,
                MinIDD=MinIDD,
                BioChemMTech=BioChemMTech,
                BioChemIDD=BioChemIDD,
                BioMedMTech=BioMedMTech,
                BioMedIDD=BioMedIDD,
                MSTMTech=MSTMTech,
                MSTIDD=MSTIDD,
                PharmaBtech=PharmaBtech,
                PharmaMTech=PharmaMTech,
                PharmaIDD=PharmaIDD,
                EngPhy=EngPhy,
                MNC=MNC,
                InC=InC,
                CTC=CTC,
                In_Hand=In_Hand
            )
            objects.save()
    return render(request, 'tpo/companyResponseSheet.html')
def Calender(request):
    return render(request, 'tpo/Calender.html')
def Zip(request):
    return FileResponse(open("tpo/static/Downloads/IIT(BHU)_JNF_INF.zip", 'rb'), content_type='application/zip')
def Leave_Page(request):
    form = LeaveForm()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LeaveForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in request.POST.get as required
            # ...
            # redirect to a new URL
            leave_form = form.save()
            Name = leave_form.Name
            Email = leave_form.Email
            Phone = leave_form.Phone
            Subject = leave_form.Subject
            Message = leave_form.Message
            body = "\nCompany Name - " + str(Name) + "\nMessage - " + str(Message)
            send_mail(subject=Subject, message=body, fail_silently=False, from_email="shubhagrakasav@gmail.com",
                      recipient_list=['shubhagra8353@gmail.com'])
            messages.add_message(request, messages.warning, 'Feedback Submitted')
            print("done")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LeaveForm()

    return render(request, 'tpo/leavePage.html', {'form': form})
def Feedback(request):
    form = FeedbackForm()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FeedbackForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in request.POST.get as required
            # ...
            # redirect to a new URL
            feedback_form = form.save()


    # if a GET (or any other method) we'll create a blank form
    else:
        form = FeedbackForm()

    return render(request, 'tpo/feedback.html', {'form': form})
def Varanasi(request):
    return render(request, 'tpo/varanasi.html')
def Overview(request):
    return render(request, 'tpo/overview.html')
def Disciplines(request):
    return render(request, 'tpo/disciplines.html')
def Beyond(request):
    return render(request, 'tpo/Beyond.html')
def Why(request):
    return render(request, 'tpo/why.html')
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        ff=0
        while True:   
            if not re.search("@iitbhu.ac.in", email): 
                messages.warning(request,'Email-id should end with @iitbhu.ac.in')
                ff=-1
                return render(request, 'tpo/register.html')
                break
            else:
                ff=0
                break
        
        password = password1
        flag = 0
        while True:   
            if (len(password)<8): 
                flag = -1
                messages.warning(request,'Password length must be at least 8 characters.NOTE: Password must contain at least one capital alphabet and numeric digit.')
                return render(request, 'tpo/register.html')
                break
            elif not re.search("[A-Z]", password): 
                flag = -1
                messages.warning(request,'Password must contain atleast one capital alphabet.NOTE:Password must contain at least one capital alphabet and numeric digit.')
                return render(request, 'tpo/register.html')
                break
            elif not re.search("[0-9]", password): 
                flag = -1
                messages.warning(request,'Password must contain atleast one numeric digit. NOTE:Password must contain at least one capital alphabet and numeric digit.')
                return render(request, 'tpo/register.html')
                break
            else: 
                flag = 0
                break
  
    
   

        if password1==password2 and flag == 0 and ff==0:
            if User.objects.filter(username=username).exists():
                messages.warning(request,'Username taken')
                return render(request, 'tpo/register.html')
            elif User.objects.filter(email=email).exists():
                messages.warning(request,'Email already registered')
                return render(request, 'tpo/register.html')
            else:
                user = User.objects.create_user(username=username, password=password1 , email=email, first_name=first_name, last_name=last_name)
                user.save()
                print("usr don")
                messages.success(request, 'Registered Successfully')
                return render(request,'tpo/register.html')
        else:
            messages.warning(request,'Password not matching')
            return render(request, 'tpo/register.html')
        return redirect('/')
    else:
        return render(request,'tpo/register.html')


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.warning(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'tpo/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
def Brochure_pdf(request):
    return FileResponse(open("tpo/static/Downloads/placement_brochure.pdf", 'rb'), content_type='application/pdf')
def Tpomsg(request):
    return render(request, 'tpo/tpomsg.html')
def Directormsg(request):
    return render(request, 'tpo/Directormsg.html')
def Facilities(request):
    return render(request, 'tpo/facilities.html')
def Policy_pdf(request):
    return FileResponse(open("tpo/static/Downloads/Placement_Policy_2019_20.pdf", 'rb'), content_type='application/pdf')
def CompanyVisiting(request):
	context = {
		'Companies': CompanyProfile.objects.all()
	}
	return render(request, 'tpo/CompanyVisiting.html', context=context)
def Prevrec(request):
        return render(request, 'tpo/prevrec.html')       
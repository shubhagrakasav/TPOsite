from django.conf.urls import url, include
from tpo import views
from django.contrib import auth
from django.conf import settings

app_name = 'tpo'

urlpatterns = [
	url(r'^$', views.Home, name='Home'),
    url(r'^contactUs$', views.Contact_Us, name='Contact_Us'),
    url(r'^Procedure&Policy', views.Procedure_And_Policy, name='Procedure_And_Policy'),
	url(r'^companyResponseSheet$', views.CompanyResponseSheet, name='CompanyResponseSheet'),
	url(r'^calender$', views.Calender, name='Calender'),
	url(r'^zip$',views.Zip, name='Zip'),
	url(r'^leavePage$', views.Leave_Page, name='Leave_Page'),
	url(r'^feedback$', views.Feedback, name='Feedback'),
	url(r'^varanasi$', views.Varanasi, name='Varanasi'),
	url(r'^overview$', views.Overview, name='overview'),
	url(r'^disciplines$', views.Disciplines, name='disciplines'),
	url(r'^Beyond$', views.Beyond, name='Beyond'),
	url(r'^why$', views.Why, name='Why'),
	url(r'^register$',views.register,name='register'),
    url(r'^login$',views.login,name='login'),
    url(r'^logout$',views.logout,name='logout'),
    url(r'^Brochurepdf$',views.Brochure_pdf, name='Brochure_pdf'),
    url(r'^tpomsg$', views.Tpomsg, name='tpomsg'),
    url(r'^directormsg$', views.Directormsg, name='directormsg'),
    url(r'^facilities$', views.Facilities, name='Facilities'),
    url(r'^Policypdf$',views.Policy_pdf, name='Policy_pdf'),
    url(r'^CompanyVisiting$',views.CompanyVisiting, name='CompanyVisiting'),
    url(r'^prevrec$', views.Prevrec, name='prevrec'),
]
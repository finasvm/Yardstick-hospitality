from django.shortcuts import render
from django.views.generic import View,CreateView,TemplateView
from admin1.views import *
from admin1.models import *
from .models import *
from django.core.mail import send_mail
import smtplib,ssl

# Create your views here.

class Home(View):
    def get(self,request):
        site_details=SiteDetails.objects.all()
        first_banner=Banner.objects.get(Banner_title='first banner')
        second_banner=Banner.objects.get(Banner_title='second banner')
        third_banner=Banner.objects.get(Banner_title='third banner')
        client_details=Clients.objects.all()
        context={'details':site_details,'first_banner':first_banner,'client_details':client_details,'second_banner':second_banner,
                 'third_banner':third_banner}
        return render(request,'index.html', context)

class About(View):
     def get(self,request):
        site_details=SiteDetails.objects.all()
        return render(request,'about.html', {'details':site_details})

class WhyUs(View):
      def get(self,request):
        site_details=SiteDetails.objects.all()
        return render(request,'whyus.html', {'details':site_details})
      
class ClientsView(View):
    def get(self,request):
        client_details=Clients.objects.all()
        site_details=SiteDetails.objects.all()
        context= {'clients':client_details,'details':site_details}
        return render(request,'clients.html',context)
    

class Gallery(View):
     def get(self,request):
        site_details=SiteDetails.objects.all()
        client_photos=ClientImages.objects.all()
        client_details=Clients.objects.exclude(title=None)
        context= {'client_details':client_details,'details':site_details,'client_photos':client_photos}
        return render(request,'gallery.html',context)

class BookNow(View):
    def get(self,request):
        site_details=SiteDetails.objects.all()
        return render(request,'booknow.html', {'details':site_details})
    def post(self,request):
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        receiver='sanifvm00@gmail.com' 
        contact_details=Contacts.objects.create(fullname=name,email=email,subject=subject,message=message)
        if contact_details:
            message=f'You have a mail \nFrom:{name}\nEmail :{email}\nsubject:{subject}\nMessage:\n{message}'
            send_mail(
            'Query about yardstick hospitality consultants',
            message,
            email,
            [receiver],
            fail_silently=False,
            html_message=None,
            )
            return render(request,'thankyou.html')
        else:
            return redirect('booknow')  


class PlanningDevelopment(View):
   def get(self,request):
        site_details=SiteDetails.objects.all()
        return render(request,'planning.html', {'details':site_details})

class CustomerExperiece(View):
   def get(self,request):
        site_details=SiteDetails.objects.all()
        return render(request,'customerexperience.html', {'details':site_details})

class OperationManagement(View):
    def get(self,request):
        site_details=SiteDetails.objects.all()
        return render(request,'operations.html', {'details':site_details})

class HumanResources(View):
    def get(self,request):
        site_details=SiteDetails.objects.all()
        return render(request,'humanresource.html', {'details':site_details})

class Wellness(View):
    def get(self,request):
        site_details=SiteDetails.objects.all()
        return render(request,'wellness.html', {'details':site_details})

class Foodbev(View):
    def get(self,request):
        site_details=SiteDetails.objects.all()
        return render(request,'foodbevarages.html', {'details':site_details})
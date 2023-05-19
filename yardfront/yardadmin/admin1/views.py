from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,TemplateView,FormView,UpdateView,DeleteView
from .forms import *
from .models import *
from django.contrib import messages
from django.urls import reverse_lazy
# Create your views here.

class Login(View):
   def get(self,request):
    if request.session.has_key('key'):
       return redirect('Clientview')
    else:
       return render(request,'login.html')
   def post(self,request):
        if request.session.has_key('key'):
            return redirect('homeadmin')
        else:
            username = request.POST['username']
            password = request.POST['password']
            if (username=='finasvm' and password=='1234'):
                request.session['key'] = 'sir'
                return redirect('Clientview')
            else:
                return redirect('loginadmin')
       
            
       
       
# class Home(View):
#     def get(self,request):
#         if request.session.has_key('key'):
#             return render(request,'home.html')
#         else:
#             return redirect('loginadmin')
        

class ClientView(View):
    def get(self,request):
        if request.session.has_key('key'):
            client_details=Clients.objects.all()
            return render(request,'showclients.html', {'clients':client_details})
        else:
            return redirect('loginadmin')

class AddClient(View):
    def get(self,request):
       if request.session.has_key('key'):
            return render(request,'addclient.html')
       else:
           return redirect('loginadmin')
    def post(self,request):
        if request.session.has_key('key'):
            title=request.POST['title1']
            img=request.FILES['image1']
            Clients.objects.create(Title=title,profimage=img)
            messages.success(self.request,'client Added successfully')
            return redirect('Clientview')
        else:
            return redirect('loginadmin')


class EditClient(UpdateView):
    template_name='editclient.html'
    form_class=ClientForm
    model=Clients
    success_url=reverse_lazy('Clientview')
    pk_url_kwarg='id'
    

    def form_valid(self, form):
            """If the form is valid, save the associated model."""
            self.object = form.save()
            messages.success(self.request,'client updated successfully')
            return super().form_valid(form)
    
class DeleteClient(DeleteView):
    template_name='deleteclients.html'
    model=Clients
    success_url=reverse_lazy('Clientview')
    pk_url_kwarg='id'
   
    
class ClientGalleryView(View):
    def get(self,request):
        if request.session.has_key('key'):
            client_details=ClientImages.objects.all()
            return render(request,'clientgalview.html', {'clients':client_details})
        else:
            return redirect('loginadmin')


class AddClientImages(View):
    def get(self,request):
            client_title=Clients.objects.all()
            return render(request,'addclientphotos.html', {'clients':client_title})
    
    def post(self,request):
        if request.session.has_key('key'):
            title=request.POST['title1']
            img=request.FILES['image1']
            custitle = Clients.objects.get(Title=title)
            ClientImages.objects.create(clienttitle=custitle,images=img)
            messages.success(self.request,'client image added successfully')

            return redirect('Clientgalview')
        else:
            return redirect('loginadmin')
    
class EditClientPic(UpdateView):
    template_name='editclientphoto.html'
    form_class=ClientFormGal
    model=ClientImages
    success_url=reverse_lazy('Clientgalview')
    pk_url_kwarg='id'

    def form_valid(self, form):
            """If the form is valid, save the associated model."""
            self.object = form.save()
            messages.success(self.request,'client image updated successfully')
            return super().form_valid(form)
    
class DeleteClientPic(DeleteView):
    template_name='deleteclientphotos.html'
    model=ClientImages
    success_url=reverse_lazy('Clientgalview')
    pk_url_kwarg='id'
    
class SiteDetailsView(View):
    def get(self,request):
            site_details=SiteDetails.objects.all()
            return render(request,'sitedetview.html', {'details':site_details})

    
class AddSiteDet(CreateView):
    model=SiteDetails
    form_class=SiteDetChange
    template_name='addsitedet.html'
    success_url=reverse_lazy('sitedetview')
    
    def form_valid(self, form):
            form.instance.user=self.request.user
            self.object = form.save()
            messages.success(self.request,'site details added successfully')
            return super().form_valid(form)

        
class EditSiteDetails(UpdateView):
    template_name='editsitedet.html'
    form_class=SiteDetChange
    model=SiteDetails
    success_url=reverse_lazy('sitedetview')
    pk_url_kwarg='id'

    def form_valid(self, form):
            """If the form is valid, save the associated model."""
            self.object = form.save()
            messages.success(self.request,'site details updated successfully')
            return super().form_valid(form)
    
class BannerView(View):
     def get(self,request):
            banner_details=Banner.objects.all()
            return render(request,'bannerview.html', {'details':banner_details})
     
class AddBannerImg(CreateView):
    model=Banner
    form_class=BannerImg
    template_name='addbannerimg.html'
    success_url=reverse_lazy('bannerview')

    def form_valid(self, form):
            form.instance.user=self.request.user
            self.object = form.save()
            messages.success(self.request,'Banner added successfully')
            return super().form_valid(form)

class EditBanner(UpdateView):
    template_name='editbanner.html'
    form_class=BannerImg
    model=Banner
    success_url=reverse_lazy('bannerview')
    pk_url_kwarg='id'

    def form_valid(self, form):
            """If the form is valid, save the associated model."""
            self.object = form.save()
            messages.success(self.request,'Banner updated successfully')

            return super().form_valid(form)
      
    
class DeleteBanner(DeleteView):
    template_name='deletebanner.html'
    model=Banner
    success_url=reverse_lazy('bannerview')
    pk_url_kwarg='id'

class Logout(View):
    def get(self,request):
        request.session.flush()
        return redirect('loginadmin')
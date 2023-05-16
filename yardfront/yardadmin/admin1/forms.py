from django import forms
from .models import *

class ClientFormGal(forms.ModelForm):
    class Meta:
        model=ClientImages
        fields  = ['images', 'clienttitle']
        labels={
            'clienttitle':'Title',
             'images':'Image'
        }
        widgets ={
            'Title':forms.TextInput(attrs={'class':'form-control'}),
            'Image':forms.ClearableFileInput(attrs={'class':'form-control'})
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model=Clients
        fields  = ['Title', 'profimage']
        labels={
            'profimage':'Image'
        }
        widgets ={
            'Title':forms.TextInput(attrs={'class':'form-control'}),
            'Image':forms.FileInput(attrs={'class':'form-control'})
        }

class SiteDetChange(forms.ModelForm):
    class Meta:
        model=SiteDetails
        fields  = ['email', 'ph_number','whatsapp_link','insta_link','facebook_link','twitter_link','utube_link','footer_copyright']
        labels={
            'Email':'email',
            'phone number':'ph_number',
            'whatsapp link':'whatsapp_link',
            'instagram link':'insta_link',
            'facebook link':'facebook_link',
            'twitter link':'twitter_link',
            'youtube link':'utube_link',
            'copyright marker':'footer_copyright'
            

        }
        widgets ={
            'Email':forms.EmailInput(attrs={'class':'form-control'}),
            'phone number':forms.NumberInput(attrs={'class':'form-control'}),
            'whatsapp link':forms.TextInput(attrs={'class':'form-control'}),
            'instagram lin':forms.TextInput(attrs={'class':'form-control'}),
            'facebook link':forms.TextInput(attrs={'class':'form-control'}),
            'twitter link':forms.TextInput(attrs={'class':'form-control'}),
            'youtube link':forms.TextInput(attrs={'class':'form-control'}),
            'copyright marker':forms.TextInput(attrs={'class':'form-control'})


        }

class BannerImg(forms.ModelForm):
    class Meta:
        model=Banner
        fields  = ['Banner_images', 'Banner_title']
        labels={
            'Banner images':'Banner_images',
            'Banner title':'Banner_title',
        }

        widgets ={
        'Banner images':forms.ClearableFileInput(attrs={'class':'form-control'}),
        'Banner title':forms.TextInput(attrs={'class':'form-control'})
        }
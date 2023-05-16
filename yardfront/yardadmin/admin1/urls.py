from django.urls import path
from .views import *
urlpatterns = [
    path('log/',Login.as_view(),name='loginadmin'),
    # path('home/',Home.as_view(),name='homeadmin'),
    path('showclients/',ClientView.as_view(),name='Clientview'),
    path('addclient/',AddClient.as_view(),name='addclients'),
    path('editclients/<int:id>/',EditClient.as_view(),name='editclients'),
    path('deleteclients/<int:id>/',DeleteClient.as_view(),name='deleteclients'),
    path('clientgallery/',ClientGalleryView.as_view(),name='Clientgalview'),
    path('addclientimages/',AddClientImages.as_view(),name='addclientsimage'),
    path('editclientsphotos/<int:id>/',EditClientPic.as_view(),name='editclientsgal'),
    path('deleteclientsphotos/<int:id>/',DeleteClientPic.as_view(),name='deleteclientsgal'),
    path('sitedetailsview/',SiteDetailsView.as_view(),name='sitedetview'),
    path('addsitedet/',AddSiteDet.as_view(),name='addsitedet'),
    path('editsitedet/<int:id>/',EditSiteDetails.as_view(),name='editsitedet'),
    # path('deletesitedet/<int:id>/',DeleteSiteDet.as_view(),name='deletesitedet'),
    path('bannerimgview/',BannerView.as_view(),name='bannerview'),
    path('addbanner/',AddBannerImg.as_view(),name='addbanner'),
    path('editbanner/<int:id>/',EditBanner.as_view(),name='editbanner'),
    path('deletebanner/<int:id>/',DeleteBanner.as_view(),name='deletebanner'),
    path('deletebanner/<int:id>/',DeleteBanner.as_view(),name='deletebanner'),
    path('logout/',Logout.as_view(),name='logout'),











]
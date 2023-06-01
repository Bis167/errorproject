from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home,name ='home' ),
path('aboutus', aboutus,name ='aboutus' ),
path('banner', banner,name ='banner' ),
path('contact', contact,name ='contact' ),
path('demo', demo,name ='demo' ),
path('faq', faq,name ='faq' ),
path('footer', footer,name ='footer' ),
path('form', form,name ='form' ),
path('hero', hero,name ='hero' ),
path('payment', payment,name ='payment' ),
path('registerform', registerform,name ='registerform' ),
path('reviews', reviews,name ='reviews' ),
path('searchResults', searchResults,name ='searchResults' ),
path('service', service,name ='service' ),
path('service1', service1,name ='service1' ),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

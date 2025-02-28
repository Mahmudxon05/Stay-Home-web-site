from django.urls import path
from .views import *

# Create your urls here.

urlpatterns = [
    path('home/',home_view),
    path('ourservices/',ourservices_view),
    path('servicestypes/',ServisTypesView.as_view()),
    path('property/',property_view),
    path('ourproperty/',OurPropertyView.as_view()),
    path('about/',about_view),
    path('agency/',agency_view),    
    path('dating/',dating_view),    
    path('works/',How_it_works_View.as_view()),    
    path('offer/',offer_view), 
    path('ouragents/',ouragent_view),  
    path('agents/',AgentView.as_view()),    
    path('ourblog/',ourblog_view),    
    path('blog/',BlogView.as_view()),    
    path('read/',read_view),    
    path('contact/',contact_view),    
    path('info/',info_view),    
    path('information/',information_view),    
    path('stayhome/',stayhome_view),    
    path('question/',question_view),    
    path('input/',input_view),
]
 
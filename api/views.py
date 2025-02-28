from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import *
from .serializer import *
from app.models import *
# Create your views here.

#----------------------_Home_View_Class_--------------------#
@api_view(['GET'])
def home_view(request):
    home = Home.objects.first()
    ser = HomeSerializer(home)
    return Response(ser.data)

#--------------------_Services_View_Classes_-------------------#

@api_view(['GET'])
def ourservices_view(request):
    services = OurServices.objects.first()
    ser = OurservicesSerializer(services)
    return Response(ser.data)


class ServisTypesView(generics.ListAPIView):
    queryset = ServicesTypes.objects.all()
    serializer_class = ServiceTypesSerializer
    permission_classes = [AllowAny]

#--------------------_Listening_View_Classs_--------------------#

@api_view(['GET'])
def property_view(request):
    property  = Property.objects.first()
    ser = PropertySerializer(property)
    return Response(ser.data)

class OurPropertyView(generics.ListAPIView):
    queryset = OurProperty.objects.all()
    serializer_class = OurPropertySerializer
    permission_classes = [AllowAny]

#---------------------_About_View_Classes_--------------------#

@api_view(['GET'])
def about_view(request):
    about = About.objects.last()
    ser = AboutSerializer(about)
    return Response(ser.data)


@api_view(['GET'])
def agency_view(request):
    agency = Agency.objects.all()
    ser = AgencySerializer(agency, many=True)
    return Response(ser.data)

#--------------------_How-it-Works_View_Classes_--------------------#

@api_view(['GET'])
def dating_view(request):
    date = Dating.objects.first()
    ser = DatingSerializer(date)
    return Response(ser.data)


class How_it_works_View(generics.ListAPIView):
    queryset = How_it_Works.objects.all()
    serializer_class = How_it_worksSerializer
    permission_classes = [AllowAny]


@api_view(['GET'])
def offer_view(request):
    offer = Offer.objects.all()
    ser = OfferSerializer(offer, many=True)
    return Response(ser.data)

#----------------------_Agent_View_Classes_-------------------# 

@api_view(['GET'])
def ouragent_view(request):
    ouragent = OurAgent.objects.last()
    data = OurAgentSerializer(ouragent)
    return Response(data.data)


class AgentView(generics.ListAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    permission_classes = [AllowAny]


@api_view(['GET'])
def ourblog_view(request):
    ourblog = OurBlog.objects.first()
    ser = OurBlogSerializer(ourblog)
    return Response(ser.data)

#----------------------_Blog_View_Classes_-------------------#

class BlogView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [AllowAny]


@api_view(['GET'])
def read_view(request):
    read = Read.objects.all()
    ser = ReadSerializer(read, many=True)
    return Response(ser.data)


@api_view(['GET'])
def contact_view(request):
    cont = Contact.objects.first()
    ser = ContactSerializer(cont)
    return Response(ser.data)

#--------------------_Contact_View_Classes--------------------#

@api_view(['GET'])
def info_view(request):
    info = Info.objects.first()
    ser = InfoSerializer(info)
    return Response(ser.data)


@api_view(['POST'])
def input_view(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    input = Input.objects.create(
        name = username,
        email = email,
        subject = subject,
        message  = message)
    return Response(InputSerializer(input).data)


@api_view(['GET'])
def information_view(request):
    infor = Information.objects.last()
    ser = InformationSerializer(infor)
    return Response(ser.data)


@api_view(['GET'])
def stayhome_view(request):
    stayhome = Stayhome.objects.last()
    ser = StayhomeSerializer(stayhome)
    return Response(ser.data)


@api_view(['GET'])
def question_view(request):
    savol = Question.objects.last()
    ser = QuestionSerializer(savol)
    return Response(ser.data)
from rest_framework import serializers
from app.models import *

class  HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = "__all__"


class OurservicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurServices
        fields = "__all__"


class ServiceTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesTypes
        fields = ["title","text"]              


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['title']


class OurPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = OurProperty
        fields = "__all__"


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"


class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = "__all__"


class How_it_worksSerializer(serializers.ModelSerializer):
    class Meta:
        model = How_it_Works
        fields = "__all__"


class DatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dating
        fields = ["title", "text"]


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ["title", "text","image","price"] 


class OurAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurAgent
        fields = ['title']       



class AgentSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Agent
        fields = "__all__"


class OurBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurBlog
        fields = ["title", "text"]


class BlogSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Blog
        fields = "__all__"  


class ReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Read
        fields = ["sharh", "title"]


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__" 


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"


class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Input
        fields = "__all__"


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = "__all__"


class StayhomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stayhome
        fields = ['title', 'text','instagram','twitter','facebook']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"                                                                                                     

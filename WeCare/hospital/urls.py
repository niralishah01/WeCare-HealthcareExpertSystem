from django.urls import path
from .views import gethospitalinfo,addhospitalinfo,gethospital,viewhospital,getupdatedhospitalinfo,updatehospitalinfo,deletehospital
from django.views.generic import TemplateView

urlpatterns=[
    path('gethospitalinfo/',gethospitalinfo),
    path('addhospitalinfo/',addhospitalinfo),
    path('viewhospital/',viewhospital),
    path('gethospital/',gethospital),
    path('getupdatedhospitalinfo/',getupdatedhospitalinfo),
    path('updatehospitalinfo/',updatehospitalinfo),
    path('deletehospital/',deletehospital)

]
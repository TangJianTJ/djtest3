from django.urls import path,re_path
from  .views import ClassifyControl
from  .views import ClassifyObject
from . import views
app_name = 'fruit'
urlpatterns = [
    path('classify/',ClassifyControl.as_view()),
    re_path('classify/(?P<uid>[0-9]+)',ClassifyObject.as_view()),
    path('classifylist/',views.ClassifyList.as_view({"get":"list","post":"create"})),
    re_path('classifylist/(?P<pk>\d+)/',views.ClassifyList.as_view({"get":"retrieve","delete":"destroy","put":"update"}))
]
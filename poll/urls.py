from .views import detail,results,vote,index
from django.urls import path


app_name = 'poll'
urlpatterns = [
    path('', index, name='index'),
    path('poll/<int:question_id>',detail,name="detail"),
    path('result/<int:question_id>',results,name="result"),
    path('vote/<int:question_id>',vote,name="vote"),
    
]
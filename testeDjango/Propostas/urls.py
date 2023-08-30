from django.urls import path

from . import views

app_name = 'proposta'

url = 'api/v1/'

urlpatterns = [
     # Apis View
     path(
        url, views.PropostaApiList.as_view(), name='proposta'
     ),
     path(
        f"{url}<int:id>/", views.PropostaUserApiList.as_view(), name='proposta_user'
     ),
     path(
        f"{url}campo-proposta/", views.CampoPropostaApiList.as_view(), name='campo'
     ),
    
     path(
          f"{url}register/", views.PropostaApiRegister.as_view(),
          name='proposta_register'
     ),
    

     path(f"{url}delete/<int:pk>/", views.PropostaDeleteAPI.as_view(), 
     name='proposta_delete'),

]
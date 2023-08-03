from django.urls import path,include
from.import views


urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login",),
    path('register/', views.register, name="register"),
    path('logout', views.logout, name='logout'),
    path('accountinfo/', views.accinfo),
    path('contact/', views.contact, name="contact"),
    path('projects/', views.projects, name="projects"),
    path('Maintenance_service/', views.Maintenance_service, name="Maintenance_service"),
    path('Wiring_service/', views.Wiring_service, name="Wiring_service"),
    path('Tiling_service/', views.Tiling_service, name="Tiling_service"),
    path('Audio_visual_service/', views.Audio_visual_service, name="Audio_visual_service"),
    path('Electrial_service/', views.Electrial_service, name="Electrial_service"),
    path('Plumbing_service/', views.Plumbing_service, name="Plumbing_service"),
    path('handyman/<int:myid>', views.handyman, name="handyman"),
    path('AboutUs/', views.AboutUs, name="AboutUs"),
    path('services/', views.services, name="services"),
    path('test/', views.test, name="services"),
    path('handlerequest/', views.handlerequest, name="handlerequest"),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('submit_review/<int:product_id>/', views.submit_review, name='submit_review'),

]


from django.conf.urls import url, patterns
from brandid import views

#URLS
app_name = 'brandid'
urlpatterns = [
    #Index URL. Displays the first page 
    url(r'^$', views.home, name='home'),
    # url(r'^beta_details/(?P<startup_id>.+)/$', views.beta_details,
    #      name='beta_details'),
    url(r'^success/$', views.success, name='success'),
    url(r'^startup_mvps/$', views.startup_mvps, name='startup_mvps'),
    url(r'^logo_design/$', views.logo_design, name='logo_design'),
    url(r'^web_design/$', views.web_design, name='web_design'),
    url(r'^services/$', views.services, name='services'),
    url(r'^mobile_app_design/$', views.mobile_app_design, name='mobile_app_design'),
    url(r'^print_design/$', views.print_design, name='print_design'),
    url(r'^corperate_branding/$', views.corperate_branding, name='corperate_branding'),
    url(r'^web_development/$', views.web_development, name='web_development'),
    url(r'^mobile_app_development/$', views.mobile_app_development, name='mobile_app_development'),
    url(r'^ecommerce_development/$', views.ecommerce_development, name='ecommerce_development'),
    url(r'^enterprise_software/$', views.enterprise_software, name='enterprise_software'),
    url(r'^cloud_deployment/$', views.cloud_deployment, name='cloud_deployment'),
    url(r'^database_migration/$', views.database_migration, name='database_migration'),
    url(r'^ecommerce/$', views.ecommerce, name='ecommerce'),
    url(r'^churches/$', views.churches, name='churches'),
    url(r'^corperate/$', views.corperate, name='corperate'),
    url(r'^small_businessess/$', views.small_businessess, name='small_businessess'),
    url(r'^education/$', views.education, name='education'),
    url(r'^government/$', views.government, name='government'),
    url(r'^ngos/$', views.ngos, name='ngos'),
    url(r'^startups/$', views.startups, name='startups'),
    url(r'^social_media_branding/$', views.social_media_branding, name='social_media_branding'),
    url(r'^about_us/$', views.about_us, name='about_us'),
    # url(r'^get_in_touch/$', views.get_in_touch, name='get_in_touch'),
    # url(r'^get_in_touch2/$', views.get_in_touch2, name='get_in_touch2'),


    ]
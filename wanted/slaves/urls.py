from django.conf.urls import url

from . import views , forms


app_name='subordinates'
urlpatterns = [
    url(r'^$', views.ShowSl),
    url(r'^a$', views.ListSubordinatesView.as_view(), name='list'),
    url(r'^add$', views.CreateSubordinate.as_view(),name="add" ),
    url(r'^sla(?P<pk>\d+)$',  views.DetailSubordinateView.as_view(), name='detail'),
    #url(r'^a(?P<pk>\d+)$',  views.DetailSubordinateView.as_view(), name='detail'),

    # url(r'^sl', 'subordinates.urls') ,
    # url(r'^admin/', admin.site.urls),
]

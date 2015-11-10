from django.conf.urls import *
from mysite.views import *
urlpatterns = patterns('',
    (r'^picture/(?P<path>.*)','django.views.static.serve',{'document_root':'./template/'}),
    (r'^search/$',search),
    (r'^detail/(.*)/$',detail),
    (r'^search/Delete/(.*)/$',search_again),
    (r'^search_Add/$',search_add),  
    (r'^update/(.*)/$',update),
)
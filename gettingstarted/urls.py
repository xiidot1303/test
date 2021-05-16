from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView, PasswordChangeView
admin.autodiscover()
from hello.views import *

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

urlpatterns = [
    path('', login),
    path('files/<str:ps>', contract),
    path('security/', open_site),
    path('folder/', folder, name='folder'),
    path('sortfolder/<str:ps>/', sortfolder, name='sortfolder'),
    path('accounts/login/', LoginView.as_view(), name='private'),
    path('changepassword/', PasswordChangeView.as_view(template_name = 'registration/change_password.html')),
    path('changepassword/done', PasswordChangeDoneView.as_view(template_name = 'bot/newpassword.html'), name='password_change_done'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profiles/', Profiles, name='profiles'),
    path('profilessortby/<str:ps>/<str:by>/', SortProfiles, name='sortprof'), 
    path('allaccountssort/<str:ps>/<str:status>/<str:year>/<str:month>/', sortallaccounts, name='sortacc'),
    path('add/account', AccCreateView.as_view(), name='createacc'),
    path('add/profile', ProfCreateView.as_view(), name = 'createprof'),
    path('delete/<int:pk>/', ProfDeleteView.as_view(), name='delprof'),
    path('afterdeleting/<str:ps>/<str:login>/', afterdeleting),
    path('account/<str:pse>/', accounts, name='account'),
    path('update/<int:pk>', AccEditView.as_view(), name='edit'),
    path('editprofile/<int:pk>', ProfEditView.as_view(), name='editprofile'),
    path('sendmessage/<str:ps>/<str:issent>', Sendmessage, name='sendmessage'),
    path('new/<int:pk>/', ProfDetailView.as_view()),
    path('detail/<int:pk>', AccDetailView.as_view()),
    path('editpassword/<int:pk>', SecEditView.as_view(), name='editpassword'),
    path('allaccounts/', allaccounts, name='allaccount'),
    path('deleteacc/<int:pk>/', AccDeleteView.as_view(), name='deleteacc'),
    path('addadmin/', addadmin),
    path('actionstory/', ActionStory),
    path('file/<str:file>', get_file),
    path('files/<str:y>/<str:m>/<str:d>/<str:f>/', sendfile),
    
    path('admin/', admin.site.urls),
    path('uploadcontract/<int:pk>/', ContractEditView.as_view()),
    

    path('content/<str:ps>/<int:pk>', content, name='content'),
    
    path('add/audio', AudioCreateView.as_view(), name='create_audio'),
    path('add/video', VideoCreateView.as_view(), name='create_video'),
    
    path('audio_detail/<int:pk>', AudioDetailView.as_view()),
    path('video_detail/<int:pk>', VideoDetailView.as_view()),
    
    path('delete_audio/<int:pk>', delete_audio, name='delaudio'),
    path('delete_video/<int:pk>', delete_video, name='delvideo'),

    path('update_audio/<int:pk>', AuidoEditView.as_view(), name='edit_audio'),
    path('update_video/<int:pk>', VideoEditView.as_view(), name='edit_video'),
    path('playsound', play_sound, name='playmusic'),
    path('add_app_file/<str:artist>/<int:pk>', generation_file, name='add_app_file'),
    path('app_list/<str:artist>', app_list, name='app_list'),
    path('open_app_file/<str:app>', open_app, name='open_app'),

    path('add_audio/<str:artist>', audio_create),
    path('add_video/<str:artist>', video_create),
]
LOGIN_REDIRECT_URL = 'bboard:folder'



from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('catalog/', include('catalog.urls'), name='library'),
    path('checkers/', include('checkers.urls'), name='checkers'),
    path('exchange_rates/', include('exchange_rates.urls'), name='exchange_rates'),
    path('file_converter/', include('file_converter.urls'), name='file_converter'),
    path('guitar_chords/', include('guitar_chords.urls'), name='guitar_chords'),
    path('seabattle/', include('seabattle.urls'), name='seabattle'),
    path('text_voice/', include('text_voice.urls'), name='text_voice'),
    path('tic_tac_toe/', include('tic_tac_toe.urls'), name='tic_tac_toe'),
    path('tutorial_english/', include('tutorial_english.urls'), name='tutorial_english'),
    path('voice_recorder/', include('voice_recorder.urls'), name='voice_recorder'),
    path('voice_text/', include('voice_text.urls'), name='voice_text'),


]

# urlpatterns += [
#     path(r'accounts/', include('django.contrib.auth.urls')),
# ]
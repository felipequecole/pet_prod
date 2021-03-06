from django.conf.urls import url
from jogo import views

urlpatterns = [
    # URLs para home
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.index, name='home'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^base_configuracoes/$', views.base_configuracoes, name='base_configuracoes'),
    url(r'^base_aplicar_dinamica/$', views.base_aplicar_dinamica, name='base_aplicar_dinamica'),
    # Cuidado com as URLS!
    # Como estamos utilizando apenas um app, temos que colocar o class/xxx
    url(r'^medico/$', views.medico_index, name='medico_index'),
    url(r'^medico/edit/(?P<id>\d+)/$', views.medico_edit, name='medico_edit'),
    url(r'^medico/delete/(?P<id>\d+)/$', views.medico_delete, name='medico_delete'),
    url(r'^medico/new/$', views.medico_new, name='medico_new'),
    url(r'^evento/$', views.evento_index, name='evento_index'),
    url(r'^evento/edit/(?P<id>\d+)/$', views.evento_edit, name='evento_edit'),
    url(r'^evento/delete/(?P<id>\d+)/$', views.evento_delete, name='evento_delete'),
    url(r'^evento/new/$', views.evento_new, name='evento_new'),
    url(r'^rodada/$', views.rodada_index, name='rodada_index'),
    url(r'^rodada/edit/(?P<id>\d+)/$', views.rodada_edit, name='rodada_edit'),
    url(r'^rodada/new/$', views.rodada_new, name='rodada_new'),

    url(r'^emprestimo/$', views.emprestimo_index, name='emprestimo_index'),
    url(r'^emprestimo/edit/(?P<id>\d+)/$', views.emprestimo_edit, name='emprestimo_edit'),
    url(r'^emprestimo/delete/(?P<id>\d+)/$', views.emprestimo_delete, name='emprestimo_delete'),
    url(r'^emprestimo/new/$', views.emprestimo_new, name='emprestimo_new'),
    #URLs para Time
    url(r'^time/$', views.time_index, name='time_index'),
    url(r'^time/edit/(?P<id>\d+)/$', views.time_edit, name='time_edit'),
    url(r'^time/delete/(?P<id>\d+)/$', views.time_delete, name='time_delete'),
    url(r'^time/new/$', views.time_new, name='time_new'),
    # URLs para area
    url(r'^area/$', views.area_index, name='area_index'),
    url(r'^area/edit/(?P<id>\d+)/$', views.area_edit, name='area_edit'),
    url(r'^area/delete/(?P<id>\d+)/$', views.area_delete, name='area_delete'),
    url(r'^area/new/$', views.area_new, name='area_new'),

    url(r'^classe_social/$', views.classe_social_index, name='classe_social_index'),
    url(r'^classe_social/edit/(?P<id>\d+)/$', views.classe_social_edit, name='classe_social_edit'),
    url(r'^classe_social/delete/(?P<id>\d+)/$', views.classe_social_delete, name='classe_social_delete'),
    url(r'^classe_social/new/$', views.classe_social_new, name='classe_social_new'),

    url(r'^modulo/$', views.modulo_index, name='modulo_index'),
    url(r'^modulo/edit/(?P<id>\d+)/$', views.modulo_edit, name='modulo_edit'),
    url(r'^modulo/delete/(?P<id>\d+)/$', views.modulo_delete, name='modulo_delete'),
    url(r'^modulo/new/$', views.modulo_new, name='modulo_new'),
]

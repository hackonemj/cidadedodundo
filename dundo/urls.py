from django.conf.urls import url
from . import views


urlpatterns = [	
	url(r'^$', views.InicioNoticiaListView.as_view(), name='noticiasinicio'),
	url(r'^dundo/$', views.dundo, name='dundo'),
	url(r'^dundo/sobre/$', views.sobre, name='sobre'),
	url(r'^dundo/actualidades/$', views.actualidades, name='actualidades'),
	url(r'^dundo/administracao/$', views.administracao, name='administracao'),

	url(r'^turismo/$', views.turismo, name='turismo'),
	url(r'^turismo/onde-ficar/$', views.onde_ficar, name='onde_ficar'),
	url(r'^turismo/patrimonio/$', views.patrimonio, name='patrimonio'),
	url(r'^turismo/lazer/$', views.lazer, name='lazer'),
	url(r'^turismo/rent-a-car$', views.rent_a_car, name='rent_a_car'),
	url(r'^turismo/sabores-locais$', views.sabores_locais, name='sabores_locais'),


	url(r'^cidade-do-dundo/$', views.cidade_do_dundo, name='cidade_do_dundo'),
	url(r'^cidade-do-dundo/porque-o-dundo/$', views.porque_o_dundo, name='porque_o_dundo'),
	url(r'^cidade-do-dundo/cultura/$', views.cultura, name='cultura'),
	url(r'^cidade-do-dundo/desporto/$', views.desporto, name='desporto'),
	url(r'^cidade-do-dundo/educacao$', views.educacao, name='educacao'),
	url(r'^cidade-do-dundo/comercio$', views.comercio, name='comercio'),
	url(r'^cidade-do-dundo/habitar$', views.habitar, name='habitar'),


	url(r'^comunidade/$', views.comunidade, name='comunidade'),
	url(r'^comunidade/empresas/$', views.empresas, name='empresas'),
	url(r'^comunidade/galeria/$', views.galeria, name='galeria'),
	url(r'^comunidade/eventos/$', views.eventos, name='eventos'),
	url(r'^comunidade/noticias/$', views.NoticiaListView.as_view(), name='noticia_list'),
    url(r'^comunidade/noticias/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<noticia>[-\w]+)/$', views.noticia_detail, name='noticia_detail'),

    url(r'^servicos$', views.servicos, name='servicos'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.servicos, name='emprego_list_by_categoria'),

	url(r'^contacto$', views.contactos, name='contactos'),
]
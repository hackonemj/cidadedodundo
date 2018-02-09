from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Count
from django.core.urlresolvers import reverse



class CategoriaNoticia(models.Model):
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'categoria_noticia'
        verbose_name_plural = 'categoriasNoticia'

    def __str__(self):
        return self.nome


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Noticia(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    autor = models.ForeignKey(User, related_name='dundo_noticias')
    fonte_noticia = models.CharField(max_length=250, null=True, blank=True)
    fonte_url = models.URLField(blank=True)
    noticia_texto = models.TextField(max_length=10000)
    imagem_url = models.URLField(blank=True)

    # Não obriga a definir a categoria por causa do blank=True
    categoria_noticia = models.ForeignKey(CategoriaNoticia, related_name='noticias',  null=True, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    objects = models.Manager() # The default manager.
    published = PublishedManager() # The Dahl-specific manager.

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('dundo:noticia_detail', args=[self.publish.year,
                                                 self.publish.strftime('%m'),
                                                 self.publish.strftime('%d'),
                                                 self.slug])

# Eventos
class Eventos(models.Model):
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='Eventos/%Y/%m/%d', blank=True)
    criado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)



# --------Categoria para o emprego-----------
class CategoriaEmprego(models.Model):
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'categoriaEmprego'
        verbose_name_plural = 'categoriasEmprego'

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('dundo:emprego_list_by_categoria', args=[self.slug])


class Emprego(models.Model):
    categoria_emprego = models.ForeignKey(CategoriaEmprego, related_name='empregos')
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    descricao = models.TextField(blank=True)
    empresa = models.CharField(max_length=200, db_index=True, null=True)
    contactos = models.CharField(max_length=300, db_index=True, null=True)
    imagem = models.ImageField(upload_to='Emprego/%Y/%m/%d', blank=True)
    disponibilidade = models.BooleanField(default=True)
    criado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-criado',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.nome

    
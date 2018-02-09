from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Noticia, Emprego, CategoriaEmprego 
# Create your views here.

def dundo(request):
    return render(request, 'dundo/dundo.html')

def sobre(request):
    return render(request, 'dundo/sobre.html')

def actualidades(request):
    return render(request, 'dundo/actualidades.html')

def administracao(request):
    return render(request, 'dundo/administracao.html')



def turismo(request):
    return render(request, 'turismo/turismo.html')
def onde_ficar(request):
    return render(request, 'turismo/onde_ficar/onde_ficar.html')
def patrimonio(request):
    return render(request, 'turismo/patrimonio/patrimonio.html')
def lazer(request):
    return render(request, 'turismo/lazer/lazer.html')
def rent_a_car(request):
    return render(request, 'turismo/rent-a-car/rent_a_car.html')
def sabores_locais(request):
    return render(request, 'turismo/sabores_locais/sabores_locais.html')


#--------Cidade do Dundo------#

def cidade_do_dundo(request):
    return render(request, 'cidade do dundo/cidade_do_dundo.html')
def porque_o_dundo(request):
    return render(request, 'cidade do dundo/porque_o_dundo/porque_o_dundo.html')
def cultura(request):
    return render(request, 'cidade do dundo/cultura/cultura.html')
def desporto(request):
    return render(request, 'cidade do dundo/desporto/desporto.html')
def educacao(request):
    return render(request, 'cidade do dundo/educacao/educacao.html')
def comercio(request):
    return render(request, 'cidade do dundo/comercio/comercio.html')
def habitar(request):
    return render(request, 'cidade do dundo/habitar/habitar.html')


#----Comunidade------#

def comunidade(request):
    return render(request, 'comunidade/comunidade.html')
def empresas(request):
    return render(request, 'comunidade/empresas/empresas.html')
def galeria(request):
    return render(request, 'comunidade/galeria/galeria.html')
def eventos(request):
    return render(request, 'comunidade/eventos/eventos.html')


def noticia_list(request, category=None):
    object_list = Noticia.published.all()
    paginator = Paginator(object_list, 4) # 4 posts in each page
    page = request.GET.get('page')
    try:
        noticias = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        noticias = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        noticias = paginator.page(paginator.num_pages)
    return render(request, 'comunidade/noticias/noticias.html', {'page': page,
                                                                'noticias': noticias})


class NoticiaListView(ListView):
    queryset = Noticia.published.all()
    #model = Noticia
    context_object_name = 'noticias'
    paginate_by = 4
    template_name = 'comunidade/noticias/noticias.html'

class InicioNoticiaListView(ListView):
    queryset = Noticia.published.all()
    #model = Noticia
    context_object_name = 'noticias'
    paginate_by = 6
    template_name = 'principal.html'

def noticia_detail(request, year, month, day, noticia):
    noticia = get_object_or_404(Noticia, slug=noticia,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request, 'comunidade/noticias/detail.html', {'noticia': noticia})


#-------------Servicos-----------------#
def servicos(request, category_slug=None):
    categoria_emprego = None
    categorias = CategoriaEmprego.objects.all()
    empregos = Emprego.objects.filter(disponibilidade=True)
    if category_slug:
        categoria_emprego = get_object_or_404(CategoriaEmprego, slug=category_slug)
        empregos = empregos.filter(categoria_emprego=categoria_emprego)
    return render(request, 'servicos/servicos.html', {'categoria_emprego': categoria_emprego,
                                                      'categorias': categorias,
                                                      'empregos': empregos})
    

#---------- Contacto ----------------#
#   imports for sending email 
from django.shortcuts import redirect
from django.contrib import messages
from.forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context



def contactos(request):
    form = ContactForm

    if request.method == 'POST':
        form = form(data=request.POST)
        
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            form_content = form.cleaned_data['content']

            template = get_template('contact_template.txt')

            context = Context({
                'contact_name':contact_name,
                'contact_email':contact_email,
                'form_content':form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                'Submisão de novo contacto',
                content,
                'Portal da Cidade do Dundo<hi@weedinglovely.com>',
                ['benhackone@gmail.com'],
                headers={'Reply-To': contact_email}
            )
            email.send()
            messages.success(request, 'Email enviado. Obrigado por nos contactar')
            return redirect('/contacto')

        else:
            messages.error(request, 'Formulário invalido')

    return render(request, 'contactos/contactos.html', {'form': form})
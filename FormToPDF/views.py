from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from cadastro.process import html_to_pdf
from django.template.loader import render_to_string
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape, A4
from reportlab.lib.units import inch, cm
from reportlab.lib.colors import HexColor
from django.conf import settings
import os

from cadastro.models import Cliente

@login_required(redirect_field_name='redirect_to')
def relatorio(request, id=None, *args, **kwargs):
    context = {}
    context['relatorio'] = Cliente.objects.get(id=id)

    return render(request, "relatorio.html", context)

#Creating a class based view
class GeneratePdf(View):
     def get(self, request, id=None, *args, **kwargs):
        data = Cliente.objects.get(pk=id)
        open('templates/temp.html', "w").write(render_to_string('relatorio.html', {'relatorio': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('relatorio.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')

def index(request):
     # Crie o objeto HttpResponse com o cabeçalho de PDF apropriado.
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=somefilename.pdf'

    # Crie o objeto PDF, usando o objeto response como seu "arquivo".
    p = canvas.Canvas(response)

    # Desenhe coisas no PDF. Aqui é onde a geração do PDF acontece.
    # Veja a documentação do ReportLab para a lista completa de
    # funcionalidades.
    p.drawString(100, 100, "Hello world.")

    # Feche o objeto PDF, e está feito.
    p.showPage()
    p.save()
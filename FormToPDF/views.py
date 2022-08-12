from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from cadastro.process import html_to_pdf
from django.template.loader import render_to_string
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, landscape, A4
from django.conf import settings
from io import BytesIO
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
        relatorio = Cliente.objects.get(pk=id)
        arquivo = open('templates/temp.html', "w").write(render_to_string('relatorio.html', {'relatorio': relatorio}))
        response = HttpResponse(arquivo, content_type='application/pdf')

        # Converting the HTML template into a PDF file
        p = canvas.Canvas(response, pagesize=landscape(A4))
        pdf = html_to_pdf('relatorio.html')
        p.showPage()
        p.save()
         
        return response
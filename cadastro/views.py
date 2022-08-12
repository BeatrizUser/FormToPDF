from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter, landscape, A4



def index(request):
    # Crie o objeto HttpResponse com o cabeçalho de PDF apropriado.
    response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename=somefilename.pdf'
     # CRIAÇÃO DO PDF EM MODO PAISAGEM , TAMANHO A4
    p = canvas.Canvas(response, pagesize=landscape(A4))

    p.drawString(100, 100, "Hello World!")

    p.showPage()
    p.save()
    return response

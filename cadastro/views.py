from reportlab.pdfgen import canvas
from django.http import HttpResponse


def index(request):
    # Crie o objeto HttpResponse com o cabeçalho de PDF apropriado.
    response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename=somefilename.pdf'
     # CRIAÇÃO DO PDF EM MODO PAISAGEM , TAMANHO A4
    c = canvas.Canvas(arquivo, pagesize=landscape(A4))
    c.drawImage(
    '%s' % imagem,
    0,
    0,
    29.7*cm,
    21*cm
    )
    # Crie o objeto PDF, usando o objeto response como seu "arquivo".
    p = canvas.Canvas(response)

    p.drawString(100, 100, "Hello World!")

    p.showPage()
    p.save()
    return response
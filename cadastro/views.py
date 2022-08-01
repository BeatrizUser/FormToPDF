from reportlab.pdfgen import canvas
from django.http import HttpResponse


def index(request):
    # Crie o objeto HttpResponse com o cabeçalho de PDF apropriado.
    response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename=somefilename.pdf'

    # Crie o objeto PDF, usando o objeto response como seu "arquivo".
    p = canvas.Canvas(response)

    p.drawString(100, 100, "Hello world.")

    p.showPage()
    p.save()
    return response
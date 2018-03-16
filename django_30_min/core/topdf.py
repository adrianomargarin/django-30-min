from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa


class Render:

    @staticmethod
    def render(path: str, params: dict):
        template = get_template(path)
        html = template.render(params)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            return HttpResponse(response.getvalue(), content_type='application/pdf')
        else:
            return HttpResponse("Error Rendering PDF", status=400)



from django.views.generic import View
from django.utils import timezone


class Pdf(View):

    def get(self, request):
        params = {
            'today': 'today',
            'sales': 'sales',
            'request': 'request'
        }
        return Render.render('pdf.html', params)

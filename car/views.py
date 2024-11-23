from rest_framework.views import APIView
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.template.loader import render_to_string
from io import BytesIO
from rest_framework import viewsets, permissions
from car.models import Car
from car.serializers import CarSerializer

class CarViewSet(viewsets.ModelViewSet):
    """
    ViewSet to manage Car objects with filtering based on car_owner.
    """
    serializer_class = CarSerializer
    queryset= Car.objects.all()

    def get_queryset(self):
        """
        Filters cars based on the logged-in user.
        """
        user = self.request.user
        if self.action in ['list', 'retrieve']:  
            return Car.objects.all()
        if user.is_authenticated:
            return Car.objects.filter(car_owner=user)
        return Car.objects.none()  

    def get_permissions(self):
        """
        Assign permissions based on the action.
        """
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]  
        return [permissions.IsAuthenticated()]  



class PDFView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user

        cars = Car.objects.all() if user.is_superuser else  Car.objects.filter(car_owner=user)

        serializer = CarSerializer(
            cars, many=True, context={'request': request})
        context = {'cars': serializer.data}

        html_string = render_to_string('car_list.html', context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=cars_list.pdf'

        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html_string.encode("UTF-8")), result)
        if not pdf.err:
            response.write(result.getvalue())
            return response
        return HttpResponse('We had some errors <pre>' + html_string + '</pre>')
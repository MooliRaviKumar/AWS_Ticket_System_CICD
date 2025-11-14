from rest_framework import viewsets
from .models import Ticket
from .serializers import TicketSerializer
from django.http import JsonResponse

def my_view(request):
    data = {
        "message": "Hello Ravi!",
        "status": "success",
        "user_count": 42
    }
    return JsonResponse(data)


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


from rest_framework.views import APIView
from tickets.utils.s3_utils import upload_to_s3

class FileUploadView(APIView):
    def post(self, request):
        file_obj = request.FILES.get('file')
        if not file_obj:
            return JsonResponse({'error': 'No file uploaded'}, status=400)
        
        url = upload_to_s3(file_obj, file_obj.name)
        if url:
            Ticket.objects.create(
                title=request.data.get('file', 'No Title'),
                description=request.data.get('html file', ''),
                attachment=url
            )
            return JsonResponse({'url': url}, status=201)
        return JsonResponse({'error': 'Upload failed'}, status=500)

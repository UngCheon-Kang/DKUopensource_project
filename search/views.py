from django.shortcuts import render
from .models import OTCMedicine

def search_medicine(request):
    query = request.GET.get('q')
    result = None
    if query:
        result = OTCMedicine.objects.filter(medicine_name__icontains=query).first()
    return render(request, 'search/result.html', {'result': result})

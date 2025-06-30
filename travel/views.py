from django.shortcuts import render
from .models import Destination, ThingToDo

def index(request):
    # Fetch all records from the Destination model
    Historicals = Destination.objects.all()
    things_to_do = ThingToDo.objects.all()
    # Prepare the context dictionary
    context = {
        'Historical': Historicals,
        'things_to_do': things_to_do,
    
    }
    
    # Render the template with the context
    return render(request, 'index.html', context)
    
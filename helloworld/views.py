from django.shortcuts import render

# Create your views here.

def hello_world_view(request):
    context= {
        "text": "hello world"
    }
    return render(request, "hello_world_template.html", context)

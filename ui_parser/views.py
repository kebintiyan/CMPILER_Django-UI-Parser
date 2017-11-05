from django.shortcuts import render
from .forms import ParseForm
from . import ui_parser

# Create your views here.
def main(request):
    if request.method == "POST":
        form = ParseForm(request.POST, request.FILES)
        if form.is_valid():
            ui_parser.parse(request.FILES['file'])
            return render(request, 'output/output.html')
    else:
        parseForm = ParseForm()

    return render(request, 'ui_parser/main.html', {'form': parseForm})
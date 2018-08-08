from django.shortcuts import render
from .forms import SubscriberForm

def index(request):
    form = SubscriberForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        # print(request.POST)
        # print(form.cleaned_data)
        new_form = form.save()
    return render(request, "landing/landing.html", {"form" : form})

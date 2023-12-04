from django.shortcuts import render, redirect
from .forms import ReaderForm

# Create your views here.
def reader(request):
    return render(request, "reader.html", {"form":ReaderForm})


# def create_reader(request):
#     if request.method == 'POST':
#         form = ReaderForm(request.POST)
#
#         if form.is_valid():
#             reader = form.save(commit=False)
#             reader.save()
#             return redirect('book')
#         else:
#             print(form.errors)
#     else:
#         reader = ReaderForm()
#
#     context = {'reader': reader}
#     return render(request, 'add_reader.html', context=context)
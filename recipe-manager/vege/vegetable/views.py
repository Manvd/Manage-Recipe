from django.shortcuts import render, redirect
from .models import receipe

def home(request):
    return render(request, 'home.html')

def receipes(request):

    if request.method == 'POST':

        receipe_name = request.POST.get('receipe_name')
        receipe_description = request.POST.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image
        )

        return redirect('/receipes/')

    queryset = receipe.objects.all()

    context = {
        'receipes': queryset
    }

    return render(request, 'receipes.html', context)


def delete_receipe(request, id):
    data = receipe.objects.get(id=id)
    data.delete()
    return redirect('/receipes/')

def update_receipe(request, id):

    data = receipe.objects.get(id=id)

    if request.method == "POST":
        dataa = request.POST

        receipe_image = request.FILES.get('receipe_image')
        data.receipe_name = dataa.get('receipe_name')
        data.receipe_description = dataa.get('receipe_description')

        if receipe_image:
            data.receipe_image = receipe_image

        data.save()
        return redirect('/receipes/')

    context = {'receipe': data}
    return render(request, 'update_receipes.html', context)
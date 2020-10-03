from django.shortcuts import render
from crudHonda.models import ProductModel
from django.contrib import messages


def showProd(request):
    showAll = ProductModel.objects.all()
    return render(request, 'index.html', {"data": showAll})


def insertMotor(request):
    if request.method == "POST":
        if request.POST.get('nama') and request.POST.get('transmisi') and request.POST.get('warna') and request.POST.get('harga'):
            saverecord = ProductModel()
            saverecord.nama = request.POST.get('nama')
            saverecord.transmisi = request.POST.get('transmisi')
            saverecord.warna = request.POST.get('warna')
            saverecord.harga = request.POST.get('harga')
            saverecord.save()
            messages.success(request, 'Motor ' +
                             saverecord.nama + ' Is Saved Sucessfully..!')
            return render(request, 'insert.html')
    else:
        return render(request, 'insert.html')

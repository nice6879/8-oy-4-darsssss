from Goods.models import Info
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import InfoForm


@login_required
def info_list(request):
    infos = Info.objects.all()
    return render(request, 'info/info_list.html', {'infos': infos})

def info_detail(request, pk):
    info = get_object_or_404(Info, pk=pk)
    return render(request, 'info/info_detail.html', {'info': info})

@login_required
def info_create(request):
    if request.method == 'POST':
        form = InfoForm(request.POST, request.FILES)
        if form.is_valid():
            info = form.save()
            return redirect('info_detail', pk=info.pk)
    else:
        form = InfoForm()
    return render(request, 'info/info_create.html', {'form': form})

@login_required
def info_update(request, pk):
    info = get_object_or_404(Info, pk=pk)
    if request.method == 'POST':
        form = InfoForm(request.POST, request.FILES, instance=info)
        if form.is_valid():
            info = form.save()
            return redirect('info_detail', pk=info.pk)
    else:
        form = InfoForm(instance=info)
    return render(request, 'info/info_update.html', {'form': form})

@login_required
def info_delete(request, pk):
    info = get_object_or_404(Info, pk=pk)
    if request.method == 'POST':
        info.delete()
        return redirect('info_list')
    return render(request, 'info/info_delete.html', {'info': info})
from django.shortcuts import render,redirect
from django.shortcuts import render, HttpResponse
from .models import AssetBasic
from datetime import datetime
# Create your views here.
# def index(request):
#     return HttpResponse('你好')


def index(request):
    return render(request,'index.html')

def Asset_menu(request):
    return render(request,'asset_menu.html')

def Asset_list(request):
    assetitem = AssetBasic.objects.all()
    return render(request,'asset_list.html',{'ast_list':assetitem})

# 编辑出版社
def Asset_edit(request):
    if request.method == 'POST':
        edit_no = request.GET.get('no')
        edit_obj = AssetBasic.objects.get(no=edit_no)

        new_put_place = request.POST.get('edit_put_place')
        new_dept = request.POST.get('edit_dept')
        new_syid = request.POST.get('edit_syid')

        now = datetime.now()
        new_chgdate = now

        edit_obj.put_place = new_put_place
        edit_obj.dept = new_dept
        edit_obj.syid = new_syid
        edit_obj.chgdate = new_chgdate

        edit_obj.save()
        return redirect('../ast_list/')

    edit_no = request.GET.get('no')
    edit_obj = AssetBasic.objects.get(no=edit_no)
    return render(request, 'asset_edit.html', {'ast_list': edit_obj})
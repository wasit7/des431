from django.shortcuts import render
from myapp.models import Customer, Item
from myapp.forms import CustomerForm
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView

# Create your views here.
def home(request):
    context={
        'user':request.user,
        'toker':'mysecret'
    }
    return render(request, 'home.html',context=context)


def profile(request):
    instance = get_object_or_404(Customer, user=request.user)
    form = CustomerForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        context = {
            'form':form,
            'user':request.user
            }
    return render(request, 'profile.html', context) 


class ItemListView(ListView):
    model = Item
    paginate_by = 3
    #queryset=Bike.objects.filter(type='mountain')
    template_name = 'item_list.html'
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Lion
from django.core.paginator import Paginator
from .form import TwoBlogPost

# Create your views here.
def lion(request):
    lion_list = Lion.objects.all()
    paginator = Paginator(lion_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'lion.html', {'lion':lion, 'posts':posts})

def detail(request, lion_id):
    details = get_object_or_404(Lion, pk=lion_id)
    return render(request, 'detail.html', {'details': details})

def new(request):
    return render(request, 'new.html')

def create(request):
    lion = Lion()
    lion.title = request.GET['title']
    lion.body = request.GET['body']
    lion.pub_date = timezone.datetime.now()
    lion.save()
    return redirect('/lion/' + str(lion.id))

    from django.core.paginator import Paginator

def twoblogpost(request):

    if request.method == 'POST':
        form = TwoBlogPost(request.POST)
        if form.is_valid():
            ttblogpost = form.save(commit=False)
            ttblogpost.pub_date = timezone.now()
            ttblogpost.save()
            return redirect('lion')

    else:
        form = TwoBlogPost()
        return render(request, 'new.html', {'form':form})






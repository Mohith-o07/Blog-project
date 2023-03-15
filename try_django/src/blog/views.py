from django.shortcuts import render,get_object_or_404,redirect
from django.http import Http404
from .forms import BlogPostForm
from .forms import BlogPostModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
from .models import BlogPost

def blog_post_list_view(request):
	#lists out objects
	#could also be search
	qs=BlogPost.objects.published()#filter(title__icontains='holy')
	if request.user.is_authenticated:
		my_qs=BlogPost.objects.filter(user=request.user)
		qs=(qs | my_qs).distinct()
	template_name='blog/list.html'
	context={'object_list':qs}
	return render(request,template_name,context)

#@login_required
@staff_member_required
def blog_post_create_view(request):
	#create objects
	form=BlogPostModelForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		obj=form.save(commit=False)
		obj.user=request.user
		obj.title=form.cleaned_data.get("title")
		obj.save()
		form=BlogPostModelForm()
	#use form to create an object
	template_name='form.html'
	context={'form':form}
	return render(request,template_name,context)

def blog_post_detail_view(request,slug):
#can also be called retrieve view..
    obj=get_object_or_404(BlogPost,slug=slug)
    template_name='blog/details.html'
    context={"object":obj}
    return render(request,template_name,context)

@staff_member_required
def blog_post_update_view(request,slug):
	obj=get_object_or_404(BlogPost,slug=slug)
	form=BlogPostModelForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	template_name='form.html'
	context={'form':form,'title':f"Update {obj.title}"}
	return render(request,template_name,context)

@staff_member_required
def blog_post_delete_view(request,slug):
	obj=get_object_or_404(BlogPost,slug=slug)
	if request.method=="POST":
		obj.delete()
		return redirect("/blog") 
	template_name='blog/delete.html'
	context={'object':obj}
	return render(request,template_name,context)
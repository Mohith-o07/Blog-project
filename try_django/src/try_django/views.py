from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm
from blog.models import BlogPost

def home_page(request):
	my_title="I'll be back"
	qs=BlogPost.objects.all()[:5]
	context={"title":"Welcome to Try Django",'blog_list':qs}
	#template_name="title.txt"
	#template_obj=get_template(template_name)
	#rendered_item=template_obj.render(context)
	#print(rendered_item)
	#doc="<h1>{title}</h1>".format(title=mytitle)
	#django_rendered_doc="<h1>{{title}}</h1>".format(title=my_title)
	return render(request,"home.html",context)

def about_page(request):
	return render(request,"about.html",{"title":"About US.."})

def contact_page(request):
	form=ContactForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		form=ContactForm()
	context={
	"title":"Contact Us",
	"form":form
	}
	return render(request,"form.html",context)
	
def example_page(request):
	context={"title":"example"}
	template_name="hello.html"
	template_obj=get_template(template_name)
	rendered_item=template_obj.render(context)
	return HttpResponse(rendered_item)

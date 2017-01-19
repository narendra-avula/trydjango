from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
# Create your views here.

from .models import Post
from .forms import PostForm

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Not Successfully Created")
    context = {
        "form" : form,
    }
    return render(request, "post_form.html", context)


def post_detail(request, abc=None):
    instance = get_object_or_404(Post, id=abc)
    context = {
        "title" : instance.title ,
        "instance" : instance
    }
    return render(request, "post_detail.html", context)


def post_list(request):
    queryset = Post.objects.all()
    context = {
        "title" : "List",
        "objects_list" : queryset
    }
    return render(request, "index.html", context)


def post_update(request, abc=None):
    instance = get_object_or_404(Post, id=abc)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Not Successfully Updated")
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "post_form.html", context)


def post_delete(request, abc=None):
    instance = get_object_or_404(Post, id=abc)
    instance.delete()
    messages.success(request, "Successfully Deleted")
    return redirect("posts:list")




# def post_list(request):
#     if request.user.is_authenticated():
#         context = {
#             "title": "My User List"
#         }
#     else:
#         context = {
#             "title" : "List"
#         }
#     return render(request, "index.html", context)
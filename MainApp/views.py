from django.shortcuts import render, redirect

from .forms import CommentForm
from .models import Pizza, Topping, Comment
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.


def index(request):
    return render(request, "MainApp/index.html")


def pizzas(request):
    pizzas = Pizza.objects.filter(owner=request.user)

    context = {"pizzas": pizzas}

    return render(request, "MainApp/pizzas.html", context)


def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    comments = pizza.entry_set.order_by("-date_added")
    toppings = pizza.entry_set.order_by("-topping_name")

    context = {"pizza": pizza, "toppings": toppings, "comments": comments}

    return render(request, "MainApp/pizza.html", context)


@login_required
def new_comment(request, topic_id):
    pizza = Pizza.objects.get(id=topic_id)

    if request.method != "POST":
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.pizza = pizza
            new_entry.save()
            return redirect("MainApp:pizza", topic_id=topic_id)

    context = {"form": form, "pizza": pizza}

    return render(request, "MainApp/new_comment.html", context)


@login_required
def edit_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    pizza = comment.pizza

    if comment.owner != request.user:
        raise Http404

    if request.method != "POST":
        form = CommentForm(instance=comment)
    else:
        form = CommentForm(instance=comment, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect("MainApp:pizza", pizza_id=pizza.id)

    context = {"form": form, "pizza": pizza, "comment": comment}

    return render(request, "MainApp/edit_comment.html", context)

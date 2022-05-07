from django.shortcuts import render, redirect

from MainApp.forms import CommentForm
from MainApp.models import Pizza, Topping, Comment
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.


def index(request):
    return render(request, "MainApp/index.html")


def pizzas(request):
    pizzas = Pizza.objects.filter()

    context = {"pizzas": pizzas}

    return render(request, "MainApp/pizzas.html", context)


def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    comments = pizza.comment_set.order_by("-date_added")
    toppings = pizza.topping_set.order_by("-toppings_name")

    context = {"pizza": pizza, "toppings": toppings, "comments": comments}

    return render(request, "MainApp/pizza.html", context)


@login_required
def new_comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method != "POST":
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.pizza = pizza
            new_entry.owner = request.user
            new_entry.save()
            return redirect("pizza", pizza_id=pizza_id)

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
            return redirect("pizza", pizza_id=pizza.id)

    context = {"form": form, "pizza": pizza, "comment": comment}

    return render(request, "MainApp/edit_comment.html", context)

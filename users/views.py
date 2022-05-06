from django.shortcuts import render

# Create your views here.
def register(request):
    if request.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("MainApp:index")

    context = {"form": form}

    return render(request, "registration/register.html", context)

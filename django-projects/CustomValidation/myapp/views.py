# from django.shortcuts import render, redirect
# from .forms import AnagramForm
#
# def index(request):
#
#     if request.method == 'POST':
#         form = AnagramForm(request.POST)
#
#         if form.is_valid():
#             redirect('index')
#         else:
#             form = AnagramForm()
#         context = {'form' : form}
#
#         return render(request, 'index.html', context)

    from django.shortcuts import redirect, render
    from example.core.forms import AddBookForm

    def add_book(request):
        if request.method == "POST":
            form = AddBookForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("/books/")
        else:
            form = AddBookForm()
        return render(request, "add_book.html", {"form": form})

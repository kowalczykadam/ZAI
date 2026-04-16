import csv
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import ImportCSVForm
from .models import Book
from .services import fetch_books_from_api
from django.views.decorators.csrf import csrf_exempt


def import_from_api(request):
    books = fetch_books_from_api()
    return JsonResponse({"status": "ok", "imported": len(books)})


@csrf_exempt
def import_csv(request):
    if request.method == "POST":
        form = ImportCSVForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES["file"]
            decoded = file.read().decode("utf-8").splitlines()
            reader = csv.DictReader(decoded)

            for row in reader:
                Book.objects.create(
                    title=row["title"],
                    author=row["author"],
                    year=row.get("year")
                )

            return redirect("book_list")
    else:
        form = ImportCSVForm()

    return render(request, "books/import_csv.html", {"form": form})

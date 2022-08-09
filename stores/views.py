from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .forms import StoreItemForm
from stores import models
from django.http import HttpResponse


def get_store_items(request: HttpRequest) -> HttpResponse:
    store_items: list[models.StoreItem] = list(models.StoreItem.objects.all())
    context = {
        "store_items": store_items,
    }
    return render(request, "store_item_list.html", context)


def update_store_item(request, item_id):
    store_item = models.StoreItem.objects.get(id=item_id)
    form = StoreItemForm(instance=store_item)
    if request.method == "POST":
        form = StoreItemForm(request.POST, instance=store_item)
        if form.is_valid():
            form.save()
            return redirect("store-item-list")
    context = {"form": form,
               "store_item": store_item}
    return render(request, "update_store_item.html", context)


# Add a delete_store_item view.
# Accept an item_id in the parameters.
# -Try to get the StoreItem and assign it to a variable called store_item.
# -Except if it does not exist, then raise an Http404 error.
# -Delete the store_item using store_item.delete() below your try-except block.
# -At the end, Redirect to store-item-list.

def delete_store_item(request, item_id):
    try:
        store_item = models.StoreItem.objects.get(id=item_id)
    except:
        if store_item is None:
            raise HttpResponse("Store item not found")

    store_item.delete()
    return redirect("store-item-list")


def create_store_item(request):
    form = StoreItemForm

    if request.method == "POST":
        form = StoreItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("store-item-list")
    context = {
        "form": form,
    }
    return render(request, "create_store_item.html", context)

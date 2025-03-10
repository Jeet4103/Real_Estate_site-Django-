from django.shortcuts import render  , redirect
from .models import Listing
from .forms import ListingForm

#CRUD - Create, Read, Update, Delete

def Listing_list(request):
   listings = Listing.objects.all()
   context = {
         "listings": listings
   }
   return render(request, "listings.html", context)

def listing_reterive(request, id):
   listing = Listing.objects.get(id=id)
   context = {
         "listing": listing
   }
   return render(request, "listing.html", context)

def listing_create(request):
      form = ListingForm()
      if request.method == "POST":
            form = ListingForm(request.POST, request.FILES)
            if form.is_valid():
                  form.save()
                  return redirect("/")

            context = {
            "form": form
             }
            return  render(request, "listing_create.html", context)
            
      form = ListingForm()
      context = {
            "form": form
      }
      return render(request, "listing_create.html", context)

def listing_update(request, id):
      listing = Listing.objects.get(id=id)
      form = ListingForm(instance=listing)

      if request.method == "POST":
            form = ListingForm(request.POST, request.FILES, instance=listing)
            if form.is_valid():
                  form.save()
                  return redirect("/")

            context = {
            "form": form
             }
            return  render(request, "listing_update.html", context)
            
      form = ListingForm()
      context = {
            "form": form
      }
      return render(request, "listing_update.html", context)

def listing_delete(request, id):
      listing = Listing.objects.get(id=id)
      listing.delete()
      return redirect("/")


      
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Urls
from . import encoderdecoder

# Home Page
def index(request):
    return render(request,'form.html')
    
# Redirecting to the original page
def redirector(request, shortUrl):

    # Converting url to index
    short_id = encoderdecoder.toBase10(shortUrl)

    # Looking for the object in database
    try:
        obj = get_object_or_404(Urls, short_id=short_id)
    except:
        return render(request,'form.html',{'message':'The given URL does not exist'})

    # Increasing count    
    obj.count += 1

    # Updating in database
    try:
        obj.save()
    except:
        return render(request,'form.html',{'message':'Error connecting to the database'})

    # Redirecting to original URL
    return redirect(obj.long_url)

# Creating ShortURLs
def short(request):

    # Read input URL
    try:
        url = request.POST['long_url']
    except:
        return redirect('/')
    
    # Check if input URL is empty
    if len(url) > 0:
        url = url.strip()
        url = ''.join(url.split())
        try:
            # Checking if URL already exists in the database
            obj = Urls.objects.get(long_url=url)

            # If found, converting the index to Base62 
            shortLink = encoderdecoder.toBase62(obj.short_id)

            shortUrl = 'http://127.0.0.1:8000/'+shortLink
            # Returning the short url to the user
            return render(request,'form.html',{'shorturl':shortUrl})
        except:
            # The URL does not exist in the server

            # Making an object of class URLs
            url_obj = Urls(long_url = url)

            # Updating in database
            try:
                url_obj.save()
            except:
                return render(request,'form.html',{'message':'Error connecting to the database'})

            # Looking for index on the updated URL
            try:
                short_id = Urls.objects.get(long_url=url).short_id
            except:
                return render(request,'form.html',{'message':'Error connecting to the database'})

            # Converting the index to Base64    
            shortLink = encoderdecoder.toBase62(short_id)

            message = 'http://127.0.0.1:8000/'+shortLink
            # Returning the short url to the user
            return render(request,'form.html',{'shorturl':message})

    # If input URL is empty, give the following message
    return render(request,'form.html',{'message':'Please enter a url'})
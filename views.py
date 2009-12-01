from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from pixel import render_png

def index(request):
    rgb = request.GET.get("rgb", None)
    if rgb:
        return HttpResponseRedirect("/%s/" % rgb)
    else:
        return render_to_response('colossalpixel/index.html')

def notacolor(request, rgb):
    return render_to_response('colossalpixel/notacolor.html', { 'rgb': rgb, })

def rgb(request, rgb):
    return render_to_response('colossalpixel/rgb.html', { 'rgb': rgb, })

def png(request, rgb):
    png = render_png(rgb)
    return HttpResponse(png, content_type='image/png')
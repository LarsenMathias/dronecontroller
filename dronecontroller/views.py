from django.shortcuts import render
from django.http import HttpResponse
from dronecontroller.dronetesting import start,tello
# Create your views here.
def home(request):
    print("working")
    context={"objest tracking logic"}
    return render(request,"home.html")
def simple_function(request):
    print("code is working")
    fbrange=[6200,6800]
    # pid=[0.4,0.4,0]
    # pError=int(0)
    w,h=360,240
    tello.connect()
    tello.streamon()
    frame_read = tello.get_frame_read()
    tello.takeoff()
    start()
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")
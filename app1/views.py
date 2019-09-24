from django.shortcuts import render

# Create your views here.
def app1view(request):
    return render(request, 'land.html')
def dashboardview(request):
    return render(request, 'dashboard.html')
def Tview(request):
    return render(request, 'T.html')
def newframeview(request):
    return render(request, 'newframe.html')
def userprofileview(request):
    return render(request, 'userprofile.html')

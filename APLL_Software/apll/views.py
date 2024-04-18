from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def testing(request):
  mydata = Member.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
  
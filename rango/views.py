from django.http import HttpResponse


def index(request):
    return HttpResponse("<app_name> says hey there partner !")

from django.http import HttpResponse


def hello_word(request):
    print('request method: ', request.method)
    print('request meta: ', request.META)
    print('request cookies: ', request.COOKIES)
    return HttpResponse('OK')

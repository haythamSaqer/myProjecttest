from django.shortcuts import render


def test(request):

    context = {}
    return render(request, 'myWebsite/index.html', context)
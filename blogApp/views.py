from django.shortcuts import render

def post_list(request):
    return render(request, 'blogApp/post_list.html')

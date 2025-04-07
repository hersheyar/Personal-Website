from django.shortcuts import render


def project_lists_view(request):
    return render(request, "content/project_lists.html")


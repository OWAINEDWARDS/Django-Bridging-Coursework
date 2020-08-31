from django.shortcuts import render
from django.utils import timezone
from .models import CVpost, Qualifications, Projects
from django.shortcuts import render, get_object_or_404
from .forms import CVForm, QualificationsForm, ProjectsForm
from django.shortcuts import redirect

def home_view(request):
    cvposts = CVpost.objects.all()
    qposts = Qualifications.objects.all()
    pposts = Projects.objects.all()
    return render(request, 'CV/homepage.html', {'cvposts': cvposts, 'qposts':qposts, 'pposts':pposts  })

# def edit_CV(request):
#     cvposts = CVpost.objects.all()
#     return render(request, "CV/edit_CV.html", {cvposts:cvposts})

def edit_CV(request):
    cvPost = get_object_or_404(CVpost)

    if request.method == "POST":
        cvform = CVForm(request.POST, instance=cvPost)

        if cvform.is_valid():
            # print("AHHHHHH")
            cvPost = cvform.save(commit=False)
            # cvPost.author = request.user
            # cvPost.published_date = timezone.now()
            cvPost.save()
            return redirect('homepage')
    else:
        cvform = CVForm(instance=cvPost)
    return render(request, 'CV/edit_CV.html', {'cvform':cvform})

# def edit_Qualifications(request):
#     qualification = get_object_or_404(Qualifications)
#
#     if request.method == "POST":
#         qualificationsform = QualificationsForm(request.POST, instance=qualification)
#
#         if qualificationsform.is_valid():
#             # print("AHHHHHH")
#             qualification = qualificationsform.save(commit=False)
#             # cvPost.author = request.user
#             # cvPost.published_date = timezone.now()
#             qualification.save()
#             return redirect('homepage')
#     else:
#         qualificationsform = QualificationsForm(instance=qualification)
#     return render(request, 'CV/edit_CV.html', {'qform':qualificationsform})

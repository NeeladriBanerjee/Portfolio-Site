from django.shortcuts import render
from .models import Project, About, Skill, Education, Certification, ProfileLink, Research

def portfolio_home(request):
    projects = Project.objects.all().order_by('-id')
    about = About.objects.first()
    skills = Skill.objects.all()
    education_list = Education.objects.all().order_by('-id')
    certifications_list = Certification.objects.all().order_by('-id')
    coding_profiles = ProfileLink.objects.filter(category='coding')
    social_profiles = ProfileLink.objects.filter(category='social')
    
    # Fetch research works
    research_works = Research.objects.all().order_by('-id')
    
    context = {
        'projects': projects,
        'about': about,
        'skills': skills,
        'education_list': education_list,
        'certifications_list': certifications_list,
        'coding_profiles': coding_profiles,
        'social_profiles': social_profiles,
        'research_works': research_works,
    }
    
    return render(request, 'portfolio/index.html', context)
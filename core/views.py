from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import About, Client, Project, Service, Team
from .forms import ContactForm


# class HomeTemplateView(TemplateView):
#     template_name = "core/index.html"
#     form = ContactForm

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["about"] = About.objects.first()
#         context["services"] = Service.objects.all()
#         context["projects"] = Project.objects.all()
#         context["clients"] = Client.objects.all()
#         return context


def home(request):
    form = ContactForm
    about = About.objects.first()
    services = Service.objects.all()
    projects = Project.objects.all()
    clients = Client.objects.all()
    team_members = Team.objects.all()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            name = form.cleaned_data.get("name")
            messages.success(request, f"Thank you {name} for contacting Romelo")
            return redirect("core:home")
    else:
        form = ContactForm()

    context = {
        "form": form,
        "about": about,
        "services": services,
        "projects": projects,
        "clients": clients,
        "team_members": team_members,
    }

    return render(request, "core/index.html", context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    context = {
        "project": project,
    }
    return render(request, "core/project_details.html", context)

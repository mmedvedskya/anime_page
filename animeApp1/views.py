from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Character, Director, Feedback, Personal_Info
from .forms import FeedbackForm, PersonalInfoForm
from django.db.models import Count, Avg, Min, Max, StdDev, Sum


def pages(request):
    url_elements = request.path.split("/")
    if url_elements[-2] == "welcome":
            personal_form = PersonalInfoForm()
            feedback_form = FeedbackForm()
            return render(request, "index.html", {
            "personal_form": personal_form,
            "feedback_form": feedback_form
        })
    elif url_elements[-2] == "directors":
        directors = Director.objects.all()
        return render(request, "directors.html", {"directors": directors})
    elif url_elements[-2] == "top5":
        characters = Character.objects.all()
        return render(request, "characters.html", {"characters": characters})
    
    elif url_elements[-2] == "feedback":
        if request.method == "POST":
            personal_form = PersonalInfoForm(request.POST)
            feedback_form = FeedbackForm(request.POST)

            if personal_form.is_valid() and feedback_form.is_valid():
                saved_person = personal_form.save()
                feedback_instance = feedback_form.save(commit=False)
                feedback_instance.person = saved_person
                feedback_instance.save()
                return redirect("animeApp1:Feedback")
        else:
            personal_form = PersonalInfoForm()
            feedback_form = FeedbackForm()
        all_feedback = Feedback.objects.all()
        like_filter = request.GET.get("like")
        sort_by = request.GET.get("sort")
        sort_dir = request.GET.get("dir", "asc")
        min_movies = request.GET.get("min_movies")
        email_search = request.GET.get("email", '').strip()

        if email_search:
            all_feedback = all_feedback.filter(person__email__icontains=email_search)
        if min_movies:
            all_feedback = all_feedback.filter(number_of_movies__gte=min_movies)
        if like_filter in ["yes", "no"]:
            all_feedback = all_feedback.filter(like=like_filter)
        
        # all_feedback = all_feedback.filter(like='yes', characters='Totoro')
        
        if sort_by == "number_of_movies":
            if sort_dir == "asc":
                all_feedback = all_feedback.order_by("number_of_movies")
            else:
                all_feedback = all_feedback.order_by("-number_of_movies")
        elif sort_by == "date":
            if sort_dir == "asc":
                all_feedback = all_feedback.order_by("person__date")
            else:
                all_feedback = all_feedback.order_by("-person__date")
            
        feedback_data = all_feedback
        personal_data = Personal_Info.objects.all()

        # =Count('it', filter=Q(it__ ='')),
        feedback_stats = all_feedback.aggregate(
            total=Count('id'),
            avg_movies=Avg('number_of_movies'),
            max_movies=Max('number_of_movies'),
            min_movies=Min('number_of_movies'),
            stddev_movies=StdDev('number_of_movies'),
            total_movies=Sum('number_of_movies')
        )
        context = {
            "personal_form": personal_form,
            "feedback_form": feedback_form,
            "feedback_data": feedback_data,
            "personal_data": personal_data,
            "feedback_stats": feedback_stats,
            "like_filter": like_filter,
            "sort_by": sort_by,
            "email_search": email_search,
        }
        return render(request, "feedback.html", context)
    elif url_elements[-2] == "studio":
        return redirect("https://ru.wikipedia.org/wiki/Studio_Ghibli")
    else:
        return redirect("animeApp1:Welcome")
    
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.template.loader import render_to_string

import challenges

# Variables

monthly_challenges = {
    "january": "Eat no meat fo entire month.",
    "february": "Walk for at least 20 minutes every day.",
    "march": "Learn django at least 20 minutes every day.",
    "april": "Eat no meat fo entire month.",
    "may": "Walk for at least 20 minutes every day.",
    "june": "Learn django at least 20 minutes every day.",
    "july": "Eat no meat fo entire month.",
    "august": "Walk for at least 20 minutes every day.",
    "september": "Learn django at least 20 minutes every day.",
    "october": "Eat no meat fo entire month.",
    "november": "Walk for at least 20 minutes every day.",
    "december": "Learn django at least 20 minutes every day.",
}

# Challenge view


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("This month is not supported.")

    redirect_month = months[month-1]
    redirect_path = reverse('month-challenge', args=[str(redirect_month)])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported.</h1>")

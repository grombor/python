from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse

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

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("This month is not supported...")

    redirect_month = months[month-1]
    redirect_path = reverse('month-challenge', args=[str(redirect_month)])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge (request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported." + str(type(month)))
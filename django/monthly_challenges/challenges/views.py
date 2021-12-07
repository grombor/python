from django.http.response import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.shortcuts import render

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
    "december": None,
}

# Challenge view


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


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
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        raise Http404()

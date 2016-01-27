"""
Definition of urls for TwitterWatsonSentimentAnalysis.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import SearchForm


urlpatterns = patterns('',
    url(r'^$', 'app.views.search', name='searchform')
)

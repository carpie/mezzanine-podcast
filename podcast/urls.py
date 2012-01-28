from django.conf.urls.defaults import *

# Podcast patterns.
urlpatterns = patterns("podcast.views",
    url("^(?P<slug>.*)/$", "podcast_detail", name="podcast_detail"),
    url("^$", "podcast_list", name="podcast_list"),
)

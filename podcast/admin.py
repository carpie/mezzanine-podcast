from copy import deepcopy
from django.contrib import admin

from mezzanine.core.admin import DisplayableAdmin, OwnableAdmin
from models import Podcast

podcast_extra_fieldsets = ((None, {"fields": ("date", "author", "location",
    "notes", "notes_icon", "audio_file_aac", "audio_file_ogg",
    "audio_icon")}),)

class PodcastAdmin(DisplayableAdmin, OwnableAdmin):
    """
    Admin class for Podcasts
    """
    fieldsets = deepcopy(DisplayableAdmin.fieldsets) + podcast_extra_fieldsets


admin.site.register(Podcast, PodcastAdmin)

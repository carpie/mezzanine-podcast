from django.db import models

# Create your models here.
from django.db import models

from mezzanine.conf import settings
from mezzanine.core.models import Displayable, Ownable, RichText
from mezzanine.core.fields import RichTextField

fb = __import__(settings.PACKAGE_NAME_FILEBROWSER + '.fields', 
    globals(), locals(), ['FileBrowseField'], -1)

class Podcast(Displayable, Ownable, RichText):
    """
    A Podcast
    """
    date = models.DateField()
    notes = RichTextField("Notes")
    author = models.CharField("Author", max_length=128, blank=True, null=True)
    location = models.CharField("Location", max_length=128, blank=True,
        null=True)
    audio_file_aac = fb.FileBrowseField("Audio (mp4/aac)", max_length=255,
        directory="audio/", extensions=[".mp4"], blank=True, null=True)
    audio_file_ogg = fb.FileBrowseField("Audio (ogg)", max_length=255,
        directory="audio/", extensions=[".ogg"], blank=True, null=True)
    notes_icon = fb.FileBrowseField("Notes icon", max_length=255, format="Image",
        blank=True, null=True)
    audio_icon = fb.FileBrowseField("Audio icon", max_length=255, format="Image",
        blank=True, null=True)


# Migration rules for south
from south.modelsinspector import add_introspection_rules
rules = [
    (
        (fb.FileBrowseField,),
        [],
        {
            "directory": ["directory", {"default": ""}],
            "extensions": ["extensions", {"default": ""}],
            "format": ["format", {"default": ""}],
        },
    )
]
add_introspection_rules(rules, 
    ["^%s\.fields\.FileBrowseField" % settings.PACKAGE_NAME_FILEBROWSER])

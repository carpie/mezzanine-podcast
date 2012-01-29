
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import RequestContext

from mezzanine.conf import settings
from mezzanine.pages.models import RichTextPage
from mezzanine.template.loader import select_template

from models import Podcast

def podcast_page():
    """
    Return the Podcast page from the pages app.
    """
    try:
        slug = getattr(settings, "PODCAST_SLUG", "podcasts")
        return RichTextPage.objects.get(slug=slug)
    except RichTextPage.DoesNotExist:
        return None


def podcast_list(request, tag=None, year=None, month=None, username=None,
                   category=None, template="podcast/podcast_list.html"):
    """
    Provide a listing of podcasts
    """
    templates = []
    podcasts = Podcast.objects.published()
    context = {"page": podcast_page(), "podcasts": podcasts}
    templates.append(template)
    request_context = RequestContext(request, context)
    t = select_template(templates, request_context)
    return HttpResponse(t.render(request_context))


def podcast_detail(request, slug, template="podcast/podcast_detail.html"):
    """
    Display a particular podcast and handle comment submission. Custom
    templates are checked for using the name
    ``podcast_detail_XXX.html`` where ``XXX`` is the podcast's slug.
    """
    podcasts = Podcast.objects.published(for_user=request.user)
    pc = get_object_or_404(podcasts, slug=slug)
    context = {"podcast": pc}
    templates = [u"podcast/podcast_detail_%s.html" % slug, template]
    request_context = RequestContext(request, context)
    t = select_template(templates, request_context)
    return HttpResponse(t.render(request_context))


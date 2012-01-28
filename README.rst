Mezzanine Podcast
=================

This is a simple podcast manager module for the Mezzanine_ CMS.  It adds the
ability to upload audio files, notes, and some metadata for the files.  Two
views are provided, one for a listing of podcasts and one for displaying
details about a single podcast.  Sample templates are included.  The sample
detail template uses the HTML5 audio tag to stream the audio.

The module allows for uploads in ogg/vorbis format and mp4/aac format.  This
covers all major browsers that support HTML5.  If you need to target other
browsers (specifically Internet Explorer <= IE8) you'll need to provide a
Flash fallback player such as jPlayer_.

.. _Mezzanine: http://mezzanine.jupo.org/
.. _jPlayer: http://jplayer.org/


Installation
------------

You have two main options for installing.  You can install `mezzanine-podcast`
to your system package directory  or just extract the source and put the
`podcast` directory in your mezzanine project root.

If you choose to use the first option, I recommend you use `virtualenv` or
equivalent to isolate the package since it uses a rather generic `podcast`
package name.

Option 1 - Install into system packages or virtualenv::

    easy_install https://github.com/carpie/mezzanine-podcast/tarball/master

Option 2 - Install in your mezzanine project root::

    wget https://github.com/carpie/mezzanine-podcast/tarball/master -O - | tar -zxvf -
    cp -r carpie-mezzanine-podcast-<hash>/podcast <path_to_your_mez_prj>/


Usage
-----
To use:

* Add ``podcast`` to your ``INSTALLED_APPS`` in `settings.py` in your mezzanine
  project.
* Add ``("^podcasts/", include("podcast.urls")),`` to your project's `urls.py`.
* Add ogg support to the file browser by putting the following block in your
  `settings.py` file::

    # Add ogg to the filebrowser's music extensions
    FILEBROWSER_EXTENSIONS = {
        'Folder': [''],
        'Image': ['.jpg','.jpeg','.gif','.png','.tif','.tiff'],
        'Video': ['.mov','.wmv','.mpeg','.mpg','.avi','.rm'],
        'Document': ['.pdf','.doc','.rtf','.txt','.xls','.csv'],
        'Audio': ['.mp3','.mp4','.wav','.aiff','.midi','.m4p', '.ogg'],
        'Code': ['.html','.py','.js','.css']
    }

* From your mezzanine project run::

    ./manage.py migrate podcast

Now, the podcast list page should be available at the `podcasts/` url.  You
can now add podcasts through the normal admin interface.

To override the default templates, create the template files
``templates/podcast/podcast_list.html`` and
``templates/podcast/podcast_detail.html`` in your mezzanine project.



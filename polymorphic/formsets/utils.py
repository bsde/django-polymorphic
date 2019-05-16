"""
Internal utils
"""
import django
from django.forms import Media
from itertools import chain

def add_media(dest, media):
    """
    Optimized version of django.forms.Media.__add__() that doesn't create new objects.

    Only required for Django < 2.0
    """
    if django.VERSION >= (2, 2):


        dest._css_lists.extend(media._css_lists)
        dest._js_lists.extend(media._js_lists)

        flat_list = dest._js_lists
        flat_list = list(chain(*flat_list))
        dest = Media(None, dest._css, flat_list)
        print(repr(dest))


    elif django.VERSION >= (2, 0):
        combined = dest + media
        dest._css = combined._css
        dest._js = combined._js
    else:
        dest.add_css(media._css)
        dest.add_js(media._js)

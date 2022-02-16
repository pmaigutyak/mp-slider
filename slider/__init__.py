
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


def setup_settings(settings, is_prod, **kwargs):

    settings['INSTALLED_APPS'] += [
        app for app in [
            'faq',
        ] if app not in settings['INSTALLED_APPS']
    ]

    settings['STYLESHEETS'] += [
        app for app in [
            'slider/slideshow.css',
        ]
    ]

    settings['STATIC_APPS'] += [
        app for app in [
            'slick',
            'fancybox',
        ]
    ]


class SliderConfig(AppConfig):
    name = 'slider'
    verbose_name = _("Slider")


default_app_config = 'slider.SliderConfig'

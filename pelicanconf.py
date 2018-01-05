#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

AUTHOR = u'OpenStreetMap Nicaragua'
SITENAME = u'MapaNica.net - Rutas de Managua y Ciudad Sandino'
SITESUBTITLE = 'Transporte Urbano Colectivo de Managua'
SITEDESCRIPTION = 'Mapa de la red de las rutas de buses del transporte urbano colectivo (TUC) de Managua y Ciudad Sandino'
SITEKEYWORDS = 'Bus, Buses, Rutas, Ruta, IRTRAMMA, TUC, Transporte, Transporte Urbano Colectivo, Nicaragua, Managua, OpenStreetMap, Transporte público, Datos Abuertos, Open Data'

USE_LESS = True
SITEURL = 'https://rutas.mapanica.net'
SITELOGO = '/images/mapanica-rutas.png'
THEME = 'themes/mombacho'

FAVICON = '/images/favicon.ico'
ROBOTS = 'index, follow'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

AUTHOR_SAVE_AS = False
CATEGORY_SAVE_AS = False
TAG_SAVE_AS = False
ARCHIVES_SAVE_AS = False
DIRECT_TEMPLATES = ('index', 'embed')

CC_LICENSE = { 'name': 'Creative Commons Attribution-ShareAlike', 'version':'4.0', 'slug': 'by-sa' }

PATH = 'content'
STATIC_PATHS = ['images','php']

TIMEZONE = 'America/Managua'

DEFAULT_LANG = u'es'
OG_LOCALE = u'es_NI'
DEFAULT_DATE_FORMAT = ('%d %B %Y')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('email', 'mailto:contacto@mapanica.net'),
          ('facebook', 'http://www.facebook.com/mapanica'),
          ('twitter', 'http://www.twitter.com/osm_ni'),
          )

MENUITEMS = (('Mapa de Nicaragua', 'http://mapanica.net', 'map'),
             ('Rutas Managua', '/index.html', 'public-transport'),
             ('Mapas para móviles', 'http://mapanica.net/mapas-moviles.html', 'mobile'),
             ('Comunidad', 'http://mapanica.net/comunidad.html', 'community'),
             ('Descargar datos', 'http://datos.mapanica.net', 'datos'),
          )

DEFAULT_PAGINATION = False

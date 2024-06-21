AUTHOR = 'Priscyla Santos'
SITENAME = 'Blog'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt-br'

THEME = "theme/cid"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


USE_CUSTOM_MENU = True
CUSTOM_MENUITEMS = (
    ('Sobre', 'pages/sobre-pt.html'),
    ('Portfólio', 'pages/portifolio-pt.html'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
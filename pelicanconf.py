AUTHOR = 'Priscyla Santos'
SITENAME = 'Blog'
SITEURL = "https://priscylasantos.github.io/blog/"
SITETITLE = "Priscyla Santos"
SITESUBTITLE = "Priscyla - Developer"
SITEDESCRIPTION = "Blog"
SITELOGO = SITEURL + "/images/octocat.png"
FAVICON = SITEURL + "/images/favicon.ico"


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

GITHUB_URL = "https://github.com/PriscylaSantos"
CONTACTS = (
    ("twitter", "https://x.com/PriscylaCSantos"),
    ("github", GITHUB_URL),
    ("linkedin", "https://www.linkedin.com/in/priscylacsantos"),
)

MAIN_MENU = True
MENUITEMS = (
    ("Arquivos", "/archives.html"),
    ("Categorias", "/categories.html"),
    ("Tags", "/tags.html"),
)

STATIC_PATHS = [
    "images",
]

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
    "version": "4.0",
    "slug": "by-sa",
    "icon": True,
    "language": "en_US",
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
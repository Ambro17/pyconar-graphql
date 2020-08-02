"""Script para bajar las charlas de la PyconAR 2018.


Como el slider que esta en la pagina no me deja leer bien las charlas,
hice este pequeño script para exportarlas a un archivo de texto

Requisitos:
* fades https://github.com/PyAr/fades


Uso:
$ fades charlas.py > index.html

Se puede abrir index.html directamente desde el navegador
"""
import collections
import json
import sys


import requests  # fades
import bs4 # fades beautifulsoup4


DOMAIN = "https://eventos.python.org.ar"
URL_2018 = f"{DOMAIN}/events/pyconar2018/"
URL_2019 = f"{DOMAIN}/events/pyconar2019/"
DEFAULT_IMAGE = "https://via.placeholder.com/350x150"


Charla = collections.namedtuple("Charla", "titulo descripcion speaker")


def obtener_charlas(year):
    """Generador de charlas de la Pycon"""
    url = URL_2018 if year == '2018' else URL_2019
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, features="html.parser")
    slick = soup.find(id="slick_charlas")
    rows = slick.find_all(class_="row")
    for row in rows:
        titulo = row.h2.text
        imagen = DOMAIN + row.img["src"] if row.img["src"] != "None" else DEFAULT_IMAGE
        parrafos = row.find_all(class_="col-sm-6")[1].find_all('p')
        descripcion = "\n".join(p.text for p in parrafos[0:2])
        _, speaker = parrafos[2].text.split(": ")
        yield Charla(titulo, descripcion[:100] + '...', speaker)


def generar_html(charlas):
    """Genera HTML a partir de iterable de charlas"""
    template = """
<html>
<head>
  <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
  <title>Charlas PyconAR 2019</title>
</head>
<body>
  <h1>Charlas PyconAR 2019</h1>
  <div class="container">
    <div class="row">
      {charlas}
    </div>
  </div>
</body>
</html>
"""
    template_charla = """
<div class="col s12 m6">
  <div class="card">
    <div class="card-image">
      <img src="{charla.imagen}">
    </div>
    <div class="card-content">
      <span class="card-title">{charla.titulo} - {charla.speaker}</span>
      {charla.descripcion}
    </div>
  </div>
</div>
"""
    charlas_html = "\n".join(template_charla.format(charla=charla)
                             for charla in charlas)
    return template.format(charlas=charlas_html)


def main(year):
    charlas = obtener_charlas(year)
    charlas_json = [
        {
            'title': ch.titulo,
            'speaker': ch.speaker,
            'desc': ch.descripcion,
        }
        for ch in list(charlas)
    ]
    with open('charlas2018.json', 'w+') as f:
        json.dump(charlas_json, f, indent=2,  ensure_ascii=False)



if __name__ == "__main__":
    year = sys.argv[1:][0] if sys.argv[1:] else '2019'
    main(year)
import json

from playwright import sync_playwright
from dateutil.parser import parse

charlas = []

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.newPage()

    # Visit Schedule Page
    page.goto('https://eventos.python.org.ar/events/pyconar2020/schedule')

    # Get all divs with the schedule of the day
    days = page.querySelectorAll('css=div .well')
    for day in days:
        # Get the day header text
        dia = day.querySelector('h2').innerText().strip()
        print(dia)

        dia = parse(dia.split('- ')[1])  # Día 1 - 16/11/2020 --> 16/11/2020
        # Get all talks from that day.
        charlas_divs = day.querySelectorAll('css=div .fc-content')
        for charla in charlas_divs:
            """
            Expected html
                <div class="fc-time" data-start="19:00" data-full="7:00 PM - 8:00 PM">
                    <span>19:00 - 20:00</span>
                </div>
                <div class="fc-title">¿Por que no se hacen mas tests?</div>
            """
            # For each talk, get its schedule and its title
            horario = charla.querySelector('.fc-time').innerText()
            start, end = horario.split(' - ')
            start, end = parse(start).strftime('%H:%M'), parse(end).strftime('%H:%M')

            titulo = charla.querySelector('.fc-title').innerText()
            print('Charla ', titulo)
            charlas.append({
                'day': str(dia),
                'start': start,
                'end': end,
                'titulo': titulo
            })

    browser.close()

with open('charlas.json', 'w') as f:
    json.dump(charlas, f)
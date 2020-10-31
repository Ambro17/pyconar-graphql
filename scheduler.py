from datetime import timedelta
import json

from playwright import sync_playwright
from dateutil.parser import parse

charlas = []

def parse_dates(dia:str, start_hour: str, end_hour: str):
    """Build datetime from day string plus hour and minute string """
    start = parse(start_hour)
    end = parse(end_hour)

    # 16/11/2020 + 19h + 30m
    start_datetime = parse(dia) + timedelta(hours=start.hour, minutes=start.minute)
    # 16/11/2020 + 20h + 0m
    end_datetime = parse(dia) + timedelta(hours=end.hour, minutes=end.minute)

    return start_datetime, end_datetime


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

        dia = dia.split('- ')[1] # Día 1 - 16/11/2020 --> 16/11/2020
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
            start_date, end_date = parse_dates(dia, start, end)

            titulo = charla.querySelector('.fc-title').innerText()
            print('Charla ', titulo)
            charlas.append({
                'day': str(dia),
                'titulo': titulo,
                'start': start_date.isoformat(),
                'end': end_date.isoformat(),
            })

    browser.close()    


with open('./pyconar/data/2020_schedule.json', 'w', encoding='utf-8') as f:
    json.dump(charlas, f, indent=4, ensure_ascii=False)

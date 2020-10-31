from datetime import timedelta
import json

from playwright import sync_playwright
from dateutil.parser import parse


def parse_dates(dia:str, start_hour: str, end_hour: str):
    """Build datetime from day string plus hour and minute string """
    start = parse(start_hour)
    end = parse(end_hour)

    # 16/11/2020 + 19h + 30m
    start_datetime = parse(dia) + timedelta(hours=start.hour, minutes=start.minute)
    # 16/11/2020 + 20h + 0m
    end_datetime = parse(dia) + timedelta(hours=end.hour, minutes=end.minute)

    return start_datetime, end_datetime


def get_talks_schedule():
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

    return charlas


def dump_talks_with_schedule_info(schedule):
    with open('pyconar/data/charlas.json', 'r') as f:
        all_charlas = json.load(f)

    title_to_charla = {charla['titulo']: charla for charla in schedule}

    for charla in all_charlas['2020']:
        # Add schedule info
        name = charla['title']
        schedule_of_charla = title_to_charla[name]
        charla['schedule'] = {
            'time': schedule_of_charla['day'],
            'start': schedule_of_charla['start'],
            'end': schedule_of_charla['end'],
        }

    nextTalks = all_charlas['2020']
    nextTalks = sorted(nextTalks, key=lambda x: x['schedule']['start'])

    assert len(nextTalks) == len(schedule), 'Not all charlas were scheduled'

    with open('pyconar/data/2020_schedule.json', 'w') as f:
        json.dump(nextTalks , f, indent=4, ensure_ascii=False)


charlas_schedule = get_talks_schedule()
dump_talks_with_schedule_info(charlas_schedule)

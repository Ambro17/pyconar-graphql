import json

with open('schedule.json', 'r') as f:
    schedule = json.load(f)

with open('pyconar/data/charlas.json', 'r') as f:
    charlas = json.load(f)

titulos_schedule = [x['titulo'] for x in schedule]

title_to_charla = {charla['titulo']: charla for charla in schedule}
for charla in charlas['2020']:
    # Add schedule info
    name = charla['title']
    schedule_of_charla = title_to_charla[name]
    charla['schedule'] = {
        'time': schedule_of_charla['day'],
        'start': schedule_of_charla['start'],
        'end': schedule_of_charla['end'],
    }

with open('2020_schedule.json', 'w') as f:
    json.dump(charlas['2020'] , f)

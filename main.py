import csv
import json
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('ksiazka-adresowa')

log.debug('zaczynamy tworzyc ksiązke adrsową.')

ADDRESS_BOOK = [{
    'imie': 'Wojciech',
    'nazwisko': 'Nowak',
    'telefon': '+48 000 000 000'
}]

with open('/tmp/ksiazka-adresowa.json', 'w') as file:
    log.debug('Zapisujemy ksiazkę w formacie JSON')
    file.write(json.dumps(ADDRESS_BOOK))

with open('/tmp/ksiazka-adresowa.csv', 'w') as file:
        log.debug('Zapisujemy ksiazkę w formacie CSV.')

        writer = csv.DictWriter(file, quoting=csv.QUOTE_ALL, fieldnames=sorted(ADDRESS_BOOK[0].keys()))
        writer.writeheader()

        for row in ADDRESS_BOOK:
            writer.writerow(row)
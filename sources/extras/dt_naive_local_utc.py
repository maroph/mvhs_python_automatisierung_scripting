from datetime import datetime
from datetime import timezone
from dateutil import tz

# Die Python Klasse datetime enthält sowohl das Datum als auch die Uhrzeit
# und kann deshalb als Zeitstempel verwendet werden.
# Aber: beim Erzeugen einer datetime Instanz wird keine Zeitzone gesetzt.
# Solche Instanzen werden in Python "naive" genannt. Wird die Zeitzone
# hinzugefügt, werden die Instanzen "aware" genannt.

# naive : datetime Instanz ohne Zeitzone
dt_naive = datetime.now()
print(f"datetime naive         : {dt_naive} - {dt_naive.tzname()}")

# aware : datetime Instanz mit Zeitzone: hier lokale Zeitzone
dt_aware_local = dt_naive.astimezone(tz.tzlocal())
print(f"datetime aware - local : {dt_aware_local} - {dt_aware_local.tzname()}")

# aware : direktes Erzeugen einer datetime Instanz mit der Zeitzone UTC
dt_aware_utc = datetime.now(timezone.utc)
print(f"datetime aware - UTC   : {dt_aware_utc} - {dt_aware_utc.tzname()}")

# Hier einige Beispiele, wie man eine datetime Instanz als String ausgeben kann
print()
print("Verschiedene Datum/Zeit Formate:")
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
print(f"Simple              : {dt_aware_local.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"                    : {dt_aware_local.strftime('%Y-%m-%d %H:%M:%S.%f')}")
print(f"                    : {dt_aware_local.strftime('%d.%m.%Y, %H:%M:%S')}")
print(f"                    : {dt_aware_local.strftime('%d-%b-%Y %H:%M').upper()}")
print(f"                    : {dt_aware_local.strftime('%d-%b-%Y %H:%M:%S').upper()}")
print(f"    Britsh          : {dt_aware_local.strftime('%d/%m/%Y, %I:%M:%S%p')}")
print(f"    American        : {dt_aware_local.strftime('%m/%d/%Y, %I:%M:%S%p')}")
print(f"RFC 822             : {dt_aware_local.strftime('%a, %d %b %y %H:%M:%S %z')}")
print(f"                    : {dt_aware_local.strftime('%a, %d %b %Y %H:%M:%S %z')}")
print(f"RFC 3339 / ISO 8601 : {dt_aware_local.strftime('%Y-%m-%dT%H:%M:%S.%f%z')}")

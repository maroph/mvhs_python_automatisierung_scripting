#!/usr/bin/env python3
#
# Weather Service URLs:
# https://wttr.in/
# https://wttr.is/
#
# GitHub: https://github.com/chubin/wttr.in
# Usage:  https://github.com/chubin/wttr.in#usage
# Help:   https://wttr.in/:help
#
# curl sample calls:
# curl -H "Accept-Language: de" 'https://wttr.is/München?m'
# curl 'https://wttr.is/München?m&lang=de'
# curl 'https://wttr.is/München?0m&lang=de'
# curl 'https://wttr.is/München?1m&lang=de'
# curl 'https://wttr.is/München?2m&lang=de'
# curl 'https://wttr.is/München?3m&lang=de'
# curl 'https://wttr.is/München?m&lang=de&format=j1' JSON output
# curl 'https://wttr.is/München?m&lang=de&format=j2' JSON output
#
import json
import requests
import sys

if __name__ == "__main__":
    # meaning of the values of the JSON field weatherCode
    # see: https://raw.githubusercontent.com/chubin/wttr.in/refs/heads/master/internal/renderer/oneline/constants.go
    # for the original values see: https://www.worldweatheronline.com/weather-api/api/docs/weather-icons.aspx
    WWO_CODE_TO_NAME = {
        "113": "Sunny",
        "116": "PartlyCloudy",
        "119": "Cloudy",
        "122": "VeryCloudy",
        "143": "Fog",
        "176": "LightShowers",
        "179": "LightSleetShowers",
        "182": "LightSleet",
        "185": "LightSleet",
        "200": "ThunderyShowers",
        "227": "LightSnow",
        "230": "HeavySnow",
        "248": "Fog",
        "260": "Fog",
        "263": "LightShowers",
        "266": "LightRain",
        "281": "LightSleet",
        "284": "LightSleet",
        "293": "LightRain",
        "296": "LightRain",
        "299": "HeavyShowers",
        "302": "HeavyRain",
        "305": "HeavyShowers",
        "308": "HeavyRain",
        "311": "LightSleet",
        "314": "LightSleet",
        "317": "LightSleet",
        "320": "LightSnow",
        "323": "LightSnowShowers",
        "326": "LightSnowShowers",
        "329": "HeavySnow",
        "332": "HeavySnow",
        "335": "HeavySnowShowers",
        "338": "HeavySnow",
        "350": "LightSleet",
        "353": "LightShowers",
        "356": "HeavyShowers",
        "359": "HeavyRain",
        "362": "LightSleetShowers",
        "365": "LightSleetShowers",
        "368": "LightSnowShowers",
        "371": "HeavySnowShowers",
        "374": "LightSleetShowers",
        "377": "LightSleet",
        "386": "ThunderyShowers",
        "389": "ThunderyHeavyRain",
        "392": "ThunderySnowShowers",
        "395": "HeavySnowShowers"
    }

    # wttr_url = 'https://wttr.is/München?m&lang=de&format=j1'
    # wttr_url = 'https://wttr.is/München?m&lang=en&format=j1'
    # wttr_url = 'https://wttr.is/München?m&lang=de&format=j2'
    wttr_url = 'https://wttr.is/München?m&lang=en&format=j2'

    try:
        res = requests.get(wttr_url)
    except Exception as ex:
        print('Error :', ex)
        sys.exit(1)

    # print(WWO_CODE_TO_NAME.get(res.json()['current_condition'][0]['weatherCode'], "weatherCode not found"))
    # print("---")
    json.dump(res.json(), sys.stdout, indent=2, ensure_ascii=False)

#!/usr/bin/env python3
#
####################################################
# Copyright (c) 2025 by Manfred Rosenboom          #
# https://maroph.github.io/ (maroph@pm.me)         #
#                                                  #
# This work is licensed under a CC-BY 4.0 License. #
# https://creativecommons.org/licenses/by/4.0/     #
####################################################
#
# APOD: Astronomy Picture of the Day
# https://apod.nasa.gov/apod/astropix.html
#
# About APOD
# https://apod.nasa.gov/apod/lib/about_apod.html
#
import json
import requests
import webbrowser


class APODData:
    def __init__(self, apod_json_data):
        if not isinstance(apod_json_data, dict):
            raise ValueError("dictionary expected")

        self.__json = apod_json_data
        self.__title = apod_json_data.get('title')
        self.__date = apod_json_data.get('date')
        self.__url = apod_json_data.get('url')
        self.__hdurl = apod_json_data.get('hdurl')
        self.__explanation = apod_json_data.get('explanation')
        self.__media_type = apod_json_data.get('media_type')
        self.__copyright = apod_json_data.get('copyright')

    @property
    def json(self):
        return self.__json

    @property
    def title(self):
        return self.__title

    @property
    def date(self):
        return self.__date

    @property
    def url(self):
        return self.__url

    @property
    def hdurl(self):
        return self.__hdurl

    @property
    def explanation(self):
        return self.__explanation

    @property
    def media_type(self):
        return self.__media_type

    @property
    def copyright(self):
        return self.__copyright


class APOD:
    """APOD access wrapper class"""

    def __init__(self, api_key=None):
        """constructor"""
        if isinstance(api_key, str):
            self.__api_key = api_key
        else:
            self.__api_key = 'DEMO_KEY'

        self.__service_version = None
        self.__limit = None
        self.__remaining = None
        self.__status = None
        self.__status_msg = None
        self.__reason = None
        self.__error_code = None
        self.__error_msg = None

    @property
    def service_version(self):
        return self.__service_version

    @property
    def limit(self):
        return self.__limit

    @property
    def remaining(self):
        return self.__remaining

    @property
    def status(self):
        return self.__status

    @property
    def status_msg(self):
        return self.__status_msg

    @property
    def reason(self):
        return self.__reason

    @property
    def error_code(self):
        return self.__error_code

    @property
    def error_msg(self):
        return self.__error_msg

    # date : YYYY-MM-DD
    # hd   : True, False
    def fetchdata(self, date=None, hd=None):
        self.__service_version = None
        self.__limit = None
        self.__remaining = None
        self.__status = None
        self.__status_msg = None
        self.__reason = None
        self.__error_code = None
        self.__error_msg = None

        url = 'https://api.nasa.gov/planetary/apod?api_key=' + self.__api_key
        if isinstance(date, str):
            url += '&date=' + date
        if isinstance(hd, bool):
            url += '&hd=' + str(hd)

        headers = {"Content-Type": "application/json;charset=utf-8"}

        try:
            res = requests.get(url, headers=headers)
        except Exception as ex:
            print('Error :', ex)
            return None

        if res is not None:
            json_data = {}
            if res.text:
                try:
                    json_data = json.loads(res.text)
                except json.decoder.JSONDecodeError:
                    json_data = {}

            self.__service_version = json_data.get('service_version')
            self.__limit = res.headers.get('X-RateLimit-Limit')
            self.__remaining = res.headers.get('X-RateLimit-Remaining')
            self.__status = res.status_code
            self.__reason = res.reason

            if res.ok:
                apod_data = APODData(json_data)
                return apod_data
            else:
                try:
                    res.raise_for_status()
                except Exception as ex:
                    self.__status_msg = str(ex)
                if json_data is not None:
                    self.__error_code = json_data.get('code')
                    self.__error_msg = json_data.get('msg')
                return None

        return None


if __name__ == '__main__':
    apod = APOD()
    # apod = APOD('APOD_KEY')
    data = apod.fetchdata()
    # data = apod.fetchData('2023-05-15')
    if data:
        print('JSON             :', data.json)
        print('title            :', data.title)
        print('date             :', data.date)
        print('url              :', data.url)
        print('hdurl            :', data.hdurl)
        print('explanation      :', data.explanation)
        print('media type       :', data.media_type)
        if data.copyright:
            print('copyright        :', data.copyright)
        print('service version  :', apod.service_version)
        print('limit            :', apod.limit)
        print('remaining        :', apod.remaining)
        #
        # https://docs.python.org/3/library/webbrowser.html
        # new:
        #     0: url is opened in the same browser window if possible
        #     1: a new browser window is opened if possible
        #     2: a new browser page ("tab") is opened if possible
        # autoraise: If autoraise is True (default), the window is raised if possible
        webbrowser.open(url=data.url, new=2, autoraise=True)
        webbrowser.open_new_tab(data.url)
    else:
        print('service version  :', apod.service_version)
        print('limit            :', apod.limit)
        print('remaining        :', apod.remaining)
        print('HTTP status code :', apod.status)
        print('HTTP status msg  :', apod.status_msg)
        print('reason           :', apod.reason)
        print('error code       :', apod.error_code)
        print('error message    :', apod.error_msg)

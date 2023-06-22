""" Plugin to download data from https://open-meteo.com/.
"""
from datetime import datetime, \
    timedelta
import os
import pathlib

import requests

from app.config import settings

# Constants
#: timeout for http requests
REQUEST_TIMEOUT = 10
#: subpath for openmeto data
OM_SUBPATH = "openmeteo"
#: encoding of the downloaded data files
ENCODING = "utf-8"
#: date format for the created file and to create one if none is given
DATE_FMT   = "%Y%m%d"
OMDATE_FMT = "%Y-%m-%d"
#: default date delay from today in case no date is given (in days)
DATE_DELAY = 10
#: separator for openmeteo date
OM_SEP = "-"
#: created openmeteo file name pattern
OM_FILE_PATTERN = "openmeteo-{}-{}.csv"
#: url to dl the openmeteo files
OM_URL = "https://archive-api.open-meteo.com/v1/era5?"
#: openmeteo query string (url) pattern
OM_QUERY_PATTERN = "latitude={}&longitude={}&start_date={}&end_date={}" + \
    "&daily={}&timezone={}&format={}"
# // Constants


def fmt_date(date):
    """ Format the date for the open-meteo api.

        Arguments:
            date (str): date (format : YYYYMMDD)

        Returns:
            str: date (fromat YYYY-MM-DD)
    """
    fmt   = DATE_FMT
    omfmt = OMDATE_FMT

    dt_date = datetime.strptime(date, fmt)

    sp_date = datetime.strftime(dt_date, omfmt)

    return sp_date


def int_date(date=None, days=DATE_DELAY):
    """ Format the date to the YYYYMMDD format.

        Arguments:
            date (str): date (format : YYYYMMDD) or None (now)
            days (int): delay in days between the date and the data to download

        Returns:
            str: date (fromat YYYYMMDD)
    """
    fmt = DATE_FMT

    if date is None:
        date = datetime.now()
    else:
        date = datetime.strptime(date, fmt)

    date = (date - timedelta(days=days)).strftime(fmt)

    return date


def build_om_url(config):
    """ Build the url to download openmeteo data.

        Arguments:
            config (dict): informations to build openmeteo url

        Returns:
            str: openmeteo ulr to call
    """
    om_url  = OM_URL
    pattern = OM_QUERY_PATTERN

    url = om_url + pattern.format(config['latitude'],
                                  config['longitude'],
                                  config['start'],
                                  config['end'],
                                  config['daily'],
                                  config['timezone'],
                                  config['format'])

    return url


def build_filename(city, date):
    """ Build the name of the file to write.

        Arguments:
            city (str): name of the city of the data
            date (str): date of the the data (YYYYMMDD)

        Returns:
            str: name of the file to create
    """
    file_pattern = OM_FILE_PATTERN

    return file_pattern.format(city, date)


class Downloader:
    """ Main class to deal with downloads from open-meteo.
    """
    def __init__(self, config):
        self.config = config

    def download(self, date=None):
        """ Download a csv with data at a given date.
        """
        encoding = ENCODING
        timeout  = REQUEST_TIMEOUT
        datapath = os.path.join(settings.datapath, OM_SUBPATH)
        if not os.path.exists(datapath):
            os.makedirs(datapath)
        config   = self.config

        date   = int_date(date)
        omdate = fmt_date(date)
        config["start"] = omdate
        config["end"]   = omdate

        print(f"download file of {date} ...", flush=True)
        url = build_om_url(config)
        response = requests.get(url, timeout=timeout)

        filename = build_filename(config["city"], date)
        path     = os.path.normpath(os.path.join(pathlib.Path().resolve(),
                                                 datapath,
                                                 filename))
        with open(path, "w", encoding=encoding) as dwnld:
            dwnld.write(response.content.decode())

        return {"name": filename,
                "date": os.path.getctime(path),
                "size": os.path.getsize(path)}

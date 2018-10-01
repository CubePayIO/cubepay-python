from urllib.request import Request
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import urllib.parse
import ssl
import json


class HttpRequest:
    def __init__(self, url):
        self.__url = url

    def get_response(self,method, params={}):
        url = self.__url + method
        try:
            req = Request(url=url)
            postdate = urllib.parse.urlencode(params)
            ssl._create_default_https_context = ssl._create_unverified_context
            resp = urlopen(req, data=postdate.encode("utf-8"))
            result = self.json_parse(resp.read().decode("utf-8"))
            resp.close()
        except HTTPError as e:
            result = self.json_parse(e.read().decode("utf-8"))
            if not result:
                result = {"status": e.code, "data": e.reason}
            else:
                e.close()
        except URLError as e:
            result = {"status": 500, "data": e.reason}

        return result

    @staticmethod
    def json_parse(json_str):
        try:
            result = json.loads(json_str)
        except Exception:
            result = False

        return result

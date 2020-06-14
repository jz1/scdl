# -*- encoding: utf-8 -*-

import requests
from scdl import CLIENT_ID


class Client():

    def get_collection(self, url, token):
        params = {
            'client_id': CLIENT_ID,
            'linked_partitioning': '1',
        }
        if token:
            params['oauth_token'] = token
        resources = list()
        while url:
            response = requests.get(url,
                headers={
                "Sec-Fetch-Mode":"cors",
                "Origin": "https://soundcloud.com",
                "Authorization": "OAuth {}".format(token),
                "Content-Type": "application/json",
                "Accept": "application/json, text/javascript, */*; q=0.1",
                "Referer": "https://soundcloud.com/",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
                "DNT": "1",
                })
            response.raise_for_status()
            json_data = response.json()
            if 'collection' in json_data:
                resources.extend(json_data['collection'])
            else:
                resources.extend(json_data)
            if 'next_href' in json_data:
                url = json_data['next_href']
            else:
                url = None
        return resources

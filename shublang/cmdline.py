#!/usr/bin/env python

import argparse
from shublang import evaluate
import requests
import logging
import ast

class HTTPBanError(Exception):

    def __init__(self, message):
        self.message = message

def fetch_data(url):
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;'
                         'q=0.8,application/signed-exchange;v=b3',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
               'Connection': 'keep-alive',
               'Dnt': '1',
               'Referer': 'https://www.google.com/',
               'Upgrade-Insecure-Requests':	'1',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/77.0.3865.120 Safari/537.36',
               }
    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        logging.error(f'Received Status Code {r.status_code}. Content could not be fetched from the website')
        raise HTTPBanError(f'Content Could Not be Fetched from {url}')

    else:
        return r.text



def execute_from_command_line():

    parser = argparse.ArgumentParser(description='Evaluate shublang expression')
    group = parser.add_mutually_exclusive_group(required=True)
    parser.add_argument('expression', help='Shublang expression to be evaluated')
    group.add_argument('data', nargs='?', type=lambda x: ast.literal_eval(x),
                       help='Data on which the shublang expression needs to be applied')
    group.add_argument('--url', dest='url', help='URL of the website from which content needs to be fetched')
    parser.add_argument('--verbose', help='Enable tracing', action='store_true' )
    args = parser.parse_args()
    data = args.data
    if not args.data:
        data = [fetch_data(args.url)]
    print(evaluate(args.expression, data))

if __name__ == "__main__":
    execute_from_command_line()
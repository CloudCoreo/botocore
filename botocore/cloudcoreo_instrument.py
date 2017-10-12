# Copyright 2017 CloudCoreo, Inc. All Rights Reserved

import json
import logging
from os import environ
import pdb
import requests

from botocore.endpoint import Endpoint

CC_DEFAULT_ENDPOINT = 'http://localhost:4444'
CC_ENDPOINT = environ.get('CC_ENDPOINT', CC_DEFAULT_ENDPOINT)

def cloudcoreo_inspect(parsed_request, raw_request,
                       parsed_response, raw_response, host):

    data = _parse(parsed_request,
                  raw_request,
                  parsed_response,
                  raw_response,
                  host)

    return requests.post(CC_ENDPOINT, data = data)

def _parse(req, raw_req, res, raw_res, host):
    res_meta = res['ResponseMetadata']

    req_headers = {k: v for k, v in raw_req.headers.items()}
    if host.find("://"):
        host = host.split("://")[1]
    req_headers['Host'] = host

    data = {
        'url': req['url'],
        'http_verb': req['method'],
        'devtime_id': '5754ffb4-983c-4033-b593-2b06145a413e',
        'request_headers': json.dumps(req_headers),
        'request_body': req['body'],
        'response_status': res_meta['HTTPStatusCode'],
        'response_headers': json.dumps(res_meta['HTTPHeaders']),
        'response_body': raw_res.text
    }

    return data

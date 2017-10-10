# Copyright 2017 CloudCoreo, Inc. All Rights Reserved

import json
import logging
from os import environ
import pdb

from botocore.endpoint import Endpoint

CC_DEFAULT_ENDPOINT = 'localhost:12345/spy'

def cloudcoreo_inspect(request, parsed_response, raw_response):
    cc_token_key_id = environ.get('CC_TOKEN_KEY_ID')
    cc_token_secret_key = environ.get('CC_TOKEN_SECRET_KEY')
    cc_team_id = environ.get('CC_TEAM_ID')
    cc_endpoint = environ.get('CC_ENDPOINT', CC_DEFAULT_ENDPOINT)

    data = _parse(request, parsed_response, raw_response)
    print(data)

def _parse(req, res, raw_res):
    res_meta = res['ResponseMetadata']

    data = {
        'url': req['url'],
        'http_verb': req['method'],
        'devtime_id': 'devtime-id-goes-here',
        'request_headers': req['headers'],
        'request_body': req['body'],
        'response_status': res_meta['HTTPStatusCode'],
        'response_headers': res_meta['HTTPHeaders'],
        'response_body': raw_res.text
    }

    return json.dumps(data)

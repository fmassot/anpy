# -*- coding: utf-8 -*-

import json

from datetime import datetime


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)


def json_dumps(data, *args, **kwargs):
    return JSONEncoder(*args, **kwargs).encode(data)
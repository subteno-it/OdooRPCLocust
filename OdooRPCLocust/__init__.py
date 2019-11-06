# -*- coding: utf-8 -*-
# Copyright 2018 SYLEAM

import odoorpc
import time
import sys

from locust import Locust, events


class ODOO(odoorpc.ODOO):
    def json(self, url, params):
        if url == '/jsonrpc':
            method = params['method']
            model = params['args'][3]
            model_method = params['args'][4]
            call_name = '{method} {model}.{model_method}'.format(
                    method=method, model=model, model_method=model_method)
        else:
            call_name = url

        start_time = time.time()
        try:
            res = super(ODOO, self).json(url, params)
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(
                request_type='OdooRPC %s' % self._protocol,
                name=call_name,
                response_time=total_time,
                exception=e,
            )
            raise e
        else:
            total_time = int((time.time() - start_time) * 1000)
            events.request_success.fire(
                request_type='OdooRPC %s' % self._protocol,
                name=call_name,
                response_time=total_time,
                response_length=sys.getsizeof(res),
            )
        return res

    def http(self, url, data=None, headers=None):
        start_time = time.time()
        try:
            res = super(ODOO, self).http(url, data=data, headers=headers)
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(
                request_type='OdooRPC %s' % self._protocol,
                name=url,
                response_time=total_time,
                exception=e,
            )
            raise e
        else:
            total_time = int((time.time() - start_time) * 1000)
            events.request_success.fire(
                request_type='OdooRPC %s' % self._protocol,
                name=url,
                response_time=total_time,
                response_length=sys.getsizeof(res),
            )
        return res


class OdooRPCLocust(Locust):
    host = 'localhost'
    port = 8069
    database = 'demo'
    user = 'admin'
    password = 'admin'
    protocol = 'jsonrpc'

    def __init__(self, *args, **kwargs):
        super(OdooRPCLocust, self).__init__(*args, **kwargs)
        self.client = ODOO(
            host=self.host,
            port=self.port,
            protocol=self.protocol,
        )
        self.client.login(self.database, self.user, self.password)

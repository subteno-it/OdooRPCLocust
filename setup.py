# -*- coding: utf-8 -*-
# Copyright 2018 SYLEAM

from setuptools import setup

setup(
    name='OdooRPCLocust',
    version='1.0.0',
    description='Easily load test Odoo using Locust and OdooRPC.',
    url='https://github.com/syleam/OdooRPCLocust',
    author='Sylvain GARANCHER',
    author_email='sylvain.garancher@syleam.fr',
    packages=['OdooRPCLocust'],
    install_requires=[
        'odoorpc',
        'locustio',
    ],
    keywords='odoo locust odoorpc loadtest',
    license='BSD',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ],
)

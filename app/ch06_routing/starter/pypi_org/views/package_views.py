# _*_ coding: utf-8 _*_
# !/usr/bin/env python3

"""
Created on: 17/06/2020

@author: Collisio-Adolebitque
"""


import flask
from pypi_org.infrastructure.view_modifiers import response
import pypi_org.services.package_services as package_services


blueprint = flask.Blueprint('packages', __name__, template_folder='templates')


@blueprint.route('/project/<package_name>')
def package_details(package_name: str):
    return f"Package details for {package_name}"


@blueprint.route('/<int:rank>')
def popular(rank: int):
    return f"The details for {rank}th most popular package"

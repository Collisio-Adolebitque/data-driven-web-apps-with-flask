# _*_ coding: utf-8 _*_
# !/usr/bin/env python3

"""
Created on: 17/06/2020

@author: Collisio-Adolebitque
"""


import flask
from pypi_org.infrastructure.view_modifiers import response
import pypi_org.services.package_services as package_services


blueprint = flask.Blueprint('account', __name__, template_folder='templates')


# ################### INDEX ##################################################


@blueprint.route('/account')
@response(template_file='account/account.html')
def index():
    return {}


# ################### REGISTER ###############################################


@blueprint.route('/account/register', methods=['GET'])
@response(template_file='home/register.html')
def register_get():
    return {}


@blueprint.route('/account/register', methods=['POST'])
@response(template_file='home/register.html')
def register_post():
    return {}


# ################### LOGIN ##################################################


@blueprint.route('/account/login', methods=['GET'])
@response(template_file='home/login.html')
def login_get():
    return {}


@blueprint.route('/account/login', methods=['POST'])
@response(template_file='home/login.html')
def login_post():
    return {}


# ################### LOGOUT #################################################


@blueprint.route('/account/logout', methods=['GET'])
@response(template_file='home/login.html')
def logout():
    return {}

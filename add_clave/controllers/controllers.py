# -*- coding: utf-8 -*-
from odoo import http

# class AddClave(http.Controller):
#     @http.route('/add_clave/add_clave/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/add_clave/add_clave/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('add_clave.listing', {
#             'root': '/add_clave/add_clave',
#             'objects': http.request.env['add_clave.add_clave'].search([]),
#         })

#     @http.route('/add_clave/add_clave/objects/<model("add_clave.add_clave"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('add_clave.object', {
#             'object': obj
#         })
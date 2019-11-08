# -*- coding: utf-8 -*-
from odoo import http

# class Salecommission(http.Controller):
#     @http.route('/salecommission/salecommission/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/salecommission/salecommission/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('salecommission.listing', {
#             'root': '/salecommission/salecommission',
#             'objects': http.request.env['salecommission.salecommission'].search([]),
#         })

#     @http.route('/salecommission/salecommission/objects/<model("salecommission.salecommission"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('salecommission.object', {
#             'object': obj
#         })
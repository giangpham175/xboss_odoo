# -*- coding: utf-8 -*-
from odoo import http

# class Productcategory(http.Controller):
#     @http.route('/productcategory/productcategory/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/productcategory/productcategory/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('productcategory.listing', {
#             'root': '/productcategory/productcategory',
#             'objects': http.request.env['productcategory.productcategory'].search([]),
#         })

#     @http.route('/productcategory/productcategory/objects/<model("productcategory.productcategory"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('productcategory.object', {
#             'object': obj
#         })
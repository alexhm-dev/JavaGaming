# -*- coding: utf-8 -*-
from odoo import http

# class JavaGaming(http.Controller):
#     @http.route('/java_gaming/java_gaming/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/java_gaming/java_gaming/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('java_gaming.listing', {
#             'root': '/java_gaming/java_gaming',
#             'objects': http.request.env['java_gaming.java_gaming'].search([]),
#         })

#     @http.route('/java_gaming/java_gaming/objects/<model("java_gaming.java_gaming"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('java_gaming.object', {
#             'object': obj
#         })
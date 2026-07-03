# -*- coding: utf-8 -*-
# from odoo import http


# class PortManagement(http.Controller):
#     @http.route('/port_management/port_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/port_management/port_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('port_management.listing', {
#             'root': '/port_management/port_management',
#             'objects': http.request.env['port_management.port_management'].search([]),
#         })

#     @http.route('/port_management/port_management/objects/<model("port_management.port_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('port_management.object', {
#             'object': obj
#         })


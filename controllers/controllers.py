# -*- coding: utf-8 -*-
# from odoo import http


# class CursoOdoo(http.Controller):
#     @http.route('/curso_odoo/curso_odoo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/curso_odoo/curso_odoo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('curso_odoo.listing', {
#             'root': '/curso_odoo/curso_odoo',
#             'objects': http.request.env['curso_odoo.curso_odoo'].search([]),
#         })

#     @http.route('/curso_odoo/curso_odoo/objects/<model("curso_odoo.curso_odoo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('curso_odoo.object', {
#             'object': obj
#         })

from odoo import models, fields, api
from odoo.exceptions import UserError


class PortTypeMarchandise(models.Model):
    _name = 'port.type.marchandise'
    _description = 'type de marchandise'

    name = fields.Char(string="Désignation")
    majoration = fields.Float(string="Majoration")

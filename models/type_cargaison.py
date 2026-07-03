from odoo import models, fields, api
from odoo.exceptions import UserError


class PortTypeCargaison(models.Model):
    _name = 'port.type.cargaison'
    _description = 'type de cargaison'

    name = fields.Char(string="Type")
    tarif_line_ids = fields.One2many(
        'port.type.cargaison.tarif',
        'type_cargaison_id',
        string='Prestation')

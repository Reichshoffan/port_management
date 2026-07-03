from odoo import models, fields, api
from odoo.exceptions import UserError


class PortCargaisonLine(models.Model):
    _name = 'port.cargaison.line'
    _description = 'Ligne de cargaison'

    name = fields.Char(string="Désignation")

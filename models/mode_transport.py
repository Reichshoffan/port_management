from odoo import models, fields, api
from odoo.exceptions import UserError


class PortModeTransport(models.Model):
    _name = 'port.mode.transport'
    _description = 'Mode de transport'

    name = fields.Char(string="Désignation")

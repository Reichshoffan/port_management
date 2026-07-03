from odoo import models, fields, api
from datetime import date


class PortOrdreLivraison(models.Model):
    _name = 'port.ordre.livraison'
    _description = 'Ordre de livraison'

    name = fields.Char(string="Numéro")
    date_livraison = fields.Date("Date")

from odoo import models, fields, api
from odoo.exceptions import UserError


class PortTarifTypeCargaison(models.Model):
    _name = 'port.type.cargaison.tarif'
    _description = 'Tarification type de cargaison'

    product_id = fields.Many2one('product.template', string="Produit")
    type_cargaison_id = fields.Many2one('port.type.cargaison', string="Type cargaison")
    prix = fields.Float("Prix")

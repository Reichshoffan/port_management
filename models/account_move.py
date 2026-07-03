from odoo import models, fields, api
from odoo.exceptions import UserError

class AccountMoveInherit(models.Model):
    _inherit = 'account.move'

    cargaison_id = fields.Many2one(
        'port.cargaison',
        string="N°Dossier",
    )





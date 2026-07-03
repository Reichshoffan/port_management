from odoo import models, fields, api
from odoo.exceptions import ValidationError


class DepartCargaison(models.Model):
    _name = 'port.depart.cargaison'
    _description = 'Départ de cargaison'
    _rec_name = 'name'

    name = fields.Char(
        string="N° Départ",
        required=True,
        copy=False,
        default="Nouveau"
    )

    date_depart = fields.Date(
        string="Date de départ",
        required=True,
        default=fields.Datetime.now
    )

    cargaison_id = fields.Many2one(
        'dry.port.cargaison',
        string="Cargaison",
        required=True
    )

    client_id = fields.Many2one(
        'res.partner',
        string="Client",
        related='cargaison_id.client_id',
        store=True
    )

    transporteur_id = fields.Many2one(
        'res.partner',
        string="Transporteur"
    )

    chauffeur = fields.Char(
        string="Chauffeur"
    )

    immatriculation = fields.Char(
        string="Immatriculation camion"
    )

    destination = fields.Char(
        string="Destination"
    )

    poids = fields.Float(
        string="Poids expédié (Kg)"
    )

    observation = fields.Text(
        string="Observations"
    )

    statut = fields.Selection([
        ('draft', 'Brouillon'),
        ('confirmed', 'Confirmé'),
        ('done', 'Expédié'),
        ('cancel', 'Annulé')
    ], default='draft', string="Statut")

    user_id = fields.Many2one(
        'res.users',
        string="Responsable",
        default=lambda self: self.env.user
    )

    def action_confirm(self):
        self.write({'statut': 'confirmed'})

    def action_done(self):
        self.write({'statut': 'done'})

        if self.cargaison_id:
            self.cargaison_id.statut = 'livree'

    def action_cancel(self):
        self.write({'statut': 'cancel'})

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'Nouveau') == 'Nouveau':
                vals['name'] = self.env['ir.sequence'].next_by_code(
                    'dry.port.depart.cargaison'
                ) or 'Nouveau'
        return super().create(vals_list)
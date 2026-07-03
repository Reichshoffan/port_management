from Scripts.odoo.api import readonly
from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import date

class PortCargaison(models.Model):
    _name = 'port.cargaison'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Cargaison'

    name = fields.Char("N° dossier", required=True, default= "NEW", tracking=True)
    num_voyage = fields.Char("N° voyage")
    client_id = fields.Many2one('res.partner', string="Client")
    type_cargaison_id = fields.Many2one('port.type.cargaison', string="Cargaison")
    gps_id = fields.Many2one('port.gps', string="Numéro GPS")
    type_marchandise_id = fields.Many2one('port.type.marchandise', string="Type de marchandise")
    mode_transport_id = fields.Many2one('port.mode.transport', string="Mode de transport")
    date_depart = fields.Datetime("Date de départ")
    date_entree = fields.Datetime("Date d'entrée")
    date_sortie = fields.Datetime("Date de sortie")
    sejour = fields.Integer(string="Séjour", compute="_compute_sejour")
    poids = fields.Float("Poids (Kg)")
    code_sh = fields.Char(string="Code SH")
    volume = fields.Float("Volume (m³)")
    immat_vehicule = fields.Char("Immat_vehicule", required=True,tracking=True)

    conducteur = fields.Char("Conducteur")
    permis_conduire = fields.Char("Permis de conduire")
    provenance = fields.Char("Provenance")
    destination = fields.Char("Destination")
    bill_of_lading = fields.Char("N°Bill of Landing")
    nb_colis = fields.Integer(string="Nombre de colis")
    num_colis = fields.Char(string="N° de colis")
    nb_conteneur = fields.Integer(string="Nombre de conteneurs")
    num_conteneur = fields.Char("N°Conteneur")
    num_voyage = fields.Char("N°Voyage")
    t1 = fields.Char("N° et date T1")
    num_titre_transit = fields.Char("N°Titre transit")
    num_d15 = fields.Char("N°D15")
    num_dic = fields.Char("N°DIC")
    facture_total = fields.Monetary(
        string="Montant facturé",
        currency_field='currency_id',
        compute="_compute_facture_data"
    )
    currency_id = fields.Many2one(
        'res.currency',
        default=lambda self: self.env.company.currency_id
    )
    statut_depart = fields.Selection([
        ('brouillon', 'Brouillon'),
        ('valide', 'Validé')
    ], default='brouillon', string="Statut")
    statut = fields.Selection([
        ('brouillon', 'Brouillon'),
        ('depart', 'Départ'),
        ('entree', 'Entrée'),
        ('traitement', 'En Traitement'),
        ('facture', 'Facturé'),
        ('paye', 'Payé'),
        ('sortie', 'Sortie'),
    ], default='brouillon', string="Statut", tracking=True)

    def action_depart(self):
        self.write({
            'statut': 'depart',
            'date_depart': fields.Datetime.today()
        })

    def action_entrer(self):
        self.write({
            'statut': 'entree',
            'date_entree': fields.Datetime.today()
        })

    def action_traiter(self):
        self.write({'statut': 'traitement'})

    def action_facturer(self):
        self.write({'statut': 'facture'})

        # Créer la facture client
        if self.type_cargaison_id:
            invoice_lines = []

            for tarif in self.type_cargaison_id.tarif_line_ids:
                invoice_lines.append((0, 0, {
                    'product_id': tarif.product_id.id,
                    'quantity': 1,
                    'price_unit': tarif.prix,
                }))

            invoice = self.env['account.move'].create({
                'move_type': 'out_invoice',
                'cargaison_id': self.id,
                'partner_id': self.client_id.id,
                'invoice_line_ids': invoice_lines,
            })

    def action_sortir(self):
        self.write({
            'statut': 'sortie',
            'date_sortie': fields.Datetime.today()
        })

    def action_payé(self):
        self.write({'statut': 'paye'})

    def action_sortie(self):
        self.write({'statut': 'sortie'})

    def action_open_facture(self):
        self.ensure_one()
        action = self.env.ref('account.action_move_out_invoice_type').read()[0]

        action['domain'] = [
            ('move_type', '=', 'out_invoice'),
            ('cargaison_id', '=', self.id)
        ]

        action['context'] = {
            'default_move_type': 'out_invoice',
            'default_cargaison_id': self.id,
        }

        return action

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            # Générer le numéro uniquement si pas déjà défini
            if vals.get('name', 'Nouveau') == 'Nouveau':
                vals['name'] = self.env['ir.sequence'].next_by_code(
                    'port.cargaison'
                ) or 'Nouveau'
        return super().create(vals_list)

    def copy(self, default=None):
        default = dict(default or {})
        # Lors d'un duplicata, forcer un nouveau numéro
        default['name'] = self.env['ir.sequence'].next_by_code(
            'port.cargaison'
        )
        return super().copy(default)

    @api.depends()
    def _compute_facture_data(self):
        for rec in self:
            factures = self.env['account.move'].search([
                ('move_type', '=', 'out_invoice'),
                ('cargaison_id', '=', rec.id),
                ('state', '!=', 'cancel'),
            ])

            rec.facture_total = sum(factures.mapped('amount_total'))

    @api.depends('date_entree', 'date_sortie')
    def _compute_sejour(self):
        for rec in self:
            if rec.date_entree and rec.date_sortie:
                rec.sejour = (rec.date_sortie - rec.date_entree).days
            else:
                rec.sejour = 0
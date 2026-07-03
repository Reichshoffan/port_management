from odoo import models, fields

class PortGPS(models.Model):
    _name = 'port.gps'
    _description = 'Stock de GPS'
    _rec_name = 'reference'

    reference = fields.Char(
        string='Référence',
        required=True,
        copy=False,
        default='Nouveau'
    )

    name = fields.Char(
        string='Désignation',
        required=True
    )

    modele = fields.Char(
        string='Modèle'
    )

    numero_serie = fields.Char(
        string='Numéro de série'
    )

    imei = fields.Char(
        string='IMEI'
    )

    date_acquisition = fields.Date(
        string="Date d'acquisition"
    )

    etat = fields.Selection([
        ('stock', 'En stock'),
        ('affecte', 'Affecté'),
        ('maintenance', 'En maintenance'),
        ('hors_service', 'Hors service'),
    ], default='stock', string='État')

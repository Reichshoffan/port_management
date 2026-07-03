from odoo import models, fields, api
from odoo.exceptions import ValidationError


class VehiculeCargaison(models.Model):
    _name = 'port.vehicule'
    _description = 'Véhicule'
    _rec_name = 'name'

    name = fields.Char(
        string="N° Immatriculation",
        required=True,
        copy=False,
        default="Nouveau"
    )
    marque = fields.Char(
        string="Marque"
    )
    num_gps = fields.Char(
        string="Numéro GPS"
    )
    nom_conducteur = fields.Char(
        string="Conducteur"
    )
    cni_conducteur = fields.Char(
        string="N°Identité"
    )

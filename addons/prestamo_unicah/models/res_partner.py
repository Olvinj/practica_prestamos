
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    prestamo_ids = fields.One2many(
        comodel_name="prestamo.prestamo",
        inverse_name="partner_id",
        string="Préstamos",
    )

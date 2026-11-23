
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class PrestamoLinea(models.Model):
    _name = "prestamo.linea"
    _description = "Equipo del préstamo"

    prestamo_id = fields.Many2one(
        comodel_name="prestamo.prestamo",
        string="Préstamo",
        required=True,
        ondelete="cascade",
    )

    equipo_id = fields.Many2one(
        comodel_name="prestamo.equipo",
        string="Equipo",
        required=True,
        domain="[('estado', '=', 'disponible')]",
        ondelete="restrict",
    )

    categoria = fields.Selection(
        related="equipo_id.categoria",
        string="Categoría",
        readonly=True,
    )

    observacion = fields.Char(
        string="Observación",
    )

    @api.constrains("equipo_id", "prestamo_id")
    def _check_equipo_disponible(self):
        for linea in self:
            if (
                linea.prestamo_id.state == "borrador"
                and linea.equipo_id.estado != "disponible"
            ):
                raise ValidationError(
                    "Solo se pueden agregar equipos que estén disponibles."
                )

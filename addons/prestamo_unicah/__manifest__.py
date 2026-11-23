{
    "name": "Préstamo de equipo UNICAH",
    "version": "20.0.1.0.0",
    "summary": "Control de préstamos y devoluciones de equipo universitario",
    "category": "Services",
    "author": "Olvin Javier Martínez Funez",
    "license": "LGPL-3",
    "depends": ["base", "mail"],
    "data": [
        "security/ir.access.csv",
        "data/prestamo_equipo_data.xml",
        "views/prestamo_equipo_views.xml",
        "views/prestamo_views.xml",
        "views/res_partner_views.xml",
    ],
    "application": True,
    "installable": True,
}

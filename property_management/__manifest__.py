# -*- coding: utf-8 -*-
{
    "name": "Property Management",
    "version": "1.0",
    "summary": "Simple property management addon",
    "description": "An example Odoo extra addon for property management.",
    "author": "Your Name",
    "category": "Real Estate",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/property_views.xml",
    ],
    "installable": True,
    "application": False,
}

from odoo import api, fields, models


class StockInherited(models.Model):
    _inherit = 'product.template'

    # Add new fields
    product_price_over_10 = fields.Char(string='Product price over 10')

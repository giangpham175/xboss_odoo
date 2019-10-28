from odoo import models, fields, api


class PurchaseCategories(models.Model):
    _name = "purchase.order.line"
    _inherit = "purchase.order.line"

    categ_types = fields.Selection([('products', 'Products'), ('services', 'Services'), (
        'assets', 'Assets'), ('charge', 'Charges')], 'Category', default='products')

    @api.onchange('categ_types')
    def onchange_use_insurance(self):
        res = {}
        if self.categ_types == 'charge':
            res['domain'] = {'product_id': [
                ('purchase_ok', '=', True), '&', ('type', '=', 'service'), ('categ_charge', '=', True)]}
        elif self.categ_types == 'services':
            res['domain'] = {'product_id': [
                ('purchase_ok', '=', True), '&', ('type', '=', 'service'), ('categ_service', '=', True)]}
        else:
            res['domain'] = {'product_id': [
                ('purchase_ok', '=', True), '&', ('type', '=', 'service'), ('categ_assets', '=', True)]}
        return res

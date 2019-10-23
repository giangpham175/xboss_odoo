from odoo import models, fields, api


class Category(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    categ_product = fields.Boolean('Products', default=False)

    @api.constrains('categ_product')
    def _check_product(self):
        if self.type == 'consu' or self.type == 'product' or self.type == 'service':
            for r in self:
                if r.categ_product == True and self.categ_assets == True:
                    raise models.ValidationError(
                        'Any one of the category type should be selected')
                if r.categ_product == True and self.categ_charge == True:
                    raise models.ValidationError(
                        'Any one of the category type should be selected')
                if r.categ_product == True and self.categ_service == True:
                    raise models.ValidationError(
                        'Any one of the category type should be selected ')

    @api.onchange('type')
    def _change_type(self):
        self.categ_product = False

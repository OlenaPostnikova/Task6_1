from odoo import fields, models, _
from odoo.exceptions import UserError


class LibraryPublisher(models.Model):
    _name = 'library.publisher'
    _description = 'Library Publishing Houses'

    name = fields.Char(required=True)


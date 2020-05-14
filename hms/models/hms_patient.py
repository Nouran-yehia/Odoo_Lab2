from odoo import models, fields, api


class HmsPatient(models.Model):
    _name = "hms.patient"

    Firstname = fields.Char()
    Lastname = fields.Char()
    Birthdate = fields.Date()
    History = fields.Html()
    CRRatio = fields.Float()
    Blood = fields.Selection([
        ("O", "O blood"),
        ("A", "A blood"),
        ("B", "B blood"),
    ])
    PCR = fields.Boolean()
    Image = fields.Binary()
    Address = fields.Text()
    Age = fields.Integer()
    department_id = fields.Many2one("hms.department")
    states = fields.Selection([
        ("good", "good"),
        ("Undetirmend", "Undetirmend"),
        ("fair", "fair"),
        ("serious", "serious")
    ])
    doctor_id = fields.Many2many("hms.doctor")

    # is_department_open = fields.Boolean(related = "department_id.", "")

    @api.onchange("Age")
    def onchange_age(self):
        if self.Age < 30:
            self.PCR = True


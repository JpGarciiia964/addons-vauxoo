# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#    Copyright (C) OpenERP Venezuela (<http://openerp.com.ve>).
#    All Rights Reserved
# ##############Credits######################################################
#    Coded by: Humberto Arocha <hbto@vauxoo.com>
#    Planified by: Rafael Silva <rsilvam@vauxoo.com>
#    Audited by: Nhomar Hernandez <nhomar@vauxoo.com>
#############################################################################
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#     by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################
{
    "name": "Customer's Due Report",
    "version": "0.2",
    "author": "Vauxoo",
    "category": "Generic Modules/Others",
    "description": """
This module will allow you to get in Multicurrency:
A Customer & Supplier Detail Due Report,
A Customer & Supplier Aging Due Report,
    Comming Soon:
A Customer's Formal Due Report,
A Supplier's Formal Due Report,
""",
    "website": "http://www.vauxoo.com/",
    "license": "",
    "depends": [
        "account",
        "controller_report_xls",
    ],
    "demo": [],
    "data": [
        "data/aging_due_report_paper_format.xml",
        "data/aging_due_report_style.xml",
        "views/wizard.xml",
        "views/customer_aging_due_report_qweb.xml",
        "views/customer_formal_due_report_qweb.xml",
        "views/customer_detail_due_report_qweb.xml",
        "views/supplier_formal_due_report_qweb.xml",
        "views/aging_due_report.xml"
    ],
    "test": [],
    "js": [],
    "css": [],
    "qweb": [],
    "installable": True,
    "auto_install": False,
    "active": False
}

# Copyright (c) 2025, Frederick Lim and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator

class AirplaneFlight(WebsiteGenerator):
    def on_submit(self):
        self.set_status_completed()

    def set_status_completed(self):
        self.status = "Completed"

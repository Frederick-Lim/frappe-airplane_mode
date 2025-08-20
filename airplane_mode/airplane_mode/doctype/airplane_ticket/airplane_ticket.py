# Copyright (c) 2025, Frederick Lim and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class AirplaneTicket(Document):
	def validate(self):
		self.remove_duplicate_item()
		self.calculate_total_amount()

	def calculate_total_amount(self):
		# Calculate total amount based on flight_price and the sum of add_ons items
		self.total_amount = self.flight_price + sum(item.amount for item in self.add_ons) or 0

	def remove_duplicate_item(self):
		# Set to track seen items and rows for removal
		seen_items = set()
		rows_to_remove = set()

		# Iterate through child table rows
		for row in self.add_ons:
			if row.item in seen_items:
				# Mark this row for removal (duplicate)
				rows_to_remove.add(row)
			else:
				# Mark this item as seen
				seen_items.add(row.item)

		# Remove duplicates from the child table
		for row in rows_to_remove:
			self.remove(row)
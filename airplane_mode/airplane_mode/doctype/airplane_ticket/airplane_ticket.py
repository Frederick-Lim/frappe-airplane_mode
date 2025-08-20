# Copyright (c) 2025, Frederick Lim and contributors
# For license information, please see license.txt

import frappe
import random
from frappe.model.document import Document


class AirplaneTicket(Document):
	def validate(self):
		self.remove_duplicate_item()
		self.calculate_total_amount()

	def calculate_total_amount(self):
		# Calculate total amount based on flight_price and the sum of add_ons items
		# self.total_amount = self.flight_price + (sum(item.amount for item in self.add_ons) or 0)
		total_add_ons = sum(item.amount for item in self.add_ons) or 0
		self.total_amount = self.flight_price + total_add_ons


	def remove_duplicate_item(self):
		# Track seen items and rows for removal
		seen_items = set()
		rows_to_remove = []

		# Iterate through child table rows
		for row in self.add_ons:
			if row.item in seen_items:
				# Mark this row for removal (duplicate)
				rows_to_remove.append(row)
			else:
				# Mark this item as seen
				seen_items.add(row.item)

		# Remove duplicates from the child table
		for row in rows_to_remove:
			self.remove(row)

	def before_submit(self):
		self.check_status()

	def check_status(self):
		if self.status != "Boarded":
			frappe.throw('Ticket Status must be "Boarded"')

	def before_insert(self):
		self.set_seat()
		
	def set_seat(self):
		self.seat = f"{random.randint(1, 60)}{random.choice('ABCDE')}"
import frappe
from frappe import _

def get_context(context):
	grades = frappe.get_list("Student grades", fields=[
		"student_name",
		'physical_education',
		"logic",
		"philosophy",
		"physics",
		"literature",
		"english",
		"computer_science",
		"databases",
		"programming",
		"math",
	])
	subjects = frappe.get_list("Subject", fields=["title"])
	context.subjects = subjects
	context.grades = grades

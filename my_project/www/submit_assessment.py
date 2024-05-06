import frappe
from frappe import _

def get_context(context):

	try:
		assessment = frappe.get_doc({
			"doctype": "Student grades",
			"student_name": frappe.request.form.get('student_name'),
			"physical_education": frappe.request.form.get('Physical education'),
			"logic": frappe.request.form.get('Logic'),
			"philosophy": frappe.request.form.get('Philosophy'),
			"physics": frappe.request.form.get('Physics'),
			"literature": frappe.request.form.get('Literature'),
			"english": frappe.request.form.get('English'),
			"computer_science": frappe.request.form.get('Computer science'),
			"databases": frappe.request.form.get('Databases'),
			"programming": frappe.request.form.get('Programming'),
			"math": frappe.request.form.get('Math'),
		})
		assessment.insert()

		frappe.db.commit()
		context.message = 'Assessment submitted successfully'
	except Exception as e:
		context.message = str(e)

import frappe
from frappe.sessions import generate_csrf_token


def get_context(context):
	# Получаем список предметов из базы данных
	subjects = frappe.get_list("Subject", fields=["title", 'name'])

	# Передаем список предметов в контекст шаблона
	context.subjects = subjects

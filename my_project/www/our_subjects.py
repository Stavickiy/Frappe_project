import frappe


def get_context(context):
	# Получаем список предметов из базы данных
	subjects = frappe.get_list("Subject", fields=["title"])

	# Передаем список предметов в контекст шаблона
	context.subjects = subjects

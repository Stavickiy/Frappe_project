from __future__ import unicode_literals
from frappe import _

def get_routes():
    return [
        {
            "from_route": "/submit_assessment/",
            "to_route": "submit_assessment",
            "defaults": {
                "doctype": "Assessment"
            }
        }
    ]

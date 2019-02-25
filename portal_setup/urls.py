from flask import Blueprint
from .views import portals, portal_setup_api, edit_portal, delete_portal, add_portal, portalproductrel_api

# router register blueprint
portal_setup_router = Blueprint('portal_setup', __name__)

# # register views
portal_setup_router.add_url_rule('/portals/', view_func=portals, methods=['GET'])
portal_setup_router.add_url_rule('/portals/<int:portal_id>/', view_func=portals, methods=['GET'])
portal_setup_router.add_url_rule('/portals/add/', view_func=add_portal, methods=['GET', 'POST'])
portal_setup_router.add_url_rule('/portals/<int:portal_id>/edit/', view_func=edit_portal, methods=['GET', 'POST'])
portal_setup_router.add_url_rule('/portals/<int:portal_id>/delete/', view_func=delete_portal, methods=['GET', 'DELETE'])

# register apis
portal_setup_router.add_url_rule('/api/v1/portals/', defaults={'portal_id': None}, view_func=portal_setup_api, methods=['GET'])
portal_setup_router.add_url_rule('/api/v1/portals/', view_func=portal_setup_api, methods=['POST'])
portal_setup_router.add_url_rule('/api/v1/portals/<int:portal_id>/', view_func=portal_setup_api, methods=['GET', 'PUT', 'DELETE'])

# portal setup
portal_setup_router.add_url_rule('/api/v1/portalproductrels/', view_func=portalproductrel_api, methods=['GET'])
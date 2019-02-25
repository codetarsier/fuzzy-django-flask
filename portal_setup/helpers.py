from .models import PortalCityRel, PortalProductRel, PortalHomeHealthCheckForRel, PortalVenueRel
from config.constants import db_session

def save_portal_cities_rel(portal_id, portal_cities):
	for city_id in portal_cities:
		portal_city_rel = PortalCityRel()
		portal_city_rel.portal_id = portal_id
		portal_city_rel.city_id = city_id
		db_session.add(portal_city_rel)
		db_session.commit()

	return True


def save_portal_product_rel(portal_id, portal_products):
	for product_id in portal_products:
		portal_product_rel = PortalProductRel()
		portal_product_rel.portal_id = portal_id
		portal_product_rel.product_id = product_id
		db_session.add(portal_product_rel)
		db_session.commit()

	return True


def save_portal_home_health_check_rel(portal_id, portal_home_health_check_for_ids):
	for portal_home_health_check_for_id in portal_home_health_check_for_ids:
		portal_home_health_check_for_rel = PortalHomeHealthCheckForRel()
		portal_home_health_check_for_rel.portal_id = portal_id
		portal_home_health_check_for_rel.home_health_check_for_id = portal_home_health_check_for_id
		db_session.add(portal_home_health_check_for_rel)
		db_session.commit()

	return True


def save_portal_venues_rel(portal_id, portal_venues):
	for portal_venue in portal_venues:
		portal_venue_rel = PortalVenueRel()
		portal_venue_rel.portal_id = portal_id
		portal_venue_rel.venue_id = portal_venue
		db_session.add(portal_venue_rel)
		db_session.commit()

	return True

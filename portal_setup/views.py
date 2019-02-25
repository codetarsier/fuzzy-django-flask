from flask.views import MethodView

from common.models import Company, ConsignmentCity, Product, HodAsset
from portal_setup.models import HomeHealthCheckFor, PortalCityRel, PortalProductRel, PortalHomeHealthCheckForRel, \
	PortalVenueRel
from .serializers import *
from flask import jsonify, request, render_template, redirect, url_for, flash

from config.constants import db_session

from .serializers import PortalSetupListSerializer, PortalSetupSerializer, PortalProductReListSerializer
from .models import PortalSetup
from .helpers import save_portal_cities_rel, save_portal_home_health_check_rel, save_portal_product_rel, save_portal_venues_rel
from .forms import PortalSetupForm


def portals(portal_id=None):
	if portal_id:
		portal = PortalSetup.query.filter_by(id=portal_id).first()
		context = {'portal': portal}
		return render_template('portal_setup/portal_details.html', **context)
	
	portals = PortalSetup.query.all()
	context = {'portals': portals}
	return render_template('portal_setup/index.html', **context)


def add_portal():
	# update portal setup
	if request.method == 'POST':
		portal_form = PortalSetupForm(request.form)

		portal = PortalSetup()
		portal.portal_name = portal_form.data.get('portal_name')
		portal.company_id = portal_form.data.get('company_id')
		portal.is_pincode_enable = portal_form.data.get('is_pincode_enable')
		portal.is_home = portal_form.data.get('is_home')
		portal.is_enable_slot_home = portal_form.data.get('is_enable_slot_home')
		portal.is_enable_slot_office = portal_form.data.get('is_enable_slot_office')
		portal.is_pay_later = portal_form.data.get('is_pay_later')
		portal.is_pay_now = portal_form.data.get('is_pay_now')
		portal.home_visit_charges = portal_form.data.get('home_visit_charges')
		portal.company_url = portal_form.data.get('company_url')
		portal.is_view_bookings = portal_form.data.get('is_view_bookings')
		portal.is_for_demo = portal_form.data.get('is_for_demo')

		# save portal setting
		db_session.add(portal)
		db_session.commit()

		#import pdb
		#pdb.set_trace()

		# save cities
		save_portal_cities_rel(portal.id, request.form.getlist('portal_cities'))

		# save products
		save_portal_product_rel(portal.id, request.form.getlist('portal_products'))

		# save Home Health Check Options
		save_portal_home_health_check_rel(portal.id, request.form.getlist('portal_home_health_check_for_ids'))

		# save venues
		save_portal_venues_rel(portal.id, request.form.getlist('portal_venues'))

		flash('You have successfully added company details.')
		return redirect(url_for('portal_setup.portals'))

	# all active companies
	active_companies = Company.query.filter(Company.status == 'A').all()
	# active cities
	active_cities = ConsignmentCity.query.filter(ConsignmentCity.status == 'A').all()
	# all products
	products = Product.query.filter(Product.status == 'A').all()
	# all active venues
	venues = HodAsset.query.filter(HodAsset.status == 'A').all()
	# home health check for
	home_health_check_options = HomeHealthCheckFor.query.all()

	context = {'active_companies': active_companies, 'active_cities': active_cities,
			   'products':products, 'venues':venues, 'home_health_check_options':home_health_check_options}

	return render_template('portal_setup/add_portal.html', **context)


def edit_portal(portal_id=None):
	portal = PortalSetup.query.filter_by(id=portal_id).first()
	portal_form = PortalSetupForm(request.form)

	# update portal setup
	if request.method == 'POST':
		portal.portal_name = portal_form.data.get('portal_name')
		db_session.add(portal)
		db_session.commit()

		flash('You have successfully changed the company details.')
		return redirect(url_for('portal_setup.portals'))

	context = {'portal': portal, 'form': portal_form}
	return render_template('portal_setup/edit_portal.html', **context)


def delete_portal(portal_id=None):
	portal = PortalSetup.query.filter_by(id=portal_id).first()
	portal_name = portal.portal_name
	db_session.delete(portal)
	db_session.commit()

	flash('You have successfully deleted the {}.'.format(portal_name))
	return redirect(url_for('portal_setup.portals'))


class PortalSetupAPI(MethodView):
	single_portal_serializer = PortalSetupSerializer
	many_portal_serializer = PortalSetupListSerializer


	def get(self, portal_id=None):
		if portal_id:
			portal = PortalSetup.query.filter_by(id=portal_id).first()
			if not portal:
				return jsonify({'details': '{} Does not Exists'.format(portal_id)}), 404
			
			output = self.single_portal_serializer.dump(portal).data
			return jsonify(output), 200
		
		portals = PortalSetup.query.all()
		output = self.many_portal_serializer.dump(portals).data
		return jsonify(output), 200
 
portal_setup_api = PortalSetupAPI.as_view('portals_api')

class PortalProductReAPI(MethodView):
	many_portal_serializer = PortalProductReListSerializer

	def get(self):
		portal_products = PortalProductRel.query.all()
		output = self.many_portal_serializer.dump(portal_products).data
		return jsonify(output), 200		


portalproductrel_api = PortalProductReAPI.as_view('portalproductrel_api')
# app.add_url_rule('/portalproductrel/', view_func=UserAPI.as_view('users'))

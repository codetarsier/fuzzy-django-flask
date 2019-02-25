from config.constants import db
from common.models import TimeStampedBaseModel
from sqlalchemy import Column, DateTime, Integer, String, Boolean, ForeignKey, Float

class PortalSetup(TimeStampedBaseModel):
    """
    """
    __tablename__ = 'portal_setup'
    id = Column(Integer, primary_key=True)
    portal_name = Column(String(256), name='portal_name')
    company_id = Column(Integer)
    is_pincode_enable = Column(Boolean, default=False)
    is_home = Column(Boolean, default=False)
    is_enable_slot_home = Column(Boolean, default=False)
    is_office = Column(Boolean, default=False)
    is_enable_slot_office = Column(Boolean, default=False)
    home_visit_charges = Column(Float, default=0.0)
    is_pay_now = Column(Boolean, default=False)
    is_pay_later = Column(Boolean, default=True)
    logo_url = Column(String(256))
    company_url = Column(String(256))
    is_view_bookings = Column(Boolean, default=False)
    is_for_demo = Column(Boolean, default=True)
    portal_products = db.relationship('PortalProductRel', backref='portal_setup', lazy=True)
    portal_cities = db.relationship('PortalCityRel', backref='portal_setup', lazy=True)
    portal_venues = db.relationship('PortalVenueRel', backref='portal_setup', lazy=True)
    portal_home_health_check_for_ids = db.relationship('PortalHomeHealthCheckForRel', backref='portal_setup',
                                                       lazy=True)


#home health check setup
class HomeHealthCheckFor(TimeStampedBaseModel):
    __tablename__ = 'home_health_check_for'

    id = Column(Integer, primary_key=True)
    name = Column(String(256), name='name')


class PortalProductRel(TimeStampedBaseModel): 
    __tablename__ = 'portal_product_rel'

    id = Column(Integer, primary_key=True)
    portal_id = Column(Integer, ForeignKey('portal_setup.id'), nullable=False)
    product_id = Column(Integer)
    home_price = Column(Integer)
    #office_price = Column(Integer) # appointment_voucher table price. use @property


class PortalCityRel(TimeStampedBaseModel):
    __tablename__ = 'portal_city_rel'

    id = Column(Integer, primary_key=True)
    portal_id = Column(Integer, ForeignKey('portal_setup.id'), nullable=False)
    city_id = Column(Integer)


class PortalVenueRel(TimeStampedBaseModel):
    __tablename__ = 'portal_venue_rel'

    id = Column(Integer, primary_key=True)
    portal_id = Column(Integer, ForeignKey('portal_setup.id'), nullable=False)
    venue_id = Column(Integer)


class PortalHomeHealthCheckForRel(TimeStampedBaseModel):
    __tablename__ = 'portal_home_health_check_for_rel'

    id = Column(Integer, primary_key=True)
    portal_id = Column(Integer, ForeignKey('portal_setup.id'), nullable=False)
    home_health_check_for_id = Column(Integer, ForeignKey('home_health_check_for.id'), nullable=False)
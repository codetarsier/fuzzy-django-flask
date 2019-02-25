from config.constants import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy import Column, DateTime, Integer, String, Float, text, Boolean
from sqlalchemy.sql import func


__all__ = ['TimeStampedBaseModel']


class TimeStampedBaseModel(db.Model):
    __abstract__ = True

    created_on = Column(DateTime(timezone=True), server_default=func.now())
    updated_on = Column(DateTime(timezone=True), onupdate=func.now())


class TimeStampedBaseModelWithUUID(TimeStampedBaseModel):
    __abstract__ = True
    uuid = Column(UUID, name='uuid')



class Company(db.Model):
    __tablename__ = 'company'
    __table_args__ = {u'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=db.FetchedValue(), name='company_id')
    uuid = Column(UUID, name='company_uuid')
    name = Column(String(50), name='company_name')
    email = Column(String(50), name='company_email')
    mobile = Column(String(15), name='company_phone')
    address = Column(String(512), name='company_address')
    location = Column(String(100), name='company_location')
    area = Column(String(100), name='company_area')
    city = Column(String(50), name='company_city')
    state = Column(String(50), name='company_state')
    country = Column(String(30), name='company_country')
    pin_code = Column(String(6), name='company_pincode')
    latitude = Column(Float, name='company_latitude')
    longitude = Column(Float, name='company_longitude')
    parent_id = Column(String(10), name='company_parent_id')
    employee_count = Column(Integer, name='company_emp_count')
    mew_score = Column(Integer, name='company_mew_score')
    logo_url = Column(String(512), name='company_logo_url')
    image1_url = Column(String(512), name='company_image1')
    image2_url = Column(String(512), name='company_image2')
    image3_url = Column(String(512), name='company_image3')
    hod_balance = Column(Integer, name='company_hod_balance')
    designated_contact_mobile = Column(String(15), name='company_designated_contact_no_mobile')
    designated_contact_email = Column(String(50), name='company_designated_contact_email')
    designated_contact_name = Column(String(30), name='company_designated_contact_name')
    website_url = Column(String(512), name='company_website_url')
    intranet_link_url = Column(String(512), name='company_intranet_link_url')
    create_dttm = Column(DateTime(True), server_default=text("now()"), name='create_dttm')
    update_dttm = Column(DateTime(True), server_default=text("now()"), name='update_dttm')
    status = Column(String(2), name='company_status')
    company_app_url = Column(String(50), name='company_app_url')
    category = Column(String(2))

    def __repr__(self):
        return self.name


class ConsignmentCity(db.Model):
    __tablename__ = 'consignment_city'

    city_id = Column(Integer, primary_key=True, server_default=text("nextval('consignment_city_seq'::regclass)"))
    city_name = Column(String(256))
    status = Column(String(2), name='status')
    create_dttm = Column(DateTime(True), server_default=text("now()"))
    update_dttm = Column(DateTime(True), server_default=text("now()"))
    tanita_region = Column(Integer)

    def __repr__(self):
        return str(self.city_name).title()


class Product(db.Model):
    __tablename__ = 'product'
    __table_args__ = {u'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue(), name='product_id', )
    uuid = db.Column(UUID, name='product_id_uuid')
    name = db.Column(db.String(500), name='product_name')
    desc = db.Column(db.String(10000), name='product_desc')
    rating = db.Column(db.Float, name='product_rating')
    thumbnail_url = db.Column(db.String(1000), name='product_thumbnail',default='https://imghod.s3.amazonaws.com/careplan/1507029805png')
    image_1 = db.Column(db.String(1000), name='product_image_1', default='https://imghod.s3.amazonaws.com/careplan/1507029805png')
    image_2 = db.Column(db.String(1000), name='product_image_2', default='https://imghod.s3.amazonaws.com/careplan/1507029805png')
    image_3 = db.Column(db.String(1000), name='product_image_3',default='https://imghod.s3.amazonaws.com/careplan/1507029805png')
    status = db.Column(db.String(2), name='product_status', server_default='A')
    favourites_count = db.Column(db.Integer, name='product_favourites_count')
    official_partner_id = db.Column(db.Integer, name='official_partner_id', default = 22)
    type_of = db.Column(db.String(100), name='product_type_of')
    cost_original = db.Column(db.String(20), name='product_cost_original',default = 0)
    update_dttm = db.Column(db.DateTime(True), server_default=db.FetchedValue(), name='update_dttm')
    note = db.Column(db.String(1024), name='product_note')
    units_available = db.Column(db.Integer, name='product_units_available')
    delivery_method = db.Column(db.String(20), name='product_delivery_method')
    official_partner_discount = db.Column(db.Float, name='product_partner_discount')
    hod_discount = db.Column(db.Float, name='product_hod_discount')
    preorder_discount = db.Column(db.Float, name='product_preorder_discount')
    used_for = db.Column(db.String(2048), name='product_used_for')
    user_price = db.Column(db.Float, name='product_user_price')
    email_recommendation_notes = db.Column(db.Text, name='email_recommendation_notes')
    delivery_charges = db.Column(db.String(10), name='product_delivery_charges')

    is_popular = db.Column(db.String(1), server_default=db.FetchedValue(), name='popular')
    cp_pathway_id = db.Column(db.Integer, name='cp_pathway_id')
    pathway_type = db.Column(db.String(3), name='pathway_type')
    is_prime = db.Column(db.String(1), name='is_prime',default = 'N')
    care_plan_id = db.Column(db.Integer, name='careplan_id')
    inv_desc = db.Column(db.String(200), name='inv_desc', default='NA')
    has_plain = db.Column(db.String(20), name='has_plain', default='Y')
    has_flouride = db.Column(db.String(20), name='has_flouride')

    @hybrid_property
    def test_count(self):
        s = set()
        for test in self.tests:
            s.add(test.humain_code)
        return len(s)

    @test_count.expression
    def test_count(cls):
        return (db.session.query(func.count(Test.humain_code).label('test_count')).join(ProductTest,
                                                                                        ProductTest.test_id == Test.id).filter(
            ProductTest.product_id == cls.id).label('test_count'))

    def __repr__(self):
        return self.name


class ProductTest(db.Model):
    __tablename__ = 'product_test'

    id = Column(Integer, primary_key=True, server_default=text("nextval('product_test_id_seq'::regclass)"))
    test_id = Column(Integer)
    product_id = Column(Integer)
    create_dttm = Column(DateTime(True), server_default=text("now()"))
    update_dttm = Column(DateTime(True), server_default=text("now()"))


class Test(db.Model):
    __tablename__ = 'tests'

    id = Column(Integer, primary_key=True, server_default=text("nextval('test_seq'::regclass)"))
    test_code = Column(String(10))
    test_name = Column(String(50))
    profile_id = Column(Integer)
    seq_id = Column(Integer)
    update_dttm = Column(DateTime(True), server_default=text("now()"))
    ref_ranges = Column(String(2000))
    internal_ref_ranges = Column(String(2000))
    units = Column(String(50))
    method = Column(String(200))
    abbrevation = Column(String(20))
    description = Column(String(500))
    interpretation_type = Column(String(32))
    normal_qualitative = Column(String(1024), default='')
    abnormal_qualitative = Column(String(1024), default='')
    document_category_id = Column(Integer)
    mandatory = Column(Boolean(), default=True)
    humain_code = Column(String(32))
    humain_name = Column(String(64))


class HodAsset(db.Model):
    __tablename__ = 'hod_asset'
    __table_args__ = {u'schema': 'public'}

    id = Column(Integer, primary_key=True, server_default=db.FetchedValue(), name='hod_id')
    uuid = Column(UUID, name='hod_id_uuid')
    address = Column(String(256), name='hod_address')
    area = Column(String(128), name='hod_area')
    city = Column(String(50), name='hod_city')
    pin = Column(String(10), name='hod_pin')
    company = Column(String(100), name='hod_company')
    contact_hr = Column(String(100), name='hod_contact_hr')
    manager = Column(String(100), name='hod_mgr')
    duration = Column(String(10), name='hod_duration')
    update_dttm = Column(DateTime(True), server_default=text("now()"), name='update_dttm')
    latitude = Column(String(30), name='hod_latitude')
    longitude = Column(String(30), name='hod_longitude')
    manager_mobile = Column(String(30), name='hod_mgr_phone')
    status = Column(String(3), server_default=text("'A'::character varying"), name='hod_status')
    name = Column(String(50), name='hod_name')
    parent = Column(String(10), name='hod_parent')
    create_dttm = Column(DateTime(True), server_default=text("now()"), name='create_dttm')
    city_id = Column(Integer, name='city_id')
    code = Column(String(50), name='hod_code')
    building_id = Column(Integer, name='building_id')
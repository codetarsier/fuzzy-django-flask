from flask_admin.contrib.sqla import ModelView
from .models import (PortalCityRel, PortalHomeHealthCheckForRel, PortalProductRel, 
                     PortalSetup, PortalVenueRel, HomeHealthCheckFor)
from config.constants import db
from config.constants import app_admin as port_setup_admin


class PortalSetupAdmin(ModelView):
    form_excluded_columns = ('created_on', 'updated_on')

class HomeHealthCheckForAdmin(ModelView):
    pass

class PortalProductRelAdmin(ModelView):
    pass

class PortalCityRelAdmin(ModelView):
    pass

class PortalVenueRelAdmin(ModelView):
    pass

class PortalHomeHealthCheckForRelAdmin(ModelView):
    pass


port_setup_admin.add_view(PortalSetupAdmin(PortalSetup, db.session))
port_setup_admin.add_view(HomeHealthCheckForAdmin(HomeHealthCheckFor, db.session))
port_setup_admin.add_view(PortalProductRelAdmin(PortalProductRel, db.session))
port_setup_admin.add_view(PortalCityRelAdmin(PortalCityRel, db.session))
port_setup_admin.add_view(PortalVenueRelAdmin(PortalVenueRel, db.session))
port_setup_admin.add_view(PortalHomeHealthCheckForRelAdmin(PortalHomeHealthCheckForRel, db.session))


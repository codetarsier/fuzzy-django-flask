from config.constants import marshmallow
from .models import PortalSetup, PortalProductRel, PortalCityRel


__all__ = ['PortalSetupSerializer', 'PortalSetupListSerializer']



class PortalCityRelSchema(marshmallow.ModelSchema):
    class Meta:
        model = PortalCityRel


class PortalProductRelSchema(marshmallow.ModelSchema):
    class Meta:
        model = PortalProductRel


PortalProductReListSerializer = PortalProductRelSchema(many=True)

class PortalSetupSchema(marshmallow.ModelSchema):
    portal_products = marshmallow.Nested('PortalProductRelSchema', many=True, exclude=['id'])
    portal_cities = marshmallow.Nested('PortalCityRelSchema', many=True, exclude=['id'])

    class Meta:
        model = PortalSetup


PortalSetupSerializer = PortalSetupSchema()
PortalSetupListSerializer = PortalSetupSchema(many=True)

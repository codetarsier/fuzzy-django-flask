from wtforms_alchemy import ModelForm
from .models import PortalSetup

class PortalSetupForm(ModelForm):
    class Meta:
        model = PortalSetup

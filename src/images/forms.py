from django import forms
from .models import Image
from django.utils.translation import gettext as _


class ImageForm(forms.ModelForm):
	option = forms.ChoiceField(label="", initial='',widget=forms.Select(),choices=((0, _("JEE")),(1, _("NDA")),(2, _("IAS")),(3, _("SSC CHSL")),(4, _("SBI")),(5, _("CUSTOM"))),required=True)
	class Meta:
		model = Image
		fields = ('image','option','height','width',)
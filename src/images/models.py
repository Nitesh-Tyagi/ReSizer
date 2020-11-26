from django.db import models
from PIL import Image as Im
from django.utils.translation import gettext as _

# Create your models here.
class Image(models.Model):
	title = models.CharField(max_length=200)
	image = models.ImageField(upload_to='')
	option = models.IntegerField(choices=((0, _("JEE")),(1, _("NDA")),(2, _("IAS")),(3, _("SSC CHSL")),(4, _("SBI")),(5, _("CUSTOM"))), default=0)
	height = models.IntegerField(default=100)
	width = models.IntegerField(default=100)

	def __str__(self):
		return self.title
	def save(self):
		if self.image:
			photo1 = Im.open(self.image)
			# WIDTH , HEIGHT
			
			l=[(100,100),(200,200),(300,300),(400,400),(500,500),(self.height,self.width)]
			# size=((l[self.option][0] , l[self.option][1]))
			photo2=photo1.resize((l[self.option][0] , l[self.option][1]))
			photo2.save(self.image.path)

			

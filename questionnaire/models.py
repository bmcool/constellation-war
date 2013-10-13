#-*- encoding: utf-8 -*-

from django.db import models

from django.utils.translation import ugettext, ugettext_lazy as _
from django_ezutils.models import TimestampModel

GENDER_CHOICES = (
	("m", _("Male")),
	("f", _("Female")),
)

class Question(TimestampModel):
	title = models.CharField(_('Title'), max_length=50)
	description = models.TextField(_('Description'))
	gender = models.CharField(_('Gender'), max_length=1, default=None, choices=GENDER_CHOICES, blank=True, null=True)
	is_active = models.BooleanField(_('Active'), default=True)
	
	def __unicode__(self):
		return self.title

# 魔羯座 (12/22 - 1/19) Capricorn 
# 水瓶座 (1/20 - 2/18) Aquarius 
# 雙魚座 (2/19 - 3/20) Pisces 
# 牡羊座 (3/21 - 4/20) Aries 
# 金牛座 (4/21 - 5/20) Taurus 
# 雙子座 (5/21 - 6/21) Gemini 
# 巨蟹座 (6/22 - 7/22) Cancer 
# 獅子座 (7/23 - 8/22) Leo 
# 處女座 (8/23 - 9/22) Virgo 
# 天秤座 (9/23 - 10/22) Libra 
# 天蝎座 (10/23 - 11/21) Scorpio 
# 射手座 (11/22 - 12/21) Sagittarius

CONSTELLATION_CHOICES = (
	("capricorn", _("Capricorn")),
	("aquarius", _("Aquarius")),
	("pisces", _("Pisces")),
	("aries", _("Aries")),
	("taurus", _("Taurus")),
	("gemini", _("Gemini")),
	("cancer", _("Cancer")),
	("leo", _("Leo")),
	("virgo", _("Virgo")),
	("libra", _("Libra")),
	("scorpio", _("Scorpio")),
	("sagittarius", _("Sagittarius")),
)

class Vote(TimestampModel):
	question = models.ForeignKey(Question)
	voter = models.ForeignKey('account.Member')
	voter_constellation = models.CharField(_("Voter constellation"), max_length=20, choices=CONSTELLATION_CHOICES)
	gender = models.CharField(_('Gender'), max_length=1, default=None, choices=GENDER_CHOICES, blank=True, null=True)
	constellation = models.CharField(_("Constellation"), max_length=20, choices=CONSTELLATION_CHOICES)
	
	class Meta:
		unique_together = ('question', 'voter', 'gender')
	
	def __unicode__(self):
		return "%s # %s to %s" % (self.question, self.voter_constellation, self.constellation)
	
	def save(self, *args, **kwargs):
		if not self.id:
			self.from_constellation = self.voter.constellation
		super(Vote, self).save(*args, **kwargs)

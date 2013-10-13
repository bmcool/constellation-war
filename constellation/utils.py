
from datetime import date as d

def to_constellation_by_date(date):
	year = date.year
	
	if date >= d(year - 1, 12, 22) and date <= d(year, 1, 19):
		return "capricorn"
	elif date >= d(year, 1, 20) and date <= d(year, 2, 18):
		return "aquarius"
	elif date >= d(year, 2, 19) and date <= d(year, 3, 20):
		return "pisces"
	elif date >= d(year, 3, 21) and date <= d(year, 4, 20):
		return "aries"
	elif date >= d(year, 4, 21) and date <= d(year, 5, 20):
		return "taurus"
	elif date >= d(year, 5, 21) and date <= d(year, 6, 21):
		return "gemini"
	elif date >= d(year, 6, 22) and date <= d(year, 7, 22):
		return "cancer"
	elif date >= d(year, 7, 23) and date <= d(year, 8, 22):
		return "leo"
	elif date >= d(year, 8, 23) and date <= d(year, 9, 22):
		return "virgo"
	elif date >= d(year, 9, 23) and date <= d(year, 10, 22):
		return "libra"
	elif date >= d(year, 10, 23) and date <= d(year, 11, 21):
		return "scorpio"
	elif date >= d(year, 11, 22) and date <= d(year, 12, 21):
		return "sagittarius"

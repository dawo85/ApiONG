from rest_framework.test import APITestCase
from ApiOpenaid.utils.activities_data import UpdateData
from CallsRegisters.models import Register
from CallsRegisters.models import AidMonetary

class TestUpdateData(APITestCase):

	def setUp(self):
		self.info = {
			"iati-activities": [
				{
					"iati-activity": {
						"transaction": [
							{
								"transaction-date": {"iso-date":	"2008-09-30"},
								"provider-org": {
									"narrative": "Testing AAA",
									"ref": "44002"
								},
								"value": {
									"text": "1000",
									"value-date": "2008-09-30"
								}
							},
							{
								"transaction-date": {"iso-date":	"2008-09-30"},
								"provider-org": {
									"narrative": "Testing BBB",
									"ref": "44002"
								},
								"value": {
									"text": "100",
									"value-date": "2008-09-30"
								}
							}
						]
					}
				},
				{
					"iati-activity": {
						"transaction": [
							{
								"transaction-date": {"iso-date":	"2008-12-30"},
								"provider-org": {
									"narrative": "Testing AAA",
									"ref": "44002"
								},
								"value": {
									"text": "1500",
									"value-date": "2008-12-30"
								}
							}
						]
					}
				}
			]
		}

	def test_update_data(self):
		year_initial = '2005'
		year_end = '2010'
		country = 'SD'
		UpdateData().update(country, year_initial, year_end, self.info)
		registers = Register.objects.all()
		aids = AidMonetary.objects.all()
		self.assertEquals(len(registers), 1)
		self.assertEquals(len(aids), 2)
		self.assertEquals(aids[0].budget, 2500)
		self.assertEquals(aids[1].budget, 100)
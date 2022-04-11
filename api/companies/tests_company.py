import json
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from companies.models import (
    Company,
)

companyExample = {
	"ticker": "EEE",
	"name": "new test",
	"description": "lorem ipsum",
	"stock_market": [
		{
			"C": 322.85,
			"H": 381.69,
			"L": 206.33,
			"O": 233.09,
			"date": "2022-02-20"
		},
		{
			"C": 102.7,
			"H": 476.9,
			"L": 180.27,
			"O": 179.12,
			"date": "2022-02-21"
		},
		{
			"C": 161.57,
			"H": 430.52,
			"L": 193.08,
			"O": 435.31,
			"date": "2022-02-22"
		},
		{
			"C": 383.46,
			"H": 295.35,
			"L": 199.03,
			"O": 223.91,
			"date": "2022-02-23"
		},
		{
			"C": 478.97,
			"H": 271.78,
			"L": 225.84,
			"O": 476.68,
			"date": "2022-02-24"
		},
		{
			"C": 420.62,
			"H": 351.21,
			"L": 128.82,
			"O": 456.28,
			"date": "2022-02-25"
		},
		{
			"C": 368.71,
			"H": 390.44,
			"L": 234.41,
			"O": 495.36,
			"date": "2022-02-26"
		},
		{
			"C": 213.27,
			"H": 451.57,
			"L": 142.7,
			"O": 291.55,
			"date": "2022-02-27"
		},
		{
			"C": 223.09,
			"H": 390.26,
			"L": 208.33,
			"O": 190.33,
			"date": "2022-02-28"
		},
		{
			"C": 377.87,
			"H": 383.21,
			"L": 182.3,
			"O": 313.04,
			"date": "2022-03-01"
		},
		{
			"C": 198.8,
			"H": 334.27,
			"L": 222.87,
			"O": 266.11,
			"date": "2022-03-02"
		},
		{
			"C": 424.89,
			"H": 360.45,
			"L": 106.17,
			"O": 224.5,
			"date": "2022-03-03"
		},
		{
			"C": 297.85,
			"H": 420.13,
			"L": 199.54,
			"O": 113.61,
			"date": "2022-03-04"
		},
		{
			"C": 132.95,
			"H": 299.11,
			"L": 187.12,
			"O": 297.24,
			"date": "2022-03-05"
		},
		{
			"C": 289.35,
			"H": 271.81,
			"L": 118.1,
			"O": 371.47,
			"date": "2022-03-06"
		},
		{
			"C": 352.75,
			"H": 481.24,
			"L": 212.61,
			"O": 475.25,
			"date": "2022-03-07"
		},
		{
			"C": 208.83,
			"H": 299.93,
			"L": 113.27,
			"O": 461.0,
			"date": "2022-03-08"
		},
		{
			"C": 414.98,
			"H": 490.6,
			"L": 197.97,
			"O": 400.85,
			"date": "2022-03-09"
		},
		{
			"C": 123.44,
			"H": 494.96,
			"L": 231.08,
			"O": 168.69,
			"date": "2022-03-10"
		},
		{
			"C": 479.24,
			"H": 442.39,
			"L": 234.07,
			"O": 155.63,
			"date": "2022-03-11"
		},
		{
			"C": 410.57,
			"H": 307.41,
			"L": 130.58,
			"O": 409.06,
			"date": "2022-03-12"
		},
		{
			"C": 400.51,
			"H": 251.69,
			"L": 239.37,
			"O": 206.33,
			"date": "2022-03-13"
		},
		{
			"C": 137.25,
			"H": 272.17,
			"L": 214.83,
			"O": 251.69,
			"date": "2022-03-14"
		},
		{
			"C": 490.31,
			"H": 376.57,
			"L": 126.57,
			"O": 150.75,
			"date": "2022-03-15"
		},
		{
			"C": 243.75,
			"H": 407.02,
			"L": 211.96,
			"O": 313.68,
			"date": "2022-03-16"
		},
		{
			"C": 111.42,
			"H": 422.92,
			"L": 238.13,
			"O": 206.05,
			"date": "2022-03-17"
		},
		{
			"C": 270.25,
			"H": 445.46,
			"L": 139.91,
			"O": 339.08,
			"date": "2022-03-18"
		},
		{
			"C": 435.57,
			"H": 324.54,
			"L": 249.44,
			"O": 385.76,
			"date": "2022-03-19"
		},
		{
			"C": 497.1,
			"H": 355.53,
			"L": 239.42,
			"O": 418.05,
			"date": "2022-03-20"
		},
		{
			"C": 250.0,
			"H": 326.3,
			"L": 218.0,
			"O": 206.19,
			"date": "2022-03-21"
		},
		{
			"C": 192.37,
			"H": 265.57,
			"L": 200.66,
			"O": 399.72,
			"date": "2022-03-22"
		},
		{
			"C": 252.63,
			"H": 268.05,
			"L": 207.8,
			"O": 443.68,
			"date": "2022-03-23"
		},
		{
			"C": 403.07,
			"H": 258.08,
			"L": 114.64,
			"O": 229.18,
			"date": "2022-03-24"
		},
		{
			"C": 308.81,
			"H": 442.19,
			"L": 122.95,
			"O": 485.96,
			"date": "2022-03-25"
		},
		{
			"C": 313.87,
			"H": 336.07,
			"L": 146.09,
			"O": 426.29,
			"date": "2022-03-26"
		},
		{
			"C": 242.31,
			"H": 465.76,
			"L": 133.44,
			"O": 377.38,
			"date": "2022-03-27"
		},
		{
			"C": 262.08,
			"H": 450.42,
			"L": 206.31,
			"O": 439.19,
			"date": "2022-03-28"
		},
		{
			"C": 356.2,
			"H": 309.35,
			"L": 187.82,
			"O": 108.6,
			"date": "2022-03-29"
		},
		{
			"C": 102.93,
			"H": 256.05,
			"L": 239.04,
			"O": 340.88,
			"date": "2022-03-30"
		},
		{
			"C": 168.68,
			"H": 366.92,
			"L": 110.68,
			"O": 499.16,
			"date": "2022-03-31"
		},
		{
			"C": 167.77,
			"H": 362.46,
			"L": 175.07,
			"O": 390.51,
			"date": "2022-04-01"
		},
		{
			"C": 477.59,
			"H": 286.02,
			"L": 154.45,
			"O": 464.29,
			"date": "2022-04-02"
		},
		{
			"C": 412.04,
			"H": 279.63,
			"L": 235.51,
			"O": 116.36,
			"date": "2022-04-03"
		},
		{
			"C": 474.5,
			"H": 442.61,
			"L": 245.0,
			"O": 397.58,
			"date": "2022-04-04"
		},
		{
			"C": 396.95,
			"H": 283.05,
			"L": 109.88,
			"O": 425.29,
			"date": "2022-04-05"
		},
		{
			"C": 374.15,
			"H": 293.65,
			"L": 198.68,
			"O": 162.12,
			"date": "2022-04-06"
		},
		{
			"C": 495.01,
			"H": 489.72,
			"L": 163.13,
			"O": 261.44,
			"date": "2022-04-07"
		},
		{
			"C": 287.43,
			"H": 378.71,
			"L": 130.28,
			"O": 434.23,
			"date": "2022-04-08"
		},
		{
			"C": 359.07,
			"H": 311.19,
			"L": 190.68,
			"O": 480.85,
			"date": "2022-04-09"
		},
		{
			"C": 484.06,
			"H": 252.18,
			"L": 131.47,
			"O": 357.28,
			"date": "2022-04-10"
		}
	],
	"created_at": "2022-04-10T12:28:49.923035-05:00",
	"updated_at": "2022-04-10T12:52:13.392932-05:00"
}

class CompanyTestCase(TestCase):
    def test_list_companies(self):
        response = self.client.get("/api/v1/company/")

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(result["count"], 0)

    def test_create_company_success(self):
        response = self.client.post(
            "/api/v1/company/",
            {
	              "name": "Google",
	              "ticker": "GOOG",
	              "description": "Google Inc. description"
            },
        )

        result = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertIn("id", result)
        self.assertIn("ticker", result)
        self.assertIn("name", result)
        self.assertIn("description", result)
        self.assertIn("stock_market", result)
        self.assertIn("created_at", result)
        self.assertIn("updated_at", result)

    def test_create_company_ticker_work(self):
        response = self.client.post(
            "/api/v1/company/",
            {
                "name": "Google",
                "ticker": "AAAAAAAAAA",
                "description": "Google Inc. description"
            },
        )

        result = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertIn("ticker", result)
        self.assertEqual(result["ticker"], "The ticker structure is wrong")

    def test_get_company_success(self):
        c = Company.objects.create(**companyExample)
        c.save()

        response = self.client.get(f"/api/v1/company/{c.id}/")

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn("id", result)
        self.assertIn("ticker", result)
        self.assertIn("name", result)
        self.assertIn("description", result)
        self.assertIn("stock_market", result)
        self.assertIn("created_at", result)
        self.assertIn("updated_at", result)

    def test_patch_company_success(self):
        c = Company.objects.create(**companyExample)
        c.save()

        response = self.client.patch(
            f"/api/v1/company/{c.id}/",
            {
                "name": "Testing 2",
            },
        )

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn("id", result)
        self.assertIn("ticker", result)
        self.assertIn("name", result)
        self.assertEqual(result["name"], "Testing 2")
        self.assertIn("description", result)
        self.assertIn("stock_market", result)
        self.assertIn("created_at", result)
        self.assertIn("updated_at", result)


    def test_delete_company_success(self):
        c = Company.objects.create(**companyExample)
        c.save()

        response = self.client.delete(f"/api/v1/company/{c.id}/")

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)




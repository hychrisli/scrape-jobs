import scrapy
from os.path import dirname, realpath 


fileDir = realpath(__file__)
rootDir = dirname(dirname(dirname(fileDir)))

class JobsSpider(scrapy.Spider):
	name = "jobs"

	def start_requests(self):
		urls = [
		'https://stackoverflow.com/jobs/166865/google-software-engineer-site-reliability-new-google',
		'https://stackoverflow.com/jobs/138222/software-engineer-at-google-google',
		'https://stackoverflow.com/jobs/166867/software-engineer-tools-and-infrastructure-new-google',
		'https://stackoverflow.com/jobs/172530/sr-software-engineer-identity-and-access-atlassian',
		'https://stackoverflow.com/jobs/93322/senior-ui-engineer-hytrust'
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		print(response.url)
		tokens = response.url.split('/')

		filename = rootDir + '/data/' + tokens[4] + '.html';
		with open(filename, 'wb') as f:
			f.write(response.body)
			self.log('Saved file %s' % filename)

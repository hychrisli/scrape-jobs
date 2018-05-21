from os.path import dirname, realpath 
from lxml import html, etree

fileDir = realpath(__file__)
rootDir = dirname(dirname(fileDir))
dataFile = rootDir + '/pages/data/138222.html'

root = html.parse(dataFile)
find_text = etree.XPath("//h1/a/text()");
title = find_text(root)
print(title)


def divider():
	print ("-"*20 + "\n")


# About Sections
aboutSect = root.xpath('.//h2[text()="About this job"]/ancestor::section')
# print(aboutSect[0])
aboutRoot = etree.ElementTree(aboutSect[0])
# print(etree.tostring(aboutRoot))
jobTypeSpan = aboutRoot.xpath('.//span[contains(text(),"Job type")]/ancestor::div[position()=1]')
# print(jobTypeSpan)
# print(etree.tostring(jobTypeSpan[0]))

jobTypeRoot = etree.ElementTree(jobTypeSpan[0])

jobType = jobTypeRoot.xpath('//span/text()')
print("Job Type: " + jobType[1])


# Technology Section
techSect = root.xpath('.//h2[text()="Technologies"]/ancestor::section')
techRoot = etree.ElementTree(techSect[0])
skills = techRoot.xpath('//div/a/text()')
print("Skills: ", skills)

# Job Desc 
jobDescSect = root.xpath('.//h2[text()="Job description"]/ancestor::section')
jobDescRoot = etree.ElementTree(jobDescSect[0])
desc = jobDescRoot.xpath('//div/p/text()')
print ("Job Desc: ", desc)
divider()

# Responsibilty
respon = jobDescRoot.xpath('//div/ul[1]/li/text()')
print ("Responsibility", respon)
divider()

# Min Qualification
minQual = jobDescRoot.xpath('//div/ul[2]/li/text()')
print("Minimum Qualification", minQual)
divider()

# Preferred Qualification
preferQual = jobDescRoot.xpath('//div/ul[3]/li/text()')
print("Prefered Qualification", preferQual)
divider()


# About the company
companySect = root.xpath('//section[contains(@class, "-about-company")]')
print(companySect)
print(etree.tostring(companySect[0]))
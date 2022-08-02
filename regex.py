import re


class Validator:
    def email(self, data):
        return re.findall('(\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b)', data)
Validate = Validator()

class Extractor:
    def email(self, data):
        regex = re.compile(r'([A-z0-9.]+[@]+[A-z]+[.][A-z]+)')
        return re.findall(regex, data)
    def url(self, data):
        regex = re.compile('([A-z0-9.]+:[/]+[A-z0-9/:%\-_$–.+!*‘(),]+)')
        return re.findall(regex, data)
    def phoneN(self, data):
        # not all numbers
        regex = re.compile('(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
        return re.findall(regex, data)
Extract = Extractor()

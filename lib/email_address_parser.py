import re

class EmailAddressParser:

  def __init__(self, emails):
    self.emails = emails

  def parse(self):
    pattern = r"([A-z.]+@[a-z]+[.][a-z]{3})"
    regex = re.compile(pattern)
    return sorted(regex.findall(self.emails))
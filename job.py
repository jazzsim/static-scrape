class Job:
    def __init__(self, title, company, desc, location):
        self.title = title
        self.company = company
        self.desc = desc
        self.location = location
        
    def job_listing_card(self):
        print("{:*^85}".format(self.title))
        print("Company: {0:20}".format(self.company))
        print("Location: {0:20}".format(self.location))
        print('\nJob Description:\n' + self.desc)
        print('=' * 85)
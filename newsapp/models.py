from django.db import models

class Investor(models.Model):
    name = models.CharField(max_length=50)
    investor_type = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    contact_email = models.CharField(max_length=50)
    linkedin = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)

class Deal(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    company = models.ForeignKey(Company)
    firm = models.ManyToManyField(Firm)

    def __unicode__(self):
        return self.name

class Firm(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    deals = models.ManyToManyField(Deal)
    Vertical = models.ManyToManyField(Vertical)
    Company = models.ManyToManyField(Company)
    
    def __unicode__(self):
        return self.name

class Vertical(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    Company = models.ManyToManyField(Company)

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.ForeignKey(Company)
    location = models.CharField(max_length=200)
    field = models.CharField(max_length=200)

# ('ACQ',"Acquistition"),
#             ('NFUN',"New Fund"),
#             ('NFUND',"New Funding"),
#             ('O',"Other"),
#             ('BNKR',"Bankruptcy"),
#             ('MRGR', "Merger"),
#             ('MRGR', "Merger"),
    
class Company(models.Model):
    name = models.CharField(max_length=200)
    year_founded = models.IntegerField()
    last_funding_date = models.DateField()
    last_funding_amount = models.DecimalField(max_digits=10)
    last_funding_round = models.CharField(
        max_length=10,
        choices=[
            ('PS', "Pre-Seed"),
            ('S', "Seed"),
            ('A', "Series A"),
            ('B', "Series B"),
            ('C', "Series C"),
            ('D', "Series D"),
            ('E', "Series E"),
        ]
    )

class Person(models.Model):
    name = models.CharField(max_length=200)
    firm = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    alma_mater = models.CharField(max_length=200)
    company = models.ForeignKey(Company)
    main_location = models.CharField(max_length=200)
    leads_rounds = models.Choices(max_length=200)
    
class NewsClip(models.Model): 
    headline = models.CharField(max_length=64)
    author = models.CharField(max_length=256)
    publisher = models.CharField(max_length=256)
    industry = models.CharField(
        max_length=10,
        choices=[
            ('ACQ',"Acquistition"),
            ('NFUN',"New Fund"),
            ('NFUND',"New Funding"),
            ('O',"Other"),
            ('BNKR',"Bankruptcy"),
            ('MRGR', "Merger"),
            ('SERA', "Series A"),
            ('SERB', "Series B"),
            ('SERC', "Series C"),
            ('SERD', "Series D"),
            ('SERE', "Series E"),
        ]
    )
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    link = models.CharField(max_length=500, default='')

## A single models.py file holds multiple models. It is found in the app directory.

## A model is just a Python class

## Dream big

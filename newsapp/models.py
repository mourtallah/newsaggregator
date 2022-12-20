from django.db import models
from django.forms import ModelForm


class Investor(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200, unique=True, blank=False, null=False)
    twitter_handle = models.CharField(max_length=50, unique=True, blank=True, null=True)


class InvestorForm(ModelForm):
    class Meta:
        model = Investor
        fields = ["name", "twitter_handle"]


class Company(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    last_funding_quarter = models.CharField(
        max_length=2, choices=[("Q1", "Q1"), ("Q2", "Q2"), ("Q3", "Q3"), ("Q4", "Q4")]
    )
    industry = models.CharField(max_length=200, default="Probably Tech")
    location = models.CharField(max_length=200, default="Probably San Francisco")


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ["name", "last_funding_quarter", "industry", "location"]


class Deal(models.Model):
    def __str__(self):
        return (
            "Deal Name "
            + str(self.funding_round)
            + "; "
            + self.quarter
            + "/"
            + str(self.year)
        )

    quarter = models.CharField(
        default="Q1",
        choices=[("Q1", "Q1"), ("Q2", "Q2"), ("Q3", "Q3"), ("Q4", "Q4")],
        max_length=2,
    )
    year = models.CharField(max_length=4, default="2023")
    company = models.ManyToManyField(Company)
    investor = models.ManyToManyField(Investor)
    funding_round = models.CharField(
        max_length=10,
        default="Series A",
        choices=[
            ("PS", "Pre-Seed"),
            ("S", "Seed"),
            ("A", "Series A"),
            ("B", "Series B"),
            ("C", "Series C"),
            ("D", "Series D"),
            ("E", "Series E"),
        ],
    )


class DealForm(ModelForm):
    class Meta:
        model = Deal
        fields = ["quarter", "year", "company", "investor", "funding_round"]
    


# class Firm(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()
#     deals = models.ManyToManyField(Deal)
#     Vertical = models.ManyToManyField(Vertical)
#     Company = models.ManyToManyField(Company)

#     def __unicode__(self):
#         return self.name


# class Deal(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()
#     date = models.DateField()
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     firm = models.ManyToManyField(
#         Firm,
#     )


# class Firm(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()
#     deals = models.ManyToManyField(Deal)
#     Vertical = models.ManyToManyField(Vertical)
#     Company = models.ManyToManyField(Company)

#     def __unicode__(self):
#         return self.name


# class Deal(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()
#     date = models.DateField()
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     firm = models.ManyToManyField(
#         Firm,
#     )

#     def __unicode__(self):
#         return self.name


# class Vertical(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()
#     Company = models.ManyToManyField(Company)


# class Job(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     company = models.ForeignKey(Company)
#     location = models.CharField(max_length=200)
#     field = models.CharField(max_length=200)


# # ('ACQ',"Acquistition"),
# #             ('NFUN',"New Fund"),
# #             ('NFUND',"New Funding"),
# #             ('O',"Other"),
# #             ('BNKR',"Bankruptcy"),
# #             ('MRGR', "Merger"),
# #             ('MRGR', "Merger"),


# class Person(models.Model):
#     name = models.CharField(max_length=200)
#     firm = models.CharField(max_length=200)
#     title = models.CharField(max_length=200)
#     alma_mater = models.CharField(max_length=200)
#     company = models.ForeignKey(Company)
#     main_location = models.CharField(max_length=200)
#     leads_rounds = models.Choices(max_length=200)


class NewsClip(models.Model):
    def __str__(self) -> str:
        return self.headline

    headline = models.CharField(max_length=64)
    author = models.CharField(max_length=256)
    publisher = models.CharField(max_length=256)
    industry = models.CharField(
        max_length=10,
        choices=[
            ("ACQ", "Acquistition"),
            ("NFUN", "New Fund"),
            ("NFUND", "New Funding"),
            ("O", "Other"),
            ("BNKR", "Bankruptcy"),
            ("MRGR", "Merger"),
            ("SERA", "Series A"),
            ("SERB", "Series B"),
            ("SERC", "Series C"),
            ("SERD", "Series D"),
            ("SERE", "Series E"),
        ],
    )
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    link = models.CharField(max_length=500, default="")


# ## A single models.py file holds multiple models. It is found in the app directory.

# ## A model is just a Python class

# ## Dream big

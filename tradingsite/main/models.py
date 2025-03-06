from django.db import models
class Stock(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return self.symbol

class Correlation(models.Model):
    stocks = models.ManyToManyField(Stock)
    correlation = models.FloatField()

    def __str__(self):
        return f"Correlation between {', '.join([stock.symbol for stock in self.stocks.all()])}"
    

class COTReport(models.Model):
    market = models.ForeignKey(Stock, on_delete=models.CASCADE)
    report_date = models.DateField()
    long_positions = models.IntegerField()
    short_positions = models.IntegerField()

    def __str__(self):
        return f"COT Report for {self.market} on {self.report_date}"

class Market(models.Model):
    market = models.ForeignKey(Stock, on_delete=models.CASCADE)
    symbol_longs = models.IntegerField()
    symbol_shorts= models.IntegerField()

    def __str__(self):
        return self.symbol_longs

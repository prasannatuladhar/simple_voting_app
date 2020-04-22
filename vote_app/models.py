from django.db import models

class Vote(models.Model):
    question_text = models.CharField(max_length=250)
    option_one_text = models.CharField(max_length=20,default="a")
    option_two_text = models.CharField(max_length=20,default="b")
    option_three_text = models.CharField(max_length=20,default="c")
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    
    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count

    def in_percent_one(self):
        result =  self.option_one_count / (self.option_one_count + self.option_two_count + self.option_three_count) *100   
        return round(result,1)

    def in_percent_two(self):
        result =  self.option_two_count / (self.option_one_count + self.option_two_count + self.option_three_count) *100   
        return round(result,1)

    def in_percent_three(self):
        result = self.option_three_count / (self.option_one_count + self.option_two_count + self.option_three_count) *100   
        return round(result,1)
        
    def __str__(self):
        return self.question_text



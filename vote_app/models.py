from django.db import models

class Vote(models.Model):
    question_text = models.CharField(max_length=250)
    option_one_text = models.CharField(max_length=20,default="a")
    option_two_text = models.CharField(max_length=20,default="b")
    option_three_text = models.CharField(max_length=20,default="c")
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    option_one_image_url = models.CharField(max_length=250,default="https://images.unsplash.com/photo-1515549832467-8783363e19b6?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=282&q=80")
    option_two_image_url = models.CharField(max_length=250,default="https://images.unsplash.com/photo-1515549832467-8783363e19b6?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=282&q=80")
    option_three_image_url = models.CharField(max_length=250,default="https://images.unsplash.com/photo-1515549832467-8783363e19b6?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=282&q=80")
    
    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count

    def in_percent_one(self):
        total = self.option_one_count + self.option_two_count + self.option_three_count
        if total > 0:
            result =  self.option_one_count / total *100   
            return round(result,1)
        else:
            return 0   

        

    def in_percent_two(self):
        total = self.option_one_count + self.option_two_count + self.option_three_count
        if total > 0:
            result =  self.option_two_count / total *100   
            return round(result,1)
        else:
            return 0 

    def in_percent_three(self):
        total = self.option_one_count + self.option_two_count + self.option_three_count
        if total > 0:
            result =  self.option_three_count / total *100   
            return round(result,1)
        else:
            return 0 
        
    def __str__(self):
        return self.question_text



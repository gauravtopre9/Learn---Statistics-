import math
def confidence_interval(mean,stdev,no_of_sample,CIP=95):
    per_val = {80:1.282,85:1.440,90:1.645,95:1.960,99:2.576,99.5:2.807,99.9:3.291}
    val = per_val[CIP]
    margin = val*(stdev/(math.sqrt(no_of_sample)))
    range = [round(mean-margin,2), round(mean+margin,2)]
    print(range)

'''
#Ex.1 Are the apples big enough?
There are hundreds of apples on the trees, so you randomly choose just 46 apples and get:

a Mean of 86
a Standard Deviation of 6.2
So let's calculate the confidence interval (95%)
'''
confidence_interval(mean=86,stdev=6.2,no_of_sample=46,CIP=95)

#output : [84.21, 87.79]
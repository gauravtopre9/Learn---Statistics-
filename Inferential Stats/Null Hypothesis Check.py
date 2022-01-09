import math
def hypo_acceptance(mean_hyp,mean_sample,stdev_sample,no_of_sample,conf_per):
    per_val = {80:1.282,85:1.440,90:1.645,95:1.960,99:2.576,99.5:2.807,99.9:3.291}
    CIP_val = per_val[conf_per]
    Z_o = CIP_val*(stdev_sample/(math.sqrt(no_of_sample)))
    Z_cal = (mean_sample-mean_hyp)/(stdev_sample/math.sqrt(no_of_sample))
    if Z_cal > Z_o:
        print("Null Hypothesis is Rejected")
    else:
        print("Null Hypothesis is Accepted")

"""
Let's Consider the scenario where we are having following Hypothesis
Null Hypothesis : Average battery life of Headset is exact 15Hrs
Alternate Hypothesis : Avegare battery life of headset ui not 15Hrs (Exact)

We have taken sample of 20 Headsets and calculated Average Battery life which came out to be 17Hrs
and Standard Deviation as 3Hrs

So we have decide that given null hypothesis is Accepted or Rejected

"""

hypo_acceptance(mean_hyp=15,mean_sample=17,stdev_sample=3,no_of_sample=20,conf_per=95)

#ANS : Null Hypothesis is Rejected

hypo_acceptance(mean_hyp=15,mean_sample=17,stdev_sample=3,no_of_sample=20,conf_per=80)

#ANS : Null Hypothesis is Rejected
"""
Consider a showroom of electronic products, where there are various salesmen. Each
salesman is given a commission of 5%, depending on the sales made per month. In case
the sale done is less than 50000, then the salesman is not given any commission. Write
a function to calculate total sales of a salesman in a month, commission and remarks
for the salesman. Sales done by each salesman per week is to be provided as input.
Assign remarks according to the following criteria:
Excellent: Sales >=80000
Good: Sales>=60000 and <80000
Average: Sales>=40000 and <60000
Work Hard: Sales < 40000
"""
def sales(mon_list):
 
    fl_list = [float(i) for i in mon_list]

    total = sum(fl_list)

    if total >= 8000:
        remark = "Excellent Work" 
    elif total >= 6000 and total <8000:
        remark = "Good job"
    elif total >= 4000 and total <6000:
        remark = "Expected performance"
    else:
        remark = "Below expectation"

    return total, remark

jan_list = ["2528", "3433", "2438", "2234"]

print(sales(jan_list))

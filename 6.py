def compute_pay(hours_worked, hourly_rate):
    regular_hours = 40
    overtime_rate = 1.5
    if hours_worked <= regular_hours:
        regular_pay = hours_worked * hourly_rate
        overtime_pay = 0
    else:
        regular_pay = regular_hours * hourly_rate
        overtime_hours = hours_worked - regular_hours
        overtime_pay = overtime_hours * hourly_rate * overtime_rate
    total_pay = regular_pay + overtime_pay
    return total_pay
hours = 45
rate = 10
pay = compute_pay(hours, rate)
print(f"The pay for {hours} hours at a rate of {rate} is: {pay}")

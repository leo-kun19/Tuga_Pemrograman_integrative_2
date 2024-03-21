import datetime

def print_future_date(days):
    today = datetime.date.today()
    future_date = today + datetime.timedelta(days=days)
    print(future_date.strftime("%A, %B %d, %Y"))

if __name__ == "__main__":
    days = int(input("Enter number of days: "))
    print_future_date(days)

from datetime import datetime
now = datetime.now()
hour = now.strftime("%H")
ampm =now.strftime("%p")
##print(now)

from datetime import date
today = date.today()
datum = today.strftime("%Y_%m_%d_%p")

putanja = "/opt/utrace/BEER/" + datum + "/beoldcs1asvolsv/AIF_101.txt.0"

print(putanja)

def check_string(x):
    with open(putanja) as temp_f:
        datafile = temp_f.readlines()
    for line in datafile:
        if 'validated' in line:
            x = x + 1
    return(x)

brojac = check_string(0)
print ("Broj biltena je:", brojac)
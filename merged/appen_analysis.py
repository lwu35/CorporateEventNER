import pandas as pd
from collections import Counter
# import configparser

# config = configparser.ConfigParser()
# config.read('configg.ini')

df = pd.read_csv("full_86.csv")

ids = df.id.unique()
#print(ids)

#num_events = df[df.id==151].please_select_the_event_type.unique()

company_agg = []
date_agg = []
time_agg = []
event_agg = []
fy_agg = []
fp_agg = []
tz_agg = []


for i in ids:
    num_comps = df[df.id==i].copy_the_company_name_from_the_text.str.lower().unique()
    company_agg.append(len(num_comps))
    num_dates = df[df.id==i].enter_date_here_mmddyyyy.unique()
    date_agg.append(len(num_dates))
    num_times = df[df.id==i].enter_time_here_hhmm_pmam.unique()
    time_agg.append(len(num_times))
    num_events = df[df.id==i].please_select_the_event_type.unique()
    event_agg.append(len(num_events))
    num_fy = df[df.id==i].select_fiscal_year.unique()
    fy_agg.append(len(num_fy))
    num_fp = df[df.id==i].select_the_fiscal_period_check_as_many_as_it_applies.unique()
    fp_agg.append(len(num_fp))
    num_tz = df[df.id==i].select_timezone.unique()
    tz_agg.append(len(num_tz))



c = Counter(company_agg)
d = Counter(date_agg)
e = Counter(time_agg)
f = Counter(event_agg)
g = Counter(fy_agg)
h = Counter(fp_agg)
j = Counter(tz_agg)

print("Unique Rows:", len(company_agg))
print("Company Name agreement", [(i, c[i] / len(company_agg) * 100.0) for i, count in c.most_common()])
print("Date agreement", [(i, d[i] / len(date_agg) * 100.0) for i, count in d.most_common()])
print("Time agreement", [(i, e[i] / len(time_agg) * 100.0) for i, count in e.most_common()])
print("Event Type agreement", [(i, f[i] / len(event_agg) * 100.0) for i, count in f.most_common()])
print("Fiscal Year agreement", [(i, g[i] / len(fy_agg) * 100.0) for i, count in g.most_common()])
print("Fiscal Period agreement", [(i, h[i] / len(fp_agg) * 100.0) for i, count in h.most_common()])
print("Time Zone agreement", [(i, j[i] / len(tz_agg) * 100.0) for i, count in j.most_common()])

#take output of gpt3
#softmax into next layer, 12 values for month
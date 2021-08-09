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
num_ann = []

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
    num_ann.append(len(df[df.id==i]))

a_comp = []
a_date = []
a_time = []
a_event = []
a_fy= []
a_fp = []
a_tz = []    
for i in range (len(company_agg)):
    agrees_comp = - (int(num_ann[i]) // - int(company_agg[i])) #ceiling division
    a_comp.append(agrees_comp)

    agrees_date = - (int(num_ann[i]) // - int(date_agg[i])) 
    a_date.append(agrees_date)

    agrees_time = - (int(num_ann[i]) // - int(time_agg[i])) 
    a_time.append(agrees_time)

    agrees_event = - (int(num_ann[i]) // - int(event_agg[i])) 
    a_event.append(agrees_event)

    agrees_fy = - (int(num_ann[i]) // - int(fy_agg[i])) 
    a_fy.append(agrees_fy)

    agrees_fp = - (int(num_ann[i]) // - int(fp_agg[i])) 
    a_fp.append(agrees_fp)

    agrees_tz = - (int(num_ann[i]) // - int(tz_agg[i])) 
    a_tz.append(agrees_tz)


c = Counter(a_comp)
d = Counter(a_date)
e = Counter(a_time)
f = Counter(a_event)
g = Counter(a_fy)
h = Counter(a_fp)
j = Counter(a_tz)
k = Counter(num_ann)

print("Unique Rows:", len(company_agg))
print("Number of Annotators", [(i, k[i]) for i, count in k.most_common()])
print("Number of Annotators %", [(i, k[i] / len(num_ann) * 100.0) for i, count in k.most_common()],'\n')

print("Company Name agreement", c.most_common())
print("Company Name agreement %", [(i, c[i] / len(num_ann) * 100.0) for i, count in c.most_common()],'\n')

print("Date agreement", d.most_common())
print("Date agreement %", [(i, d[i] / len(num_ann) * 100.0) for i, count in d.most_common()],'\n')

print("Time agreement", e.most_common())
print("Time agreement %", [(i, e[i] / len(num_ann) * 100.0) for i, count in e.most_common()],'\n')

print("Event Type agreement", f.most_common())
print("Event Type agreement %", [(i, f[i] / len(num_ann) * 100.0) for i, count in f.most_common()],'\n')

print("Fiscal Year agreement", g.most_common())
print("Fiscal Year agreement %", [(i, g[i] / len(num_ann) * 100.0) for i, count in g.most_common()],'\n')

print("Fiscal Period agreement", h.most_common())
print("Fiscal Period agreement %", [(i, h[i] / len(num_ann) * 100.0) for i, count in h.most_common()],'\n')

print("Time Zone agreement", j.most_common())
print("Time Zone agreement %", [(i, j[i] / len(num_ann) * 100.0) for i, count in j.most_common()])
#print(a_comp)

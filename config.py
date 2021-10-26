# coding=utf-8

""" configuration """

from . import project_path

# home path 
home_path = project_path  
# data directory 
data_path = '{}/data'.format(home_path)
# temp data directory
temp_path = '{}/tmp'.format(home_path)

#
MIN_UNIT = 1e-7

# -----------------------------
#
# antico runtime parameters
#
# -----------------------------
date_format = '%Y-%m-%d'
datetime_format = '%Y-%m-%d %H:%M:%S'
# metric options {gini1, gini2, vc, kurt, skew}
metric = 'gini2'
# fusion options {mul, exp, sig}
fusion = 'mul' # 'sig'

# -----------------------------
#
# Testcase configure
#
# -----------------------------

# beginning date
start_date = '2020-09-01'
# ending date 
end_date   = '2020-10-31'
# time spans
time_spans = [30,31]
# 
time_window = sum(time_spans)

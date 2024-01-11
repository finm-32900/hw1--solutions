###########################
## Template



##########################
# Solution

from matplotlib import pyplot as plt
import pandas as pd
import load_merged_repo_data

start_date = "2014-08-22"
end_date = "2024-01-03"
df = load_merged_repo_data.load_all(start_date=start_date, end_date=end_date)

################
## Exercise 4.1
##
new_labels = {
    'REPO-TRI_AR_OO-P':'Tri-Party Overnight Average Rate',
    'RRPONTSYAWARD': 'ON-RRP facility rate',
    'Gen_IORB': 'Interest on Reserves', # This series uses FRED's Interest on 
    # Reserve Balances series. However, this doesn't go back very far, so it is
    # backfilled with interest on excess reserves when necessary.
}
##
df_norm = df.copy()
df['target_midpoint'] = (df['DFEDTARU'] + df['DFEDTARL'])/2
for s in ['DFEDTARU', 'DFEDTARL', 'REPO-TRI_AR_OO-P', 
          'EFFR', 'target_midpoint', 
          'Gen_IORB', 'RRPONTSYAWARD', 'SOFR']:
    df_norm[s] = df[s] - df['target_midpoint']
##
fig, ax = plt.subplots()
date_start = '2014-Aug'
date_end = '2019-Dec'
_df = df_norm.loc[date_start:date_end, :]
ax.fill_between(_df.index, _df['DFEDTARU'], _df['DFEDTARL'], alpha=0.2)
_df[['REPO-TRI_AR_OO-P', 'EFFR']].rename(columns=new_labels).plot(ax=ax)
plt.ylim(-0.4, 1.0)
plt.ylabel("Spread of federal feds target midpoint (percent)")
arrowprops = dict( 
    arrowstyle = "->"
)
ax.annotate('Sep. 17, 2019: 3.06%', 
            xy=('2019-Sep-17', 0.95), 
            xytext=('2017-Oct-27', 0.9),
            arrowprops = arrowprops);
i_replicated_figure_1 = True


## Exercise 4.2
df['is_tri_above_fed_upper'] = df['REPO-TRI_AR_OO-P'] > df['DFEDTARU']
spike_dates = df.index[df['is_tri_above_fed_upper']]



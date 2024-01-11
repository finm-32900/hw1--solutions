import pandas as pd

import load_fred
import load_ofr_api_data

# # ################################################
# # ## Template
# series_descriptions ={}

# def load_all(start_date="2014-08-22", end_date="2024-01-03", normalize_timing=True):
#     """Merge the data sets created in load_fred and load_ofr_api_data
#     """    
#     df = pd.DataFrame()

#     # The following is useful for replication of the Kahn et al. (2023)
#     # if normalize_timing:
#     #     # Normalize end-of-day vs start-of-day difference
#     #     df.loc['2016-12-14', ['DFEDTARU', 'DFEDTARL']] = df.loc['2016-12-13', ['DFEDTARU', 'DFEDTARL']]
#     #     df.loc['2015-12-16', ['DFEDTARU', 'DFEDTARL']] = df.loc['2015-12-15', ['DFEDTARU', 'DFEDTARL']]

#     return df



###############################################
# Solutions

def load_all(start_date="2014-08-22", end_date="2024-01-03", normalize_timing=True):
    df_fred = load_fred.pull_fred_repo_data(start_date, end_date)
    df_ofr = load_ofr_api_data.pull_repo_data(start_date, end_date)
    
    df = pd.concat([df_fred, df_ofr], axis=1)
    if normalize_timing:
        # Normalize end-of-day vs start-of-day difference
        df.loc['2016-12-14', ['DFEDTARU', 'DFEDTARL']] = df.loc['2016-12-13', ['DFEDTARU', 'DFEDTARL']]
        df.loc['2015-12-16', ['DFEDTARU', 'DFEDTARL']] = df.loc['2015-12-15', ['DFEDTARU', 'DFEDTARL']]
    return df

_descriptions_1 = load_fred.series_descriptions
_descriptions = load_ofr_api_data.series_descriptions
series_descriptions = {
    **_descriptions_1, 
    **_descriptions,
    }

if __name__ == "__main__":
    pass
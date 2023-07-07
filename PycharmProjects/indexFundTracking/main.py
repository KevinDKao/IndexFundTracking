import pandas as pd
import os
import yfinance as yf
from datetime import datetime

domestic_index_funds = ['FXAIX', 'FSMAX', 'FSPGX','FLCOX','FSMDX','FMDGX','FIMVX','FSSNX','FECGX','FISVX','FITLX','FSKAX','FZROX','FNILX','FZIPX'] # List of index funds
international_index_funds = ['FPADX','FSGGX','FSPSX','FNIDX','FTIHX','FZILX']
ficc_index_funds = ['FBIIX','FMBIX','FIPDX','FUAMX','FNBGX','FUMBX','FXNAX','FNSOX','FNDSX']
specialty_index_funds = ['FSRNX','FNCMX','FFNOX']

large_value_mutual_funds = ['FBCVX','FLVEX','FSLVX','FVDFX']
small_mid_value_mutual_funds = ['FLPSX','FSMVX','FDVLX','FSLSX','FCPVX']
income_oriented_mutual_funds = ['FEQTX','FEQIX','FGRIX','FDGFX']
large_blend_mutual_funds = ['FEQHX','FSEBX','FULVX','FDEQX','FLCEX','FLCSX','FGRTX']
small_mid_blend_mutual_funds = ['FMEIX','FCPEX','FSLCX','FDSCX','FSCRX','FMCSX']
go_anywhere_mutual_funds = ['FDCAX','FCNTX','FMAGX','FMILX']
large_growth_mutual_funds = ['FBGRX','FEXPX','FTQGX','FFIDX','FDSVX','FDGRX','FLGEX','FOCPX','FDSSX','FTRNX']
small_mid_growth_mutual_funds = ['FDEGX','FSSMX','FCPGX']
diversifiers_mutual_funds = ['FWOMX','FIFNX','FLVCX']

all_index = domestic_index_funds + international_index_funds + ficc_index_funds + specialty_index_funds
all_mutual_funds = large_value_mutual_funds + small_mid_value_mutual_funds + income_oriented_mutual_funds + large_blend_mutual_funds + small_mid_blend_mutual_funds + go_anywhere_mutual_funds + large_growth_mutual_funds + small_mid_growth_mutual_funds + diversifiers_mutual_funds

def printPercentageReturns(fund_list):
    for fund in fund_list:
        index_fund_data = yf.download(fund, start=start_date, end=end_date, progress = False)
        initial_price = index_fund_data['Close'][0]  # Closing price on start_date
        current_price = index_fund_data['Close'][-1]  # Last available closing price
        percentage_return = (current_price - initial_price) / initial_price * 100
        print(f"{fund} percentage return from {start_date} to {end_date}: {percentage_return:.2f}%")

if __name__ == '__main__':
    start_date = datetime(2020, 1, 1)
    end_date = datetime.now()

    print('Index Fund Analysis')
    printPercentageReturns(all_index)

    print('All Mutual Funds Analysis')
    printPercentageReturns(all_mutual_funds)

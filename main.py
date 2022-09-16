import yfinance as yf
import winsound
import pandas as pd
import datetime
import pyautogui
import matplotlib.pyplot as plt
import time
'''new_stock_list=[]
for i in range(len(stock_listB)):
    print(i)
    new_stock_list.append(stock_listB[i])
    new_stock_list.append(stock_listB[i])
print(new_stock_list)'''
#stock list has to have duplicates in order for the program can extract min , max prices on a time scale
stock_listb =   ['didiy', 'didiy', 'open', 'open', 'BWV', 'BWV', 'GOVX', 'GOVX', 'TEVA', 'TEVA',
                 'SNAP', 'SNAP', 'CCL', 'CCL', 'LABU', 'LABU', 'FXLV', 'FXLV', 'FFIE', 'FFIE', 'CS', 'CS',
                 'TLRY', 'TLRY', 'ITUB', 'ITUB', 'PLTR', 'PLTR', 'NOK', 'NOK', 'ABEV', 'ABEV', 'RIOT', 'RIOT',
                 'BBD', 'BBD', 'NLY', 'NLY', 'FNGU', 'FNGU', 'CMRX', 'CMRX', 'HLN', 'HLN', 'SWN', 'SWN', 'NU', 'NU',
                 'NYCB', 'NYCB', 'AUPH', 'AUPH', 'OPEN', 'OPEN', 'GRAB', 'GRAB', 'SOFI', 'SOFI', 'GGB', 'GGB',
                 'HUT', 'HUT', 'SDIG', 'SDIG', 'TAL', 'TAL', 'AUY', 'AUY', 'TBLT', 'TBLT', 'VTRS', 'VTRS',
                 'DNA', 'DNA', 'UEC', 'UEC', 'UMC', 'UMC', 'NVTA', 'NVTA', 'DB', 'DB', 'COMM', 'COMM', 'SNDL', 'SNDL',
                 'KGC', 'KGC', 'PTON', 'PTON', 'FCEL', 'FCEL', 'LYG', 'LYG', 'BULZ', 'BULZ', 'YMM', 'YMM',
                 'CPG', 'CPG', 'FUBO', 'FUBO', 'SIRI', 'SIRI', 'HLX', 'HLX', 'VNET', 'VNET', 'ACHR', 'ACHR',
                 'SID', 'SID', 'RIG', 'RIG', 'LU', 'LU', 'WE', 'WE', 'BCS', 'BCS', 'CIG', 'CIG', 'BTG', 'BTG',
                 'TELL', 'TELL', 'GEVO', 'GEVO', 'BBBY', 'BBBY', 'CMRA', 'CMRA', 'TME', 'TME', 'IQ', 'IQ',
                 'FTCH', 'FTCH', 'AERC', 'AERC', 'CGC', 'CGC', 'AM', 'AM', 'WTI', 'WTI', 'EVTL', 'EVTL',
                 'JBLU', 'JBLU', 'HOOD', 'HOOD', 'GFI', 'GFI', 'FRO', 'FRO', 'DM', 'DM', 'AMRS', 'AMRS',
                 'UAA', 'UAA', 'NKLA', 'NKLA', 'AMTD', 'AMTD', 'SRNE', 'SRNE', 'GOEV', 'GOEV', 'NEX', 'NEX',
                 'ARVL', 'ARVL', 'AGEN', 'AGEN', 'KOS', 'KOS', 'CLVS', 'CLVS', 'AG', 'AG', 'HL', 'HL', 'STNE', 'STNE',
                 'IS', 'IS', 'GDXU', 'GDXU', 'REAL', 'REAL', 'CUK', 'CUK', 'GPS', 'GPS', 'MNSO', 'MNSO',
                 'APLD', 'APLD', 'IAG', 'IAG', 'VIPS', 'VIPS', 'ORC', 'ORC', 'ETHE', 'ETHE', 'BB', 'BB',
                 'CORZ', 'CORZ', 'NEO', 'NEO', 'SPCE', 'SPCE', 'VLD', 'VLD', 'RIDE', 'RIDE', 'WEBL', 'WEBL',
                 'ERIC', 'ERIC', 'FSM', 'FSM', 'EOSE', 'EOSE', 'ZY', 'ZY', 'PSLV', 'PSLV', 'OPK', 'OPK',
                 'SABR', 'SABR', 'BLDP', 'BLDP', 'PAYO', 'PAYO', 'LAZR', 'LAZR', 'NN', 'NN', 'BNGO', 'BNGO',
                 'UUUU', 'UUUU', 'OCGN', 'OCGN', 'AUR', 'AUR',  'PZN', 'PZN', 'FRGT', 'FRGT',
                 'RES', 'RES', 'UA', 'UA', 'WKHS', 'WKHS', 'ICL', 'ICL', 'IMGN', 'IMGN', 'INO', 'INO', 'FTI', 'FTI',
                 'ASX', 'ASX', 'MNKD', 'MNKD', 'MQ', 'MQ', 'XXII', 'XXII', 'EGO', 'EGO', 'NXE', 'NXE', 'BLND', 'BLND',
                 'BTBT', 'BTBT', 'PACB', 'PACB', 'SAN', 'SAN', 'AEG', 'AEG', 'ALVR', 'ALVR', 'USOI', 'USOI',
                 'MVIS', 'MVIS', 'BHC', 'BHC', 'CLOV', 'CLOV','clvs','clvs','sunw','sunw']

stock_listB = ['didiy', 'bbby', 'open', 'BWV', 'GOVX', 'TEVA', 'SNAP', 'CCL', 'LABU', 'FXLV', 'FFIE', 'CS', 'TLRY',
               'ITUB','PLTR', 'NOK', 'ABEV', 'RIOT', 'BBD', 'NLY', 'FNGU', 'CMRX', 'HLN', 'SWN', 'NU', 'NYCB',
               'AUPH', 'OPEN', 'GRAB', 'SOFI', 'GGB', 'HUT', 'SDIG', 'TAL', 'AUY', 'TBLT', 'VTRS', 'DNA',
               'UEC', 'UMC', 'NVTA', 'DB', 'COMM', 'SNDL', 'KGC', 'PTON', 'FCEL', 'LYG', 'BULZ', 'YMM', 'CPG',
               'FUBO', 'SIRI', 'HLX', 'VNET', 'ACHR', 'SID', 'RIG', 'LU', 'WE', 'BCS', 'CIG',
               'BTG', 'TELL', 'GEVO', 'BBBY', 'CMRA', 'TME', 'IQ', 'FTCH', 'AERC', 'CGC', 'AM',
               'WTI', 'EVTL', 'JBLU', 'HOOD', 'GFI', 'FRO', 'DM', 'AMRS', 'UAA', 'NKLA', 'AMTD',
               'SRNE', 'GOEV', 'NEX', 'ARVL', 'AGEN', 'KOS', 'CLVS', 'AG', 'HL', 'STNE', 'IS', 'GDXU', 'REAL',
               'CUK', 'GPS', 'MNSO', 'APLD', 'IAG', 'VIPS', 'ORC', 'ETHE', 'BB', 'CORZ', 'NEO',
               'SPCE', 'VLD', 'RIDE', 'WEBL', 'ERIC', 'FSM', 'EOSE', 'ZY', 'PSLV', 'OPK', 'SABR', 'BLDP',
               'PAYO', 'LAZR', 'NN', 'BNGO', 'UUUU', 'OCGN', 'AUR', 'CDEV', 'PZN', 'FRGT', 'RES', 'UA',
               'WKHS', 'ICL', 'IMGN', 'INO', 'FTI', 'ASX', 'MNKD', 'MQ', 'XXII', 'EGO', 'NXE', 'BLND',
               'BTBT', 'PACB', 'SAN', 'AEG', 'ALVR', 'USOI', 'MVIS', 'BHC', 'CLOV']
#
'''bought_stocks={'alna': 1}
completed_sales={}
#scoop_up_price={}
for item in stock_listB:
    #bought_stocks[item]=0
    completed_sales[item]= 0
    #scoop_up_price[item]=0'''
priced_low_stocks={}
for item in stock_listb:
    priced_low_stocks[item]=0
print('priced low stocks  ',priced_low_stocks)
cleaned_near_low_stock_list=[]
near_low_stock_list=[]
stock_litsd=[]
price_price=[]
max_price=0
max_peek_price=0
min_price=1000
min_peek_price=1000
while True:
    for stock in stock_listb:

        try:
            df = yf.download(stock, period='5d', interval='5m')  # start_date, end_date, interval = "1h")
        except:

            print('data download failure')
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # print(df)
        df["ma100"] = df['Close'].rolling(100).mean()
        df100_sma = df['ma100'][-1]
        df['ma50'] = df['Close'].rolling(50).mean()
        df50_sma = df['ma50'][-1]

        time.sleep(4.5)
        df = df.dropna()

        print(stock)
        print('len df ',len(df))
        #last_data = df['Close'][-1]
        #print(f'last data   {last_data:.5f}')

        count = 0
        for i in range(-len(df), -1, 1):  # goes threw list of stock prices
            #print(f'i  {df["Close"][i]:.6f}')
            #print(f'i-1  {df["Close"][-1]:.6f}')


            price_price.append(df['Close'][i])#creates alist

            if max_peek_price==df['Close'][i]:#looks for max price
                print(' max i  ',i)
            if min_peek_price==df['Close'][i]:#looks for min price
                print('min i  ',i)

                if i > -100 and priced_low_stocks[stock]==0:#finds lowest price in the last 100 5 minutes time steps
                        print(f'stock {stock} it worked')
                        priced_low_stocks[stock] = 1
                        winsound.Beep(1000,300)
                        near_low_stock_list.append(stock) #appends to near low stock lists
                cleaned_near_low_stock_list=[*set(near_low_stock_list)]# corrects for duplicates in stock list

                #low_close=df['Close'][i-1]
                '''# Python 3 code to demonstrate
                    # removing duplicate elements from the list
                    l = [1, 2, 4, 2, 1, 4, 5]
                    print("Original List: ", l)
                    res = [*set(l)]
                    print("List after removing duplicate elements: ", res)'''


                #print(f'lowest point  {df["Close"][i]:.3f}')



                time.sleep(.1)

        try:
            print('price price ',price_price)
            print('max price ',max(price_price))# finds  max price in list
            max_peek_price=max(price_price)
            print('min price ',min(price_price))#finds min price in list
            min_peek_price=min(price_price)
            price_price.clear() #clears list so no duplicates live there

            print(f'cleaned near low stock price  {cleaned_near_low_stock_list} ')
            print(f'stock near low price  {priced_low_stocks}')
        except:
            print('empty value')
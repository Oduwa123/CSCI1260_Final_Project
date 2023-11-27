#! pyton3
#Import needed modules 
import numpy as np
import pandas as pd
import io
import openpyxl
import xlrd
import matplotlib.pyplot as plt


def analyzeCOT():

    #  get data for excel into pandas dataframe
    df = pd.read_excel(r'.\data\Forexdata3.xlsx')

    # update date to datetime format
    df['Date'] =pd.to_datetime(df['Date'])

    # Sort the data by Futures and Date
    df = df.sort_values(by = ['Futures','Date'], ascending=[True,False])

    # Calculate the week by week changes in long
    df['Change_in_long'] = df['long'] - df.groupby(['Futures'])['long'].shift(-1)

    # Calculate the week by week changes in short
    df['Change_in_short'] = df['short'] - df.groupby(['Futures'])['short'].shift(-1)

    # Find the over all percentage of long
    df['Percentage_of_long'] = ((df['long']/ (df['long'] + df['short']) ) * 100).round()
    df['Percentage_of_long'] = df['Percentage_of_long'].astype(str) +'%'

    # Find the overall percentage of short
    df['Percentage_of_short'] = ((df['short']/ (df['long'] + df['short'])) * 100).round()
    df['Percentage_of_short'] = df['Percentage_of_short'].astype(str) +'%'

    # Get the net position of the currency
    df['Net_Position'] = df['long'] - df['short']

    return df


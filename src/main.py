import numpy as np
import pandas as pd
import seaborn as sns

import clean as cl

def readyUpDate(df):
    columns_to_drop_2 = ["Case Number", "Date", "Time", "datetime", "Year"]

    df = cl.cleanYear(df, 1900)
    df = cl.cleanDate(df)
    df = cl.changeDateType(df)
    df = cl.addMonthCol(df)
    df = cl.addYearCol(df)
    df = cl.reorderColumn(df, column="year", position=0)
    df = cl.reorderColumn(df, column="month", position=1)
    df = cl.dropColumns(df, columns_to_drop_2)

    return df


def main():
    attacks_raw = pd.read_csv("data/attacks.csv", encoding='unicode_escape')

    columns_to_rename = {'Sex ': 'Sex',
                         'Species ': 'Species',
                         'Fatal (Y/N)': 'Fatal'}
    columns_to_drop = ["pdf", "Investigator or Source", "href formula", "href", "Case Number.1", 
                       "Case Number.2", "original order", "Unnamed: 22", "Unnamed: 23", "Injury", "Name"]

    attacks_raw = cl.renameColumns(attacks_raw, columns_to_rename)
    attacks_raw = cl.dropColumns(attacks_raw, columns_to_drop)
    attacks_raw = cl.dropRows(attacks_raw)
    
    attacks_raw = readyUpDate(attacks_raw)

    attacks_raw = cl.cleanType(attacks_raw)
    attacks_raw = cl.upperCountry(attacks_raw)
    attacks_raw = cl.cleanActivities(attacks_raw)

    attacks_raw = cl.cleanSex(attacks_raw)
    attacks_raw = cl.cleanAge(attacks_raw)
    attacks_raw = cl.changeAgeType(attacks_raw)

    attacks_raw = cl.cleanFatal(attacks_raw)
    attacks_raw = cl.changeFatalType(attacks_raw)
    attacks_raw = cl.cleanSpecies(attacks_raw)

    attacks_raw.to_csv("data/attacks_clean.csv", index = False, encoding='unicode_escape')


if __name__ == "__main__":
    main()
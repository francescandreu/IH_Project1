import numpy as np
import pandas as pd
import seaborn as sns


# ------------------------------------------ STRUCTURAL ------------------------------------------
# Rename columns to easier handled versions
def renameColumns(df, dict_columns):
    df.rename(columns=dict_columns, inplace=True, errors='raise')
    return df

# Drop columns of information not valuable to study
def dropColumns(df, cols):
    df.drop(columns=cols, inplace=True)
    return df

# Clear dataset of rows with at least three values as NA
def dropRows(df):
    df.dropna(how="all", inplace=True)
    df.dropna(thresh=6, inplace=True)
    return df

# Given df, column and position, reorder given column into new position
def reorderColumn(df, column, position):
    col = df.pop(column)
    df.insert(position, col.name, col)
    return df


# ------------------------------------------ DATE ------------------------------------------
# Clear dataset of rows where Year is before given year, when no year given or bad data
def cleanYear(df, year):
    df.drop(df[df.Year < year].index, inplace=True)
    return df[df.Year.notna()]

# Clean Date column to dateformat and drop other date related columns
def cleanDate(df):
    df['Date'] = df['Date'].str.extract('(\d{2}-\w{3}-\d{4})')
    return df[df['Date'].notna()]

# Change Data type from objecto to datetime64
def changeDateType(df):
    df['datetime'] = pd.to_datetime(df['Date'], format='%d-%b-%Y')
    return df

def addMonthCol(df):
    df['month'] = pd.DatetimeIndex(df['datetime']).month
    return df

def addYearCol(df):
    df['year'] = pd.DatetimeIndex(df['datetime']).year
    return df


# ------------------------------------------ TYPE ------------------------------------------
# Clean Type column to have similar values and drop invalids
def cleanType(df):
    df.Type.replace('Boatomg', 'Boat', inplace=True)
    df.Type.replace('Boating', 'Boat', inplace=True)
    df.drop(df[df.Type == 'Invalid'].index, inplace=True)
    return df

# ------------------------------------------ COUNTRY ------------------------------------------
# Upper case all countries
def upperCountry(df):
    df['Country'] = df['Country'].str.upper()
    return df

# ------------------------------------------ ACTIVITY ------------------------------------------
# Clean Activities
def cleanActivities(df):
    df.Activity = df.Activity.str.lower()
    df.Activity = df.Activity.str.strip()

    activities_to_clean = [['surf','surfing'], ['board','surfing'], ['fish','fishing'], ['swim','swimming'], ['diving','diving'], 
                        ['boat','boat'], ['float', 'floating'], ['bath','bathing'], ['snork','snorkeling'], ['jump','jumping'], ['sail', 'boat'], 
                        ['row','rowing sports'], ['kayak', 'rowing sports'], ['canoeing','rowing sports'], ['padd','rowing sports'],
                        ['stand','standing'], ['drift', 'drifting'], ['tread','treading'], ['disaster', 'shipwreck'], ['feed','feeding sharks'],
                        ['sank','shipwreck'], ['sit','sitting'], ['walk','walking'], ['sink','shipwreck'], ['film','filming']]
    for match, new in activities_to_clean:
        df.Activity = df.Activity.str.replace('(^.*'+match+'.*$)', new, regex = True)
    popular_activities = df.Activity.value_counts()[0:20].index.tolist()
    df.loc[~df["Activity"].isin(popular_activities), "Activity"] = "other"
    return df

# ------------------------------------------ SEX ------------------------------------------
# Clean Sex
def cleanSex(df):
    df.Sex = df.Sex.str.strip()
    df.Sex.replace('lli', 'M', inplace=True)
    df.Sex.replace('N', np.nan, inplace=True)
    df.Sex.replace('.', np.nan, inplace=True)
    return df

# ------------------------------------------ AGE ------------------------------------------
# Clean Age
def cleanAge(df):
    df.Age = df.Age.str.strip()
    df.Age = df.Age.str.extract('(\d{1,2})')
    return df

# Change Age type to Int64
def changeAgeType(df):
    df.Age = pd.to_numeric(df.Age)
    df.Age = df.Age.astype('Int64')    
    return df

# ------------------------------------------ FATAL ------------------------------------------
# Clean Fatal
def cleanFatal(df):
    df.Fatal.replace('UNKNOWN', np.nan, inplace=True)
    df.Fatal.replace('2017', np.nan, inplace=True)
    df.Fatal.replace(' N', np.nan, inplace=True)
    df.Fatal.replace('M', np.nan, inplace=True)
    return df

# Change Fatal type to bool
def changeFatalType(df):
    df.loc[(df.Fatal == 'Y'),'Fatal']=True
    df.loc[(df.Fatal == 'N'),'Fatal']=False

    df['Fatal'] = df['Fatal'].astype('bool')
    return df

# ------------------------------------------ SPECIES ------------------------------------------
# Clean Species
def cleanSpecies(df):
    df.Species = df.Species.str.lower()
    df.Species = df.Species.str.strip()
    species_to_clean = [['white','white'], ['tiger','tiger'], ['lemon','lemon'], ['bull','bull'], ['grey reef','grey reef'], ['reef','reef'],
                        ['wobbegong','wobbegong'], ['black','blacktip'], ['galapagos', 'galapagos'], ['nurse','nurse'], ['catshark','cat'],
                        ['cookie','cookiecutter'], ['spinner','spinner'], ['blue','blue'], ['caribbean reef','caribbean reef'],
                        ['smooth hound','smooth hound'], ['sevengill','sevengill'], ['seven-gill','sevengill'], ['angel','angel'], ['copper','copper'],
                        ['dogfish','dogfish'], ['mako','mako'], ['bronze whale','copper'], ['hammerhead','hammerhead'], ['raggedtooth', 'raggedtooth'], 
                        ['goblin', 'goblin'], ['silky', 'silky'], ['sandbar','sandbar'], ['sand shark','raggedtooth'], ['porbeagle','porbeagle'],
                        ['7-gill','sevengill'], ['salmon','salmon'], ['zambesi','zambesi'], ['thresher','thresher'], ['spurdog','spurdog'],
                        ['dusky','dusky'], ['basking','basking'], ['whale','whale'], ['soupfin','soupfin'], ['zambezi','zambezi'], ['carpet','carpet'],
                        ['bonita','bonita'], ['leopard','leopard'], ['shovelnose','shovelnose'], ['leucas','bull'], 
                        ['limbatus', 'blacktip'], ['sting','unknown'], ['shark','unknown'], ['unident','unknown']]
    for match, new in species_to_clean:
        df.Species = df.Species.str.replace('(^.*'+match+'.*$)', new, regex = True)
    df.Species = df.Species.str.replace('(^.*\d.*$)', 'unknown', regex = True)
    df.Species = df.Species.fillna('unknown')
    return df
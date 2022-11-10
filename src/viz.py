import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def configStyle():
    sns.set(style="darkgrid")
    return True

def plotFatal(df):
    plt.figure(figsize = (15,2))
    fatal = sns.countplot(data=df, y='Fatal')
    fatal.set_yticklabels(["Injured", "Fatal"])
    fatal.set(xlabel='Attacks', ylabel='')
    plt.savefig('../images/fatalvsinjured.png')

def plotType(df):
    plt.figure(figsize = (15,2))
    type_sex = sns.countplot(data=df, y="Type")
    type_sex.set(xlabel='Attacks', ylabel='Type')
    plt.savefig('../images/type.png')

def plotSex(df):
    plt.figure(figsize = (15,2))
    sex = sns.countplot(data=df, y='Sex')
    sex.set(xlabel='Attacks', ylabel='')
    sex.set_yticklabels(["Female", "Male"])
    plt.savefig('../images/sex.png')

def plotSexFatal(df):
    plt.figure(figsize = (15,2))
    fatal_sex = sns.countplot(data=df, y="Sex", hue="Fatal")
    fatal_sex.set_yticklabels(["Female", "Male"])
    fatal_sex.set(xlabel='Attacks', ylabel='')
    plt.savefig('../images/sexfatal.png')

def plotSexType(df):
    plt.figure(figsize = (15,2))
    type_sex = sns.countplot(data=df, y="Sex", hue="Type")
    type_sex.set_yticklabels(["Female", "Male"])
    type_sex.set(xlabel='Attacks', ylabel='')
    plt.savefig('../images/sextype.png')

def plotAge(df):
    plt.figure(figsize = (15,4))
    age = sns.histplot(data=df, x='Age', kde=True, bins=82)
    age.set(xlabel='Age', ylabel='Attacks')
    plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80], ['0','10','20','30','40','50','60','70','80'])
    plt.savefig('../images/age.png')

def plotCountries(df):
    fig, ax = plt.subplots(1,2)
    fig.set_figheight(5)
    fig.set_figwidth(15)
    p1 = sns.countplot(data=df, x='Country', order=pd.value_counts(df['Country']).iloc[:3].index, ax = ax[0])
    p2 = sns.countplot(data=df, x='Country', order=pd.value_counts(df['Country']).iloc[3:10].index, ax = ax[1])
    plt.setp(p1.get_xticklabels(), rotation=0)
    p1.set(xlabel='Top 3 Countries', ylabel='Attacks')
    plt.setp(p2.get_xticklabels(), rotation=45)
    p2.set(xlabel='', ylabel='')
    plt.savefig('../images/topcountries.png')

def plotRegionTopCountries(df):
    sub_usa = pd.DataFrame()
    sub_usa["Area"] = df.loc[df["Country"] == 'USA'].Area

    sub_aus = pd.DataFrame()
    sub_aus["Area"] = df.loc[df["Country"] == 'AUSTRALIA'].Area

    sub_sa = pd.DataFrame()
    sub_sa["Area"] = df.loc[df["Country"] == 'SOUTH AFRICA'].Area

    fig, ax = plt.subplots(3,1, sharex=True)
    fig.set_figheight(10)
    fig.set_figwidth(15)

    a1 = sns.countplot(y=sub_usa["Area"], order=sub_usa.Area.value_counts().iloc[:8].index, ax=ax[0])
    a2 = sns.countplot(y=sub_aus["Area"], order=sub_aus.Area.value_counts().iloc[:8].index,ax=ax[1])
    a3 = sns.countplot(y=sub_sa["Area"], order=sub_sa.Area.value_counts().iloc[:3].index,ax=ax[2])

    a1.set(xlabel='', ylabel='USA')
    a2.set(xlabel='', ylabel='Australia')
    a3.set(xlabel='Attacks', ylabel='South Africa')
    plt.savefig('../images/top3areas.png')

def plotYearsAndMonths(df):
    fig, ax = plt.subplots(1,2)
    fig.set_figheight(5)
    fig.set_figwidth(15)

    year = sns.countplot(data=df, x='year', ax=ax[0])
    year.set_xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 118])
    plt.setp(year.get_xticklabels(), rotation=45)
    year.set(xlabel='Years', ylabel='Attacks')

    month = sns.countplot(data=df, x='month', ax=ax[1])
    plt.setp(month.get_xticklabels(), rotation=0)
    month.set(xlabel='Months', ylabel='')
    plt.savefig('../images/historic.png')

def plotSpecies(df):
    plt.figure(figsize = (15,6))
    sharks = sns.countplot(y=df["Species"], order=df.Species.value_counts().iloc[1:20].index)
    sharks.set(xlabel='Attacks', ylabel='Species')
    plt.savefig('../images/species.png')

def plotSpeciesFatal(df):
    plt.figure(figsize = (15,6))
    fatal_species = sns.countplot(data=df, y="Species", hue="Fatal", order=df.Species.value_counts().iloc[1:11].index)
    fatal_species.set(xlabel='Attacks', ylabel='Species')
    plt.savefig('../images/speciesfatal.png')

def plotHistSpeciesFatal(df):
    plt.figure(figsize = (15,6))
    p = sns.histplot(data=df, x='year', y='Species', hue='Fatal')
    plt.savefig('../images/histspeciesfatal.png')

def plotHistSpeciesActivityFatal(df):
    plt.figure(figsize = (15,6))
    activity_species = sns.histplot(data=df, x='Activity', y='Species', hue='Fatal')
    plt.setp(activity_species.get_xticklabels(), rotation=45)
    plt.savefig('../images/speciesactivityfatal.png')

def plotAttacksActivity(df):
    plt.figure(figsize = (15,6))
    sns.countplot(y=df["Activity"], order=df.Activity.value_counts().iloc[0:20].index)
    plt.savefig('../images/attacksactivity.png')

def plotActivityYear(df):
    plt.figure(figsize = (15,6))
    sns.histplot(data=df, x='year', y='Activity')
    plt.savefig('../images/activityYear.png')

def plotActivityFatality(df):
    plt.figure(figsize = (15,6))
    sns.histplot(data=df, x='year', y='Activity', hue='Fatal')
    plt.savefig('../images/activityfatal.png')
from os import read
import nltk
import re
import numpy as np
import pandas as pd
from pandas.io.parsers import read_csv
from tkinter import *
import regex

def load_datasets():
    CHILDES = read_csv("C:/Users/AzF/unit analysis/childes.csv")
    compound_df = read_csv("C:/Users/AzF/unit analysis/compound_df.csv")
    return CHILDES,compound_df

def subset_datasets(CHILDES):
    CHILDES_utterances = CHILDES['stem'].str.lower()


    return CHILDES_utterances


def modify_df(compound_df):
    mod_compund_df = compound_df[['index','original','category','replacement']]
   
    return mod_compund_df

def categories(mod_compund_df):
    categoties = mod_compund_df["category"]
    unique_categories = categoties.unique()
    
    return unique_categories

def word_replace(mod_compund_df,CHILDES_utterances):
    #keep only words with replacement
    mod_compund_df = mod_compund_df.dropna()
    replace_dict = dict(zip(mod_compund_df.original, mod_compund_df.replacement))
    replaced_CHILDES = CHILDES_utterances.replace(replace_dict, regex = True)
    replaced_CHILDES.to_csv('C:/Users/AzF/unit analysis/replaced_childes.csv')

    return replace_dict , replaced_CHILDES

def main():
    CHILDES,compound_df=load_datasets()
    # compound_df = import_datasets()
    # mod_compund_df = modify_df(compound_df)
    # unique_categories = categories(mod_compund_df)
    # word_replace(mod_compund_df,CHILDES_utterances)


main()
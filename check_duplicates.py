import pandas as pd
import numpy as np
import re
import os


def return_non_duplicates(df):
    sample_size = 4
    df["DUPLICATED"] = df.duplicated(subset='CONTROL', keep='first')
    # First, find controls for patients whose controls are not duplicated.
    not_duplicated = df[df.DUPLICATED == False]
    patient_not_duplicated_count = not_duplicated.groupby('PATIENT')['CONTROL'].nunique().reset_index()

    not_duplicated_more_than_4 = not_duplicated[
        not_duplicated.PATIENT.isin(patient_not_duplicated_count[patient_not_duplicated_count.CONTROL >= sample_size].PATIENT)]

    not_duplicated_sample4 = not_duplicated_more_than_4.groupby("PATIENT").sample(n=sample_size)
    patients_left_over = df[~df.PATIENT.isin(not_duplicated_sample4.PATIENT)&~df.CONTROL.isin(not_duplicated_sample4.CONTROL)]

    return(not_duplicated_sample4, patients_left_over)

csv_filenamea = '/Users/amb538_1/Downloads/R3_4034_MAZUL_20_ALL_FIELDS_MORE_RANDOM_2024_01_04.csv'

csv_filenameb = '/Users/amb538_1/Downloads/R3_4034_MAZUL_20_ALL_FIELDS_2024_01_03.csv'
dfa = pd.read_csv(csv_filenamea)
dfb = pd.read_csv(csv_filenameb)
df=pd.concat([dfa, dfb])
df.nunique()
not_duplicated_sample4_round1, patients_left_over_r1 = return_non_duplicates(df)
not_duplicated_sample4_round2, patients_left_over_r2 = return_non_duplicates(patients_left_over_r1)
not_duplicated_sample4_round3, patients_left_over_r3 = return_non_duplicates(patients_left_over_r2)
not_duplicated_sample4_round4, patients_left_over_r4 = return_non_duplicates(patients_left_over_r3)
not_duplicated_sample4_round5, patients_left_over_r5 = return_non_duplicates(patients_left_over_r4)
not_duplicated_sample4_round6, patients_left_over_r6 = return_non_duplicates(patients_left_over_r5)
not_duplicated_sample4_round7, patients_left_over_r7 = return_non_duplicates(patients_left_over_r6)
not_duplicated_sample4_round8, patients_left_over_r8 = return_non_duplicates(patients_left_over_r7)
not_duplicated_sample4_round9, patients_left_over_r9 = return_non_duplicates(patients_left_over_r8)
not_duplicated_sample4_round10, patients_left_over_r10 = return_non_duplicates(patients_left_over_r9)
not_duplicated_sample4_round11, patients_left_over_r11 = return_non_duplicates(patients_left_over_r10)
not_duplicated_sample4_round12, patients_left_over_r12 = return_non_duplicates(patients_left_over_r11)
not_duplicated_sample4_round13, patients_left_over_r13 = return_non_duplicates(patients_left_over_r12)
not_duplicated_sample4_round14, patients_left_over_r14 = return_non_duplicates(patients_left_over_r13)
#4556 patients total



#First, find controls for patients whose controls are not duplicated.
All_not_duplicated = pd.concat([not_duplicated_sample4_round1,not_duplicated_sample4_round2,not_duplicated_sample4_round3,not_duplicated_sample4_round4, not_duplicated_sample4_round5])

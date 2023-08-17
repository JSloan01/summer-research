import pandas as pd

# Selecting the variables we want from each set of files (note that not every set has been used here)

Var_Behaviour = ['CB68_ACDMC_SCIENCE', 'CB68_ACDMC_LANG', 'CB68_ACDMC_MATH', 'CB68_ACDMC_HIST',
                        'SA_TSCORE', 'GA_TSCORE', 'P_TSCORE', 'SP_TSCORE', 'D_TSCORE', 'ANXIETYTOTAL', 'ANXDEPTOTAL']

Var_Cognitive = ['S0B_TGT_ACCURACY', 'S0B_NONTGT_ACCURACY', 'S1B_TGT_ACCURACY', 'S1B_NONTGT_ACCURACY', 'S2B_TGT_ACCURACY', 'S2B_NONTGT_ACCURACY',
                 'MT_ST_PCRT', 'MT_ST_MCRTT', 'MT_ST_PSIT', 'MT_ST_SSRTT', 'MT_ST_PSRRT']

Var_Demographic = ['HSHLD_INCOME', 'CLINICALDX', 'ASDANXIET', 'ASDAPHAS', 'ASDAPRAX', 'ASDADHD', 'ASDAUDPRO', 'ASDASD', 'ASDCEREBPAL', 'ASDDOWNSYN', 'ASDINTDIS', 'ASDLEARNDIS',
                   'ASDMOTORSK', 'ASDMOVEDIS', 'ASDNEURO', 'ASDOCD', 'ASDPANIC', 'ASDRETT', 'ASDSENS', 'ASDSOCPHOB', 'ASDSPEECH', 'ASDWILLIAM',
                   'ASDALLERG', 'ASDANEM', 'ASDASTHM', 'ASDBRAINDAM', 'ASDCANCER', 'ASDCHRNHEAD', 'ASDCONHERT', 'ASDCONSTIP', 'ASDCYSTFIB', 'ASDDIABET', 'ASDENCEPH',
                   'ASDEPILEP', 'ASDGASTRO', 'ASDIMMUN', 'ASDMULTSCL', 'ASDORTHOPED', 'ASDREFLUX', 'ASDSEIZ', 'ASDSLEEP', 'ASDSPINABIF', 'ASDTUBERSCL',
                   'ASDOTHCOMOR', 'ASDOTHCOMORSP', 'ASDPREMAT', 'ASDBRANTRAM', 'ASDBRTRSP']

# Importing the data (note that the order is always Behaviour, Cognitive, Demographics)

adhd_1, adhd_2, adhd_3, asd_1, asd_2, asd_3, ocd_1, ocd_2, ocd_3, subadhd_1, subadhd_2, subadhd_3, other_1, other_2, other_3, typ_1, typ_2, typ_3 = pd.read_excel(r"/Users/3052307/Downloads/Clinical_Behaviour_ADHD.xlsx"), pd.read_excel(r"/Users/3052307/Downloads/Clinical_Cognitive_ADHD.xlsx"), pd.read_excel(r"/Users/3052307/Downloads/Clinical_Demographics_ADHD.xlsx"), pd.read_excel(r"/Users/3052307/Downloads/Clinical_Behaviour_ASD.xlsx"), pd.read_excel(r"/Users/3052307/Downloads/Clinical_Cognitive_ASD.xlsx"), pd.read_excel(r"/Users/3052307/Downloads/Clinical_Demographics_ASD.xlsx"), pd.read_excel(r"/Users/3052307/Downloads/Clinical_Behaviour_OCD.xlsx"), pd.read_excel(r"/Users/3052307/Downloads/Clinical_Cognitive_OCD.xlsx"), pd.read_excel(r"/Users/3052307/Downloads/Clinical_Demographics_OCD.xlsx"), pd.read_excel(r"/Users/3052307/Downloads/Clinical_Behaviour_Sub-threshold-ADHD.xlsx"), pd.read_excel(r"/Users/3052307/Downloads/Clinical_Cognitive_Sub-threshold-ADHD.xlsx"), pd.read_excel(r"/Users/3052307/Downloads/Clinical_Demographics_Sub-threshold-ADHD.xlsx"), pd.read_excel(r"/Users/3052307/Downloads/Clinical_Behaviour_Other-Diagnoses.xlsx"), pd.read_excel(r"/Users/3052307/Downloads/Clinical_Cognitive_Other-Diagnoses.xlsx"), pd.read_excel(r"/Users/3052307/Downloads/Clinical_Demographics_Other-Diagnoses.xlsx"), pd.read_excel(r"/Users/3052307/Downloads/Clinical_Behaviour_Typically-Developing.xlsx"), pd.read_excel(r"/Users/3052307/Downloads/Clinical_Cognitive_Typically-Developing.xlsx"), pd.read_excel(r"/Users/3052307/Downloads/Clinical_Demographics_Typically-Developing.xlsx")

dfs = [adhd_1, adhd_2, adhd_3, asd_1, asd_2, asd_3, ocd_1, ocd_2, ocd_3, subadhd_1, subadhd_2, subadhd_3, other_1, other_2, other_3, typ_1, typ_2, typ_3]

# For subjects who contributed data two separate times, the second time is marked by adding a '*' to the subject_id

for df in dfs:
    df.loc[df['repeat_instance'] == 2, 'subject_id'] += '*'
    df.sort_values('subject_id', inplace=True)

# Converting each dataframe from long to wide form

wide_data = [df.pivot(index='subject_id', columns='field_name', values='field_value') for df in dfs]

# Shrinking each dataframe to the relevant variables, then combining into one dataframe for each diagnosis
# Then adding a column to specify the diagnosis (slightly different process for 'Other' - see below)

adhd_1, adhd_2, adhd_3 = wide_data[0].loc[:, Var_Behaviour], wide_data[1].loc[:, Var_Cognitive], wide_data[2].loc[:, Var_Demographic]
adhd_all = pd.concat([adhd_1, adhd_2, adhd_3], axis=1)
adhd_all.insert(0, 'primary_diagnosis', len(adhd_all)*['ADHD'])

asd_1, asd_2, asd_3 = wide_data[3].loc[:, Var_Behaviour], wide_data[4].loc[:, Var_Cognitive], wide_data[5].loc[:, Var_Demographic]
asd_all = pd.concat([asd_1, asd_2, asd_3], axis=1)
asd_all.insert(0, 'primary_diagnosis', len(asd_all)*['ASD'])

ocd_1, ocd_2, ocd_3 = wide_data[6].loc[:, Var_Behaviour], wide_data[7].loc[:, Var_Cognitive], wide_data[8].loc[:, Var_Demographic]
ocd_all = pd.concat([ocd_1, ocd_2, ocd_3], axis=1)
ocd_all.insert(0, 'primary_diagnosis', len(ocd_all)*['OCD'])

subadhd_1, subadhd_2, subadhd_3 = wide_data[9].loc[:, Var_Behaviour], wide_data[10].loc[:, Var_Cognitive], wide_data[11].loc[:, Var_Demographic]
subadhd_all = pd.concat([subadhd_1, subadhd_2, subadhd_3], axis=1)
subadhd_all.insert(0, 'primary_diagnosis', len(subadhd_all)*['Sub-threshold-ADHD'])

other_1, other_2, other_3 = wide_data[12].loc[:, Var_Behaviour], wide_data[13].loc[:, Var_Cognitive], wide_data[14].loc[:, Var_Demographic]
other_all = pd.concat([other_1, other_2, other_3], axis=1)
other_all.insert(0, 'primary_diagnosis', [dfs[12].loc[dfs[12]['subject_id'] == x].iloc[0,0] for x in other_all.index])

typ_1, typ_2, typ_3 = wide_data[15].loc[:, Var_Behaviour], wide_data[16].loc[:, Var_Cognitive], wide_data[17].loc[:, Var_Demographic]
typ_all = pd.concat([typ_1, typ_2, typ_3], axis=1)
typ_all.insert(0, 'primary_diagnosis', len(typ_all)*['Typically-Developing'])

# 'Stacking' all the rows to form one dataframe with all of the data
# Adding on two columns for our new variables: MENTAL_SUM and PHYSICAL_SUM

new_file = pd.concat([adhd_all, asd_all, ocd_all, subadhd_all, other_all, typ_all], axis=0)

mental_diagnoses = ['ASDANXIET', 'ASDAPHAS', 'ASDAPRAX', 'ASDADHD', 'ASDAUDPRO', 'ASDASD', 'ASDCEREBPAL', 'ASDDOWNSYN', 'ASDINTDIS', 'ASDLEARNDIS',
                    'ASDMOTORSK', 'ASDMOVEDIS', 'ASDNEURO', 'ASDOCD', 'ASDPANIC', 'ASDRETT', 'ASDSENS', 'ASDSOCPHOB', 'ASDSPEECH', 'ASDWILLIAM']

physical_diagnoses = ['ASDALLERG', 'ASDANEM', 'ASDASTHM', 'ASDBRAINDAM', 'ASDCANCER', 'ASDCHRNHEAD', 'ASDCONHERT', 'ASDCONSTIP', 'ASDCYSTFIB', 'ASDDIABET', 'ASDENCEPH',
                      'ASDEPILEP', 'ASDGASTRO', 'ASDIMMUN', 'ASDMULTSCL', 'ASDORTHOPED', 'ASDREFLUX', 'ASDSEIZ', 'ASDSLEEP', 'ASDSPINABIF', 'ASDTUBERSCL']

new_file['MENTAL_SUM'] = new_file[mental_diagnoses].sum(axis=1)
new_file['PHYSICAL_SUM'] = new_file[physical_diagnoses].sum(axis=1)

new_file.to_excel(r"/Users/3052307/Downloads/Extracted-Data.xlsx", index=True)



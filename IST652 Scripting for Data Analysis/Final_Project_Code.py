#!/usr/bin/env python
# coding: utf-8

# In[1]:


# RATE OF VIOLENCE BY POPULATION 

import pandas as pd
import numpy as np
datapath = 'Rate-of-Violent-Crime-Offenses-by-Population12_10_2021.csv'
rateofviolence_data  = pd.read_csv(datapath, sep=',')
rateofviolence_data.shape


# In[2]:


rateofviolence_data.columns.values.tolist()


# In[3]:


rateofviolence_data.head()


# In[4]:


NorthCarolina = [362.7, 346.3, 353.5, 341.0, 329.1, 346.1, 371.8, 370.4, 356.2, 378.7, 419.3]
UnitedStates = [404.5, 387.1, 387.8, 369.1, 361.6, 373.7, 397.5, 394.9, 383.4, 380.8, 398.5]
index = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
df = pd.DataFrame({'NorthCarolina': NorthCarolina,
                   'UnitedStates': UnitedStates}, index=index)
ax = df.plot.bar(rot=0)


# In[13]:


# ALL VIOLENT CRIME - OFFENDER AGE # DEMOGRAPHICS

import pandas as pd
path_to_file = 'Offender-Age_AllViolentCrime12_10_2021.csv'
OffenderAgeAllViolentCrime_data  = pd.read_csv(path_to_file, encoding='utf-8')
print(type(OffenderAgeAllViolentCrime_data))


# In[14]:


OffenderAgeAllViolentCrime_data


# In[77]:


OffenderAgeAllViolentCrime_data['value'].sum()


# In[12]:


Age = [9470, 6209, 5401, 4346, 3183, 682, 159, 34, 23, 19]
index = ['20 to 29', '30 to 39', 'unknown', '10 to 19', '40 to 49', '60 to 69', '70 to 79', '0 to 9', '80 to 89', '90 to older']
df = pd.DataFrame({'Age': Age}, index=index)
                   
ax = df.plot.bar(rot=30)


# In[17]:


# ALL VIOLENT CRIME - VICTIM AGE # DEMOGRAPHICS

import pandas as pd
path_to_file = 'Victim-Age_AllViolentCrime12_10_2021.csv'
VictimAgeAllViolentCrime_data  = pd.read_csv(path_to_file, encoding='utf-8')
print(type(VictimAgeAllViolentCrime_data))


# In[18]:


VictimAgeAllViolentCrime_data.shape


# In[19]:


VictimAgeAllViolentCrime_data 


# In[79]:


VictimAgeAllViolentCrime_data['value'].sum()


# In[20]:


People = [11727, 8637, 6107, 5536, 3770, 2118, 1855, 609, 401, 132, 47]
index = ['20 to 29', '30 to 39', '10 to 19', '40 to 49', '50 to 59', '0 to 9', '60 to 69', '70 to 79', 'unknown', '80 to 89', '90 to Older']
df = pd.DataFrame({'People': People}, index=index)
                   
ax = df.plot.bar(rot=30)


# In[23]:


# ALL VIOLENT CRIME - LOCATION TYPE # DEMOGRAPHICS

import pandas as pd
path_to_file = 'Location-Type_AllViolentCrime12_10_2021.csv'
LocationTypeAllViolentCrime_data  = pd.read_csv(path_to_file, encoding='utf-8')
print(type(LocationTypeAllViolentCrime_data))


# In[24]:


LocationTypeAllViolentCrime_data.shape


# In[25]:


LocationTypeAllViolentCrime_data


# In[80]:


LocationTypeAllViolentCrime_data['value'].sum()


# In[27]:


Locations = [23207, 7236, 1786, 1783, 1038, 975, 971, 811, 574, 571, 434, 420, 410, 343, 279, 278, 243, 137, 132, 130, 104, 82, 80, 64, 64, 40, 39, 33, 32, 27, 23, 23, 22, 20, 19, 18, 18, 13, 10, 8, 8, 6, 5, 0, 0, 0]
index = ['Residence Home', 'Highway/Alley/Street/Sidewalk', 'Convenience Store', 'Parking Garage/Lot', 'Hotel/Motel', 'Unknown', 'Gas Station', 'Restaurant', 'Specialty Store', 'Department/Discount Store', 'Park/Playground', 'Commercial/Office Building',
        'Grocery Store', 'Field/Woods', 'Jail/Prison/Corrections Facility', 'Drug Store/Doctors Office/Hospital', 'Bar/Nightclub', 'Gambling Facility/Casino/Race Track', 'Bank', 'School Elementary/Secondary', 'Government/Public Building', 'Air/Bus/Train Terminal', 'Shopping Mall',
        'Church/Synagogue/Temple/Mosque', 'Rest Area', 'Lake/Waterway/Beach', 'School College/University', 'Rental Storage Facility', 'Daycare Facility', 'ATM Separate From Bank', 'Construction Site', 'Mission/Homeless Shelter', 'Abandoned Condemned/Structure', 'Industrial Site', 
        'Auto Dealership', 'Campground', 'Liquor Store', 'Community Center', 'Amusement Park', 'Farm Facility', 'School/College', 'Dock/Wharf/Shipping Terminal', 'Arena/Stadium/Fairgrounds', 'Cyberspace', 'Military Base', 'Tribal Lands']
df = pd.DataFrame({'Locations': Locations}, index=index)
                   
ax = df.plot.bar(rot=90)


# In[28]:


# ALL VIOLENT CRIME - VICTIM RELATIONSHIP TO THE OFFENDER # DEMOGRAPHICS

import pandas as pd
path_to_file = 'Victim-relationship-to-the-offender_AllViolentCrime12_10_2021.csv'
VictimRelationshipAllViolentCrime_data  = pd.read_csv(path_to_file, encoding='utf-8')
print(type(VictimRelationshipAllViolentCrime_data))


# In[30]:


VictimRelationshipAllViolentCrime_data.shape


# In[78]:


VictimRelationshipAllViolentCrime_data


# In[81]:


VictimRelationshipAllViolentCrime_data['value'].sum()


# In[32]:


Relationships = [14559, 7437, 5782, 4017, 3169, 1112, 886, 779, 734, 664, 597, 509, 428, 292, 148, 116, 107, 74, 73, 64, 60, 46, 37, 27, 20, 0]
index = ['Relationship Unknown', 'Stranger', 'Acquaintance', 'Boyfriend/Girlfriend', 'Otherwise Known', 'Friend', 'Spouse', 'Offender', 'Child', 'Other Family Member', 'Neighbor', 'Sibling',
        'Parent', 'Ex Spouse', 'Child of Boyfriend/Girlfriend', 'Stepchild', 'In-Law', 'Common Law Spouse', 'Stepparent', 'Employee', 'Grandchild', 'Grandparent', 'Employer',
        'Stepsibling', 'Babysittee', 'Homosexual Relationship'] 
       
df = pd.DataFrame({'Relationships': Relationships}, index=index)
                   
ax = df.plot.bar(rot=90)


# In[33]:


# ALL VIOLENT CRIME - TYPE OF WEAPON INVOLVED # CHARACTERISTICS

import pandas as pd
path_to_file = 'Type-of-weapon-involved-by-offense_AllViolentCrime12_10_2021.csv'
TypeofWeaponInvolvedAllViolentCrime_data  = pd.read_csv(path_to_file, encoding='utf-8')
print(type(TypeofWeaponInvolvedAllViolentCrime_data))


# In[35]:


TypeofWeaponInvolvedAllViolentCrime_data.shape


# In[36]:


TypeofWeaponInvolvedAllViolentCrime_data 


# In[83]:


TypeofWeaponInvolvedAllViolentCrime_data['value'].sum()


# In[38]:


NumberofWeapons = [8565, 6160, 3684, 3259, 1897, 1796, 1118, 1054, 772, 439, 366, 235, 168, 112, 53, 46, 30, 20, 13, 5, 4, 0, 0, 0, 0, 0, 0, 0]
index = ['Handgun', 'Personal Weapons', 'Knife/Cutting Instrument', 'Firearm', 'None', 'Blunt Object', 'Uknown', 'Other',
        'Rifle', 'Handgun (Automatic)', 'Shotgun', 'Other FireArm', 'Asphyxiation', 'Firearm (Automatic)', 'Drugs/Narcotics/Sleeping Pills', 'Rifle (Automatic)',
        'Fire/Incendiary Device', 'Explosives', 'Poison', 'Shotgun (Automatic)', 'Other Firearm (Automatic)', 'Pushed or Thrown Out Window',
        'Drowning', 'Strangulation - Include Hanging', 'Unarmed', 'Lethal Cutting Instrument', 'Club/Blancjack/Brass Knuckles',
        'Motor Vehicle'] 
       
df = pd.DataFrame({'NumberofWeapons': NumberofWeapons}, index=index)
                   
ax = df.plot.bar(rot=90)


# In[39]:


# ALL VIOLENT CRIME - OFFENSE LINKED TO ANOTHER OFFENSE # CHARACTERISTICS

import pandas as pd
path_to_file = 'Offense-linked-to-another-offense_AllViolentCrime12_10_2021.csv'
OffenseLinkedtoAnotherOffenseAllViolentCrime_data  = pd.read_csv(path_to_file, encoding='utf-8')
print(type(OffenseLinkedtoAnotherOffenseAllViolentCrime_data))


# In[40]:


OffenseLinkedtoAnotherOffenseAllViolentCrime_data.shape


# In[42]:


OffenseLinkedtoAnotherOffenseAllViolentCrime_data


# In[82]:


OffenseLinkedtoAnotherOffenseAllViolentCrime_data['value'].sum()


# In[44]:


NumberofOffenses = [3410, 931, 924, 724, 711, 535, 362, 283, 266, 210, 172, 149, 145, 136, 91, 85, 59, 52, 42, 31, 31, 23,
                    21, 17, 11, 8, 7, 6, 6, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
index = ['Destruction/Damage/Vandalism of Property', 'Simple Assault', 'Weapon Law Violations', 'Burglary/Breaking & Entering',
        'Kidnapping/Abduction', 'Drug/Narcotic Violations', 'All Other Larceny', 'Aggravated Assault',
         'Drug Equipment Violations', 'Robbery', 'Motor Vehicle Theft', 'Intimidation', 'Stolen Property Offenses',
         'Murder and Nonnegligent Manslaughter', 'Shoplifting', 'Theft from Motor Vehicle', 'Theft From Building',
         'Sodomy', 'False Pretenses/Swindle/Confidence game', 'Fondling', 'Bribery', 'Credit Card/Automated Teller Machine Fraud',
         'Arson', 'Sexual Assault with an Object', 'Counterfeiting/Forgery', 'Animal Cruelty', 'Purse-snatching',
         'Identity Theft', 'Pocket-Picking', 'Statutory Rape', 'Theft of Motor Vehicle Parts or Accessories', 
         'Assisting or Promoting Prostitution', 'Impersonation', 'Pornography/Obscene Material',
         'Human Trafficking, Involuntary Servitude', 'Prostitution', 'Human Trafficking, Commercial Sex Acts',
         'Purchasing Prostitution', 'Negligent Manslaughter', 'Wire Fraud', 'Embezzlement', 'Welfare Fraud',
         'Extortion/Blackmail', 'Theft from Coin-operated Machine or Device', 'Gambling Equipment Violation',
         'Incest', 'Operating/Promoting/Assisting Gambling', 'Hacking/Computer Invasion', 'Sports Tampering',
         'Betting/Wagering'] 
       
df = pd.DataFrame({'NumberofOffenses': NumberofOffenses}, index=index)
                   
ax = df.plot.bar(rot=90)


# In[45]:


# RATE OF HOMICIDE BY POPULATION 

import pandas as pd
path_to_file = 'Rate-of-Homicide-Offenses-by-Population12_10_2021.csv'
rateofhomicideoffensesbypopulation_data  = pd.read_csv(path_to_file, encoding='utf-8')
print(type(rateofhomicideoffensesbypopulation_data))


# In[46]:


rateofhomicideoffensesbypopulation_data.shape


# In[47]:


rateofhomicideoffensesbypopulation_data


# In[48]:


UnitedStates = [4.8, 4.7, 4.7, 4.5, 4.4, 4.9, 5.4, 5.3, 5.0, 5.1, 6.5]
NorthCarolina = [5.0, 5.2, 4.9, 4.7, 5.0, 5.2, 6.7, 6.1, 5.5, 6.2, 8.0]
index = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
df = pd.DataFrame({'UnitedStates': UnitedStates,
                   'NorthCarolina': NorthCarolina}, index=index)
ax = df.plot.bar(rot=0)


# In[49]:


# HOMICIDE OFFENDER VS. VICTIM DEMOGRAPHICS # OFFENDER AGE

import pandas as pd
path_to_file = 'Offender-Age_Homicide12_10_2021.csv'
OffenderAgeHomicide_data  = pd.read_csv(path_to_file, encoding='utf-8')
print(type(OffenderAgeHomicide_data))


# In[50]:


OffenderAgeHomicide_data.shape


# In[51]:


OffenderAgeHomicide_data


# In[84]:


OffenderAgeHomicide_data['value'].sum()


# In[52]:


Age = [344, 154, 138, 72, 66, 34, 13, 8, 3, 0, 0]
index = ['20 to 29','10 to 29', '30 to 39', 'unknown', '40 to 49', '50 to 59', '60 to 69', '70 to 79', '80 to 89', '0 to 9', '90 to older']
df = pd.DataFrame({'Age': Age}, index=index)
                   
ax = df.plot.bar(rot=60)


# In[53]:


# HOMICIDE OFFENDER VS. VICTIM DEMOGRAPHICS # VICTIM AGE

import pandas as pd
path_to_file = 'Victim-Age_Homicide12_10_2021.csv'
VictimAgeHomicide_data  = pd.read_csv(path_to_file, encoding='utf-8')
print(type(VictimAgeHomicide_data))


# In[54]:


VictimAgeHomicide_data.shape


# In[55]:


VictimAgeHomicide_data 


# In[85]:


VictimAgeHomicide_data['value'].sum()


# In[56]:


Age = [263, 154, 90, 74, 69, 36, 23, 20, 6, 5, 2]
index = ['20 to 29','30 to 39', '10 to 19', '40 to 49', '50 to 59', '60 to 69', '0 to 9', '70 to 79', 'unknown', '80 to 89', '90 to older']
df = pd.DataFrame({'Age': Age}, index=index)
                   
ax = df.plot.bar(rot=60)


# In[57]:


# HOMICIDE VICTIM DEMOGRAPHICS # LOCATION TYPE

import pandas as pd
path_to_file = 'Location-TypeHomicide12_10_2021.csv'
LocationTypeHomicide_data  = pd.read_csv(path_to_file, encoding='utf-8')
print(type(LocationTypeHomicide_data))


# In[58]:


LocationTypeHomicide_data.shape


# In[59]:


LocationTypeHomicide_data


# In[61]:


LocationTypeHomicide_data['value'].sum()


# In[62]:


Locations = [387, 168, 49, 22, 21, 14, 12, 10, 10, 8, 6, 5, 5, 5, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
index = ['Residence Home', 'Highway/Alley/Street/Sidewalk', 'Parking Garage/Lot', 'Convenience Store', 'Unknown', 'Hotel/Motel', 'Field/Woods', 'Bar/Nightclub', 'Park/Playground',
         'Commercial/Office Building', 'Gas Station', 'Drug Store/Doctors Office/Hospital', 'Jail/Prison/Corrections Facility', 'Restaurant', 'Church/Synagogue/Temple/Mosque',
         'Grocery Store', 'Air/Bus/Train Terminal', 'School Elementary/Secondary', 'Amusement Park', 'Community Center', 'Construction Site', 'Department/Discount Store',
         'Gambling Facility/Casino/Race Track', 'Government/Public Building', 'Industrial Site', 'Liquor Store',
         'Mission/Homeless Shelter', 'Specialty Store', 'Bank', 'Abandoned Condemmend/Structure', 'Arena/Stadium/Fairgrounds',
         'ATM Separate From Bank', 'Auto Dealership', 'Campground', 'Cyberspace', 'Daycare Facility', 'Dock/Wharf/Shipping Terminal',
         'Farm Facility', 'Lake/Waterway/Beach', 'Military Base', 'Rental Storage Facility', 'Rest Area', 'School/College',
         'School College/University', 'Shopping Mall', 'Tribal Lands']
        
        
df = pd.DataFrame({'Locations': Locations}, index=index)
                   
ax = df.plot.bar(rot=90)


# In[63]:


# HOMICIDE VICTIM DEMOGRAPHICS # VICTIM RELATIONSHIP TO THE OFFENDER

import pandas as pd
path_to_file = 'Victim-relationship-to-the-offenderHomicide12_10_2021.csv'
VictimRelationshiptotheOffenderHomicide_data  = pd.read_csv(path_to_file, encoding='utf-8')
print(type(VictimRelationshiptotheOffenderHomicide_data))


# In[64]:


VictimRelationshiptotheOffenderHomicide_data.shape


# In[65]:


VictimRelationshiptotheOffenderHomicide_data


# In[66]:


VictimRelationshiptotheOffenderHomicide_data['value'].sum()


# In[67]:


Relationships = [437, 163, 62, 53, 38, 25, 22, 21, 12, 11, 8, 7, 7, 6, 4, 2, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]
index = ['Relationship Unknown', 'Acquaintance', 'Otherwise Known', 'Stranger', 'Boyfriend/Girlfriend', 'Spouse', 
         'Friend', 'Child', 'Parent', 'Other Family Member', 'Sibling', 'Neighbor', 'Offender', 'Grandparent', 
         'Child of Boyfriend/Girlfriend', 'Ex Spouse', 'Grandchild', 'In-Law', 'Stepchild', 'Stepparent',
         'Stepsibling', 'Common Law Spouse', 'Babysittee', 'Employee', 'Employer', 'Homosexual Relationship'] 
       
df = pd.DataFrame({'Relationships': Relationships}, index=index)
                   
ax = df.plot.bar(rot=90)


# In[68]:


# HOMICIDE - OFFENSE LINKED TO ANOTHER OFFENSE # CHARACTERISTICS

import pandas as pd
path_to_file = 'Offense-linked-to-another-offenseHomicide12_10_2021.csv'
HomicideOffenseLinkedtoAnotherOffenseHomicide_data  = pd.read_csv(path_to_file, encoding='utf-8')
print(type(HomicideOffenseLinkedtoAnotherOffenseHomicide_data))


# In[69]:


HomicideOffenseLinkedtoAnotherOffenseHomicide_data.shape


# In[70]:


HomicideOffenseLinkedtoAnotherOffenseHomicide_data['value'].sum()


# In[71]:


NumberofOffenses = [117, 47, 24, 18, 11, 9, 6, 5, 5, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
index = ['Aggravated Assault', 'Destruction/Damage/Vandalism of Property', 'Weapon Law Violation', 'Robbery',
        'Drug/Narcotic Violations', 'Kidnapping/Abduction', 'Drup Equipment Violations', 'Motor Vehicle Theft', 
        'Burglary/Braking & Entering', 'Theft from Motor Vehicle', 'Simple Assault', 'All Other Lacerny',
        'Stolen Property Offenses', 'False Pretenses/Swindle/Confidence game', 'Arson', 'Indentity Theft', 'Fondling',
        'Bribery', 'Pocket-Picking', 'Murder and Nonnegligent Manslaughter', 'Welfare Fraud', 'Extortion/Blackmail',
        'Theft from Coin-operated Machine or Device', 'Statutory Rape', 'Intimidation', 'Gambling Equipment Violation',
        'Shoplifting', 'Incest', 'Animal Cruelty', 'Operating/Promoting/Assisting Gambling', 'Hacking/Computer Invasion',
         'Sports Tampering', 'Impersonation', 'Negligent Manslaugther', 'Wire Fraud', 'Theft From Building',
         'Theft of Motor Vehicle Parts or Accessories', 'Sexual Assault with an Object', 'Counterfeiting/Forgery',
         'Purse-snatching', 'Prostitution', 'Embezzlement', 'Credir Card/Automated Teller Machina Fraud',
         'Pornography/Obscene Material', 'Human Trafficking, Commercial Sex Acts', 'Betting/Wagering',
         'Human Trafficiking, Involutary Servitude', 'Purchasing Prostitution', 'Assisting or Promoting Prostitution',
         'Sodomy']
       
df = pd.DataFrame({'NumberofOffenses': NumberofOffenses}, index=index)
                   
ax = df.plot.bar(rot=90)


# In[72]:


# ALL VIOLENT CRIME - TYPE OF WEAPON INVOLVED # CHARACTERISTICS

import pandas as pd
path_to_file = 'Type-of-weapon-involved-by-offenseHomicide12_10_2021.csv'
TypeofWeaponHomicide_data  = pd.read_csv(path_to_file, encoding='utf-8')
print(type(TypeofWeaponHomicide_data))


# In[73]:


TypeofWeaponHomicide_data.shape 


# In[74]:


TypeofWeaponHomicide_data 


# In[86]:


TypeofWeaponHomicide_data['value'].sum()


# In[75]:


NumberofWeapons = [279, 195, 51, 38, 33, 25, 17, 14, 10, 8, 6, 3, 3, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
index = ['Handgun', 'Firearm', 'Knife/Cutting Instrument', 'Unknown', 'Personal Weapons', 'Rifle', 'Handgun (Automatic)', 
        'Drugs/Narcotics/Sleeping Pills', 'Blunt Object', 'Shotgun', 'Other', 'Other Firearm', 'Asphyxiation',
         'Firearm (Automatic)', 'Rifle (Automatic)', 'None', 'Shotgun (Automatic)', 'Other Firearm (Automatic)',
         'Puched or Thrown Out Window', 'Drowning', 'Strangulation - Include Hanging', 'Unarmed', 'Lethal Cutting Instrument',
         'Club/Blackjack/Brass Knuckles', 'Motor Vehicle', 'Poison', 'Explosives', 'Fire/Incendiary Device']
       
df = pd.DataFrame({'NumberofWeapons': NumberofWeapons}, index=index)
                   
ax = df.plot.bar(rot=90)


# In[ ]:





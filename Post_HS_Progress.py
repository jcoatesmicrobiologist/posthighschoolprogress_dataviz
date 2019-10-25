#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


highschool_data = pd.read_csv('/resources/data/High_Schools__Post_High_School_Progress_2016.csv')


# In[4]:


get_ipython().run_cell_magic('capture', '', '! pip install seaborn')


# In[5]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


classof2009 = highschool_data[['Class2009_PctEnroll_privGA_1yr','Class2009_PctEnroll_pubGA_1yr','Class2009_PctEnroll_techGA_1yr','Class2009_PctEnroll_outGA_1yr','Class2009_Pct_Unknown_1yr','Class2009_PctWorkGAnoEnroll_1yr','Class2009_Pct_Earnd_Cert_5yrs',
                              'Class2009_Pct_Earnd_AA_5yrs','Class2009_Pct_Earnd_BA_5yrs','Class2009_Pct_Earnd_MAorHi_5yrs','Class2009_Pct_OtherCred_5yrs','Class2009_Pct_EnrollnoCred_5yrs','Class2009_Pct_Not_Enrolled_5yrs','X','Y','SYSTEM_ID','SYSTEM_NAME',
                              'SCHOOL_NAME','SCHOOL_CITY']]

classof2009.head()


# In[7]:


classof2009_group_one = classof2009.groupby(['SYSTEM_NAME'],as_index=False).mean()
classof2009_group_one


# In[8]:


classof2009_group_one.corr()


# In[9]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib as mpl
import matplotlib.pyplot as plt


# In[10]:


print ('Matplotlib version: ', mpl.__version__) # >= 2.0.0


# In[11]:


print(plt.style.available)
mpl.style.use(['ggplot']) # optional: for ggplot-like style


# In[12]:


condition = classof2009['SYSTEM_NAME'] == 'Houston County'
houston = classof2009[condition]
houston.head()


# In[13]:


houston_clean = houston.transpose()
houston_clean_final = houston_clean.drop([141,142], axis =1)
houston_clean_final


# In[14]:


houston_compare_enroll_data = [['Private GA', 8,12,11,8],['Public GA', 51,56,36,54],['Technical GA',13,10,17,10],['OutGA', 8,5,4,6],['Working',12,10,18,11],['Unknown',9,8,15,10]]
houston_compare_enroll_df = pd.DataFrame(houston_compare_enroll_data, columns = ['Status','Perry High School','Houston County High School','Northside High School','Warner Robins High School'], index = ['Private GA','Public GA','Technical GA','Out GA','Working','Unknown'])


houston_compare_enroll_df.plot(kind='bar', figsize=(10, 6))

plt.xlabel('Status') # add to x-label to the plot
plt.ylabel('Percent Enrolled') # add y-label to the plot
plt.title('Warner Robins High School class of 2009 graduates were more likely to enroll in public colleges in GA than Northside High School 2009 Graduates' ) # add title to the plot

plt.show()


# In[15]:


houston_compare_5post_data = [['Certificate', 2,0,3,2],['Associates', 12,10,6,11],['BA',25,30,11,23],['MA or Higher', 1,0,0,0],['Other Credentials',0,0,1,1],['Enrolled No Credentials',22,24,24,25],['Not Enrolled',38,35,55,38]]
houston_compare_post_df = pd.DataFrame(houston_compare_5post_data, columns = ['Status','Perry High School','Houston County High School','Northside High School', 'Warner Robins High School'], index = ['Certificate','Associates','BA','MA or Higher','Other Credentials','Enrolled No Credentials','Not Enrolled No Credentials'])

houston_compare_post_df.plot(kind='bar', figsize=(10, 6))

plt.xlabel('Status') # add to x-label to the plot
plt.ylabel('Percent Enrolled') # add y-label to the plot
plt.title('Warner Robins High School Class of 2009 graduates were more likely to earn Associates and Bachelors Degrees 5 years post graduation than Northside High School Graduates' ) # add title to the plot

plt.show()


# In[16]:


houston.describe()


# In[17]:


houston_enrolled_data = [['Private GA', 9.8],['Public GA', 49.3],['Technical GA',12.5],['OutGA', 5.8],['Working',12.8],['Unknown',10.5]]
houston_enrolled_df = pd.DataFrame(houston_enrolled_data, columns = ['Status','Percent'], index = ['Private GA','Public GA','Technical GA','Out GA','Working','Unknown'])


houston_enrolled_df.plot(kind='bar', figsize=(10, 6))

plt.xlabel('Status') # add to x-label to the plot
plt.ylabel('Percent Enrolled') # add y-label to the plot
plt.title('The majority of Houston County class of 2009 GA gradutes enrolled in public GA colleges within one year of graduation.' ) # add title to the plot

plt.show()


# In[18]:


houston_5post_data = [['Certificate', 1.8],['Associates', 9.8],['BA',22.3],['MA or Higher', 0.3],['Other Credentials',0.5],['Enrolled No Credentials',23.8],['Not Enrolled',41.5]]
houston_post_df = pd.DataFrame(houston_5post_data, columns = ['Status','Percent'], index = ['Certificate','Associates','BA','MA or Higher','Other Credentials','Enrolled No Credentials','Not Enrolled No Credentials'])

houston_post_df.plot(kind='bar', figsize=(10, 6))

plt.xlabel('Status') # add to x-label to the plot
plt.ylabel('Percent Enrolled') # add y-label to the plot
plt.title('The majority of Houston County class of 2009 GA gradutes were not enrolled in college with no credentials 5 years post graduation' ) # add title to the plot

plt.show()


# In[19]:


classof2009.describe()


# In[20]:


classof2009_enrolled_data = [['Private GA', 5.2],['Public GA', 43.0],['Technical GA',12.3],['OutGA', 8.6],['Working',17.1],['Unknown',14.4]]
enrolled_df = pd.DataFrame(classof2009_enrolled_data, columns = ['Status','Percent'], index = ['Private GA','Public GA','Technical GA','Out GA','Working','Unknown'])
enrolled_df.head()


# In[21]:


enrolled_df.plot(kind='bar', figsize=(10, 6))

plt.xlabel('Status') # add to x-label to the plot
plt.ylabel('Percent Enrolled') # add y-label to the plot
plt.title('The majority of class of 2009 GA gradutes enrolled in public GA colleges within one year of graduation.' ) # add title to the plot

plt.show()


# In[22]:


classof2009_5post_data = [['Certificate', 2.8],['Associates', 6.9],['BA',17.8],['MA or Higher', 0.2],['Other Credentials',0.6],['Enrolled No Credentials',21.9],['Not Enrolled',49.7]]
post_df = pd.DataFrame(classof2009_5post_data, columns = ['Status','Percent'], index = ['Certificate','Associates','BA','MA or Higher','Other Credentials','Enrolled No Credentials','Not Enrolled No Credentials'])
post_df.head()


# In[23]:


post_df.plot(kind='bar', figsize=(10, 6))

plt.xlabel('Status') # add to x-label to the plot
plt.ylabel('Percent Enrolled') # add y-label to the plot
plt.title('The majority of class of 2009 GA gradutes were not enrolled in college with no credentials 5 years post graduation' ) # add title to the plot

plt.show()


# In[24]:


condition_two = highschool_data['SCHOOL_NAME'] == 'Warner Robins High School'
wrhs = highschool_data[condition_two]
wrhs.head()


# In[25]:


wrhs_clean = wrhs.drop(['X','Y','SYSSCHOOL','SYSTEM_ID','SYSTEM_NAME','SCHOOL_ID','FAC_SCHTYP','GRADE_RANGE','OBJECTID','SCHOOL_ADD','SCHOOL_CITY','STATE','SCHOOL_ZIP','SCHOOL_PHONE','GlobalID','last_edited_date'],axis =1)
wrhs_clean.head()


# In[26]:


wrhs_clean_enrolled = wrhs_clean[['Class2007_PctEnroll_pubGA_1yr','Class2008_PctEnroll_pubGA_1yr','Class2009_PctEnroll_pubGA_1yr','Class2010_PctEnroll_pubGA_1yr','Class2011_PctEnroll_pubGA_1yr']].values

wrhs_clean_post = wrhs_clean[['Class2007_Pct_Earnd_BA_5yrs','Class2008_Pct_Earnd_BA_5yrs','Class2009_Pct_Earnd_BA_5yrs','Class2010_Pct_Earnd_BA_5yrs','Class2011_Pct_Earnd_BA_5yrs']].values


# In[27]:


wrhs_clean_enrolled

wrhs_clean_enrolled_data = [['Class of 2007', 48 ],['Class of 2008', 49],['Class of 2009',54],['Class of 2010', 46],['Class of 2011',41]]
wrhs_clean_enrolled_df = pd.DataFrame(wrhs_clean_enrolled_data, columns = ['Class','Percent'], index = ['Class of 2007','Class of 2008','Class of 2009','Class of 2010','Class of 2011'])
wrhs_clean_enrolled_df.head()


# In[28]:


wrhs_clean_enrolled_df.plot(kind='bar', figsize=(10, 6))

plt.xlabel('Class') # add to x-label to the plot
plt.ylabel('Percent Enrolled') # add y-label to the plot
plt.title('WRHS class of 2009 had the highest number of students enrolled in public colleges in GA 1 year post graduation' ) # add title to the plot

plt.show()


# In[29]:


wrhs_clean_post

wrhs_clean_post_data = [['Class of 2007', 23 ],['Class of 2008', 24],['Class of 2009',23],['Class of 2010', 20],['Class of 2011', 17]]
wrhs_clean_post_df = pd.DataFrame(wrhs_clean_post_data, columns = ['Class','Percent'], index = ['Class of 2007','Class of 2008','Class of 2009','Class of 2010','Class of 2011'])
wrhs_clean_post_df.head()

wrhs_clean_post_df


# In[30]:


wrhs_clean_post_df.plot(kind='bar', figsize=(10, 6))

plt.xlabel('Class') # add to x-label to the plot
plt.ylabel('Percent Enrolled') # add y-label to the plot
plt.title('WRHS class of 2009 had the highest number of students enrolled in public colleges in GA 1 year post graduation' ) # add title to the plot

plt.show()


# In[31]:


highschool_group_one = highschool_data.groupby(['SYSTEM_NAME'],as_index=False).mean()
highschool_corr = highschool_group_one.corr()


# In[32]:


pd.options.display.max_rows = 80000
highschool_corr


# In[33]:


condition_three = highschool_data['SYSTEM_NAME'] == 'Houston County'
houston_total = highschool_data[condition_three]
houston_total.head()


# In[52]:


houston_total_group_one = houston_total.groupby(['SCHOOL_NAME'],as_index=False).mean()
houston_total_group_one


# In[53]:


houston_total_group_one.set_index('SCHOOL_NAME', inplace=True)


# In[78]:


houston_total_group_one = pd.DataFrame(houston_total_group_one)

new_enrolled = houston_total_group_one[['Class2007_PctEnroll_pubGA_1yr', 'Class2008_PctEnroll_pubGA_1yr', 'Class2009_PctEnroll_pubGA_1yr','Class2010_PctEnroll_pubGA_1yr','Class2011_PctEnroll_pubGA_1yr']].copy()


# In[79]:


new_enrolled = pd.DataFrame(new_enrolled)


# In[80]:


new_enrolled = new_enrolled.rename(columns={"Class2007_PctEnroll_pubGA_1yr": "2007", "Class2008_PctEnroll_pubGA_1yr": "2008", "Class2009_PctEnroll_pubGA_1yr": "2009", 
                             "Class2010_PctEnroll_pubGA_1yr": "2008", "Class2011_PctEnroll_pubGA_1yr": "2011" })
new_enrolled.head()


# In[81]:


new_enrolled = new_enrolled.transpose()
new_enrolled.head()


# In[93]:



new_enrolled.plot(kind='area', 
                  alpha = 0.5,
                  color=['purple','blue', 'yellow', 'red', 'orange','white'],
                 stacked=False,
                 figsize=(10, 5), # pass a tuple (x, y) size
             )

plt.title('Public College Enrollment within One Year of Graduation')
plt.ylabel('Percent of Students Enrolled')
plt.xlabel('Years')

plt.show()


# In[98]:


houston_total_group_one = pd.DataFrame(houston_total_group_one)

new_BA = houston_total_group_one[['Class2007_Pct_Earnd_BA_5yrs', 'Class2008_Pct_Earnd_BA_5yrs', 'Class2009_Pct_Earnd_BA_5yrs', 'Class2010_Pct_Earnd_BA_5yrs', 'Class2011_Pct_Earnd_BA_5yrs']].copy()


# In[99]:


new_BA = new_BA.rename(columns={"Class2007_Pct_Earnd_BA_5yrs": "2007", "Class2008_Pct_Earnd_BA_5yrs": "2008", "Class2009_Pct_Earnd_BA_5yrs": "2009", 
                             "Class2010_Pct_Earnd_BA_5yrs": "2008", "Class2011_Pct_Earnd_BA_5yrs": "2011" })
new_BA.head()


# In[100]:


new_BA = new_BA.transpose()
new_BA.head()


# In[104]:


new_BA.plot(kind='area', 
                  alpha = 0.5,
                  color=['purple','blue', 'yellow', 'red', 'orange','white'],
                 stacked=False,
                 figsize=(10, 5), # pass a tuple (x, y) size
             )

plt.title('BA Degrees Received within 5 Years of Graduation')
plt.ylabel('Percent of Students Enrolled')
plt.xlabel('Years')

plt.show()


# In[ ]:





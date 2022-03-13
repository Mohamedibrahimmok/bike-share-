#!/usr/bin/env python
# coding: utf-8

# > **Tip**: Welcome to the Investigate a Dataset project! You will find tips in quoted sections like this to help organize your approach to your investigation. Once you complete this project, remove these **Tip** sections from your report before submission. First things first, you might want to double-click this Markdown cell and change the title so that it reflects your dataset and investigation.
# 
# # Project:FBI Gun Data  - [FBI Gun Data]
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# ### Dataset Description 
# 
# > **Tip**: In this section of the report, provide a brief introduction to the dataset you've selected/downloaded for analysis. Read through the description available on the homepage-links present [here](https://docs.google.com/document/d/e/2PACX-1vTlVmknRRnfy_4eTrjw5hYGaiQim5ctr9naaRd4V9du2B5bxpd8FEH3KtDgp8qVekw7Cj1GLk1IXdZi/pub?embedded=True). List all column names in each table, and their significance. In case of multiple tables, describe the relationship between tables. 
# 
# 
# ### Questions for Analysis
# ##Question 1 (which weapon is the most sale)
# ##Question 2  (which state is the most buying for evry weapon )
# ##Question 3  (which state is the most buying for all weapon )
# ##Question 4  (What is the expected number of sale of each type of weapon and all of them )
# ##Question 5  (How does education affect procurement? 
# ##Question 6  (Is trade booming or waning? 
# 

# In[46]:


# Use this cell to set up import statements for all of the packages that you
#   plan to use.
import pandas as pd
import numpy as np
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
# Remember to include a 'magic word' so that your visualizations are plotted
#   inline with the notebook. See this page for more:
#   http://ipython.readthedocs.io/en/stable/interactive/magics.html


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# > **Tip**: In this section of the report, you will load in the data, check for cleanliness, and then trim and clean your dataset for analysis. Make sure that you **document your data cleaning steps in mark-down cells precisely and justify your cleaning decisions.**
# 
# 
# ### General Properties
# > **Tip**: You should _not_ perform too many operations in each cell. Create cells freely to explore your data. One option that you can take with this project is to do a lot of explorations in an initial notebook. These don't have to be organized, but make sure you use enough comments to understand the purpose of each code cell. Then, after you're done with your analysis, create a duplicate notebook where you will trim the excess and organize your steps so that you have a flowing, cohesive report.

# In[47]:


# Load your data and print out a few lines. Perform operations to inspect data
# types and look for instances of missing or possibly errant data.
df_census = pd.read_csv('US_Census_Data.csv')
df_gun = pd.read_excel('gun_data.xlsx')


# In[48]:


df_census.head()
##let's take a look 


# 
# ### Data Cleaning
# > **Tip**: Make sure that you keep your reader informed on the steps that you are taking in your investigation. Follow every code cell, or every set of related code cells, with a markdown cell to describe to the reader what was found in the preceding cell(s). Try to make it so that the reader can then understand what they will be seeing in the following cell(s).
#  

# In[49]:


# After discussing the structure of the data and any problems that need to be
#   cleaned, perform those cleaning steps in the second part of this section.
##every table must have index and the united sheet must have one and it will be states names but it's total must match rows total
# now we need to gethering data iin the seem sheet how? by this
index_census_state = df_census.iloc[0].index
index_census_state = index_census_state[2:]
len(index_census_state)


# In[50]:


##now when we gathering the data we need index for both but we have a problem
index_gun_state = df_gun.groupby('state').sum().index
len(index_gun_state)


# In[51]:


##now  we have Five rows more in gun that doesn't make a match but we have a way to solve it we will delete the  five more rows
##now we need to change the form to another to be topical to make the match
df_census_t= df_census.T
df_census_t=df_census_t.drop(['Fact','Fact Note'])#those are unimportant rows In our analysis


# In[52]:


##we need to know which rows is doesn't match becuse that wee asked what in gun sheet not exaist in census sheet
for s in index_gun_state:
    if s not in df_census_t.index:
        print(s)


# In[53]:


##we have 5 index more we need to equel two sheets
df_gun_by_state=df_gun.groupby('state').sum()
df_gun_by_state.drop([
'District of Columbia',
'Guam',
'Mariana Islands',
'Puerto Rico',
'Virgin Islands'],inplace=True)
len(df_gun_by_state.index)


# In[54]:


df_census_t.columns


# In[55]:


##we need to remove unimportant column
df_census_t.drop([84,83,82,81,80,79,78,77,76,75,74,73,72,71,70,69,68,67,66,65,64,63,62,61,60,59,58,57,56,55,54,53,52,51,50,49,48,47,46,45,44,43,42,41,40,39,38,37,36,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,11,10,9,8,7,6,5,4,3,2,1],axis=1,inplace=True)


# In[56]:


##and give names to important columns 
df_census_t.rename(columns={0: "Population",12:"White",13:"Black",14:"American Indian",15:"Asian",16:"Hawaiian",34:"high_school_graduates",35:"college_graduates"},inplace=True)


# In[ ]:





# In[57]:


##first : populition 
##mmmm we have a problem (,) must be remowe to return it to integer
df_census_t['Population']=df_census_t['Population'].str.replace(',','')
df_census_t['Population'].inplace=True
df_census_t['Population']


# In[58]:


##we need the Population in integer to make calculations 
df_census_t['Population']=pd.to_numeric(df_census_t['Population'], downcast='integer')


# In[59]:


df_census_t##let's see if its done 


# In[60]:


##messing value have a 'z' that mean zero 
df_census_t['Hawaiian']['Maine']='0'
df_census_t['Hawaiian']['Michigan']='0'
df_census_t['Hawaiian']['Vermont']='0'
df_census_t['Hawaiian']['West Virginia']='0'


# In[61]:


##k=columns names we will need it 
k=['White', 'Black', 'American Indian', 'Asian', 'Hawaiian','high_school_graduates', 'college_graduates']


# In[62]:


##we need to convert it to number 
## firist step is remove (%)
for i in k:
    df_census_t[i]=df_census_t[i].str.replace('%','')
    df_census_t[i].inplace=True
    df_census_t[i]=pd.to_numeric(df_census_t[i],downcast='integer')## second turn it to integer
    ## third multiplie it in 100 to get the number we will used 
    df_census_t[i]['New Mexico']=df_census_t[i]['New Mexico']*100
    df_census_t[i]['New York']=df_census_t[i]['New York']*100
    df_census_t[i]['North Carolina']=df_census_t[i]['North Carolina']*100
    df_census_t[i]['North Dakota']=df_census_t[i]['North Dakota']*100
    df_census_t[i]['Oklahoma']=df_census_t[i]['Oklahoma']*100
    df_census_t[i]['Ohio']=df_census_t[i]['Ohio']*100
    df_census_t[i]['Oregon']=df_census_t[i]['Oregon']*100
    df_census_t[i]['Pennsylvania']=df_census_t[i]['Pennsylvania']*100
    df_census_t[i]['Rhode Island']=df_census_t[i]['Rhode Island']*100
    df_census_t[i]['South Carolina']=df_census_t[i]['South Carolina']*100
    df_census_t[i]['South Dakota']=df_census_t[i]['South Dakota']*100
    df_census_t[i]['Tennessee']=df_census_t[i]['Tennessee']*100
    ##now divided on 100 to get the real number we needed
    df_census_t[i]=df_census_t[i]/100
    df_census_t[i]=df_census_t[i]*df_census_t['Population']##the real number = The decimal form of the percentage multiplied by the total value
    


# In[63]:


pd.set_option('display.float_format', lambda x: '%.0f' % x)##make it cleare make it int 

df_census_t


# In[ ]:





# In[ ]:





# now we have the seem index list

# ### getharing data

# In[64]:


##time to get the sheet we will work on we will gethering the edit gun sheet with the edit census sheet
FBI_Gun_Data=df_gun_by_state.append(df_census_t)
FBI_Gun_Data


# In[65]:


##how we solve it Easy by droping the nan cells
FBI_Gun_Data = FBI_Gun_Data.apply(lambda x: pd.Series(x.dropna().values))
FBI_Gun_Data


# what is your opinion now matched right 

# In[ ]:





# In[ ]:





# In[66]:


##why columns is flouts if we talk about gun what mean undivided unit let's make it integers
FBI_Gun_Data.fillna(0, inplace=True)
FBI_Gun_Data['permit']=pd.to_numeric(FBI_Gun_Data['permit'], downcast='integer')
FBI_Gun_Data['permit_recheck']=pd.to_numeric(FBI_Gun_Data['permit_recheck'], downcast='integer')
FBI_Gun_Data['handgun']=pd.to_numeric(FBI_Gun_Data['handgun'], downcast='integer')
FBI_Gun_Data['long_gun']=pd.to_numeric(FBI_Gun_Data['long_gun'], downcast='integer')
FBI_Gun_Data['multiple']=pd.to_numeric(FBI_Gun_Data['multiple'], downcast='integer')
FBI_Gun_Data['admin']=pd.to_numeric(FBI_Gun_Data['admin'], downcast='integer')
FBI_Gun_Data['prepawn_handgun']=pd.to_numeric(FBI_Gun_Data['prepawn_handgun'], downcast='integer')
FBI_Gun_Data['prepawn_long_gun']=pd.to_numeric(FBI_Gun_Data['prepawn_long_gun'], downcast='integer')
FBI_Gun_Data['prepawn_other']=pd.to_numeric(FBI_Gun_Data['prepawn_other'], downcast='integer')
FBI_Gun_Data['redemption_handgun']=pd.to_numeric(FBI_Gun_Data['redemption_handgun'], downcast='integer')
FBI_Gun_Data['redemption_long_gun']=pd.to_numeric(FBI_Gun_Data['redemption_long_gun'], downcast='integer')
FBI_Gun_Data['redemption_other']=pd.to_numeric(FBI_Gun_Data['redemption_other'], downcast='integer')
FBI_Gun_Data['returned_handgun']=pd.to_numeric(FBI_Gun_Data['returned_handgun'], downcast='integer')
FBI_Gun_Data['returned_long_gun']=pd.to_numeric(FBI_Gun_Data['returned_long_gun'], downcast='integer')
FBI_Gun_Data['returned_other']=pd.to_numeric(FBI_Gun_Data['returned_other'], downcast='integer')
FBI_Gun_Data['private_sale_handgun']=pd.to_numeric(FBI_Gun_Data['private_sale_handgun'], downcast='integer')
FBI_Gun_Data['private_sale_long_gun']=pd.to_numeric(FBI_Gun_Data['private_sale_long_gun'], downcast='integer')
FBI_Gun_Data['private_sale_other']=pd.to_numeric(FBI_Gun_Data['private_sale_other'], downcast='integer')
FBI_Gun_Data['return_to_seller_handgun']=pd.to_numeric(FBI_Gun_Data['return_to_seller_handgun'], downcast='integer')
FBI_Gun_Data['return_to_seller_long_gun']=pd.to_numeric(FBI_Gun_Data['return_to_seller_long_gun'], downcast='integer')
FBI_Gun_Data['return_to_seller_other']=pd.to_numeric(FBI_Gun_Data['return_to_seller_other'], downcast='integer')
FBI_Gun_Data['rentals_handgun']=pd.to_numeric(FBI_Gun_Data['rentals_handgun'], downcast='integer')
FBI_Gun_Data['rentals_long_gun']=pd.to_numeric(FBI_Gun_Data['rentals_long_gun'], downcast='integer')


# In[67]:


##problem of index Easy we are ready for it
FBI_Gun_Data.set_index((df_gun_by_state.index),inplace=True)


# In[ ]:





# In[ ]:





# In[ ]:





# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# > **Tip**: Now that you've trimmed and cleaned your data, you're ready to move on to exploration. **Compute statistics** and **create visualizations** with the goal of addressing the research questions that you posed in the Introduction section. You should compute the relevant statistics throughout the analysis when an inference is made about the data. Note that at least two or more kinds of plots should be created as part of the exploration, and you must  compare and show trends in the varied visualizations. 
# 
# 
# 
# > **Tip**: - Investigate the stated question(s) from multiple angles. It is recommended that you be systematic with your approach. Look at one variable at a time, and then follow it up by looking at relationships between variables. You should explore at least three variables in relation to the primary question. This can be an exploratory relationship between three variables of interest, or looking at how two independent variables relate to a single dependent variable of interest. Lastly, you  should perform both single-variable (1d) and multiple-variable (2d) explorations.
# 
# 
# ### Research Question 1 (which weapon is the most sale)

# 

# In[68]:


# Use this, and more code cells, to explore your data. Don't forget to add
#   Markdown cells to document your observations and findings.
##firist we must know which type  of gun is the top of sales
##firist sum gun types
handgun_sum=df_gun['handgun'].sum()
long_gun_sum=df_gun['long_gun'].sum()
other_sum=df_gun['other'].sum()
multiple_sum=df_gun['multiple'].sum()
##second who is the best seller
if handgun_sum > long_gun_sum and other_sum and multiple_sum:
    print('the_Most_popular_type_of_weapon_is_handgun')
if long_gun_sum > handgun_sum and other_sum and multiple_sum:
        print('the_Most_popular_type_of_weapon_is_long_gun')
if other_sum > long_gun_sum and handgun_sum and multiple_sum:
        print('the_Most_popular_type_of_weapon_is_other')
if multiple_sum > long_gun_sum and handgun_sum and other_sum:
        print('the_Most_popular_type_of_weapon_is_multiple')


# ### Research Question 2  (which state is the most buying for evry weapon )

# In[69]:


# Continue to explore the data to address your additional research
#   questions. Add more headers as needed if you have more questions to
#   investigate.
##which state is the most bought handgun
handgun_totals = df_gun[['state','handgun']]
handgun_totals.set_index('state',inplace=True)
handgun_totals=handgun_totals[::-1]
handgun_totals_by_state = handgun_totals.groupby('state').sum()
print('the most state buying handgun guns is',handgun_totals_by_state.idxmax())


# In[70]:


##which state is the most bought long_gun
long_gun_totals = df_gun[['state','long_gun']]##we make a small table from gun sheet just 2 columns
long_gun_totals.set_index('state',inplace=True)##filter the table by states
long_gun_totals=long_gun_totals[::-1]##show all rows
long_gun_totals_by_state = long_gun_totals.groupby('state').sum()
print('the most state buying long_gun guns is',long_gun_totals_by_state.idxmax())##get the maximam state not value
##repiet steps for other parts


# In[71]:


##which state is the most bought long_gun
multiple_gun_totals = df_gun[['state','multiple']]
multiple_gun_totals.set_index('state',inplace=True)
multiple_gun_totals=multiple_gun_totals[::-1]
multiple_gun_totals_by_state = multiple_gun_totals.groupby('state').sum()
print('the most state buying multiple guns is',multiple_gun_totals_by_state.idxmax())


# In[72]:


##which state is the most bought other
other_gun_totals = df_gun[['state','other']]
other_gun_totals.set_index('state',inplace=True)
other_gun_totals=other_gun_totals[::-1]
other_gun_totals_by_state = other_gun_totals.groupby('state').sum()
print('the most state buying other guns is',other_gun_totals_by_state.idxmax())


# In[73]:


##which state is the most bought permit
permit_gun_totals = df_gun[['state','permit']]
permit_gun_totals.set_index('state',inplace=True)
permit_gun_totals=permit_gun_totals[::-1]
permit_gun_totals_by_state = permit_gun_totals.groupby('state').sum()
print('the most state permit guns is',permit_gun_totals_by_state.idxmax())


# ### Research Question 3  (which state is the ##which state is the most bought for all weapons )

# In[74]:


all_df_gun_totals = df_gun[['state','totals']]
all_df_gun_totals.set_index('state',inplace=True)
all_df_gun_totals=all_df_gun_totals[::-1]
gun_totals_groupby_state = all_df_gun_totals.groupby('state').sum()
print('the most state buying guns is',gun_totals_groupby_state.idxmax())


# In[ ]:





# ### Research Question 4  (What is the expected number of sales of each type of weapon and all of them )

# In[75]:


handgun_totals_alone = df_gun['handgun']##get hand gun alone without index
handgun_totals_alone_mean=handgun_totals_alone.mean()##get the meaan
hg=handgun_totals_alone.hist()
hg.set_title('hand gun salles range in month')
hg.set_xlabel('ranges')
hg.set_ylabel('The number of repetitions');
print('handgun expected to sales is ',handgun_totals_alone_mean)##get all other guns


# In[ ]:





# In[76]:


long_gun_totals_alone = df_gun['long_gun']
long_gun_totals_alone_mean=long_gun_totals_alone.mean()
lg=long_gun_totals_alone.hist()
lg.set_title('long gun salles range in month')
lg.set_xlabel('ranges')
lg.set_ylabel('The number of repetitions');
print('long_gun expected to sales is ',long_gun_totals_alone_mean)


# In[77]:


multiple_totals_alone = df_gun['multiple']
multiple_totals_alone_mean=multiple_totals_alone.mean()
mg=multiple_totals_alone.hist()
mg.set_title('multiple gun salles range in month')
mg.set_xlabel('ranges')
mg.set_ylabel('The number of repetitions')
print('multiple guns expected to sales is ',multiple_totals_alone_mean)


# In[78]:


other_totals_alone = df_gun['other']
other_totals_alone_mean=other_totals_alone.mean()
og=other_totals_alone.hist()
og.set_title('other gun salles range in month')
og.set_xlabel('ranges')
og.set_ylabel('The number of repetitions')
print('other guns expected to sales is ',other_totals_alone_mean)


# In[79]:


totals_totals_alone = df_gun['totals']
totals_totals_alone_mean=totals_totals_alone.mean()
tt=totals_totals_alone.hist()
tt.set_title('totals gun salles range in month')
tt.set_xlabel('ranges')
tt.set_ylabel('The number of repetitions')
print('totals guns expected to sales is ',totals_totals_alone_mean)


# ### Research Question 5  (How does education affect procurement? )

# In[ ]:





# In[80]:


l=['White', 'Black', 'American Indian', 'Asian', 'Hawaiian','high_school_graduates', 'college_graduates','Population']
##We need this list to be the variable instead of repeating the steps for each parameter


# In[ ]:


for s in l:
    ts=FBI_Gun_Data[['{}'.format(s),'totals']]
    ts= ts.plot.bar(rot=0).legend(prop={'size': 35})
    plt.rcParams["figure.figsize"] = (40,20)
    plt.title('total sales {}'.format(s)).set_size(40)
    plt.xlabel('states').set_size(40)
    plt.ylabel('Total').set_size(40)
    plt.gcf().autofmt_xdate()


# In[ ]:





# In[ ]:





# ### Research Question 6  (What is the improvement in growth every year seince 2005?and what we ecpecting for the next year? )

# In[ ]:


##month column didn't useful like that we need to sorted sales by year so we must change it to time form
df_gun['month'] = pd.to_datetime(df_gun['month'])
df_gun['year'] = df_gun['month'].dt.year
df_gun['Month'] = df_gun['month'].dt.month


# In[ ]:





# In[ ]:


df_gun_totals_for_rate = df_gun['totals']##we selected the column we needed


# In[ ]:


##now we will the rate of the growth ,how? rate=((year we need it rate -sstander year)/stander year )*100
print('Sales growth rate from 2005 until 2017')
gun_totals_groupby_state= df_gun_totals_for_rate.groupby(df_gun['year'] ).sum()
t_2006=(((gun_totals_groupby_state[2006]-gun_totals_groupby_state[2005])/gun_totals_groupby_state[2005])*100).round(2)
print('Sales growth rate in 2006 is {}%'.format(t_2006))
t_2007=(((gun_totals_groupby_state[2007]-gun_totals_groupby_state[2005])/gun_totals_groupby_state[2005])*100).round(2)
print('Sales growth rate in 2007 is {}%'.format(t_2007))
t_2008=(((gun_totals_groupby_state[2008]-gun_totals_groupby_state[2005])/gun_totals_groupby_state[2005])*100).round(2)
print('Sales growth rate in 2008 is {}%'.format(t_2008))
t_2009=(((gun_totals_groupby_state[2009]-gun_totals_groupby_state[2005])/gun_totals_groupby_state[2005])*100).round(2)
print('Sales growth rate in 2009 is {}%'.format(t_2009))
t_2010=(((gun_totals_groupby_state[2010]-gun_totals_groupby_state[2005])/gun_totals_groupby_state[2005])*100).round(2)
print('Sales growth rate in 2010 is {}%'.format(t_2010))
t_2011=(((gun_totals_groupby_state[2011]-gun_totals_groupby_state[2005])/gun_totals_groupby_state[2005])*100).round(2)
print('Sales growth rate in 2011 is {}%'.format(t_2011))
t_2012=(((gun_totals_groupby_state[2012]-gun_totals_groupby_state[2005])/gun_totals_groupby_state[2005])*100).round(2)
print('Sales growth rate in 2012 is {}%'.format(t_2012))
t_2013=(((gun_totals_groupby_state[2013]-gun_totals_groupby_state[2005])/gun_totals_groupby_state[2005])*100).round(2)
print('Sales growth rate in 2013 is {}%'.format(t_2013))
t_2014=(((gun_totals_groupby_state[2014]-gun_totals_groupby_state[2005])/gun_totals_groupby_state[2005])*100).round(2)
print('Sales growth rate in 2014 is {}%'.format(t_2014))
t_2015=(((gun_totals_groupby_state[2015]-gun_totals_groupby_state[2005])/gun_totals_groupby_state[2005])*100).round(2)
print('Sales growth rate in 2015 is {}%'.format(t_2015))
t_2016=(((gun_totals_groupby_state[2016]-gun_totals_groupby_state[2005])/gun_totals_groupby_state[2005])*100).round(2)
print('Sales growth rate in 2016 is {}%'.format(t_2016))
t_2017=(((gun_totals_groupby_state[2017]-gun_totals_groupby_state[2005])/gun_totals_groupby_state[2005])*100).round(2)
print('Sales growth rate in 2017 is {}%'.format(t_2017))


# In[ ]:





# In[ ]:


##ok we know rate of growth for every year ,what about expicting the groth rate for the next year
##we make list for which year rate we get 
expect_list=pd.Series([t_2006,t_2007,t_2008,t_2009,t_2010,t_2011,t_2012,t_2013,t_2014,t_2015,t_2016,t_2017])


# In[ ]:


ecpected=expect_list.sum()/expect_list.count()##mean =Sum of items over the number of items


# In[ ]:


print('we ecpected to next year to get {}% for Sales growth rate in 2018'.format(ecpected))


# In[ ]:


gun_totals_groupby_month=df_gun_totals_for_rate.groupby(df_gun['month'] ).sum()
##time 


# In[ ]:


ax = gun_totals_groupby_month.loc['2005':'2017'].plot(figsize=(20,10),fontsize=15) 
legend =['']
for i in range(2006,2017): 
    ax = gun_totals_groupby_month.loc[str(i):str(i+1)].plot(ax=ax)
    legend.append(str(i))
ax.legend(legend,fontsize=20)
ax.set_xticks(np.arange(12))
ax.set_title('Yearly Pattern 2006-2017', fontsize=25)
ax.set_xlabel('years', fontsize=25)
ax.set_ylabel('Total', fontsize=25);
ax.plot()


# <a id='conclusions'></a>
# ## Conclusions
# 
# > **Tip**:1) the biggest market for all types is Kentucky with 84% high school graduates and 22% college graduates and in states that have a high rate of college graduates we see the seller go down like new york but it's Not the only cause the biggest one is where white race is becuse the biggest buyer is the white race firist and black race second and the other races looklike they don't have a marcket 
# 
# > **Tip**2)the growth  rate is going high since 2012 and is expected to  going down then 100% for coming years 
# 
# > **Tip**3)long gun is  the best-seller next is the handgun we must focus on them
# 
# > **Tip**4)we must focus on Kentucky we need more diteiles about it it have around 4.5 m pipole and its normal number to other state but it salle About 6 times its population There is some factors missing 
# 
# 
# 
# 
# 
# 
# ## Submitting your Project 
# 
# > **Tip**: Before you submit your project, you need to create a .html or .pdf version of this notebook in the workspace here. To do that, run the code cell below. If it worked correctly, you should get a return code of 0, and you should see the generated .html file in the workspace directory (click on the orange Jupyter icon in the upper left).
# 
# > **Tip**: Alternatively, you can download this report as .html via the **File** > **Download as** submenu, and then manually upload it into the workspace directory by clicking on the orange Jupyter icon in the upper left, then using the Upload button.
# 
# > **Tip**: Once you've done this, you can submit your project by clicking on the "Submit Project" button in the lower right here. This will create and submit a zip file with this .ipynb doc and the .html or .pdf version you created. Congratulations!

# In[ ]:





# In[ ]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])


# In[ ]:





# In[ ]:





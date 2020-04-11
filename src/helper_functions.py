import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='darkgrid')

def get_obese_data(df, lst):
    obesity_data_states = df[df['Question'] == 'Percent of adults aged 18 years and older who have obesity']
    
    tot_obsty_state_dict = dict()
    avg_obsty_state_dict = dict()
    out_fig = plt.figure()
    
    for idx, state in enumerate(lst):

        tot_obsty_state_dict[state] = obesity_data_states[obesity_data_states['LocationAbbr'] == str(state)][['YearStart','Data_Value']]
        avg_obsty_state_dict[state] = tot_obsty_state_dict[state].groupby('YearStart').mean().reset_index()

        sns.lineplot(x='YearStart', y='Data_Value', data=avg_obsty_state_dict[state], label=state)
    plt.xlabel('Year')
    plt.ylabel('Percent Population Obese')
    plt.title('Percent Obesity in Select U.S. States', fontsize=18)
    plt.legend(loc='center right', bbox_to_anchor=(1.20, 0.5))

    plt.show()
    return out_fig

def get_physAct_data(df, lst):
    physAct_data_states = df[df['Question'] == 'Percent of adults who engage in no leisure-time physical activity']

    tot_physAct_state_dict = dict()
    avg_physAct_state_dict = dict()
    out_fig = plt.figure()
    
    for idx, state in enumerate(lst):
        tot_physAct_state_dict[state] = physAct_data_states[physAct_data_states['LocationAbbr'] == str(state)][['YearStart','Data_Value']]
        avg_physAct_state_dict[state] = tot_physAct_state_dict[state].groupby('YearStart').mean().reset_index()

        sns.lineplot(x='YearStart', y='Data_Value', data=avg_physAct_state_dict[state], label=state)
    plt.xlabel('Year')
    plt.ylabel('Percent Population Inactive')
    plt.title('Percent Inactivity in Select U.S. States', fontsize=18)
    plt.legend(loc='center right', bbox_to_anchor=(1.20, 0.5))
    plt.show()
    return out_fig

def get_ntrtnveg_data(df, lst):
    fig_ntrtn = plt.figure(figsize=(6.4*1.4, 4.8*1.1))
    fig_ntrtn.suptitle('Fruit and Vegetable Consumption', fontsize=22)

    plt.title('Less Than 1 Vegetable Daily in Select U.S States')
    
    ax_ntrtn_frt = fig_ntrtn.add_subplot(1,2,1)
    ax_ntrtn_veg = fig_ntrtn.add_subplot(1,2,2)
    
    
    
    
    ntrtnfruit_data_states = df[df['Question'] == 'Percent of adults who report consuming fruit less than one time daily']
    
    tot_ntrtnfruit_state_dict = dict()
    bar_ntrtnfruit_state_dict = dict()
    
    for idx, state in enumerate(lst):
        tot_ntrtnfruit_state_dict[state] = ntrtnfruit_data_states[ntrtnfruit_data_states['LocationAbbr'] == str(state)][['YearStart','Data_Value', 'LocationAbbr']]
           
        df_temp = tot_ntrtnfruit_state_dict[state]
        bar_ntrtnfruit_state_dict[state] = df_temp.rename(columns={"LocationAbbr" : "LocationAbbr_{}".format(state)})
        ax_ntrtn_frt.bar(x=idx, height = bar_ntrtnfruit_state_dict[state]['Data_Value'].mean())

    
    plt.subplot(1,2,1)
    
    
    plt.title('Less Than 1 Fruit \n Daily in Select U.S States')
    plt.ylabel('% Population')
    plt.xticks(ticks = [0, 1, 2, 3, 4, 5], labels=['CA', 'TX', 'FL', 'NY', 'PA', 'NJ'])
    plt.ylim(0,42)
    



    ntrtnveg_data_states = df[df['Question'] == 'Percent of adults who report consuming vegetables less than one time daily']
    
    tot_ntrtnveg_state_dict = dict()
    bar_ntrtnveg_state_dict = dict()
    
    for idx, state in enumerate(lst):
        tot_ntrtnveg_state_dict[state] = ntrtnveg_data_states[ntrtnveg_data_states['LocationAbbr'] == str(state)][['YearStart','Data_Value', 'LocationAbbr']]
           
        df_temp = tot_ntrtnveg_state_dict[state]
        bar_ntrtnveg_state_dict[state] = df_temp.rename(columns={"LocationAbbr" : "LocationAbbr_{}".format(state)})
        ax_ntrtn_veg.bar(x=idx, height = bar_ntrtnveg_state_dict[state]['Data_Value'].mean())
    plt.subplot(1,2,2)
    plt.title('Less Than 1 Vegetable \n Daily in Select U.S States')
    
    
    plt.xticks(ticks = [0, 1, 2, 3, 4, 5], labels=['CA', 'TX', 'FL', 'NY', 'PA', 'NJ'])
    plt.ylim(0,42)
    
    
    
    
    plt.tight_layout()
    ax_ntrtn_veg.tick_params(axis='y', which='left')
    #plt.setp(ax_ntrtn_veg.get_yticklabels(), visible=False)
    plt.subplots_adjust(top=0.8)
    plt.show()
    return fig_ntrtn
 


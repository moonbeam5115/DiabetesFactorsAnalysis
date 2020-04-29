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
 
def join_dataframes(data_dict, factor_list):

    cdc_df_dict = dict()
    df_list = list()
    
    for idx, val in enumerate(factor_list):
        cdc_df_dict[val] = data_dict[factor_list[idx]]
    
    count = 1

    if len(cdc_df_dict)>4 :
        for key, val in cdc_df_dict.items():
            cdc_df_dict[key] = val.rename(columns={'Data_Value': '{}'.format(factor_list[count-1])})
            cdc_df_dict[key] = pd.DataFrame(cdc_df_dict[key].groupby('StateAbbr').mean()[key])
            if count <= len(cdc_df_dict) and count > 0:
                curr_df = cdc_df_dict[factor_list[count-1]][factor_list[count-1]]
                df_list.append(curr_df)
        
            count +=1
    else:
        rename_list = ['Obesity', 'Inactivity', 'Lack Fruit', 'Lack Veggies']
        for key, val in cdc_df_dict.items():
            cdc_df_dict[key] = val.rename(columns={'Data_Value': '{}'.format(rename_list[count-1])})
            cdc_df_dict[key] = pd.DataFrame(cdc_df_dict[key].groupby('LocationAbbr').mean()[rename_list[count-1]])
            if count <= len(cdc_df_dict) and count > 0:
                curr_df = cdc_df_dict[factor_list[count-1]][rename_list[count-1]]
                df_list.append(curr_df)
            # cdc_df_dict[key] = val.rename(columns={factor_list[count-1]: '{}'.format(rename_list[count-1])}) 
            count +=1
            

    return df_list
    


def make_heat_map(df):
    
    corr = df.corr()
    corr_hlth_var_Fig = plt.figure(figsize=(6.4*1.4, 4.8*1.1))
    ax = sns.heatmap(
        corr, 
        vmin=-1, vmax=1, center=0,
        cmap=sns.diverging_palette(20,250, n=200),
        square=True
    )
    ax.set_title('Correlation Among Health Variables', pad=20, fontsize=18)
    ax.set_yticklabels(ax.get_yticklabels(), rotation=0, horizontalalignment='right')
    plt.show()
    return corr_hlth_var_Fig



def plotdist(df):
    inactive_dist_fig_01 = plt.figure()
    ax = sns.distplot(
        df['Data_Value'], norm_hist=False, kde=False, bins=50, hist_kws={'alpha': 1}
    )

    ax.set_title('Inactivity Data Distribution', pad=25, fontsize=20)
    ax.set_xlabel('Percent', fontsize=16)
    ax.set_ylabel('Count', fontsize=16)
    plt.show()

    return inactive_dist_fig_01

def distsubplots(dictionary):
    factor_list = ['Inactivity', 'Lack of Sleep', 'Drinking', 'Smoking', 'Diabetes', 'Obesity']
    distr_tot_fig, axs = plt.subplots(2, 3, sharex='col', sharey='row',figsize=(6.4*1.5, 4.8*1.2))
    distr_tot_fig.suptitle('Data Distribution for Select Health Variables', fontsize=20)
    distr_tot_fig.subplots_adjust(hspace=0.4, wspace=0.2)
    distr_tot_fig.text(0.04, 0.5, 'Count', va='center', rotation='vertical', fontsize=15)
    distr_tot_fig.text(0.5, 0.04, 'Percent', ha='center', rotation='horizontal', fontsize=15)

    count = 0
    for i in range(2):
        for j in range(3):
            axs[i,j].hist(dictionary[factor_list[count]]['Data_Value'], bins=20, color='skyblue')
            axs[i,j].set_title('{}'.format(factor_list[count]))
            count += 1
    mycountx = 0
    mycounty = 0
    for ax in axs.flat:
        if mycountx == 0 or mycountx == 3:
            #ax.set(ylabel='Count')
            pass

        if mycounty == 1 and mycountx >= 0:
            #ax.set(xlabel='Percent')
            pass
        mycountx += 1
        
        if mycountx == 3:
            mycounty += 1
    
    return distr_tot_fig



def corrsubplots(df):
    factor_list2 = ['Inactivity', 'Lack of Sleep', 'Drinking', 'Obesity', 'Diabetes', 'Smoking']

    tot_corr_fig2, axs2 = plt.subplots(2, 3, sharex='col', sharey='row',figsize=(6.4*2, 4.8*1.8))
    tot_corr_fig2.suptitle('Correlation Amongst Select \n Health Variables', fontsize=22)
    tot_corr_fig2.subplots_adjust(hspace=0.5, wspace=0.1)
    tot_corr_fig2.text(0.04, 0.5, '% Population Diabetic', va='center', rotation='vertical', fontsize=18)

    mygrid = plt.GridSpec(2, 3, wspace=0.2)

    count = 0
    for i in range(2):
        for j in range(3):
            if axs2[i,j] == axs2[1,1]:
                count+=1
                axs2[1,1].set_visible(False)
                
                continue
            axs2[i,j].scatter(x=df[factor_list2[count]], y=df['Diabetes'], color='skyblue')
            axs2[i,j].set_title('{}'.format(factor_list2[count]), fontsize=16)
            count += 1
    mycountx = 0
    mycounty = 0


    woot = axs2[0,1].get_xaxis()
    woot.set_visible(True)
    axs2[0,1].tick_params(axis='x', reset=True, length=0.0)



    for ax in axs2.flat:
        # if mycountx == 0 or mycountx == 3:
        #     ax.set(ylabel='Percent Diabetic')
        if mycounty == 0 and mycountx == 1:
            ax.set_xlabel('% of Population', fontsize=14)
            
            

        if mycounty == 1 and mycountx >= 0:
            ax.set_xlabel("% of Population", fontsize=14)
        mycountx += 1
        
            
        
        if mycountx == 3:
            mycounty += 1

    plt.tight_layout(pad=8.0, h_pad=3.75, w_pad=2.75)

    return tot_corr_fig2
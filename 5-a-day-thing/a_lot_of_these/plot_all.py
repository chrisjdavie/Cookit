'''
Plots bar charts of how many portions of fruit and veg
a day are consumed by various demographic groups in the
UK.

Plots pngs of all applicable data files in 'base_dir'
Saves the pngs in 'pic_dir'

Demographics plotted:  
    gross income quintile group, UK Reigons, 
    school leaving age, old age, household composition,
    income decile


Created on 13 Nov 2014

@author: chris
'''


def main():
    
    from quintiles import get_fruit_n_veg_data, plottity
    import matplotlib.pyplot as pl
    
    base_dir = '/home/chris/Projects/Cookit/family-food-datasets/'
    pic_dir = base_dir + 'plots/'
    
    fig_i = -1
    
    
    '''gross income quintile group'''
    suff = 'ConsINCHH-12dec13.xls'
    fname = base_dir + suff
      
    quintiles_dat = get_fruit_n_veg_data(fname)
      
    quints_to_plot = [ 'Quintile 1', 'Quintile 2', 'Quintile 3', 'Quintile 4', 'Quintile 5' ]
  
    fig_i += 1
    plottity(quintiles_dat, quints_to_plot, ('Q1', 'Q2', 'Q3', 'Q4', 'Q5'), 'Household Income Quintiles', 'income quintile', fig_i)
    
    pl.gcf().subplots_adjust(bottom=0.15,top=0.95)
    pl.savefig(pic_dir + suff[:-4] + '.png', format='png')
    
#     pl.show()
    pl.clf()
    
     
    '''UK Reigons'''
    
    suff = 'ConsGORHH-12dec13.xls'
    fname = base_dir + suff
      
    regions_dat = get_fruit_n_veg_data(fname)
  
    Countries = [ 'England', 'Wales', 'Scotland', 'Northern Ireland' ]
      
    fig_i += 1
    plottity(regions_dat, Countries, Countries, 'Countries in the UK', 'country', fig_i)

    pl.gcf().subplots_adjust(bottom=0.15,top=0.95)
    pl.savefig(pic_dir + suff[:-4] + '_countries_' + '.png', format='png')
    pl.clf()
      
    England_areas = [ 'North East', 'North West', 'Yorkshire and The Humber', 'South West', 'South East', 'East Midlands', 'West Midlands', 'London' ]
    England_labels = [ 'North\n East', 'North\n West', 'Yorkshire', 'South\n West', 'South\n East', 'East\n Midlands', 'West\n Midlands', 'London' ]
 
    fig_i += 1
    plottity(regions_dat, England_areas, England_labels, 'Regions in England', 'region', 2)

    pl.gcf().subplots_adjust(bottom=0.15,top=0.95)
    pl.savefig(pic_dir + suff[:-4] + '_regions_' + '.png', format='png')
    pl.clf()
    
    
    '''By school leaving age'''
    suff = 'ConsAGEHRPEDHH-12dec13.xls'
    fname = base_dir + suff
      
    dat = get_fruit_n_veg_data(fname)
      
    Ages = [ 'Aged 14 and Under', 'Aged 15', 'Aged 16', 'Aged 17 and under 19', 'Aged 19 and Under 22', 'Aged 22 or over' ]     
    Ages_labels = [ '<14', '15', '16', '>= 17\n and < 19', '>= 19\n < 22', '>= 22' ]
      
    fig_i += 1
    plottity(dat, Ages, Ages_labels, 'Age ranges', 'age', fig_i)
    
    pl.gcf().subplots_adjust(bottom=0.15,top=0.95)
    pl.savefig(pic_dir + suff[:-4] + '.png', format='png')
    pl.clf()
        
      
    '''By old age'''
    suff = 'ConsAGEHRPHH-12dec13.xls'
    fname = base_dir + suff
      
    dat = get_fruit_n_veg_data(fname)
      
    Ages = [ 'Under 30', '30-39', '40-49', '50-64', '65-74', '75 and over' ]
      
    Ages_labels = [ 'Under 30', '30-39', '40-49', '50-64', '65-74', '75\n and over' ]
      
    fig_i += 1
    plottity(dat, Ages, Ages_labels, 'Age ranges', 'age', fig_i)
    
    pl.gcf().subplots_adjust(bottom=0.15,top=0.95)
    pl.savefig(pic_dir + suff[:-4] + '.png', format='png')
    pl.clf()   
     
         
    '''By household composition'''
    suff = 'ConsCOMPHH-12dec13.xls'
    fname = base_dir + suff
      
    dat = get_fruit_n_veg_data(fname)
      
    Comps = [ 'Adult1 Child0', 'Adult1 Child1+', 'Adult2 Child0', 'Adult2 Child1', 'Adult2 Child2', 'Adult2 Child3', 'Adult2 Child4+']  
    Comps_label = [ '1, 0', '1, >=1', '2, 0', '2, 1', '2, 2', '2, 3', '2, >=4']
      
    fig_i += 1
    plottity(dat, Comps, Comps_label, 'No. adults, no. children in the household', 'household (1)', fig_i, 'upper right')
    
    pl.gcf().subplots_adjust(bottom=0.15,top=0.95)      
    pl.savefig(pic_dir + suff[:-4] + '_1' + '.png', format='png')
    pl.clf()   
    
    Comps = [ 'Adult3+ Child0', 'Adult3+ Child1or2', 'Adult3+ Child3+', 'Adult4+ Child0' ]
    Comps_label = [ '>=3, 0', '>=3, 1 or 2', '>=3, >=3', '>=4, 0' ]
      
    fig_i += 1
    plottity(dat, Comps, Comps_label, 'No. adults, no. children in the household', 'household (2)', fig_i, 'upper right')
    
    pl.gcf().subplots_adjust(bottom=0.15,top=0.95)
    pl.savefig(pic_dir + suff[:-4] + '_2' + '.png', format='png')
    pl.clf()   
      
 
    '''Income Decile'''
    suff = 'ConsINCEQUIVHH-12dec13.xls'
    fname = base_dir + suff
     
    dat = get_fruit_n_veg_data(fname)
     
    Decs = [ 'Decile 1', 'Decile 2', 'Decile 3', 'Decile 4', 'Decile 5', 'Decile 6', 'Decile 7', 'Decile 8', 'Decile 9', 'Decile 10' ]
    Decs_label = [ 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10' ]
     
    fig_i += 1
    plottity(dat, Decs, Decs_label, 'Household income deciles', 'income deciles', fig_i)
     
    pl.gcf().subplots_adjust(bottom=0.15,top=0.95)
    pl.savefig(pic_dir + suff[:-4] + '.png', format='png')
    pl.clf() 
     
#     pl.show()
    
    

if __name__ == '__main__':
    main()
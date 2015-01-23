'''
Prototyping excel spreadsheet generation, multiple sheets.

Created on 13 Nov 2014

@author: chris
'''
import matplotlib.pyplot as pl

def main():
    fname = '/home/chris/Projects/Cookit/family-food-datasets/ConsINCHH-12dec13.xls'
    
    quintiles_dat = get_fruit_n_veg_data(fname)
    
    quints_to_plot = [ 'Quintile 1', 'Quintile 2', 'Quintile 3', 'Quintile 4', 'Quintile 5' ]

    plottity(quintiles_dat, quints_to_plot, ('Q1', 'Q2', 'Q3', 'Q4', 'Q5'), 'Household Income Quintiles', 'income quintile')
    
    pl.show()

def plottity(quintiles_dat, quints_to_plot, bar_labels, xlabel, title_bit, fig_i = 1, leg_loc='upper left', yr='2012'):

    q_name_to_plot = [ 'Fresh fruit', 'Processed fruit and fruit products', 'Fresh green vegetables', 'Other fresh vegetables', 'Processed vegetables excluding processed potatoes', 'Pure fruit juices (g)' ]
    divs           = [ 80.0,          80.0,                                 80.0,                     80.0,                     80.0,                                                150.0 ] 
    colours        = [ '#dc1862', '#fa5e79',                                '#31ebf3',                '#d7da52',                '#faf9d9',                                            'firebrick'    ] 
    
    import matplotlib.font_manager as font_manager
    
    path = '/usr/share/fonts/truetype/macfonts/HelveticaNeueBold.ttf'
    propb = font_manager.FontProperties(fname=path)
    
    path = '/usr/share/fonts/truetype/macfonts/HelveticaNeue.ttf'
    prop = font_manager.FontProperties(fname=path)
   
    pl.figure(fig_i)
    ax = pl.gca()
    ax.yaxis.grid(True)
    ax.set_axisbelow(True)
    
    width = 0.35
    for i, quint_to_plot in enumerate(quints_to_plot):
        qs = quintiles_dat[quint_to_plot]
        
        stack = []
        
        q_base = 0
        
        ps = []
        
        for q_name, colour, div in zip(q_name_to_plot, colours, divs):
            if q_name == 'Pure fruit juices (g)':
                try:
                    q = qs[q_name]
                except(KeyError):
                    q = qs['Pure fruit juices']
            else:
                q = qs[q_name]
            q = q/div/7.0
            stack.append(q)
            ps.append(pl.bar(i*0.5, q, width, bottom=q_base, color=colour, edgecolor = "none" ))
            q_base += q
       
    import numpy as np
    ind = np.arange(0.0, len(quints_to_plot)/2.0, 0.5)
       
    pl.xlabel(xlabel, fontweight='bold', fontproperties=propb)
    pl.ylabel('Portions/day', fontweight='bold', fontproperties=propb)
    
    pl.ylim(0,7.1)
    
    pl.xticks(ind+width/2., bar_labels, fontproperties=prop )
#     pl.yticks()
    ax.set_yticklabels(ax.get_yticks(), fontproperties=prop )
    lg = pl.legend(ps[::-1], ('Fresh fruit', 'Processed fruit', 'Fresh green vegetables', 'Other fresh vegetables', 'Processed vegetables', 'Fruit juice' )[::-1], loc=leg_loc ) 
    lg.draw_frame(False)
    ltext = lg.get_texts()
    pl.setp(ltext, fontweight='bold', fontproperties=propb)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()   
    ax.xaxis.set_ticks_position('none') 
    
    pl.hlines(5, pl.xlim()[0], pl.xlim()[1],linewidth=1.5, linestyle='--', color='grey')
    
    pl.title('Fruits and vegetable consumption, by ' + title_bit + ', in ' + yr[:4], fontweight='bold', fontproperties=propb)
    
#     pl.show()
    
#     print five_a_weeks

def get_fruit_n_veg_data(fname):
    
    from xlrd import open_workbook
    book = open_workbook(fname,on_demand=True)
    
    
    def form_cat_data(i_des, sheet_name):
        
        print sheet_name
        
        i_units = 5
        i_yr_s  = 6
        i_yr_f  = 18
        
        des   = []
        units  = []
        valss  = [] 
        
        sheet = book.sheet_by_name(sheet_name)
        col_des   = sheet.col(i_des)
        col_units = sheet.col(i_units)
        
        yrs_i = {}
        for i in range(i_yr_s,i_yr_f):
            yrs_i[str(sheet.col(i)[7].value)] = i
        
        j_off = 7
        j_cat = [  ]
        for j, row in enumerate(col_des[j_off:]):
            if len(row.value) != 0:
                j_cat.append(j)
        
#         print j_cat
        for j in j_cat:
            j = j + j_off
            des.append(col_des[j].value)
            units.append(col_units[j].value)
            
            vals = {}
            for yr in yrs_i.keys():
                vals[yr] = sheet.col(yrs_i[yr])[j].value
            
            valss.append(vals)
                
        return des, units, valss
    

    quintiles_dat = {}

    for sheet_name in book.sheet_names()[:-1]:
#     '''Main Catagory level'''
#     des1, units1, valss1 = form_cat_data(1)        
        '''Sub-catagory level'''
        des2, units2, valss2 = form_cat_data(2,sheet_name)
        '''Sub-sub-catagory level'''
        des3, units3, valss3 = form_cat_data(3,sheet_name)
            
        interest = [ 'Fresh green vegetables', 'Other fresh vegetables', 'Processed vegetables excluding processed potatoes', 'Fresh fruit', 'Processed fruit and fruit products', 'Pure fruit juices (g)', 'Pure fruit juices' ]#'Fresh and processed vegetables, excluding potatoes', 'Fresh and processed fruit' ]
        units = {}
    
        amount_a_weeks = {}
        for d, u, v in zip(des3,units3,valss3):    
            if d in interest:
                units[d] = u
                amount_a_weeks[d] = v['2012.0']
        for d, u, v in zip(des2,units2,valss2):    
            if d in interest:
                units[d] = u
                amount_a_weeks[d] = v['2012.0']    
        
        quintiles_dat[sheet_name] = amount_a_weeks

    return quintiles_dat

if __name__ == '__main__':
    main()
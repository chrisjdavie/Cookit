'''
Created on 13 Nov 2014

@author: chris
'''
from distutils.file_util import move_file

def main():
    
#     from quintiles import plottity
#     import matplotlib.pyplot as pl
        
    base_dir = '/home/chris/Projects/Cookit/family-food-datasets/'

#     pic_dir = '/tmp/movie/'
#     
#     fig_i = 0
    
    '''By old age'''
    suff = 'ConsAGEHRPHH-12dec13.xls'
    fname = base_dir + suff
      
    dat = get_fruit_n_veg_data(fname)
    
    movie_dat_fname = '/home/chris/Projects/Cookit/family-food-datasets/movie_dat/dat.p'
    
    import pickle
    
    with open(movie_dat_fname,'w+') as f:
        pickle.dump(dat,f)
      
#     Ages = [ 'Under 30', '30-39', '40-49', '50-64', '65-74', '75 and over' ]
#       
#     Ages_labels = [ 'Under 30', '30-39', '40-49', '50-64', '65-74', '75\n and over' ]
#       
#     fig_i += 1
#     plottity(dat, Ages, Ages_labels, 'Age ranges', 'age', fig_i)
#     
#     pl.gcf().subplots_adjust(bottom=0.15,top=0.95)
#     pl.savefig(pic_dir + suff[:-4] + '.pdf', format='pdf')
#     pl.clf()   

def get_fruit_n_veg_data(fname):
    
    from xlrd import open_workbook
    book = open_workbook(fname,on_demand=True)
    
    
    def form_cat_data(i_des, sheet_name):
        
#         print sheet_name
        
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
    

    

    years = ['2003-04', '2011.0', '2007.0', '2008.0', '2012.0', '2006.0', '2001-02', '2009.0', '2004-05', '2005-06', '2010.0', '2002-03']
    
    years_dat = {}
    for yr in years:
        print yr
        quintiles_dat = {}
        for sheet_name in book.sheet_names()[:-1]:
            print sheet_name
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
                    amount_a_weeks[d] = v[yr]
#                     print v.keys()
#                     raw_input() 
            for d, u, v in zip(des2,units2,valss2):    
                if d in interest:
                    units[d] = u
                    amount_a_weeks[d] = v[yr] 
                    
            
            quintiles_dat[sheet_name] = amount_a_weeks
        years_dat[yr] = quintiles_dat
    

    return years_dat     

if __name__ == '__main__':
    main()
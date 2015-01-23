'''
Created on 14 Nov 2014

@author: chris
'''
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
    
    #dat_fname = '/home/chris/Projects/Cookit/family-food-datasets/movie_dat/' + suff[:-4] + '.csv'  
    

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
                amount_a_weeks[d] = v
#                     print v.keys()
#                     raw_input() 
        for d, u, v in zip(des2,units2,valss2):    
            if d in interest:
                units[d] = u
                amount_a_weeks[d] = v
                
        
        quintiles_dat[sheet_name] = amount_a_weeks
    

    return quintiles_dat   

if __name__ == '__main__':
    main()
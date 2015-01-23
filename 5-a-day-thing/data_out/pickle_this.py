'''
Pickles the data on how many of the five a day people eat.

It also finds how much of the 5-a-day people eat.

It's more for that function and testing it, this function
is now mainly called elsewhere.

Created on 14 Nov 2014

@author: chris
'''
def main():
        
    base_dir = '/home/chris/Projects/Cookit/family-food-datasets/'
    
    '''By old age'''
    suff = 'ConsAGEHRPHH-12dec13.xls'
    fname = base_dir + suff
      
    dat, units, book_name = get_fruit_n_veg_data(fname)
    
    import pickle
    with open('/tmp/test.p','w+') as f:
        pickle.dump([dat,units,book_name], f)
    

def get_fruit_n_veg_data(fname):
    return get_data(fname,interest = [ 'Fresh green vegetables', 'Other fresh vegetables', 'Processed vegetables excluding processed potatoes', 'Fresh fruit', 'Processed fruit and fruit products', 'Pure fruit juices (g)', 'Pure fruit juices' ] )#'Fresh and processed vegetables, excluding potatoes', 'Fresh and processed fruit' ])
    
def get_data(fname,interest):
    '''finds and extracts the rows in file 'fname' associated with the row title 'interest' 
           
       returns dat, units, bookname
       dat      - dict[sheet name][catagory name][year] 
       units    - dict[catagory name]
       bookname - name of workbook, mostly unused now
          
       This works for the data format of the spreadsheets at https://www.gov.uk/government/statistical-data-sets/family-food-datasets '''
    
    from xlrd import open_workbook
    book = open_workbook(fname,on_demand=True)
    
    
    def form_cat_data(i_des, sheet_name):
        
        '''moves down rows in sheet 'sheet_name',
           saving the descriptions in column 'i_des'
           and the corresponding data.

           returns des[]   - column descriptions
                   units[] - units of column
                   valss[] - column values, each is dict
                              val[year], the value for
                              that year
           
           This is a hacky way of doing this - if it slows
           things down too much, just have this explore all
           the 3 description columns and save the not empty
           one for the description.
           
           Is working atm.  '''
#         print sheet_name
        
        i_units = 5
        i_yr_s  = 6
        i_yr_f  = 18
        
        des   = []
        units  = []
        valss  = [] 
        
        sheet = book.sheet_by_name(sheet_name)
        
#         print book_name
#         raw_input()
        
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
        
    dat = {}
    '''cycles through each sheet in the book'''
    for sheet_name in book.sheet_names()[:-1]:
        print sheet_name
#     '''Main Catagory level'''
#     des1, units1, valss1 = form_cat_data(1)        
        '''description, units, values'''
        '''Sub-catagory level'''
        des2, units2, valss2 = form_cat_data(2,sheet_name)
        '''Sub-sub-catagory level'''
        des3, units3, valss3 = form_cat_data(3,sheet_name)
            
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
                
        
        dat[sheet_name] = amount_a_weeks
        
        sheet = book.sheet_by_name(sheet_name)
        book_name = sheet.cell(4,0).value 
        print book_name    
        
    return dat, units, book_name

if __name__ == '__main__':
    main()
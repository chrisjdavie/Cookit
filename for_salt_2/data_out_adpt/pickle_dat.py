'''
Pickle the data from the spreadsheet indicated by 'suff' in the 
variable 'interest'.

This is more testing the function, it is mostly being called 
elsewhere.

Created on 7 Jan 2015

@author: chris
'''
def main():
    base_dir = '/home/chris/Projects/Cookit/family-food-datasets/2014/'
    
    '''By income quintile'''
    '''Weight'''
    suff = 'ConsINCHH-11dec14.xls'
    fname = base_dir + suff
      
    dat_wei, units_wei, book_name_wei = get_spec_data(fname)
    
    '''Price'''
    suff = 'ExpINC-11dec14.xls'
    fname = base_dir + suff
    
    dat_pri, units_pri, book_name_pri = get_spec_data(fname)
    
    import pickle
    with open('/tmp/salt_sug_test.p','w+') as f:
        pickle.dump([dat_wei,units_wei,book_name_wei,dat_pri, units_pri, book_name_pri], f)
    
def get_spec_data(fname):
    interest = [ 'Sugar', 'Salt', 'vegetables', 'potatoes', 'Fresh fruit', 'Processed fruit' ]
    return get_data(fname, interest, i_cats=[2])
    #[ 'Fresh', 'Processed', 'Soft drinks', 'Fat' ]
    
# def get_processed_fresh_data(fname):
#     interest = [  ]
#     return get_data(fname, interest, i_cats=[2])
    #[ 'Fresh', 'Processed', 'Soft drinks', 'Fat' ]    
    
def get_data(fname,interest,i_cats=[2,3]):
    '''this finds if the terms in 'interest' are in the file
        denoted by 'fname' '''
    
    '''finds and extracts the rows in file 'fname' associated with the row title 'interest' 
        
       'i_cats' indicates the ith column to search for descriptions
       held in 'interest'.  This is done as strings such as 
       'Sugar' sometimes appear multiple times, and would require
       more sophisticated string handeling.  It works now.
           
       returns dat, units, bookname
       dat      - dict[sheet name][catagory name][year] 
       units    - dict[catagory name]
       bookname - name of workbook, mostly unused now
          
       This works for the data format of the spreadsheets at https://www.gov.uk/government/statistical-data-sets/family-food-datasets '''
    
    
    from xlrd import open_workbook
    book = open_workbook(fname,on_demand=True)
    
    def _form_cat_data(i_des, sheet_name):
        return form_cat_data(i_des, sheet_name, book)
        
    quintiles_dat = {}
    for sheet_name in book.sheet_names()[:-1]:
        print sheet_name
        
        units = {}
        
        amount_a_weeks = {}
        
        for i_cat in i_cats:
            '''Catagory level'''
            des_f, units_f, valss_f = _form_cat_data(i_cat,sheet_name)
            for d, u, v in zip(des_f,units_f,valss_f):
                
                if any(i in d for i in interest):
                    units[d] = u
                    amount_a_weeks[d] = v
                
                
        quintiles_dat[sheet_name] = amount_a_weeks
        
        sheet = book.sheet_by_name(sheet_name)
        book_name = sheet.cell(4,0).value
        print book_name    
        
    return quintiles_dat, units, book_name    

    
def form_cat_data(i_des, sheet_name, book):
        ''' This retrieves all the data in the spreadsheet, I then
            parse it according to the search criteria. (whatever
            that is)
            
            moves down rows in sheet 'sheet_name',
            saving the descriptions in column 'i_des'
            and the corresponding data.
            
            returns des[]   - column descriptions
                    units[] - units of column
                    valss[] - column values, each is dict
                              val[year], the value for
                              that year            
            
            '''
        
#         print sheet_name
        
        i_units = 5
        i_yr_s  = 6
        i_yr_f  = 19
        
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

if __name__ == '__main__':
    main()
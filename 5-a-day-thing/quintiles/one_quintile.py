'''
Prototyping excel sheet generation.

Single sheet.

Created on 13 Nov 2014

@author: chris
'''
def main():
    fname = '/home/chris/Projects/Cookit/family-food-datasets/ConsINCHH-12dec13.xls'
    
    
    from xlrd import open_workbook
    book = open_workbook(fname,on_demand=True)
    
    
    def form_cat_data(i_des):
        i_units = 5
        i_yr_s  = 6
        i_yr_f  = 18
        
        des   = []
        units  = []
        valss  = [] 
        
        for sheet_name in book.sheet_names()[:1]:
            sheet = book.sheet_by_name(sheet_name)
            col_des   = sheet.col(i_des)
#             print col_des
            col_units = sheet.col(i_units)
            
            yrs_i = {}
            for i in range(i_yr_s,i_yr_f):
                yrs_i[str(sheet.col(i)[7].value)] = i
            
            j_off = 7
            j_cat = [  ]
            for j, row in enumerate(col_des[j_off:]):
                if len(row.value) != 0:
                    j_cat.append(j)
#                     print row.value, len(row.value)
#                     raw_input()
            
            print j_cat
            for j in j_cat:
                j = j + j_off
                des.append(col_des[j].value)
#                 print col_des[j], col_des[j].value 
#                 raw_input()
                units.append(col_units[j].value)
                
                vals = {}
                for yr in yrs_i.keys():
                    vals[yr] = sheet.col(yrs_i[yr])[j].value
                
                valss.append(vals)
                
        return des, units, valss
    
    
    
#     '''Main Catagory level'''
#     des1, units1, valss1 = form_cat_data(1)
    '''Sub-catagory level'''
    des2, _, valss2 = form_cat_data(2)
    '''Sub-sub-catagory level'''
    des3, _, valss3 = form_cat_data(3)
#     
#     for d, u, v in zip(des3,units3,valss3):
#         print [d], u, v['2012.0'], 'bob'
        
    interest = [ 'Fresh green vegetables', 'Other fresh vegetables', 'Processed vegetables excluding processed potatoes', 'Fresh fruit', 'Processed fruit and fruit products', 'Pure fruit juices (g)' ]#'Fresh and processed vegetables, excluding potatoes', 'Fresh and processed fruit' ]

    five_a_weeks = {}
    for d, v in zip(des3,valss3):    
        if d in interest:
            five_a_weeks[d] = v['2012.0']
    for d, v in zip(des2,valss2):    
        if d in interest:
            five_a_weeks[d] = v['2012.0']    
    
    print five_a_weeks
    
#         print col_units[7]
#             print i, cell
# #             print dir(cell)
# #             print cell.value
#             if cell.value == '501':
#                 raw_input()
#         print name

if __name__ == '__main__':
    main()
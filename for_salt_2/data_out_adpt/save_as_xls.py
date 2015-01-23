'''
Opens the pickled test food data, and saves it as
a spreadsheet.  

Is more for developing and debugging, these fuctions 
are mostly called elsewhere.  


Created on 8 Jan 2015

@author: chris
'''

import xlwt

def main():
    workbook = xlwt.Workbook()
    
    import pickle
    with open('/tmp/salt_sug_test.p','rb') as f:
        dat_wei,units_wei, _,dat_pri, units_pri, _ = pickle.load(f)
    
#     import pickle
    with open('/tmp/total_test.p','rb') as f:
        dat_pri_tot, units_pri_tot, _ = pickle.load(f)
    
    gen_wb(workbook, dat_wei, units_wei, dat_pri, units_pri, dat_pri_tot, units_pri_tot)
    workbook.save('/tmp/tst.xls')    
    
    
#     test_dat_wei = dat_wei['Under 30']
#     print test_dat_wei.keys()
#     for a in test_dat_wei: print a, test_dat_wei[a]
def gen_wb(workbook, dat_wei, units_wei, dat_pri, units_pri, dat_pri_tot, units_pri_tot):
    import numpy as np
    
    bold_style = xlwt.easyxf('font: bold 1')
    
    cat_keys = dat_wei.keys()
    ordr = [ float(k.split('_')[1]) for k in cat_keys ]
    i_sort = np.argsort(ordr)
    cat_keys = np.array(cat_keys)[i_sort]
    
    print cat_keys
    
#     fud_keys = dat_wei[cat_keys[0]].keys()
    fud_keys = [u'Sugar', u'Salt', u'Processed fruit and fruit products', u'Fresh fruit', u'Processed potatoes', u'Fresh potatoes', u'Processed vegetables excluding processed potatoes', u'Fresh green vegetables', u'Other fresh vegetables']
    print fud_keys
    
    yrs_keys = dat_wei[cat_keys[0]][fud_keys[0]].keys()
    ordr = [ k[2:4] for k in yrs_keys ]
    i_sort = np.argsort(ordr)
    yrs_keys = np.array(yrs_keys)[i_sort]
    
    print yrs_keys
    
    for fud_key in fud_keys:
        sheet_name = fud_key.split(' ')
#         print sheet_name
        if len(sheet_name) > 2 and (sheet_name[2] == 'fruit' or sheet_name[2] == 'vegetables'):
            sheet_name = sheet_name[0]+' '+sheet_name[1]+' '+sheet_name[2]
        elif len(sheet_name) > 1:
            sheet_name = sheet_name[0]+' '+sheet_name[1]
        else:
            sheet_name = sheet_name[0]
            
        sheet = workbook.add_sheet(sheet_name)
        
        sheet.write(0, 0, fud_key, bold_style)        
        
        j_0 = 2
        i_0 = 1
        
        j = build_fud_sheet(sheet, i_0, j_0, dat_wei, 'Purchased weights', 'g per person per week', fud_key, cat_keys, yrs_keys, bold_style)
        
        j_0 = 4+j+j_0
        
        build_fud_sheet(sheet, i_0, j_0, dat_pri, 'Expenditure', 'pence per person per week', fud_key, cat_keys, yrs_keys, bold_style)
    
    total_str = 'Total food and non-alcoholic drinks'
    short_total_str = 'Total food and drink'
    
    sheet = workbook.add_sheet(short_total_str)
    
    sheet.write(0, 0, total_str, bold_style)
    
    build_fud_sheet(sheet, i_0, j_0, dat_pri_tot, 'Expenditure', 'pence per person per week', 'cat105', cat_keys, yrs_keys, bold_style)
    
    
def build_fud_sheet(sheet,i_0,j_0,dat,des,units,fud_key,cat_keys,yrs_keys,bold_style):
    sheet.write(j_0,   0,   des, bold_style)
    sheet.write(j_0+1, i_0, 'Units', bold_style)
    sheet.write(j_0+1, i_0+1, units, bold_style)
    
    for i, yr_k in enumerate(yrs_keys):
        sheet.write(j_0+1, i_0+3+i, yr_k, bold_style)
    
    for j, cat_key in enumerate(cat_keys):
        sheet.write(2+j+j_0, i_0+2, cat_key, bold_style)
        
        for i, yr_k in enumerate(yrs_keys):
            sheet.write(2+j+j_0, i_0+3+i, dat[cat_key][fud_key][yr_k])
    
    return j
    
def gen_sheet_old(workbook, dat_wei, units, book_name):
    bold_style = xlwt.easyxf('font: bold 1')
    
    sheet = workbook.add_sheet(book_name)
    
    yr_keys = dat_wei[dat_wei.keys()[0]]['Fresh fruit'].keys()
    ordr = [ k[2:4] for k in yr_keys ]
    
    import numpy as np
    
    i_sort = np.argsort(ordr)
    yr_keys = np.array(yr_keys)[i_sort]
    
    for i, yr_k in enumerate(yr_keys):
        sheet.write(1, 4+i, yr_k, bold_style)
        
    sheet.write(1, 3, 'Units', bold_style)  
        
    j_0 = -2
    for age in dat_wei.keys():
        j_0 += 3
        sheet.write(1+j_0, 1, age, bold_style)
    
        for j, fud_type in enumerate(dat_wei[age].keys()):
#             print j, j+j_0
            sheet.write(2+j+j_0, 2, fud_type, bold_style)
            sheet.write(2+j+j_0, 3, units[fud_type], bold_style)
                        
            for i, yr_k in enumerate(yr_keys):
                sheet.write(2+j+j_0, 4+i, dat_wei[age][fud_type][yr_k])
        
        j_0 = j+j_0
        
        
if __name__ == '__main__':
    main()
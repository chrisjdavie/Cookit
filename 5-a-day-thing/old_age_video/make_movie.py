'''
This makes a movie of the bar charts between each year. It doesn't
actually make the movie, it outputs a few hundred images.  Using
command line tools to stich them together.

It doesn't really show what I intended, but it does make a movie.  

Created on 13 Nov 2014

@author: chris
'''


def main():
    
    from quintiles import plottity
    import matplotlib.pyplot as pl
    
    pic_dir = '/tmp/movies/'
    
    fig_i = 0
    
    '''By old age'''
    
    fname = '/home/chris/Projects/Cookit/family-food-datasets/movie_dat/dat.p'
    
    import pickle
    with open(fname,'rb') as f:
        dat = pickle.load(f)
      
    Ages = [ 'Under 30', '30-39', '40-49', '50-64', '65-74', '75 and over' ]
      
    years = ['2003-04', '2011.0', '2007.0', '2008.0', '2012.0', '2006.0', '2001-02', '2009.0', '2004-05', '2005-06', '2010.0', '2002-03']
    nums  = [ 3,        11,        7,       8,        12,       6,        1,         9,         4,         5,        10,       2              ]
    import numpy as np
    i_sort = np.argsort(nums)
    years = np.array(years)[i_sort]
    
    years = sorted(years)
    i_m = 0
    for yr_0, yr_1 in zip(years[:-1],years[1:]):
#         yr_0  = years[-2]
        dat_0 = dat[yr_0]
#         yr_1  = years[-1]
        dat_1 = dat[yr_1]
        
        fs  = 25.0
        sp0 = 1.0/fs
        
        sps = np.arange(0.0,1.0,sp0)
        
        for sp in sps:
        
            dat_sp = {}
              
            for Age in Ages:
                a_s0 = dat_0[Age]
                a_s1 = dat_1[Age]
                
                a_ssp = {}
                
                for a_name in a_s0.keys():
                    v0 = a_s0[a_name]
                    v1 = a_s1[a_name]
                    
                    vsp = (1.0-sp)*v0 + v1*sp
                     
                    a_ssp[a_name] = vsp
                dat_sp[Age] = a_ssp
              
            Ages_labels = [ 'Under 30', '30-39', '40-49', '50-64', '65-74', '75\n and over' ]
            
            fig_i += 1
            
        #     for yr in years:
        
            plottity(dat_sp, Ages, Ages_labels, 'Age ranges', 'age', fig_i, yr=yr_0)
            
            fig = pl.gcf()
            fig.subplots_adjust(bottom=0.15,top=0.95)
            f_str = 1000 + i_m
            f_str = str(int(f_str))[1:]
            print f_str
            pl.savefig(pic_dir + f_str + '.png', format='png')
            i_m += 1
            pl.close()
            
    yr = years[-1]
    plottity(dat_sp, Ages, Ages_labels, 'Age ranges', 'age', fig_i, yr=yr)
    
    fig = pl.gcf()
    fig.subplots_adjust(bottom=0.15,top=0.95)
    f_str = 1000 + i_m
    f_str = str(int(f_str))[1:]
    print f_str
    pl.savefig(pic_dir + f_str + '.png', format='png')
    pl.close()
    
    
if __name__ == '__main__':
    main()
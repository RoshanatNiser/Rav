# Package ID: knb-lter-mcm.5500.3 Cataloging System:https://pasta.edirepository.org.
# Data set title: Spectral and biological characteristics of microbial mats and mosses across Fryxell Basin, Taylor Valley, Antarctica (2018-2019).
# Data set creator:  Schuyler Borges -  
# Data set creator:  Lee Stanish -  
# Data set creator:  Sarah Power -  
# Data set creator:  Mark Salvatore -  
# Data set creator:  John "Jeb" Barrett -  
# Data set creator:  Eric Sokol -  
# Data set creator:  M. Davis -  
# Metadata Provider:    - McMurdo Dry Valleys LTER 
# Contact:  McMurdo Dry Valleys LTER Information Manager -    - im@mcmlter.org
# Stylesheet v1.3 for metadata conversion into program: John H. Porter, Univ. Virginia, jporter@virginia.edu      
# 
# This program creates numbered PANDA dataframes named dt1,dt2,dt3...,
# one for each data table in the dataset. It also provides some basic
# summaries of their contents. NumPy and Pandas modules need to be installed
# for the program to run. 

import numpy as np
import pandas as pd 

infile1  ="https://pasta.lternet.edu/package/data/eml/knb-lter-mcm/5500/3/103cfd6d96e9c7e411d7630de4b839da".strip() 
infile1  = infile1.replace("https://","http://")
                 
dt1 =pd.read_csv(infile1 
          ,storage_options={'User-Agent':'EDI_CodeGen'}
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "dataset_code",     
                    "unique_id",     
                    "date_collected",     
                    "time_collected",     
                    "stream_name",     
                    "site_id",     
                    "plot_id",     
                    "subplot_id",     
                    "mat_type",     
                    "mat_id",     
                    "moisture_content",     
                    "data_type",     
                    "latitude",     
                    "longitude",     
                    "sample_name",     
                    "sample_id",     
                    "sample_type",     
                    "number_of_cores",     
                    "spectral_id",     
                    "photo_id",     
                    "sample_description",     
                    "filtering_remarks",     
                    "freezer_remarks"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={  
#             'dataset_code':'str' ,  
#             'unique_id':'str' , 
                        
#             'date_collected':'str' , 
                        
#             'time_collected':'str' ,  
#             'stream_name':'str' ,  
#             'site_id':'str' ,  
#             'plot_id':'str' ,  
#             'subplot_id':'str' ,  
#             'mat_type':'str' ,  
#             'mat_id':'str' ,  
#             'moisture_content':'str' ,  
#             'data_type':'str' ,  
#             'latitude':'str' ,  
#             'longitude':'str' ,  
#             'sample_name':'str' ,  
#             'sample_id':'str' ,  
#             'sample_type':'str' ,  
#             'number_of_cores':'str' ,  
#             'spectral_id':'str' ,  
#             'photo_id':'str' ,  
#             'sample_description':'str' ,  
#             'filtering_remarks':'str' ,  
#             'freezer_remarks':'str'  
#        }
          ,parse_dates=[
                        'date_collected',
                        'time_collected',
                ] 
    )
# Coerce the data into the types specified in the metadata  
dt1.dataset_code=dt1.dataset_code.astype('category')  
dt1.unique_id=dt1.unique_id.astype('category') 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt1=dt1.assign(date_collected_datetime=pd.to_datetime(dt1.date_collected,errors='coerce')) 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt1=dt1.assign(time_collected_datetime=pd.to_datetime(dt1.time_collected,errors='coerce'))  
dt1.stream_name=dt1.stream_name.astype('category')  
dt1.site_id=dt1.site_id.astype('category')  
dt1.plot_id=dt1.plot_id.astype('category')  
dt1.subplot_id=dt1.subplot_id.astype('category')  
dt1.mat_type=dt1.mat_type.astype('category')  
dt1.mat_id=dt1.mat_id.astype('category')  
dt1.moisture_content=dt1.moisture_content.astype('category')  
dt1.data_type=dt1.data_type.astype('category')  
dt1.latitude=dt1.latitude.astype('category')  
dt1.longitude=dt1.longitude.astype('category')  
dt1.sample_name=dt1.sample_name.astype('category')  
dt1.sample_id=dt1.sample_id.astype('category')  
dt1.sample_type=dt1.sample_type.astype('category')  
dt1.number_of_cores=dt1.number_of_cores.astype('category')  
dt1.spectral_id=dt1.spectral_id.astype('category')  
dt1.photo_id=dt1.photo_id.astype('category')  
dt1.sample_description=dt1.sample_description.astype('category')  
dt1.filtering_remarks=dt1.filtering_remarks.astype('category')  
dt1.freezer_remarks=dt1.freezer_remarks.astype('category') 
      
print("Here is a description of the data frame dt1 and number of lines\n")
print(dt1.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt1\n")
print(dt1.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 
       
                
print(dt1.dataset_code.describe())               
print("--------------------\n\n")
                    
print(dt1.unique_id.describe())               
print("--------------------\n\n")
                    
print(dt1.date_collected.describe())               
print("--------------------\n\n")
                    
print(dt1.time_collected.describe())               
print("--------------------\n\n")
                    
print(dt1.stream_name.describe())               
print("--------------------\n\n")
                    
print(dt1.site_id.describe())               
print("--------------------\n\n")
                    
print(dt1.plot_id.describe())               
print("--------------------\n\n")
                    
print(dt1.subplot_id.describe())               
print("--------------------\n\n")
                    
print(dt1.mat_type.describe())               
print("--------------------\n\n")
                    
print(dt1.mat_id.describe())               
print("--------------------\n\n")
                    
print(dt1.moisture_content.describe())               
print("--------------------\n\n")
                    
print(dt1.data_type.describe())               
print("--------------------\n\n")
                    
print(dt1.latitude.describe())               
print("--------------------\n\n")
                    
print(dt1.longitude.describe())               
print("--------------------\n\n")
                    
print(dt1.sample_name.describe())               
print("--------------------\n\n")
                    
print(dt1.sample_id.describe())               
print("--------------------\n\n")
                    
print(dt1.sample_type.describe())               
print("--------------------\n\n")
                    
print(dt1.number_of_cores.describe())               
print("--------------------\n\n")
                    
print(dt1.spectral_id.describe())               
print("--------------------\n\n")
                    
print(dt1.photo_id.describe())               
print("--------------------\n\n")
                    
print(dt1.sample_description.describe())               
print("--------------------\n\n")
                    
print(dt1.filtering_remarks.describe())               
print("--------------------\n\n")
                    
print(dt1.freezer_remarks.describe())               
print("--------------------\n\n")
                    
                    
                 

infile2  ="https://pasta.lternet.edu/package/data/eml/knb-lter-mcm/5500/3/ee60d7ffb4334af076e1f1cdce4dba77".strip() 
infile2  = infile2.replace("https://","http://")
                 
dt2 =pd.read_csv(infile2 
          ,storage_options={'User-Agent':'EDI_CodeGen'}
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "dataset_code",     
                    "unique_id",     
                    "sample_id",     
                    "date_collected",     
                    "stream_name",     
                    "site_id",     
                    "plot_id",     
                    "subplot_id",     
                    "mat_type",     
                    "moisture_content",     
                    "afdm_mg_cm2",     
                    "chl_a",     
                    "biomass_remarks"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={  
#             'dataset_code':'str' ,  
#             'unique_id':'str' ,  
#             'sample_id':'str' , 
                        
#             'date_collected':'str' ,  
#             'stream_name':'str' ,  
#             'site_id':'str' ,  
#             'plot_id':'str' ,  
#             'subplot_id':'str' ,  
#             'mat_type':'str' ,  
#             'moisture_content':'str' , 
#             'afdm_mg_cm2':'float' , 
#             'chl_a':'float' ,  
#             'biomass_remarks':'str'  
#        }
          ,parse_dates=[
                        'date_collected',
                ] 
    )
# Coerce the data into the types specified in the metadata  
dt2.dataset_code=dt2.dataset_code.astype('category')  
dt2.unique_id=dt2.unique_id.astype('category')  
dt2.sample_id=dt2.sample_id.astype('category') 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt2=dt2.assign(date_collected_datetime=pd.to_datetime(dt2.date_collected,errors='coerce'))  
dt2.stream_name=dt2.stream_name.astype('category')  
dt2.site_id=dt2.site_id.astype('category')  
dt2.plot_id=dt2.plot_id.astype('category')  
dt2.subplot_id=dt2.subplot_id.astype('category')  
dt2.mat_type=dt2.mat_type.astype('category')  
dt2.moisture_content=dt2.moisture_content.astype('category') 
dt2.afdm_mg_cm2=pd.to_numeric(dt2.afdm_mg_cm2,errors='coerce') 
dt2.chl_a=pd.to_numeric(dt2.chl_a,errors='coerce')  
dt2.biomass_remarks=dt2.biomass_remarks.astype('category') 
      
print("Here is a description of the data frame dt2 and number of lines\n")
print(dt2.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt2\n")
print(dt2.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 
       
                
print(dt2.dataset_code.describe())               
print("--------------------\n\n")
                    
print(dt2.unique_id.describe())               
print("--------------------\n\n")
                    
print(dt2.sample_id.describe())               
print("--------------------\n\n")
                    
print(dt2.date_collected.describe())               
print("--------------------\n\n")
                    
print(dt2.stream_name.describe())               
print("--------------------\n\n")
                    
print(dt2.site_id.describe())               
print("--------------------\n\n")
                    
print(dt2.plot_id.describe())               
print("--------------------\n\n")
                    
print(dt2.subplot_id.describe())               
print("--------------------\n\n")
                    
print(dt2.mat_type.describe())               
print("--------------------\n\n")
                    
print(dt2.moisture_content.describe())               
print("--------------------\n\n")
                    
print(dt2.afdm_mg_cm2.describe())               
print("--------------------\n\n")
                    
print(dt2.chl_a.describe())               
print("--------------------\n\n")
                    
print(dt2.biomass_remarks.describe())               
print("--------------------\n\n")
                    
                    
                 

infile3  ="https://pasta.lternet.edu/package/data/eml/knb-lter-mcm/5500/3/c147dc5c157f2d1310dd3341c3f25cd8".strip() 
infile3  = infile3.replace("https://","http://")
                 
dt3 =pd.read_csv(infile3 
          ,storage_options={'User-Agent':'EDI_CodeGen'}
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "dataset_code",     
                    "unique_id",     
                    "sample_id",     
                    "date_collected",     
                    "stream_name",     
                    "plot_id",     
                    "subplot_id",     
                    "mat_type",     
                    "moisture_content",     
                    "allo_440nm_ug_cm2",     
                    "anthera_440nm_ug_cm2",     
                    "beta_440nm_ug_cm2",     
                    "butan_440nm_ug_cm2",     
                    "cantha_440nm_ug_cm2",     
                    "chla_440nm_ug_cm2",     
                    "chlb_440nm_ug_cm2",     
                    "chlc1c2_440nm_ug_cm2",     
                    "chlda_440nm_ug_cm2",     
                    "chltot_440nm_ug_cm2",     
                    "diadin_440nm_ug_cm2",     
                    "diato_440nm_ug_cm2",     
                    "echine_440nm_ug_cm2",     
                    "fuco_440nm_ug_cm2",     
                    "gyroxan_440nm_ug_cm2",     
                    "hexan_440nm_ug_cm2",     
                    "lutein_440nm_ug_cm2",     
                    "myxo_440nm_ug_cm2",     
                    "neoxan_440nm_ug_cm2",     
                    "scy_388nm_ug_cm2",     
                    "scyred_388nm_ug_cm2",     
                    "viola_440nm_ug_cm2",     
                    "zeaxan_440nm_ug_cm2",     
                    "hplc_file_id",     
                    "hplc_remarks"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={  
#             'dataset_code':'str' ,  
#             'unique_id':'str' ,  
#             'sample_id':'str' , 
                        
#             'date_collected':'str' ,  
#             'stream_name':'str' ,  
#             'plot_id':'str' ,  
#             'subplot_id':'str' ,  
#             'mat_type':'str' ,  
#             'moisture_content':'str' , 
#             'allo_440nm_ug_cm2':'float' , 
#             'anthera_440nm_ug_cm2':'float' , 
#             'beta_440nm_ug_cm2':'float' , 
#             'butan_440nm_ug_cm2':'float' , 
#             'cantha_440nm_ug_cm2':'float' , 
#             'chla_440nm_ug_cm2':'float' , 
#             'chlb_440nm_ug_cm2':'float' , 
#             'chlc1c2_440nm_ug_cm2':'float' , 
#             'chlda_440nm_ug_cm2':'float' , 
#             'chltot_440nm_ug_cm2':'float' , 
#             'diadin_440nm_ug_cm2':'float' , 
#             'diato_440nm_ug_cm2':'float' , 
#             'echine_440nm_ug_cm2':'float' , 
#             'fuco_440nm_ug_cm2':'float' , 
#             'gyroxan_440nm_ug_cm2':'float' , 
#             'hexan_440nm_ug_cm2':'float' , 
#             'lutein_440nm_ug_cm2':'float' , 
#             'myxo_440nm_ug_cm2':'float' , 
#             'neoxan_440nm_ug_cm2':'float' , 
#             'scy_388nm_ug_cm2':'float' , 
#             'scyred_388nm_ug_cm2':'float' , 
#             'viola_440nm_ug_cm2':'float' , 
#             'zeaxan_440nm_ug_cm2':'float' ,  
#             'hplc_file_id':'str' ,  
#             'hplc_remarks':'str'  
#        }
          ,parse_dates=[
                        'date_collected',
                ] 
    )
# Coerce the data into the types specified in the metadata  
dt3.dataset_code=dt3.dataset_code.astype('category')  
dt3.unique_id=dt3.unique_id.astype('category')  
dt3.sample_id=dt3.sample_id.astype('category') 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt3=dt3.assign(date_collected_datetime=pd.to_datetime(dt3.date_collected,errors='coerce'))  
dt3.stream_name=dt3.stream_name.astype('category')  
dt3.plot_id=dt3.plot_id.astype('category')  
dt3.subplot_id=dt3.subplot_id.astype('category')  
dt3.mat_type=dt3.mat_type.astype('category')  
dt3.moisture_content=dt3.moisture_content.astype('category') 
dt3.allo_440nm_ug_cm2=pd.to_numeric(dt3.allo_440nm_ug_cm2,errors='coerce') 
dt3.anthera_440nm_ug_cm2=pd.to_numeric(dt3.anthera_440nm_ug_cm2,errors='coerce') 
dt3.beta_440nm_ug_cm2=pd.to_numeric(dt3.beta_440nm_ug_cm2,errors='coerce') 
dt3.butan_440nm_ug_cm2=pd.to_numeric(dt3.butan_440nm_ug_cm2,errors='coerce') 
dt3.cantha_440nm_ug_cm2=pd.to_numeric(dt3.cantha_440nm_ug_cm2,errors='coerce') 
dt3.chla_440nm_ug_cm2=pd.to_numeric(dt3.chla_440nm_ug_cm2,errors='coerce') 
dt3.chlb_440nm_ug_cm2=pd.to_numeric(dt3.chlb_440nm_ug_cm2,errors='coerce') 
dt3.chlc1c2_440nm_ug_cm2=pd.to_numeric(dt3.chlc1c2_440nm_ug_cm2,errors='coerce') 
dt3.chlda_440nm_ug_cm2=pd.to_numeric(dt3.chlda_440nm_ug_cm2,errors='coerce') 
dt3.chltot_440nm_ug_cm2=pd.to_numeric(dt3.chltot_440nm_ug_cm2,errors='coerce') 
dt3.diadin_440nm_ug_cm2=pd.to_numeric(dt3.diadin_440nm_ug_cm2,errors='coerce') 
dt3.diato_440nm_ug_cm2=pd.to_numeric(dt3.diato_440nm_ug_cm2,errors='coerce') 
dt3.echine_440nm_ug_cm2=pd.to_numeric(dt3.echine_440nm_ug_cm2,errors='coerce') 
dt3.fuco_440nm_ug_cm2=pd.to_numeric(dt3.fuco_440nm_ug_cm2,errors='coerce') 
dt3.gyroxan_440nm_ug_cm2=pd.to_numeric(dt3.gyroxan_440nm_ug_cm2,errors='coerce') 
dt3.hexan_440nm_ug_cm2=pd.to_numeric(dt3.hexan_440nm_ug_cm2,errors='coerce') 
dt3.lutein_440nm_ug_cm2=pd.to_numeric(dt3.lutein_440nm_ug_cm2,errors='coerce') 
dt3.myxo_440nm_ug_cm2=pd.to_numeric(dt3.myxo_440nm_ug_cm2,errors='coerce') 
dt3.neoxan_440nm_ug_cm2=pd.to_numeric(dt3.neoxan_440nm_ug_cm2,errors='coerce') 
dt3.scy_388nm_ug_cm2=pd.to_numeric(dt3.scy_388nm_ug_cm2,errors='coerce') 
dt3.scyred_388nm_ug_cm2=pd.to_numeric(dt3.scyred_388nm_ug_cm2,errors='coerce') 
dt3.viola_440nm_ug_cm2=pd.to_numeric(dt3.viola_440nm_ug_cm2,errors='coerce') 
dt3.zeaxan_440nm_ug_cm2=pd.to_numeric(dt3.zeaxan_440nm_ug_cm2,errors='coerce')  
dt3.hplc_file_id=dt3.hplc_file_id.astype('category')  
dt3.hplc_remarks=dt3.hplc_remarks.astype('category') 
      
print("Here is a description of the data frame dt3 and number of lines\n")
print(dt3.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt3\n")
print(dt3.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 
       
                
print(dt3.dataset_code.describe())               
print("--------------------\n\n")
                    
print(dt3.unique_id.describe())               
print("--------------------\n\n")
                    
print(dt3.sample_id.describe())               
print("--------------------\n\n")
                    
print(dt3.date_collected.describe())               
print("--------------------\n\n")
                    
print(dt3.stream_name.describe())               
print("--------------------\n\n")
                    
print(dt3.plot_id.describe())               
print("--------------------\n\n")
                    
print(dt3.subplot_id.describe())               
print("--------------------\n\n")
                    
print(dt3.mat_type.describe())               
print("--------------------\n\n")
                    
print(dt3.moisture_content.describe())               
print("--------------------\n\n")
                    
print(dt3.allo_440nm_ug_cm2.describe())               
print("--------------------\n\n")
                    
print(dt3.anthera_440nm_ug_cm2.describe())               
print("--------------------\n\n")
                    
print(dt3.beta_440nm_ug_cm2.describe())               
print("--------------------\n\n")
                    
print(dt3.butan_440nm_ug_cm2.describe())               
print("--------------------\n\n")
                    
print(dt3.cantha_440nm_ug_cm2.describe())               
print("--------------------\n\n")
                    
print(dt3.chla_440nm_ug_cm2.describe())               
print("--------------------\n\n")
                    
print(dt3.chlb_440nm_ug_cm2.describe())               
print("--------------------\n\n")
                    
print(dt3.chlc1c2_440nm_ug_cm2.describe())               
print("--------------------\n\n")
                    
print(dt3.chlda_440nm_ug_cm2.describe())               
print("--------------------\n\n")
                    
print(dt3.chltot_440nm_ug_cm2.describe())               
print("--------------------\n\n")
                    
print(dt3.diadin_440nm_ug_cm2.describe())               
print("--------------------\n\n")
                    
print(dt3.diato_440nm_ug_cm2.describe())               
print("--------------------\n\n")
                    
print(dt3.echine_440nm_ug_cm2.describe())               
print("--------------------\n\n")
                    
print(dt3.fuco_440nm_ug_cm2.describe())               
print("--------------------\n\n")
                    
print(dt3.gyroxan_440nm_ug_cm2.describe())               
print("--------------------\n\n")
                    
print(dt3.hexan_440nm_ug_cm2.describe())               
print("--------------------\n\n")
                    
print(dt3.lutein_440nm_ug_cm2.describe())               
print("--------------------\n\n")
                    
print(dt3.myxo_440nm_ug_cm2.describe())               
print("--------------------\n\n")
                    
print(dt3.neoxan_440nm_ug_cm2.describe())               
print("--------------------\n\n")
                    
print(dt3.scy_388nm_ug_cm2.describe())               
print("--------------------\n\n")
                    
print(dt3.scyred_388nm_ug_cm2.describe())               
print("--------------------\n\n")
                    
print(dt3.viola_440nm_ug_cm2.describe())               
print("--------------------\n\n")
                    
print(dt3.zeaxan_440nm_ug_cm2.describe())               
print("--------------------\n\n")
                    
print(dt3.hplc_file_id.describe())               
print("--------------------\n\n")
                    
print(dt3.hplc_remarks.describe())               
print("--------------------\n\n")
                    
                    
                 

infile4  ="https://pasta.lternet.edu/package/data/eml/knb-lter-mcm/5500/3/7540e93df6403cae41f13a2954f2fa4f".strip() 
infile4  = infile4.replace("https://","http://")
                 
dt4 =pd.read_csv(infile4 
          ,storage_options={'User-Agent':'EDI_CodeGen'}
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "dataset_code",     
                    "unique_id",     
                    "sample_id",     
                    "date_collected",     
                    "stream_name",     
                    "plot_id",     
                    "subplot_id",     
                    "mat_type",     
                    "moisture_content",     
                    "allo_440nm_ug_g",     
                    "anthera_440nm_ug_g",     
                    "beta_440nm_ug_g",     
                    "butan_440nm_ug_g",     
                    "cantha_440nm_ug_g",     
                    "chla_440nm_ug_g",     
                    "chlb_440nm_ug_g",     
                    "chlc1c2_440nm_ug_g",     
                    "chlda_440nm_ug_g",     
                    "chltot_440nm_ug_g",     
                    "diadin_440nm_ug_g",     
                    "diato_440nm_ug_g",     
                    "echine_440nm_ug_g",     
                    "fuco_440nm_ug_g",     
                    "gyroxan_440nm_ug_g",     
                    "hexan_440nm_ug_g",     
                    "lutein_440nm_ug_g",     
                    "myxo_440nm_ug_g",     
                    "neoxan_440nm_ug_g",     
                    "scy_388nm_ug_g",     
                    "scyred_388nm_ug_g",     
                    "viola_440nm_ug_g",     
                    "zeaxan_440nm_ug_g",     
                    "hplc_file_id",     
                    "hplc_remarks"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={  
#             'dataset_code':'str' ,  
#             'unique_id':'str' ,  
#             'sample_id':'str' , 
                        
#             'date_collected':'str' ,  
#             'stream_name':'str' ,  
#             'plot_id':'str' ,  
#             'subplot_id':'str' ,  
#             'mat_type':'str' ,  
#             'moisture_content':'str' , 
#             'allo_440nm_ug_g':'float' , 
#             'anthera_440nm_ug_g':'float' , 
#             'beta_440nm_ug_g':'float' , 
#             'butan_440nm_ug_g':'float' , 
#             'cantha_440nm_ug_g':'float' , 
#             'chla_440nm_ug_g':'float' , 
#             'chlb_440nm_ug_g':'float' , 
#             'chlc1c2_440nm_ug_g':'float' , 
#             'chlda_440nm_ug_g':'float' , 
#             'chltot_440nm_ug_g':'float' , 
#             'diadin_440nm_ug_g':'float' , 
#             'diato_440nm_ug_g':'float' , 
#             'echine_440nm_ug_g':'float' , 
#             'fuco_440nm_ug_g':'float' , 
#             'gyroxan_440nm_ug_g':'float' , 
#             'hexan_440nm_ug_g':'float' , 
#             'lutein_440nm_ug_g':'float' , 
#             'myxo_440nm_ug_g':'float' , 
#             'neoxan_440nm_ug_g':'float' , 
#             'scy_388nm_ug_g':'float' , 
#             'scyred_388nm_ug_g':'float' , 
#             'viola_440nm_ug_g':'float' , 
#             'zeaxan_440nm_ug_g':'float' ,  
#             'hplc_file_id':'str' ,  
#             'hplc_remarks':'str'  
#        }
          ,parse_dates=[
                        'date_collected',
                ] 
    )
# Coerce the data into the types specified in the metadata  
dt4.dataset_code=dt4.dataset_code.astype('category')  
dt4.unique_id=dt4.unique_id.astype('category')  
dt4.sample_id=dt4.sample_id.astype('category') 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt4=dt4.assign(date_collected_datetime=pd.to_datetime(dt4.date_collected,errors='coerce'))  
dt4.stream_name=dt4.stream_name.astype('category')  
dt4.plot_id=dt4.plot_id.astype('category')  
dt4.subplot_id=dt4.subplot_id.astype('category')  
dt4.mat_type=dt4.mat_type.astype('category')  
dt4.moisture_content=dt4.moisture_content.astype('category') 
dt4.allo_440nm_ug_g=pd.to_numeric(dt4.allo_440nm_ug_g,errors='coerce') 
dt4.anthera_440nm_ug_g=pd.to_numeric(dt4.anthera_440nm_ug_g,errors='coerce') 
dt4.beta_440nm_ug_g=pd.to_numeric(dt4.beta_440nm_ug_g,errors='coerce') 
dt4.butan_440nm_ug_g=pd.to_numeric(dt4.butan_440nm_ug_g,errors='coerce') 
dt4.cantha_440nm_ug_g=pd.to_numeric(dt4.cantha_440nm_ug_g,errors='coerce') 
dt4.chla_440nm_ug_g=pd.to_numeric(dt4.chla_440nm_ug_g,errors='coerce') 
dt4.chlb_440nm_ug_g=pd.to_numeric(dt4.chlb_440nm_ug_g,errors='coerce') 
dt4.chlc1c2_440nm_ug_g=pd.to_numeric(dt4.chlc1c2_440nm_ug_g,errors='coerce') 
dt4.chlda_440nm_ug_g=pd.to_numeric(dt4.chlda_440nm_ug_g,errors='coerce') 
dt4.chltot_440nm_ug_g=pd.to_numeric(dt4.chltot_440nm_ug_g,errors='coerce') 
dt4.diadin_440nm_ug_g=pd.to_numeric(dt4.diadin_440nm_ug_g,errors='coerce') 
dt4.diato_440nm_ug_g=pd.to_numeric(dt4.diato_440nm_ug_g,errors='coerce') 
dt4.echine_440nm_ug_g=pd.to_numeric(dt4.echine_440nm_ug_g,errors='coerce') 
dt4.fuco_440nm_ug_g=pd.to_numeric(dt4.fuco_440nm_ug_g,errors='coerce') 
dt4.gyroxan_440nm_ug_g=pd.to_numeric(dt4.gyroxan_440nm_ug_g,errors='coerce') 
dt4.hexan_440nm_ug_g=pd.to_numeric(dt4.hexan_440nm_ug_g,errors='coerce') 
dt4.lutein_440nm_ug_g=pd.to_numeric(dt4.lutein_440nm_ug_g,errors='coerce') 
dt4.myxo_440nm_ug_g=pd.to_numeric(dt4.myxo_440nm_ug_g,errors='coerce') 
dt4.neoxan_440nm_ug_g=pd.to_numeric(dt4.neoxan_440nm_ug_g,errors='coerce') 
dt4.scy_388nm_ug_g=pd.to_numeric(dt4.scy_388nm_ug_g,errors='coerce') 
dt4.scyred_388nm_ug_g=pd.to_numeric(dt4.scyred_388nm_ug_g,errors='coerce') 
dt4.viola_440nm_ug_g=pd.to_numeric(dt4.viola_440nm_ug_g,errors='coerce') 
dt4.zeaxan_440nm_ug_g=pd.to_numeric(dt4.zeaxan_440nm_ug_g,errors='coerce')  
dt4.hplc_file_id=dt4.hplc_file_id.astype('category')  
dt4.hplc_remarks=dt4.hplc_remarks.astype('category') 
      
print("Here is a description of the data frame dt4 and number of lines\n")
print(dt4.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt4\n")
print(dt4.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 
       
                
print(dt4.dataset_code.describe())               
print("--------------------\n\n")
                    
print(dt4.unique_id.describe())               
print("--------------------\n\n")
                    
print(dt4.sample_id.describe())               
print("--------------------\n\n")
                    
print(dt4.date_collected.describe())               
print("--------------------\n\n")
                    
print(dt4.stream_name.describe())               
print("--------------------\n\n")
                    
print(dt4.plot_id.describe())               
print("--------------------\n\n")
                    
print(dt4.subplot_id.describe())               
print("--------------------\n\n")
                    
print(dt4.mat_type.describe())               
print("--------------------\n\n")
                    
print(dt4.moisture_content.describe())               
print("--------------------\n\n")
                    
print(dt4.allo_440nm_ug_g.describe())               
print("--------------------\n\n")
                    
print(dt4.anthera_440nm_ug_g.describe())               
print("--------------------\n\n")
                    
print(dt4.beta_440nm_ug_g.describe())               
print("--------------------\n\n")
                    
print(dt4.butan_440nm_ug_g.describe())               
print("--------------------\n\n")
                    
print(dt4.cantha_440nm_ug_g.describe())               
print("--------------------\n\n")
                    
print(dt4.chla_440nm_ug_g.describe())               
print("--------------------\n\n")
                    
print(dt4.chlb_440nm_ug_g.describe())               
print("--------------------\n\n")
                    
print(dt4.chlc1c2_440nm_ug_g.describe())               
print("--------------------\n\n")
                    
print(dt4.chlda_440nm_ug_g.describe())               
print("--------------------\n\n")
                    
print(dt4.chltot_440nm_ug_g.describe())               
print("--------------------\n\n")
                    
print(dt4.diadin_440nm_ug_g.describe())               
print("--------------------\n\n")
                    
print(dt4.diato_440nm_ug_g.describe())               
print("--------------------\n\n")
                    
print(dt4.echine_440nm_ug_g.describe())               
print("--------------------\n\n")
                    
print(dt4.fuco_440nm_ug_g.describe())               
print("--------------------\n\n")
                    
print(dt4.gyroxan_440nm_ug_g.describe())               
print("--------------------\n\n")
                    
print(dt4.hexan_440nm_ug_g.describe())               
print("--------------------\n\n")
                    
print(dt4.lutein_440nm_ug_g.describe())               
print("--------------------\n\n")
                    
print(dt4.myxo_440nm_ug_g.describe())               
print("--------------------\n\n")
                    
print(dt4.neoxan_440nm_ug_g.describe())               
print("--------------------\n\n")
                    
print(dt4.scy_388nm_ug_g.describe())               
print("--------------------\n\n")
                    
print(dt4.scyred_388nm_ug_g.describe())               
print("--------------------\n\n")
                    
print(dt4.viola_440nm_ug_g.describe())               
print("--------------------\n\n")
                    
print(dt4.zeaxan_440nm_ug_g.describe())               
print("--------------------\n\n")
                    
print(dt4.hplc_file_id.describe())               
print("--------------------\n\n")
                    
print(dt4.hplc_remarks.describe())               
print("--------------------\n\n")
                    
                    
                 

infile5  ="https://pasta.lternet.edu/package/data/eml/knb-lter-mcm/5500/3/d23786fa1139cc2222262575d4c9382e".strip() 
infile5  = infile5.replace("https://","http://")
                 
dt5 =pd.read_csv(infile5 
          ,storage_options={'User-Agent':'EDI_CodeGen'}
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "dataset_code",     
                    "unique_id",     
                    "spectral_id",     
                    "date_collected",     
                    "stream_name",     
                    "plot_id",     
                    "subplot_id",     
                    "mat_type",     
                    "moisture_content",     
                    "band_nm",     
                    "reflectance"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={  
#             'dataset_code':'str' ,  
#             'unique_id':'str' ,  
#             'spectral_id':'str' , 
                        
#             'date_collected':'str' ,  
#             'stream_name':'str' ,  
#             'plot_id':'str' ,  
#             'subplot_id':'str' ,  
#             'mat_type':'str' ,  
#             'moisture_content':'str' , 
#             'band_nm':'float' ,  
#             'reflectance':'str'  
#        }
          ,parse_dates=[
                        'date_collected',
                ] 
    )
# Coerce the data into the types specified in the metadata  
dt5.dataset_code=dt5.dataset_code.astype('category')  
dt5.unique_id=dt5.unique_id.astype('category')  
dt5.spectral_id=dt5.spectral_id.astype('category') 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt5=dt5.assign(date_collected_datetime=pd.to_datetime(dt5.date_collected,errors='coerce'))  
dt5.stream_name=dt5.stream_name.astype('category')  
dt5.plot_id=dt5.plot_id.astype('category')  
dt5.subplot_id=dt5.subplot_id.astype('category')  
dt5.mat_type=dt5.mat_type.astype('category')  
dt5.moisture_content=dt5.moisture_content.astype('category') 
dt5.band_nm=pd.to_numeric(dt5.band_nm,errors='coerce')  
dt5.reflectance=dt5.reflectance.astype('category') 
      
print("Here is a description of the data frame dt5 and number of lines\n")
print(dt5.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt5\n")
print(dt5.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 
       
                
print(dt5.dataset_code.describe())               
print("--------------------\n\n")
                    
print(dt5.unique_id.describe())               
print("--------------------\n\n")
                    
print(dt5.spectral_id.describe())               
print("--------------------\n\n")
                    
print(dt5.date_collected.describe())               
print("--------------------\n\n")
                    
print(dt5.stream_name.describe())               
print("--------------------\n\n")
                    
print(dt5.plot_id.describe())               
print("--------------------\n\n")
                    
print(dt5.subplot_id.describe())               
print("--------------------\n\n")
                    
print(dt5.mat_type.describe())               
print("--------------------\n\n")
                    
print(dt5.moisture_content.describe())               
print("--------------------\n\n")
                    
print(dt5.band_nm.describe())               
print("--------------------\n\n")
                    
print(dt5.reflectance.describe())               
print("--------------------\n\n")
                    
                    
                 

infile6  ="https://pasta.lternet.edu/package/data/eml/knb-lter-mcm/5500/3/f56637013d430419b448de22dcde119b".strip() 
infile6  = infile6.replace("https://","http://")
                 
dt6 =pd.read_csv(infile6 
          ,storage_options={'User-Agent':'EDI_CodeGen'}
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "dataset_code",     
                    "unique_id",     
                    "spectral_id",     
                    "date_collected",     
                    "stream_name",     
                    "plot_id",     
                    "subplot_id",     
                    "mat_type",     
                    "moisture_content",     
                    "band_um",     
                    "reflectance"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={  
#             'dataset_code':'str' ,  
#             'unique_id':'str' ,  
#             'spectral_id':'str' , 
                        
#             'date_collected':'str' ,  
#             'stream_name':'str' ,  
#             'plot_id':'str' ,  
#             'subplot_id':'str' ,  
#             'mat_type':'str' ,  
#             'moisture_content':'str' , 
#             'band_um':'float' ,  
#             'reflectance':'str'  
#        }
          ,parse_dates=[
                        'date_collected',
                ] 
    )
# Coerce the data into the types specified in the metadata  
dt6.dataset_code=dt6.dataset_code.astype('category')  
dt6.unique_id=dt6.unique_id.astype('category')  
dt6.spectral_id=dt6.spectral_id.astype('category') 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt6=dt6.assign(date_collected_datetime=pd.to_datetime(dt6.date_collected,errors='coerce'))  
dt6.stream_name=dt6.stream_name.astype('category')  
dt6.plot_id=dt6.plot_id.astype('category')  
dt6.subplot_id=dt6.subplot_id.astype('category')  
dt6.mat_type=dt6.mat_type.astype('category')  
dt6.moisture_content=dt6.moisture_content.astype('category') 
dt6.band_um=pd.to_numeric(dt6.band_um,errors='coerce')  
dt6.reflectance=dt6.reflectance.astype('category') 
      
print("Here is a description of the data frame dt6 and number of lines\n")
print(dt6.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt6\n")
print(dt6.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 
       
                
print(dt6.dataset_code.describe())               
print("--------------------\n\n")
                    
print(dt6.unique_id.describe())               
print("--------------------\n\n")
                    
print(dt6.spectral_id.describe())               
print("--------------------\n\n")
                    
print(dt6.date_collected.describe())               
print("--------------------\n\n")
                    
print(dt6.stream_name.describe())               
print("--------------------\n\n")
                    
print(dt6.plot_id.describe())               
print("--------------------\n\n")
                    
print(dt6.subplot_id.describe())               
print("--------------------\n\n")
                    
print(dt6.mat_type.describe())               
print("--------------------\n\n")
                    
print(dt6.moisture_content.describe())               
print("--------------------\n\n")
                    
print(dt6.band_um.describe())               
print("--------------------\n\n")
                    
print(dt6.reflectance.describe())               
print("--------------------\n\n")
                    
                    
                
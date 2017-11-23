##########################
#### Future Challenge ####
#### Author: CZB      ####
#### Time:2017-10-21  ####
##########################

import pandas as pd
import numpy as np
from datetime import *

# simple submit
def simSub(sXid,sYid,eXid,eYid,target,date):
    #### create one submit path
    sub_df = pd.DataFrame(columns=['target','date','time','xid','yid'])
    x = np.arange(sXid,eXid+((eXid-sXid)/abs(eXid-sXid)),\
            (eXid-sXid)/abs(eXid-sXid))
    y = np.arange(sYid,eYid+((eYid-sYid)/abs(eYid-sYid)),\
            (eYid-sYid)/abs(eYid-sYid))
    length = len(x)+len(y)-1
    #### path array
    sub = np.zeros((length,2))
    sub[0:len(x),0] = x
    sub[len(x):length,0] = x[-1]
    sub[0:len(x),1] = y[0]
    sub[len(x)-1:length,1] = y
    sub_df['xid'] = sub[:,0]
    sub_df['yid'] = sub[:,1]
    sub_df.xid = sub_df.xid.astype(np.int32)
    sub_df.yid = sub_df.yid.astype(np.int32)
    sub_df.target = target
    sub_df.date = date
    #### add time
    ti = datetime(2017,11,21,9,0)
    tm = [ti.strftime('%H:%M')]
    for i in range(length-1):
        ti = ti + timedelta(minutes=2)
        tm.append(ti.strftime('%H:%M'))
    sub_df.time = tm
    return sub_df

def submit_phase():
    city = pd.read_csv('CityData.csv')
    city_array = city.values
    sub_csv = pd.DataFrame(columns=['target','date','time','xid','yid'])
    for date in range(5):
        for tar in range(10):
            sub_df = simSub(city_array[0][1],city_array[0][2],\
                            city_array[tar+1][1],city_array[tar+1][2],\
                            tar+1,date+6)
            sub_csv=pd.concat([sub_csv,sub_df],axis=0)
    sub_csv.target = sub_csv.target.astype(np.int32)
    sub_csv.date = sub_csv.date.astype(np.int32)
    sub_csv.xid = sub_csv.xid.astype(np.int32)
    sub_csv.yid = sub_csv.yid.astype(np.int32)
    return sub_csv

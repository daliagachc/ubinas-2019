# project name: ubinas-2019
# created by diego aliaga daliaga_at_chacaltaya.edu.bo

from useful_scit.imps import *

SO2_MON_PATH = '../data/in-situ/so2-monitor/so2_mon.csv'
ACSM_PATH = '../data/in-situ/acsm/acsm_chacaltaya_2019.csv'

C_LT = 'local_time'
C_SO2 = 'SO2 [ppb]'
C_SO4 = 'SO4 [ug/m3]'


def import_acsm_data(path=ACSM_PATH):
    data = pd.read_csv(path,sep=';')
    utc_time_col = 'acsm_utc_time'
    time_utc = pd.to_datetime(data[utc_time_col], format='%d/%m/%Y %H:%M')
    local_time = time_utc - pd.Timedelta(hours=4)
    data[C_LT] = local_time
    data = data.rename(str,columns={'SO4':C_SO4})
    data = data.drop(utc_time_col, axis=1)
    data = data.set_index(C_LT)

    return data

def import_so2_data(path=SO2_MON_PATH):
    data = pd.read_csv(path)
    unix_col = 'unix_sec_local'
    data = data.sort_values(unix_col)
    local_time= pd.to_datetime(data[unix_col],unit='s')
    local_time.name = C_LT
    data = data.set_index(local_time)
    # data = data.drop(unix_col, axis=1)
    data = data.rename(str,columns={'so2_corrected[ppb]':C_SO2})
    data.index = pd.to_datetime(data.index)
    return data

def get_joined_ds(round_int = False):
    so2d = import_so2_data()
    acsmd = import_acsm_data()
    if round_int is not False:
        pass
    data = pd.merge(so2d,acsmd,left_index=True,right_index=True)
    return data


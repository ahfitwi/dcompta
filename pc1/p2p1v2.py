#----------------------------------------------------------
# Project_name: DC-OMP-TA Communications @ Step-3 & Step-6
# ------------------Server/Peer----------------------------
#----------------------------------------------------------
#!/usr/bin/env python3
"""
Created on Saturday September 25 14:12:27 2021
@author: alem fitwi
"""

#----------------------------------------------------------
# Import Necessary Libraries and Packages
#----------------------------------------------------------
import os
import sys
import glob
from sys import path
import numpy as np
import socket
from scipy.io import loadmat, savemat
from pickle import dumps, loads
from _thread import *
from datetime import datetime as dtt
from datetime import date,timedelta
#----------------------------------------------------------
# Global Variables
#----------------------------------------------------------
ThreadCount = 0
step3ID_lst, step6ID_lst, connections = [], [], []

#----------------------------------------------------------
# Import All Necessary Constants, config files and Paths
#----------------------------------------------------------
COM_PATH = "C:\\Users\\Alem\\Desktop\\DC_OMP_TA\\"
path.append(os.path.join(COM_PATH,'config_mdl_p2p1\\'))

from dcomptaconfigp2p1 import HEADER_SIZE, IO_PATH,\
    SERV_PORT,SERV_IP, NODES_ID, RECV_BYTES, DICTGW,\
    DICTFW, CUR_NODE_ID, TRIGGERS, SERV_KEYS3,\
    KEYS_DICT_STEP3, KEYS_DICT_STEP6, MAT_FILE_NAME3,\
    MAT_FILE_NAME6, TA_STEPS, SERV_KEYS6
#----------------------------------------------------------
# Extract keys of (ID, [g,w]) pairs of server
keys3 =  list(KEYS_DICT_STEP3.keys())
keys6 =  list(KEYS_DICT_STEP6.keys())
#----------------------------------------------------------
# Read .mat file from IO_PATH, to be sent to remote peers
#----------------------------------------------------------
def read_mat(IO_PATH, mat_name):    
    filename = mat_name  + ".mat"
    try:
        path1 = os.path.join(
              IO_PATH, filename)
        mat = loadmat(path1) 
    except:
        return False
    else:
        return mat

#----------------------------------------------------------
# Write .mat files fetched from remote peers to IO_PATH
#----------------------------------------------------------
def save_mat(IO_PATH, mat_name, matobject):    
    filename = mat_name + ".mat"
    try:
        path1 = os.path.join(
                    IO_PATH, filename)        
        savemat(path1, matobject)
    except:
        return False
    else:
        return True 

#----------------------------------------------------------
# Serialize Objects using pickle.dumps
#----------------------------------------------------------
def serialize(obj):
    try:
        ser = dumps(obj)
    except:
        return False
    else:
        return ser

#----------------------------------------------------------
# Deserialize Objects using pickle.loads
#----------------------------------------------------------
def deserialize(obj):
    try:
        deser = loads(obj)
    except:
        return False
    else:
        return deser

#----------------------------------------------------------
# Receive data from another peer
#----------------------------------------------------------
def recv_obj(conn, RECV_BYTES, HEADER_SIZE):
    """Receives objects from 
       other peers"""

    full_msg = b''   
    while True:
        pyobj = conn.recv(RECV_BYTES)
        if not pyobj:
            continue
        print("Recv: ",pyobj[:HEADER_SIZE])
        msg_len = int(pyobj[:HEADER_SIZE])
        full_msg += pyobj
        if len(full_msg) - HEADER_SIZE == msg_len:
            infos = full_msg[HEADER_SIZE:HEADER_SIZE+13
                     ].decode("utf-8")
            idd = infos[:8]
            step = infos[8:].strip()
            break
    return idd, step, deserialize(full_msg[HEADER_SIZE+13:])  

#----------------------------------------------------------
# Send data to all other peers --> ['obj_g2w2', 'obj_g3w3']
#----------------------------------------------------------
def send_obj(conn, obj):
    obj1 = serialize(obj)
    obj3 =  bytes(f"{len(obj1):<{HEADER_SIZE}}", 
                      "utf-8")+obj1
    conn.sendall(obj3)

#----------------------------------------------------------
# Check steps-3&6 .mat read-trigger in IO_PATH Continually!
#----------------------------------------------------------
def isTrigger(path2, TRIGGERS):
    fstep3 = os.path.join(path2,TRIGGERS[0])
    fstep6 = os.path.join(path2,TRIGGERS[1])
    bstep3 = os.path.exists(fstep3)
    bstep6 = os.path.exists(fstep6)
    return bstep3, bstep6

#----------------------------------------------------------
# A Function that removes a file from disk
#----------------------------------------------------------
def remove_file(path2, filename):
    try:
        path1 = os.path.join(path2, filename)
        file = glob.glob(path1)
        os.remove(file[0])           
    except:
        print(sys.exc_info()[0])

#----------------------------------------------------------
# A Function that grabs current time and date
#----------------------------------------------------------
def get_datetime():
    tday = dtt.now()
    day = tday.strftime("%A")[:3]
    mon = tday.strftime("%B")[:3]    
    time = tday.strftime("%d %H:%M:%S %Y")
    return day+' '+mon+'  '+time  

#----------------------------------------------------------
# A Function that updates the date of obj.mat object
#----------------------------------------------------------
def update_date(obj):
    datetime = get_datetime()
    tmp  = obj['__header__']
    tmp= tmp.decode("utf-8").split('Created on:')
    tmp = tmp[0]+'Created on: '+datetime
    obj['__header__'] = bytes(tmp,"utf-8")   
    return obj

#----------------------------------------------------------
# Multithreading peers,['obj_g1w1', 'obj_g2w2', 'obj_g3w3']
#----------------------------------------------------------
def parallelize_peers(conn, obj_mat_all, obj_mat_fs, error, 
    COM_PATH, IO_PATH, TRIGGERS, CUR_NODE_ID, HEADER_SIZE,
    keys3,keys6,TA_STEPS,MAT_FILE_NAME3, MAT_FILE_NAME6,
    KEYS_DICT_STEP3, KEYS_DICT_STEP6):  
    #------------------------------------------------------
    global connections
    global step3ID_lst
    global step6ID_lst    
    #------------------------------------------------------
    while True:
        #--------------------------------------------------
        if conn not in connections:
            connections.append(conn)               
            idd, step, pyobj = recv_obj(conn, RECV_BYTES, 
                                    HEADER_SIZE) 
            
        #--------------------------------------------------
            if step == TA_STEPS[0]: 
                which_step = TA_STEPS[0]

                try:
                    tmp3 = KEYS_DICT_STEP3[idd]                                  
                    for val3 in tmp3:
                        obj_mat_all[val3] = pyobj[val3]    
                        
                    if idd not in step3ID_lst:
                        step3ID_lst.append(idd)
                    print("End of for if")
                except:
                    err_msg = sys.exc_info()[0]
                    err_msg1 = "At server: "+str(err_msg)                    
                    print(err_msg1)
                    obj_mat_all['error'] = "At server: "+str(err_msg)                    
                    tmpv = "Error: please check the .mat files of all "
                    obj_mat_all['error2'] = tmpv + "nodes are good!"
                    break  

                logics3 = []
                for k3 in keys3:
                    if k3 in step3ID_lst:
                        logics3.append(True)           
                if all(logics3) and len(logics3)==len(keys3):            
                    break  
        #--------------------------------------------------
            if step == TA_STEPS[1]:
                which_step = TA_STEPS[1]   
                
                try:                    
                    if bool(pyobj['flag']) == True:
                        tmp6= KEYS_DICT_STEP6[idd]
                        for val6 in tmp6:
                            obj_mat_fs[val6] = pyobj[val6]                           
		
                    if idd not in step6ID_lst:
                        step6ID_lst.append(idd)
                except:
                    err_msg = sys.exc_info()[0]
                    err_msg1 = "At server: "+str(err_msg)
                    print(err_msg1)
                    obj_mat_fs['error'] = err_msg1
                    tmpv = "Error: please check the .mat files of all "
                    obj_mat_fs['error2'] = tmpv + "nodes are good!"
                    break  

                logics6 = []
                for k6 in keys6:
                    if k6 in step6ID_lst:
                        logics6.append(True)           
                if all(logics6) and len(logics6)==len(keys6):            
                    break            
        #--------------------------------------------------
    #------------------------------------------------------
    which_step = ''
    while True: 
        #--------------------------------------------------
        bstep3, bstep6 = isTrigger(IO_PATH, TRIGGERS)       
        if bstep3 == True:
            which_step = TA_STEPS[0]
            obj_g1w1 = read_mat(IO_PATH, CUR_NODE_ID)
            if isinstance(obj_g1w1, bool) == True:
                continue
            else:
                for skey3 in SERV_KEYS3:
                    obj_mat_all[skey3] = obj_g1w1[skey3]          

                save_mat(IO_PATH, MAT_FILE_NAME3[1], 
                                               obj_mat_all)
                filename = CUR_NODE_ID +'.mat'
                remove_file(IO_PATH, filename)            
            remove_file(IO_PATH, TRIGGERS[0])            
            break
        #--------------------------------------------------
        elif bstep6 == True and bstep3 == False:
            which_step = TA_STEPS[1]
            obj_f1w1 = read_mat(IO_PATH, MAT_FILE_NAME6[0])
            if isinstance(obj_f1w1, bool) == True:
                continue
            else:
                if bool(obj_f1w1['flag']) == True:
                    for skey6 in SERV_KEYS6:
                        obj_mat_fs[skey6]=obj_f1w1[skey6]

                save_mat(IO_PATH, MAT_FILE_NAME6[1], 
                                              obj_mat_fs)
                filename = "obj_f1w1" +'.mat'
                remove_file(IO_PATH, filename)            
            remove_file(IO_PATH, TRIGGERS[1])            
            break
        else:
            error2="No Triggers or both are simultaneously"
            obj_mat_fs['error2'] = error2 + " set!"

    #------------------------------------------------------    
    # Send objects to peers  
    #------------------------------------------------------ 
    if which_step == TA_STEPS[0]:        
        for conn3 in connections:        
            send_obj(conn3, obj_mat_all) 
            
    #------------------------------------------------------    
    if which_step == TA_STEPS[1]:        
        for conn6 in connections:        
            send_obj(conn6, obj_mat_fs)            
    #------------------------------------------------------    

    # Reset Global Variables for next connections
    step3ID_lst, step6ID_lst, connections = [], [], []  

    #------------------------------------------------------
    # Close current session  
    conn.close()

#----------------------------------------------------------
# The Main Function where every other function is run!
#----------------------------------------------------------
if __name__ == '__main__':
    #Create A Server/Peer Socket
    ServerSocket = socket.socket(socket.AF_INET, 
                              socket.SOCK_STREAM)
    #------------------------------------------------------
    # Bind Server IP Address and Port Number 
    try:
        ServerSocket.bind((SERV_IP, SERV_PORT))
    except socket.error as e:
        print(str(e))
    #------------------------------------------------------
    print('**********************************************')
    print('Waiting For Connection Requests From Peers ...')
    print('**********************************************')    
    ServerSocket.listen(5) # Listening for other peers
    #------------------------------------------------------    
    initpath = os.path.join(COM_PATH, 'config_mdl_p2p1\\')    
    error = loadmat(initpath + MAT_FILE_NAME3[3])         
    #------------------------------------------------------   
    savemat(initpath+MAT_FILE_NAME3[2], DICTGW) 
    obj_mat_all = loadmat(initpath+MAT_FILE_NAME3[2]) 
    print("---------------------------------------")  
    print(f"At Start, obj_mat_all: {obj_mat_all}")    
    print("---------------------------------------")   

    savemat(initpath+MAT_FILE_NAME6[2], DICTFW)    
    obj_mat_fs = loadmat(initpath+MAT_FILE_NAME6[2]) 
    print("---------------------------------------")  
    print(f"At Start, obj_mat_fs: {obj_mat_fs}")    
    print('**********************************************') 
    #------------------------------------------------------
    rounds = 1
    while True:   
    #------------------------------------------------------
        print('******************************************')   
        print(f"@ Round: {rounds}")    
        print('******************************************')
        # Read Base Object File for Step-3 of TA
        obj_mat_all = update_date(obj_mat_all)
        print('******************************************')   
        print(f"In A While Loop obj_mat_all: {obj_mat_all}")    
        print('******************************************')   
    #------------------------------------------------------
        # Read Base Object File for Step-6 of TA
        obj_mat_fs = update_date(obj_mat_fs)
        print('******************************************')   
        print(f"In A While Loop obj_mat_fs: {obj_mat_fs}")    
        print('******************************************')    

        # Accept Multiple Connection Requests
        print('******************************************')
        print('Listening ...')
        print('------------------------------------------') 
        try:
            conn, address = ServerSocket.accept() 
            print(f"Connected To Peer {address} ...") 
        except:
            print(sys.exc_info()[0])
            continue        
        print('******************************************')  

        print('******************************************')  
        print(f"Organizing .mat Objects In Parallel ...")              
        start_new_thread(parallelize_peers, 
           (conn, obj_mat_all, obj_mat_fs, error, 
           COM_PATH, IO_PATH, TRIGGERS, CUR_NODE_ID, 
           HEADER_SIZE, keys3,keys6,TA_STEPS,MAT_FILE_NAME3, 
           MAT_FILE_NAME6, KEYS_DICT_STEP3, 
           KEYS_DICT_STEP6))
        print('******************************************') 

        print('******************************************')  
        # Count Threads and Display the count
        print(f" Number Of Peers/Threads Running ...") 
        ThreadCount += 1        
        print('Thread Number: ' + str(ThreadCount))
        print('******************************************')  

        # Reset Count of Threads if > 2^{16}-1    
        if ThreadCount > 65535:
            ThreadCount = 0	 
        
        # Reset rounds count if > 2^{16}-1    
        if rounds > 65535:
            rounds = 0	
        rounds += True 

    #------------------------------------------------------
    #Close Server Socket  
    ServerSocket.close()
    #------------------------------------------------------
#----------------------------------------------------------
# End of p2p1.py program, which acts as a server!
#----------------------------------------------------------

#----------------------------------------------------------
# Project_name: DC-OMP-TA Communications @ Step-3 & Step-6
# ------------------Peer/Client----------------------------
#----------------------------------------------------------
#!/usr/bin/env python3
"""
Created on Saturday September 25 18:37:33 2021
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

#----------------------------------------------------------
# Import All Necessary Constants, config files and Paths
#----------------------------------------------------------
# Set the main absolute path (excluding file name) here!
COM_PATH = "C:\\Users\\Alem\\Desktop\\DC_OMP_TA\\"
path.append(os.path.join(COM_PATH,'config_mdl_p2p2\\'))

# Import all user-defined parameters and configurations 
from dcomptaconfigp2p2 import HEADER_SIZE,IO_PATH,\
    SERV_PORT,SERV_IP, NODES_ID, RECV_BYTES,\
    CUR_NODE_ID, TRIGGERS, MAT_FILE_NAME3, \
    MAT_FILE_NAME6, TA_STEPS

#----------------------------------------------------------
# Read .mat file from IO_PATH, to be sent to remote peers
#----------------------------------------------------------
def read_mat(IO_PATH, mat_name): 
    """Reads .mat MATLAB Objects to disk"""   
    filename = mat_name + ".mat"
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
    """Saves .mat MATLAB Objects to disk"""   
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
    """Pickles objects into byte-series"""
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
    """unpickles objects into objects"""
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
    """Receives objects from other peers"""
    full_msg = b''   
    while True:
        pyobj = conn.recv(RECV_BYTES)        
        msg_len = int(pyobj[:HEADER_SIZE])
        full_msg += pyobj
        if len(full_msg) - HEADER_SIZE == msg_len:            
            break
    return deserialize(full_msg[HEADER_SIZE:])  

#----------------------------------------------------------
# Send data to all other peers --> ['obj_g2w2', 'obj_g3w3']
#----------------------------------------------------------
def send_obj(conn, obj, CUR_NODE_ID, step):
    """Sends pickled objects to other peers"""
    idd = CUR_NODE_ID + step
    obj1 = serialize(obj)
    obj1 = bytes(f"{idd}", "utf-8")+obj1
    obj3 =  bytes(f"{len(obj1):<{HEADER_SIZE}}", 
                  "utf-8")+obj1
    conn.sendall(obj3)
    
#----------------------------------------------------------
# Check steps-3&6 .mat read-trigger in IO_PATH Continually!
#----------------------------------------------------------
def isTrigger(path2, TRIGGERS):
    """Checks step-3 & 6 Triggers"""
    fstep3 = os.path.join(path2,TRIGGERS[0])    
    fstep6 = os.path.join(path2,TRIGGERS[1])    
    bstep3 = os.path.exists(fstep3)
    bstep6 = os.path.exists(fstep6)
    return bstep3, bstep6

#----------------------------------------------------------
# A Function that removes a file from disk
#----------------------------------------------------------
def remove_file(path2, filename):
    """Removes files/objects from Disk"""
    try:
        path1 = os.path.join(path2, filename)
        file = glob.glob(path1)
        os.remove(file[0])           
    except:
        print(sys.exc_info()[0])

#----------------------------------------------------------
# The Main Function where every other function is run!
#----------------------------------------------------------
if __name__ == '__main__':  
    """Calls and executes all other functions"""

    rn = 1 # Rounds counter
    while True:
        # Reset Counter
        if rn > 65535:
            rn =1
    #------------------------------------------------------          
        print('******************************************')
        print('Waiting For A Trigger From MATLAB ...')
        print('---------------------------------------') 
        bstep3, bstep6 = isTrigger(IO_PATH, TRIGGERS)   
        print(f"At Round {rn}")     
        print('******************************************')
    #------------------------------------------------------              
        if bstep3 == True:
            print('**************************************')
            disp_msg0 = f"Processing Step-3 Of The "
            print(disp_msg0+f"DC_OMP_TA, @ Round {rn} ...")
            print('--------------------------------------')
            ClientSocket = socket.socket(socket.AF_INET, 
                              socket.SOCK_STREAM)
            print('**************************************')

    #------------------------------------------------------            
            obj_g2w2 = read_mat(IO_PATH,MAT_FILE_NAME3[0]) 
            print("obj_g2w2", obj_g2w2)            
            if isinstance(obj_g2w2, bool) == True: 
                print('**********************************')                
                print("No obj_g2w2.mat Object To Be Sent!")
                print('**********************************')
                continue     
            else:
                print('**********************************')
                print('Local Object obj_g2w2 Read...')
                print('----------------------------------')  
                print(f"obj_g2w2 = {obj_g2w2}")     
                print('**********************************')
    #------------------------------------------------------
            try:
                ClientSocket.connect((SERV_IP, SERV_PORT))
            except socket.error as e:
                print(str(e))
    #------------------------------------------------------
            print('**************************************')
            disp_msg1 = "Waiting To Send Local Mat Object"
            print(disp_msg1 + " To Other Peers ...")
            print('--------------------------------------')
            send_obj(ClientSocket, obj_g2w2, CUR_NODE_ID,
                            TA_STEPS[0])             
            print('--------------------------------------')
            print('obj_g2w2.mat Object Was Sent To Peers')
            print(obj_g2w2)
            print('**************************************')            
    #------------------------------------------------------
            print('**************************************')
            disp_msg3 = "Waiting To Receive Objects " 
            print(disp_msg3 + 'From Other Peers...')
            print('--------------------------------------')     
            obj_mat_all = recv_obj(ClientSocket,RECV_BYTES, 
                                              HEADER_SIZE)             
            disp_msg3 = "obj_mat_all.mat Received From "            
            print(disp_msg3 + ' Other Peers...')
            print('--------------------------------------')
            print(obj_mat_all)
            print('**************************************') 

    #------------------------------------------------------  
            print('**************************************')
            disp_msg4 = "Saving obj_mat_all.mat To "            
            print(disp_msg4 + 'MATLAB Work Space...')            
            print('--------------------------------------')                     
            save_mat(IO_PATH, MAT_FILE_NAME3[1],
                                               obj_mat_all) 
            print("obj_mat_all Was Successfully Saved!") 
            print('**************************************')
    #------------------------------------------------------ 
            print('**************************************')
            disp_msg5 = "Removing Triggers From MATLAB"
            print(disp_msg5+' Work Space...')
            print('--------------------------------------')           
            remove_file(IO_PATH, TRIGGERS[0])  
            remove_file(IO_PATH, MAT_FILE_NAME3[0]+".mat")            
            trig = "Triggers/Inputs Were Successfully "
            print(trig + "Removed From Work Space")
            print('**************************************')
    #------------------------------------------------------        
            print('**************************************')
            dp = f" @ Round {rn}"
            print(f"End Of Step-3 Of The DC_OMP_TA"+dp)
            print('--------------------------------------')

    #------------------------------------------------------
    #------------------------------------------------------
        elif bstep6 == True and bstep3 == False:
            print('**************************************')
            disp0 = f"Processing Step-6 The "
            print(disp0+f"DC_OMP_TA, @ Round {rn} ...")
            print('--------------------------------------')
            print('**************************************')
            print("Processing Step-3 of The DC_OMP_TA ...")
            ClientSocket = socket.socket(socket.AF_INET, 
                              socket.SOCK_STREAM)
            print('**************************************')
    #------------------------------------------------------
            obj_f2w2 = read_mat(IO_PATH,MAT_FILE_NAME6[0])             
            if isinstance(obj_f2w2, bool) == True:  
                print('**********************************')               
                print("No obj_f2w2.mat Object To Be Sent!")
                print('**********************************')
                continue  
            else:
                print('**********************************')
                print('Local Object obj_f2w2 Read...')
                print('----------------------------------')  
                print(f"obj_f2w2 = {obj_f2w2}")     
                print('**********************************')  
                
    #------------------------------------------------------
            try:
                ClientSocket.connect((SERV_IP, SERV_PORT))
            except socket.error as e:
                print(str(e))
    #------------------------------------------------------
            print('**************************************')
            print('Waiting To Send Mat Object To Peers...')
            print('--------------------------------------')            
            send_obj(ClientSocket, obj_f2w2, CUR_NODE_ID,
                            TA_STEPS[1])            
            print('--------------------------------------')
            print('obj_f2w2.mat Object Sent To Peers...')
            print(obj_f2w2)
            print('--------------------------------------')
            print('**************************************')
    #------------------------------------------------------
            print('**************************************')
            disp_msg6 = "Waiting To Receive Objects "
            print(disp_msg6 + 'From Other Peers...')
            print('--------------------------------------')    
            obj_mat_fs = recv_obj(ClientSocket, RECV_BYTES, 
                                              HEADER_SIZE)             
            print('--------------------------------------')
            print('obj_mat_fs Received From Other Peers!')
            print(obj_mat_fs)            
            print('**************************************')

    #------------------------------------------------------  
            print('**************************************')
            disp_msg7 = "Saving obj_mat_fs.mat To MATLAB"
            print(disp_msg7 + ' Work Space...')
            print('**************************************')                     
            save_mat(IO_PATH,MAT_FILE_NAME6[1],obj_mat_fs) 
    #------------------------------------------------------ 
            print('**************************************')
            disp_msg8 = "Removing Triggers From MATLAB "
            print(disp_msg8 + 'Work Space ...')
            print('--------------------------------------')  
            remove_file(IO_PATH, TRIGGERS[1])             
            remove_file(IO_PATH, MAT_FILE_NAME6[0]+".mat")            
            eras = "Triggers/Inputs Were Successfully"
            print(eras + " Removed From Work Space!")
            print('**************************************')

    #------------------------------------------------------        
            print('**************************************')
            dp2 = f" @ Round {rn}"
            print(f"End Of step-6 Of The DC_OMP_TA"+dp2)
            print('**************************************')
    #------------------------------------------------------        
        else:
            pass
        rn += True
    #------------------------------------------------------        
    ClientSocket.close()

#----------------------------------------------------------
# End of p2p2.py program, which acts like a peer/client!
#----------------------------------------------------------

#----------------------------------------------------------
# Configuration File of Peer/Server
#----------------------------------------------------------
#----------------------------------------------------------
#!/usr/bin/env python3
"""
Created on Sunday September 26 15:04:58 2021
@author: alem fitwi
"""
#----------------------------------------------------------
#----------------------------------------------------------
# Relative path to configuration file, CONFIG_PATH
#---------------------------------------------------------- 
CONFIG_PATH = "config_mdl_p2p1"

#----------------------------------------------------------
# Input_output path setting,IO_PATH
#---------------------------------------------------------- 
IO_PATH="C:\\Users\\Alem\\Desktop\\DC_OMP_TA\\MATLAB\\"
# IO_PATH = "D:\\DC_OMP_TA_Project\\" # for Windows OS

#----------------------------------------------------------
# User-defined Message Header-size, HEADER_SIZE
#----------------------------------------------------------
HEADER_SIZE = 17

#----------------------------------------------------------
# Server Port Number (p2p1.py), SERV_PORT
#----------------------------------------------------------
SERV_PORT = 55577

#----------------------------------------------------------
# IPv4 Address of p2p1, SERV_IP
#----------------------------------------------------------
SERV_IP = '128.226.80.61'

#----------------------------------------------------------
# List of IDs of the three Nodes, namely p2p1, p2p2, & p2p3
#----------------------------------------------------------
NODES_ID = ['obj_g1w1', 'obj_g2w2', 'obj_g3w3']
CUR_NODE_ID = 'obj_g1w1'

#----------------------------------------------------------
# List of Server-side DC-OMP-TA Keys 
#----------------------------------------------------------
SERV_KEYS3 = ['g1', 'w1']
SERV_KEYS6 = ['ff1', 'ww1']
#----------------------------------------------------------
# Dictionary all possible keys of other peers
#----------------------------------------------------------
KEYS_DICT_STEP3 = {'obj_g2w2': ['g2', 'w2'], 
                   'obj_g3w3': ['g3', 'w3']}

KEYS_DICT_STEP6 = {'obj_g2w2': ['ff2', 'ww2'], 
                   'obj_g3w3': ['ff3', 'ww3']}

#----------------------------------------------------------
# Number of Bytes received in a single communication
#----------------------------------------------------------
# Linux OS: 
    # TCP Receive Buffer Size (Min Default Max) in Bytes
        # $ cat /proc/sys/net/ipv4/tcp_rmem
        # $ sudo sysctl net ipv4.tcp_rmem
    # TCP Send Buffer Size (Min Default Max) in Bytes
        # $ cat /proc/sys/net/ipv4/tcp_wmem
        # $ sudo sysctl net ipv4.tcp_wmem
RECV_BYTES = 1048576 # Bytes

#----------------------------------------------------------
# Template For Aggregated .mat file sent back to all peers
#----------------------------------------------------------
DICTGW = {"Project":"DC_OMP_TA","By":"Alem Fitwi & Yu Chen",
        "error":"No Error!",
         "g1": '', 'w1': '', 'g2': '', 'w2': '', 'g3': '',
         "w3":''}
DICTFW = {"Project":"DC_OMP_TA","By":"Alem Fitwi & Yu Chen",
        "error":"No Error!"}

#----------------------------------------------------------
# Step-3 & Step-7 Read-Trigger Filenames
#----------------------------------------------------------
TRIGGERS = ['step3triggerw1g1.txt','step6triggerw1f1.txt']

#----------------------------------------------------------
# Object names for Step-3 & Step-6 of DC-OMP_TA
#----------------------------------------------------------
MAT_FILE_NAME3 = ["obj_g1w1", "obj_mat_all", "DICTGW.mat",
                   "error_msg.mat"]
MAT_FILE_NAME6 = ["obj_f1w1", "obj_mat_fs", "DICTFW.mat"]

#----------------------------------------------------------
# Names of Pertinent DC-OMP_TA Steps
#----------------------------------------------------------
TA_STEPS = ['step3', "step6"]

#----------------------------------------------------------
# --------------------------END---------------------------
#----------------------------------------------------------

function send_and_recvp32(g2, w2, d_ID2, trig_fname32)
%------------------------------------------------------
% Variables Assignments
local_obj_name32 = strcat(d_ID2, ".mat")
 
% Set a flag for handling a waiting loop
flag32 = 'False';
%------------------------------------------------------
% Delete stale local and global MATLAB objects
delete(local_obj_name32);
delete obj_mat_all.mat;
%clear g2 w2; 
 
%------------------------------------------------------
% Save scores (g) and corresponding indices (w) as .mat
save(local_obj_name32, "g2", "w2");
 
%------------------------------------------------------
% Send a trigger to python p2p2.py that object is ready 
fid = fopen(trig_fname32,'wt');
fprintf (fid, 'Step3: communication is triggered!');
fclose(fid);
 
%------------------------------------------------------
% Wait until [(g2, w2)] & [(g1, w1), (g3, w3)] are sent
% to other peers and received from other peers, 
% respectively.
disp ("Waiting for updates from other peers...");
 
while 1    
    try
        %clear all;
        load obj_mat_all.mat;
        flag32 = 'True';
    catch
        flag32 = 'False';
        disp("-----------------------------------------------");
        disp ("Still waiting for updates ...");
        disp("-----------------------------------------------");
    end   
    
    if strcmp(flag32,'True')
        break;
    else
        continue;
    end
    
end
disp("-----------------------------------------------");
disp("Scores & indices received from other peers...");
disp("-----------------------------------------------");
 
%------------------------------------------------------
% Remove trigger flag from disk 
delete(trig_fname32);
%------------------------------------------------------    
end
%------------------------------------------------------    

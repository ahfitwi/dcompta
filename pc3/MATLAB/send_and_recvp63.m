function send_and_recvp63(ff3, ww3, fn63, trig_fname63)
%------------------------------------------------------
% Variables Assignments
local_obj_name63 = strcat (fn63, ".mat");
 
% Set a flag for handling a waiting loop
flag_main63 = 'False';
%------------------------------------------------------
% Delete stale local and global MATLAB objects
delete(local_obj_name63);
delete obj_mat_fs.mat; %Dictionary of updates
%clear ff3 ww3; 
 
%------------------------------------------------------
% Save scores (g) and corresponding indices (w) as .mat
% If no updates, please set ff to empty!
if isempty(ww3);
    flag = 'False';
    save(local_obj_name63, "ff3", "ww3", "flag");
else
    flag = 'True';
    save(local_obj_name63, "ff3", "ww3", "flag");
end
%------------------------------------------------------
% Send a trigger to python p2p1.py that object is ready 
fid = fopen(trig_fname63,'wt');
disp("--------------------------------------------")
fprintf (fid, 'Step6: communication is triggered!');
disp('Step6: communication is triggered!')
disp("--------------------------------------------")
fclose(fid);
 
%------------------------------------------------------
% Wait until [(f3, w3)] & [(f2, w2), (f1, w1)] are sent
% to other peers and received from other peers, 
% respectively.
disp("--------------------------------------------")
disp ("Waiting for updates from other peers...");
disp("--------------------------------------------")
 
while 1    
    try
        %clear all;
        load obj_mat_fs.mat;
        flag_main63 = 'True';
    catch
        flag_main63 = 'False';
        disp("--------------------------------------------")
        disp ("Still waiting for updates ...");
        disp("--------------------------------------------")
    end   
    
    if strcmp(flag_main63,'True')
        break;
    else
        continue;
    end
    
end
disp("--------------------------------------------")
disp ("Scores updates between peers is complete ...");
disp("--------------------------------------------")
%------------------------------------------------------
% Remove trigger flag from disk 
delete(trig_fname63);
%------------------------------------------------------    
end
%------------------------------------------------------    

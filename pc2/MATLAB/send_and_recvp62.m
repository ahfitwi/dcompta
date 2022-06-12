function send_and_recvp62(ff2, ww2, fn62, trig_fname62)
%------------------------------------------------------
% Variables Assignments
local_obj_name62 = strcat (fn62, ".mat")
 
% Set a flag for handling a waiting loop
flag_main62 = 'False';
%------------------------------------------------------
% Delete stale local and global MATLAB objects
delete(local_obj_name62);
delete obj_mat_fs.mat; %Dictionary of updates
%clear ff2 ww2; 
 
%------------------------------------------------------
% Save scores (g) and corresponding indices (w) as .mat
% If no updates, please set ff to empty!
if isempty(ww2)
    flag = 'False';
    save(local_obj_name62, "ff2", "ww2", "flag");
else
    flag = 'True';
    save(local_obj_name62, "ff2", "ww2", "flag");
end
%------------------------------------------------------
% Send a trigger to python p2p2.py that object is ready 
fid = fopen(trig_fname62,'wt');
fprintf (fid, 'Step6: communication is triggered!');
fclose(fid);
 
%------------------------------------------------------
% Wait until [(f1, w1)] & [(f2, w2), (f3, w3)] are sent
% to other peers and received from other peers, 
% respectively.
disp("-----------------------------------------------");
disp("Waiting for updates from other peers...");
disp("-----------------------------------------------");

while 1    
    try
        %clear all;
        load obj_mat_fs.mat;
        flag_main62 = 'True';
    catch
        flag_main62 = 'False';
        disp("-----------------------------------------------");
        disp ("Still waiting for updates ...");
        disp("-----------------------------------------------");
    end   
    
    if strcmp(flag_main62,'True')
        break;
    else
        continue;
    end
    
end
disp("-----------------------------------------------");
disp ("Scores updates between peers is complete ...");
disp("-----------------------------------------------");
%------------------------------------------------------
% Remove trigger flag from disk 
delete(trig_fname62);
%------------------------------------------------------    
end
%------------------------------------------------------ 

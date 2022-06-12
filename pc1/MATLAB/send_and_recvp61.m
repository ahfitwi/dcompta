function send_and_recvp61(ff1, ww1, fn61, trig_fname61)
%------------------------------------------------------
% Variables Assignments
local_obj_name61 = strcat (fn61, ".mat");
 
% Set a flag for handling a waiting loop
flag_main61 = 'False';
%------------------------------------------------------
% Delete stale local and global MATLAB objects
delete(local_obj_name61);
delete obj_mat_fs.mat; %Set of updates
%clear ff1 ww1; 
 
%------------------------------------------------------
% Save scores (g) and corresponding indices (w) as .mat
% If no updates, please set ff to empty!
if isempty(ww1)
    flag = 'False';
    save (local_obj_name61, "ff1", "ww1", "flag");
else
    flag = 'True';
    save(local_obj_name61, "ff1", "ww1", "flag");
end
%------------------------------------------------------
% Send a trigger to python p2p1.py that object is ready 
fid = fopen(trig_fname61,'wt');
disp("--------------------------------------------")
fprintf (fid, 'Step6: communication is triggered!');
disp("--------------------------------------------")
fclose(fid);
 
%------------------------------------------------------
% Wait until [(f1, w1)] & [(f2, w2), (f3, w3)] are sent
% to other peers and received from other peers, 
% respectively.
disp("--------------------------------------------")
disp("Waiting for updates from other peers...");
disp("--------------------------------------------")

while 1    
    try
        %clear all;
        load obj_mat_fs.mat;
        flag_main61 = 'True';
    catch
        flag_main61 = 'False';
        disp("--------------------------------------------")
        disp("Still waiting for updates ...");
        disp("--------------------------------------------")
    end   
    
    if strcmp(flag_main61,'True')
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
delete(trig_fname61);
%------------------------------------------------------    
end
%------------------------------------------------------    

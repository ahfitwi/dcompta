function send_and_recvp31(g1, w1, d_ID1, trig_fname31)
%------------------------------------------------------
% Variables Assignments
local_obj_name31 = strcat(d_ID1, ".mat");

% Set a flag for handling a waiting loop
flag31 = 'False';
%------------------------------------------------------
% Delete stale local and global matlab objects
delete(local_obj_name31);
delete obj_mat_all.mat;
%clear g1 w1; 

%------------------------------------------------------
% Save scores (g) and correspodning indices (w) as .mat
save(local_obj_name31, "g1", "w1");

%------------------------------------------------------
% Send a trigger to python p2p1.py that object is ready 
fid = fopen(trig_fname31,'wt');
disp("--------------------------------------------")
fprintf(fid, 'communication is triggered!');
disp("--------------------------------------------")
fclose(fid);

%------------------------------------------------------
% Wait until [(g1, w1)] & [(g2, w2), (g3, w3)] are sent
% to other peers and recived from other peers, 
% respectively.
disp("--------------------------------------------")
disp("Waiting for updates from other peers...");
disp("--------------------------------------------")

while 1    
    try
        %clear all;
        load obj_mat_all.mat;        
        flag31 = 'True';
    catch
        flag31 = 'False';
        disp("--------------------------------------------")
        disp("Still waiting for updates ...");
        disp("--------------------------------------------")
    end   
    
    if strcmp(flag31,'True')
        break;
    else
        continue;
    end
    
end
disp("--------------------------------------------")
disp("Scores & indices received from other peers...");
disp("--------------------------------------------")
%------------------------------------------------------
% Remove trigger flag from disk 
delete(trig_fname31);
%------------------------------------------------------    
end
%------------------------------------------------------    

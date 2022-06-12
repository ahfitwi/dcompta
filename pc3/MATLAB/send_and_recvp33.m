function send_and_recvp33(g3, w3, d_ID3, trig_fname33)
%------------------------------------------------------
% Variables Assignments
local_obj_name33 = strcat (d_ID3, ".mat");
 
% Set a flag for handling a waiting loop
flag33 = 'False';
%------------------------------------------------------
% Delete stale local and global MATLAB objects
delete(local_obj_name33);
delete obj_mat_all.mat;
%clear g3 w3; 
 
%------------------------------------------------------
% Save scores (g) and corresponding indices (w) as .mat
save (local_obj_name33, "g3", "w3");
 
%------------------------------------------------------
% Send a trigger to python p2p1.py that object is ready 
fid = fopen(trig_fname33,'wt');
disp("--------------------------------------------")
fprintf (fid, 'Step3: communication is triggered!');
disp("'Step3: communication is triggered!");
disp("--------------------------------------------")
fclose(fid);
 
%------------------------------------------------------
% Wait until [(g3, w3)] & [(g2, w2), (g1, w1)] are sent
% to other peers and received from other peers, 
% respectively.
disp("--------------------------------------------")
disp ("Waiting for updates from other peers...");
disp("--------------------------------------------")
 
while 1    
    try
        %clear all;
        load obj_mat_all.mat;
        flag33 = 'True';
        disp(flag33)
    catch
        flag33 = 'False';
        disp("--------------------------------------------")
        disp ("Still waiting for updates ...");
        disp("--------------------------------------------")
    end   
    
    if strcmp(flag33,'True')
        break;
    else
        continue;
    end
    
end
disp("--------------------------------------------")
disp ("Scores & indices received from other peers...");
disp("--------------------------------------------")
 
%------------------------------------------------------
% Remove trigger flag from disk 
delete(trig_fname33);
%------------------------------------------------------    
end
%------------------------------------------------------    

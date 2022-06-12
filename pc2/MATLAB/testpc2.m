%------------------------------------------------------
% Test MATLAB Code @ PC-2
%------------------------------------------------------
%--------------------------------------------------
% Executing the parts of DC_OMP_TA before step-3
pause(10);
%--------------------------------------------------
% Step-3 of DC_OMP_TA
%--------------------------------------------------
% Assign values to function-3 parameters
g2 = randi(4,4);
w2 = [1:4];
d_ID2 = "obj_g2w2";
trig_fname32 = "step3triggerw2g2.txt";   
%--------------------------------------------------
% Call MATLAB Function of step-3
send_and_recvp32(g2, w2,d_ID2, trig_fname32);
%--------------------------------------------------
% Executing the parts of DC_OMP_TA b/n steps 3 & 6
pause(10);
%--------------------------------------------------
% Step-6 of DC_OMP_TA
%--------------------------------------------------
% Assign values to function-6 parameters
ff2 = randi(3,3) %flag will be set to "True";
ww2 = [1:3];
fn62 = "obj_f2w2";
trig_fname62 = "step6triggerf2g2.txt";    
%--------------------------------------------------
% Call MATLAB Function of step-6
send_and_recvp62(ff2, ww2, fn62, trig_fname62);
%--------------------------------------------------
% The rest of DC-OMP-TA code continues
%--------------------------------------------------
    


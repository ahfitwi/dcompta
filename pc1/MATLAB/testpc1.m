%------------------------------------------------------
% Test MATLAB Code @ PC-1
%------------------------------------------------------
%--------------------------------------------------
% Executing the parts of DC_OMP_TA before step-3
pause(10);
%--------------------------------------------------
% Step-3 of DC_OMP_TA
%--------------------------------------------------
% Assign values to function-3 parameters
g1 = randi(4,4);
w1 = [1:4];
d_ID1 = "obj_g1w1";
trig_fname31 = "step3triggerw1g1.txt";  
%--------------------------------------------------
% Call MATLAB Function of step-3
send_and_recvp31(g1, w1, d_ID1, trig_fname31);
%--------------------------------------------------
% Executing the parts of DC_OMP_TA b/n steps 3 & 6
pause(10);
%--------------------------------------------------
% Step-6 of DC_OMP_TA
%--------------------------------------------------
% Assign values to function-6 parameters
ff1 = randi(3,3); %flag will be set to "True"
ww1 = [1:3];   
fn61 = "obj_f1w1";
trig_fname61 = "step6triggerf1g1.txt";    
%--------------------------------------------------
% Call MATLAB Function of step-6
send_and_recvp61(ff1, ww1, fn61, trig_fname61);
%--------------------------------------------------
% The rest of DC-OMP-TA code continues 
%------------------------------------------------------

%------------------------------------------------------
% Test MATLAB Code @ PC-3
%------------------------------------------------------
%--------------------------------------------------
% Executing the parts of DC_OMP_TA before step-3
pause(10);
%--------------------------------------------------
% Step-3 of DC_OMP_TA
%--------------------------------------------------
% Assign values to function-3 parameters
g3 = randi(4,4);
w3 = [1:4];
d_ID3 = "obj_g3w3";
trig_fname33 = "step3triggerw3g3.txt";    
%--------------------------------------------------
% Call MATLAB Function of step-3
send_and_recvp33(g3, w3,d_ID3, trig_fname33);
%--------------------------------------------------
% Executing the parts of DC_OMP_TA b/n steps 3 & 6
pause(10);
%--------------------------------------------------
% Step-6 of DC_OMP_TA
%--------------------------------------------------
% Assign values to function-6 parameters
ff3 = randi(3,3); %flag will be set to "True"
ww3 = [1:3];   
fn63 = "obj_f3w3";
trig_fname63 = "step6triggerf3g3.txt";    
%--------------------------------------------------
% Call MATLAB Function of step-6
send_and_recvp63(ff3, ww3, fn63, trig_fname63);
%--------------------------------------------------     
%------------------------------------------------------
% The rest of DC-OMP-TA code continues
%------------------------------------------------------

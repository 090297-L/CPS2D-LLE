startup

% specify your paths to the datasets
name = {'0.05', '0.06', '0.07', '0.08', '0.09', '0.1', 'mix0.01-0.05', 'mix0.01-0.10'};
dataset = strcat('data', filesep, name, filesep, '*.*');

% specify methods and metrics
method = {@multiscaleRetinex @dong @npe @lime @mf @srie @BIMEF};
metric = {@loe100x100}; 
% metric = {@loe100x100 @vif}; % NOTE matlabPyrTools is required to run VIF metric (vif.m).

for n = 1:numel(dataset); data = dataset{n};
    data,  
    Test = TestImage(data);        
    Test.Method = method; 
    Test.Metric = metric;
    
    % run test and display results
    Test,                     
    
    % save test to a .csv file
    save(Test); % %save(Test, ['TestReport__' name{n} '.csv']);
end
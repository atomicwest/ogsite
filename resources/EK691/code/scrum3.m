%EK691 Back-up Data Representation, Scrum 2

%newmat = zeros(640, 520); 

%random values in the range of 2ft - 8ft (to match kinect
    %spec range), then convert to meters
    %assume chest cavity thickness is  about 3ft away from the  sensor
%generate random initial point array and distances from camera

[X Y Z] = sphere(250);

X = 2 + 3*rand().*X;
Y = 2 + 3*rand().*Y;
Z = 2 + 3*rand().*Z;
Zprime = Z;
%resolution of the frame is 640x520, 
%imgmap = (xran*0.3048) + (yran*0.3048)*rand(640, 520); 

pause on

%create an array of periodic decrement values for use in the for loop
decx = 1:100;
decrfunc = cos(decx);

for i = 1:length(decx)
    %Z = Zprime;
    %actual decrement value that will apply to the Z value
    decrval = decrfunc(i);
    
    %only want to simulate a torso breathing; turn Z into a hemisphere
    row = 1:(length(Z)/2);
    col = 1:length(Z);
    
    %for j = (length(Z)-1)/2 : length(Z)
        decrvaln = decrval;
        
        
    submat = zeros(row,col);
        Z(row,col) = 0; %min(min(Z))
        
        %statrow = ((length(Z)-1)/2) : length(Z);
        
        submat2 = Z(row, col).^(2*decrval);
        Z(row, col) = submat2;
        
        maxvalue = num2str(max(max(Z)));
        datainfo = strcat('Maximum value: ', maxvalue);
        
    %end
    
        subplot(1,2,1);
       
        pcolor(X,Y,Z);
        surf(X,Y,Z);
        axis([0 4 0 4 0 3])
        title('Breathing Area Map');
        xlabel('Torso Width');
        ylabel('Torso Length');
        zlabel('Torso Depth');
        %set viewpoint of the  subplot
        view([25 15]);
        
        subplot(1,2,2);
        
        hold off
        pcolor(X,Y,Z)
        
        %text(3.5,-0.5,datainfo)
        title(datainfo)
        xlabel('Torso Width');
        ylabel('Torso Length');
        shading interp
        hold on
        %contour(X,Y,Z,30,'k');  
        
        pause(0.5)
end
%testsurf
[X, Y] = meshgrid(-4:0.1:4);

pause on
count = 0;
while true
    
    for i = 1:9
        Z = (0.015*i*exp(-(X.^4 + (Y.^4)/7 )));
        count = count + 1;
        maxval = max(max(Z));
        maxvaluestr = num2str(maxval);
        datainfo = strcat('Maximum value: ', maxvaluestr);
    
        subplot(1,2,1)
    
        surf(X,Y,Z)
        title('Breathing Area Map');
        xlabel('Torso Width');
        ylabel('Torso Length');
        zlabel('Torso Depth');
    
        axis([-2 2 -2 2 0 0.5])
        %view([+34.5 14])
    
        subplot(1,2,2);
            
        hold on
        %pcolor(X,Y,Z)
        plot(count, maxval, '--b*')
        title(datainfo)
        xlabel('Time');
        ylabel('Breath Depth');
        %shading interp
        if maxval > 0.11
            icon = imread('warnex.jpg');
            h = msgbox('Irregular breathing pattern detected','WARNING', 'custom', icon);
        end 
        %contour(X,Y,Z,30,'k'); 
    
        pause(0.25)
    end


    for i = 1:9
        Z = (0.015*(10-i)*exp(-(X.^4 + (Y.^4)/7 )));
        count = count + 1;
        maxval = max(max(Z));
        maxvaluestr = num2str(maxval);
        datainfo = strcat('Maximum value: ', maxvaluestr);
    
        subplot(1,2,1)
    
        surf(X,Y,Z)
        title('Breathing Area Map');
        xlabel('Torso Width');
        ylabel('Torso Length');
        zlabel('Torso Depth');
        axis([-2 2 -2 2 0 0.5])
        %view([+34.5 14])
    
    
        subplot(1,2,2);
            
        hold on
        %pcolor(X,Y,Z)
        plot(count, maxval, '--b*')
        title(datainfo)
        xlabel('Time');
        ylabel('Breath Depth');
        %shading interp
        
        %contour(X,Y,Z,30,'k'); 
    
        pause(0.25)
    end
end
%Z = -sqrt(abs(X.^2) - Y.^2);

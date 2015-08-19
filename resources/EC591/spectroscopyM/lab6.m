function lab6(filename)
    
%call function lab6('file.txt')

    fid = fopen(filename,'r');
    v1 = fscanf(fid,'%f');
    v1a = zeros((length(v1)/2),1);%create v1a, the wavelength vector
    v2 = zeros((length(v1)/2),1); %create v2, the intensity vector
    count = 1;

for i = 2:2:length(v1)
    v1a(count) = v1(i-1);
    v2(count) = v1(i);
    count = count + 1;
end

plot(v1a, v2, 'k')
xlabel('Wavelength (nm)')
ylabel('Intensity')
newtitle = filename(1:(length(filename) - 4));
title(newtitle)
axis([340 1100 0 4000])

imgsave = strcat(newtitle, '.png');
saveas(gcf, imgsave, 'png')

fclose(fid);

end
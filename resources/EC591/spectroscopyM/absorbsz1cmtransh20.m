function absorbsz1cmtransh20(filename)
%absorption coefficient is in centimeters
%open aqueous solution measurements
    fid1 = fopen(filename,'r');
    v1 = fscanf(fid1,'%f');
    v1a = zeros((length(v1)/2),1);%initialize wavelength vector
    v1b = zeros((length(v1)/2),1); %initialize intensity vector
    count1 = 1;

%separate file formatting/create appropriate data vectors
    for i = 2:2:length(v1)
        v1a(count1) = v1(i-1);
        v1b(count1) = v1(i);
        count1 = count1 + 1;
    end


%create new vector to store absorbance spectrum
v1c = zeros(length(v1a),1);

for a = 1:length(v1a)
    v1c(a) = log(abs(v1b(a))); %for alpha in cm
end

% outmat = [v1a, v1b];
%store wavelength and intensity in one vector to be read into a table with
%two columns
outvec = zeros(length(v1a),1);
for k = 2:2:2048
    outvec(k-1) = v1a(k-1);
    outvec(k) = v1c(k);
end

%save data as txt
txtdel = strfind(filename, '.txt');
filename(txtdel:end) = [];
savename = strcat(filename, '-absorbsmall.txt');
fid3 = fopen(savename, 'w');
fprintf(fid3, '%f %f\r\n', outvec);

%plot absorption spectrum
plot(v1a, v1c, 'k')
xlabel('Wavelength (nm)')
ylabel('Absorption Coefficient (1/cm)')
newtitle = strcat(filename, ' absorption');
title(newtitle)
axis([340 1100 0 500])

imgsave = strcat(newtitle, '.png');
saveas(gcf, imgsave, 'png')

fclose(fid3);

fclose(fid1);
% fclose(fid2);

end
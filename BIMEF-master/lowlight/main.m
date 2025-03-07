I = imread('yellowlily.jpg');  % a color image
J = lime(I);                   % or other method
subplot 121; imshow(I); title('Original Image');
subplot 122; imshow(J); title('Enhanced Result');
// Write a JavaScript function named swapRedGreen with one parameter pixel (representing a single pixel). 
// This function should swap the red and green values of the pixel. 
// For example, if you have a pixel with red = 255, green = 100, blue = 150, after calling swapRedGreen on that pixel its new RGB values would be red = 100, green = 255, blue = 150.

var img = new SimpleImage("skyline.jpg");
function swapRedGreen(pixel){
    var newRed = pixel.getGreen();
    var newGreen = pixel.getRed();
    pixel.setRed(newRed);
    pixel.setGreen(newGreen);
    return pixel;
}

for (var pixel of img.values()){
    swapRedGreen(pixel)
}
print(img)
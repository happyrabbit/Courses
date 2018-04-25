// Write code to change the blue to be yellow
var img = new SimpleImage("duke_blue_devil.png");
for (var pixel of img.values()){
    // use this to define blue : )
    if (pixel.getBlue() > pixel.getRed() + pixel.getGreen() ){
    pixel.setRed(255);
    pixel.setGreen(255);
    pixel.setBlue(0);    
    }
}

print(img)


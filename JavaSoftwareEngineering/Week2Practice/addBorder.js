// Write a function named setBlack that has one parameter pixel (representing a single pixel) 
// and returns pixel with its red, green, and blue components changed 
// so that the pixel’s color is black.

var img = new SimpleImage("chapel.png")

function setBlack(pixel){
        pixel.setRed(0);
        pixel.setGreen(0);
        pixel.setBlue(0);
    return pixel;
}

// test function

for (pixel of img.values()){
    pixel=setBlack(pixel);
}
print(img)

// write another function named addBorder. This function will add a black border to an image

var img = new SimpleImage("smallpanda.png")

function addBorder(image, thickness){
    for (var pixel of image.values()){
        if (pixel.getX() < thickness){
            pixel = setBlack(pixel);
        }
        if (pixel.getX() >= image.getWidth()-thickness){
            pixel = setBlack(pixel);
        }
        if (pixel.getY() < thickness){
            pixel = setBlack(pixel);
        }
        if (pixel.getY() >= image.getHeight()-thickness){
            pixel = setBlack(pixel);
        }
    }
    return image;
}

print(addBorder(img, 10))

// another add border function that allows for differnt horizontal and vertical width 

function pixelOnEdge(image,pixel,horizontalThick, verticalThick){
    var x = pixel.getX();
    var y = pixel.getY();
    if (x < verticalThick || x > image.getWidth() - verticalThick){
        return true;
    }
    if (y < horizontalThick || y > image.getHeight() - horizontalThick){
        return true;
    }
    return false;
}

function addBorders(image,horizontalThick, verticalThick){
    for (var px of image.values()){
        if (pixelOnEdge(image,px,horizontalThick,verticalThick)){
            px = setBlack(px);
        }
    }
    return image;
}

var img = new SimpleImage("skyline.jpg");
img = addBorders(img,40,20);
print(img);
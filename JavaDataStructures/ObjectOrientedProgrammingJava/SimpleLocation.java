// Defining Classes and Objects
// Object Oriented Java Programming: Data Structures and Beyond
// Course 1 and Week1

public class SimpleLocation 
{
    public double latitude;
    public double longitude;
    
    public SimpleLocation(double lat, double lon)
    {
        this.latitude = lat;
        this.longitude = lon;
    }
    public double distance(SimpleLocation other)
    {
        return getDist(this.latetude, this.longitude,
                      other.latitude, other.longitude);
    }
}
  
int setPoint = 55;
String readString;
void setup()
{

  Serial.begin(9600);  // initialize serial communications at 9600 bps

}

void loop()
{
  while(!Serial.available()) {}
  // serial read section
  while (Serial.available())
  {
    if (Serial.available() >0)
    {
      readString = Serial.readString();  
    }
  }

  if (readString.length() >=0)
  {
    Serial.print("arduino received: ");
    Serial.println(readString); 
  }


}

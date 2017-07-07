#define Calibrando 1
#define Fin 0

int direc=2;
int stp=3;
int sleep=4;
int reset=5;
int ms3=6;
int ms2=7;
int ms1=8;
int enable=9;
int findecarrera=10;
unsigned long PasosRealizados;
int t=10;
unsigned long PasosEnviados;
String readString;

void setup() 
{
  pinMode(enable,OUTPUT);
  pinMode(stp,OUTPUT);
  pinMode(direc,OUTPUT);
  pinMode(reset,OUTPUT);
  pinMode(sleep,OUTPUT);
  pinMode(ms1,OUTPUT);
  pinMode(ms2,OUTPUT);
  pinMode(ms3,OUTPUT);
  pinMode(findecarrera,INPUT_PULLUP);
  digitalWrite(enable,LOW);
  digitalWrite(direc,LOW);
  digitalWrite(sleep,HIGH);
  digitalWrite(reset,HIGH);
  digitalWrite(ms1,HIGH);
  digitalWrite(ms2,HIGH);
  digitalWrite(ms3,HIGH);
  Serial.begin(9600);
  
}

void loop() 
{
int estado=Calibrando;
  switch (estado) 
  {
     case Calibrando:
          while(!Serial.available()) {}
       // serial read section
          while ((Serial.available()) )
          {
            if (Serial.available() >0)
            {
              readString = Serial.readString();  
            }
          }
          if (readString.length() >=0)
          {
          Serial.print("\t PasosEnviados= ");
          Serial.println(readString);
          PasosEnviados=readString.toInt();
          } 
          PasosRealizados=1;
          while ((PasosEnviados>0) && (PasosRealizados<PasosEnviados))
          {   
            if (digitalRead(findecarrera))
            {   
             digitalWrite(stp,HIGH);
             delay(t);
             digitalWrite(stp,LOW);
             delay(t);
             PasosRealizados=PasosRealizados+1;
             Serial.print("dT=");
             Serial.println(2*t);
             Serial.print("\t PasosRealizados=");
             Serial.println(PasosRealizados);              
             }
             else
             {  
              Serial.println("else"); 
              estado=Fin;
             }  
             if (Serial.available())
             {
              break;
             }     
           }
           break;
     case Fin:
          Serial.println("Fin"); 
           break; 
 
  }
}

  

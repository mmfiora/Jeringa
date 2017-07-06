#define Calibrando 1
#define Fin 0

int enable=8;
int direc=9;
int stp=10;
int led=13;
int fin=2;
unsigned long PasosRealizados;
int t=10 ;
unsigned long PasosEnviados;
String readString;

void setup() {
  pinMode(enable,OUTPUT);
  pinMode(stp,OUTPUT);
  pinMode(direc,OUTPUT);
  pinMode(fin,INPUT_PULLUP);
  digitalWrite(enable,LOW);
  digitalWrite(direc,LOW);
  Serial.begin(9600);
  
}
void loop() {
int estado=Calibrando;  
  switch (estado) {
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
       // pasos=300;
         } 

      for (int i=0; i < PasosEnviados; i++){      
      digitalWrite(stp,HIGH);
      delay(t);
      digitalWrite(stp,LOW);
      delay(t);
      PasosRealizados=PasosRealizados+1;}
       Serial.print("dT=");
       Serial.print(2*t);
       Serial.print("\t PasosRealizados=");
       Serial.print(PasosRealizados);              
       Serial.print("\nFIN");
       estado=Fin;
       break;
     case Fin:
     
       break; 
 
}
}

  

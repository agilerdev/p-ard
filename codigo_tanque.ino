char var = 's';         // variable to receive data from the serial port
int M1L = 3;// PWM el 3, 5, 6 y 9 son los puertos que estamos usando en el arduino para conectarlo con el puente H
int M1R = 5;// PWM
int M2L = 9;// PWM
int M2R = 6;// PWM
int vel = 255;

void setup()
{
  pinMode(M1L, OUTPUT);                                
  pinMode(M1R, OUTPUT);
  pinMode(M2L, OUTPUT);                                
  pinMode(M2R, OUTPUT);
  Serial.begin(9600);       // start serial communication at 9600bps

}

void loop() {
  if( Serial.available() )       // if data is available to read
  {      
       var= Serial.read();         // val means entrance value
    
    if( var == 'r' )
    {
      //Adelante
      analogWrite(M1L, vel); analogWrite(M2L, vel);
      analogWrite(M1R, LOW); analogWrite(M2R, LOW);                 
    }
    else if( var == 'a' )           
    {
      //Reversa
      analogWrite(M1L, LOW); analogWrite(M2L, LOW); 
      analogWrite(M1R, vel); analogWrite(M2R, vel);                   
    }
    else if( var == 'i' )       
    {
      //Izquierda
      analogWrite(M1L, LOW); analogWrite(M2L, vel);    
      analogWrite(M1R, vel); analogWrite(M2R, LOW);              
    }
   else if( var == 'd' )              
    {
      //Derecha
      analogWrite(M1L, vel); analogWrite(M2L, LOW);
      analogWrite(M1R, LOW); analogWrite(M2R, vel);                 
    }    
   else if( var == 's' ) 
   { //Parar
      analogWrite(M1L, LOW); analogWrite(M2L, LOW);
      analogWrite(M1R, LOW); analogWrite(M2R, LOW);  
    } 
    
  }
}









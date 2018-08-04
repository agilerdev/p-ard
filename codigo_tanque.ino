char var = 's';       // Variable to receive data from the serial port
int M1L = 3;          // PWM el 3, 5, 6 y 9 son los puertos que estamos usando en el arduino para conectarlo con el puente H
int M1R = 5;          // PWM
int M2L = 9;          // PWM
int M2R = 6;          // PWM
int vel = 255;        // 255 es la velocidad maxima a la cual podemos llegar con nuestros motores

void setup()
{
  pinMode(M1L, OUTPUT);     // Definimos que los pines que usaremos los usaremos como salida pues necesitamos que ellos reciban la informacion                     
  pinMode(M1R, OUTPUT);     // que enviamos y dependiendo de esta cambien
  pinMode(M2L, OUTPUT);                                
  pinMode(M2R, OUTPUT);
  Serial.begin(9600);       // Es la frecuencia a la cual se estara comunicando el arduino 9600bps

}

void loop() {
  if( Serial.available() )          // Si es que hay informacion disponible entraremos en el bucle
  {                                 // Todas estas variables llegaran a traves del programa hecho en python que las enviara a traves de un modulo Bluetooth
       var = Serial.read();         // var es para los valores que estan entrando
    
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










class Light{
  public:
    uint8_t redPin;  
    uint8_t yellowPin;
    uint8_t greenPin;
    void init(){
      pinMode(redPin, OUTPUT);
      pinMode(yellowPin, OUTPUT);
      pinMode(greenPin, OUTPUT);
    }
    void setGreen(){
      digitalWrite(redPin,0);
      digitalWrite(yellowPin,0);
      digitalWrite(greenPin, 255);      
    }
    void setYellow(){
      digitalWrite(redPin,0);
      digitalWrite(yellowPin,255);
      digitalWrite(greenPin, 0);      
    }
    void setRed(){
      digitalWrite(redPin,255);
      digitalWrite(yellowPin,0);
      digitalWrite(greenPin, 0);      
    }
    Light(uint8_t redPin_, uint8_t yellowPin_, uint8_t greenPin_){
      redPin_ = redPin;
      yellowPin_ = yellowPin;
      greenPin_ = greenPin;
    }
};
class Intersection{
  public:
    Light lights[4];
    int PrevTime = 0; // previous light switch time
   int duration = 100000; //light cycle duration
    // state 0 = double red; state 1 =  a is green  b is red ; 2 =  a is red b is greed
    int state = 0;
    intersection(int duration_,int lights_){
       duration_ = duration;
      lights_ = lights;
      };
};
void setup() {
  Intersection a(10000,new Light{ new Light(2,3,4), new Light(5,6,7), new Light(8,9,10)};
  )
  
}

void loop() {
  
  
  
}



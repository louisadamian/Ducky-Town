class StopLight{
  public:
    int timeing;
    uint8_t state = 0;// 0: double red going to A greenA; 1: = A greed, 2: double red going to B green, 3: B green;
    uint8_t redPinA;
    uint8_t redPinB;
    uint8_t greenPinA;
    uint8_t greenPinB;
    Stoplight(uint8_t redPinA_,uint8_t greenPinA_, uint8_t redPinB_, uint8_t greenPinB_){
      redPinA_ = redPinA;
      greenPinA_ = greenPinA;
      redPinB_ = redPinB;
      greenPinB_ = greenPinB;
    }
  void init(){
    pinMode(redPinA, OUTPUT);
    pinMode(redPinB, OUTPUT);
    pinMode(greenPinA, OUTPUT);
    pinMode(greenPinB, OUTPUT);
  }
  void greenA(){
    digitalWrite(greenPinA, HIGH);
    digitalWrite(redPinA, LOW);
    digitalWrite(greenPinB, LOW);
    digitalWrite(redPinB, HIGH);
    state = 1;
  }
  void greenB(){
    digitalWrite(greenPinA, LOW);
    digitalWrite(redPinA, HIGH);
    digitalWrite(greenPinB, HIGH);
    digitalWrite(redPinB, LOW);
    state = 3
  }
  void allRed(){
    digitalWrite(redPinA, HIGH);
    digitalWrite(redPinB, HIGH);
    digitalWrite(greenPinA, LOW);
    digitalWrite(greenPinB, LOW);
  }
  change(){
    if (prevTime- millis >= timing)
    if( state == 0){
      greenA();
    }else if(state == 1){
      allRed();
      state = 2
    }else if(state == 2){
      greenB();
    }else if(state == 3){
      allRed()
      state = 0
    }
  }
};

StopLight lightA(2,3,4,5);
stoplight lightB(6,7,8,9);

void setup(){
  lightA.init();

  while(true){
    LightA.chnage();
  }
void loop(){


}

//Rotary Encoder
/*You will see the angular displacement of the rotary encoder printed on Serial Monitor. 
When you turn the rotary encoder clockwise, the angular displacement is increased;
when turn it counterclockwise, the displacement is decreased.
If you press the switch on the rotary encoder, the readings will return to zero.*/
//Email: support@sunfounder.com
//Website: www.sunfounder.com
//2015.5.7
 
const int clkPin= 2; //the clk attach to pin 2
const int dtPin= 3; //the dt pin attach to pin 3

const int clk2Pin= 13; //the clk attach to pin 2
const int dt2Pin= 12; //the dt pin attach to pin 3

 
int encoderVal = 0;
int encoderVal2=0;
int checkMotorSpeedCounter=0;
int changeVal=0;

void setup()
{ 
//set clkPin,dePin,swPin as INPUT
pinMode(clkPin, INPUT);
pinMode(dtPin, INPUT);

pinMode(clk2Pin,INPUT);
pinMode(dt2Pin,INPUT);

Serial.begin(9600); // initialize serial communications at 9600 bps
}

void loop()
{

int change2=getEncoderTurn2();
int change=getEncoderTurn();
encoderVal = encoderVal + change;
encoderVal2 = encoderVal2 + change2;
checkMotorSpeedCounter+=1;
if (checkMotorSpeedCounter >5) {
  int straightVal=encoderVal2-encoderVal;
  if(straightVal>0) {Serial.println("increase the left motor");} //increase the left motor
  else {Serial.println("Increase the right motor"); }
}


if(change<1 && change2<2) {
changeVal+=1;
if (changeVal >=10) {  
Serial.println("NoMovement");
changeVal=0;}
}

}
int getEncoderTurn(void)
{
static int oldA = HIGH; //set the oldA as HIGH
static int oldB = HIGH; //set the oldB as HIGH
int result = 0;
int newA = digitalRead(clkPin);//read the value of clkPin to newA
int newB = digitalRead(dtPin);//read the value of dtPin to newB
if (newA != oldA || newB != oldB) //if the value of clkPin or the dtPin has changed
{
// something has changed
if (oldA == HIGH && newA == LOW)
{
result = (oldB * 2 - 1);
}
}
oldA = newA;
oldB = newB;
return result;
}


int getEncoderTurn2(void)
{
static int oldA = HIGH; //set the oldA as HIGH
static int oldB = HIGH; //set the oldB as HIGH
int result = 0;
int newA = digitalRead(clk2Pin);//read the value of clkPin to newA
int newB = digitalRead(dt2Pin);//read the value of dtPin to newB
if (newA != oldA || newB != oldB) //if the value of clkPin or the dtPin has changed
{
// something has changed
if (oldA == HIGH && newA == LOW)
{
result = (oldB * 2 - 1);
}
}
oldA = newA;
oldB = newB;
return result;
}



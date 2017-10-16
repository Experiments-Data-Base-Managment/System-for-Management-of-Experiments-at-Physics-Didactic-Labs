/*******************************************************************
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 *//****************************************************************/

#include <MsTimer2.h>

const char END_TRANSMISSION = '0';
const char TO_START_EXPERIMENT = '1';
const char TO_SEND_DURATION_EXPERIMENT = '2'; 

volatile  int time_ = 0;
volatile int previous_time = 0;
volatile float volt = 0.0;

const long resistor = 47;
const long capacitor = 3300;
const long tal = 5*((resistor*capacitor)/1000); //capacitor's charge time
char signal_code = ' ';
const unsigned int reset_pin = 3;

/*
 * Configura o intervalo de tempo em que os dados serÃ£o enviados
 * e ativa o reset para empedir que a corrente chegue atÃ© o capacitor antes do usuÃ¡rio
 * iniciar o experimento.
 */
void setup() {
  pinMode( reset_pin, OUTPUT );
  Serial.begin( 9600 );
  MsTimer2::set( 1000, measurement );
  digitalWrite( reset_pin, HIGH );
}

void loop() {

  /*
   * Bloco de cÃ³digo que mantÃ©m o sistema em estado de espera
   * atÃ© que o usuÃ¡rio inicie-o por meio da interface grÃ¡fica.
  */
  if(signal_code != TO_START_EXPERIMENT){
    signal_code = waitForRequest(TO_SEND_DURATION_EXPERIMENT);
    Serial.print(tal);
    signal_code = waitForRequest(TO_START_EXPERIMENT);
    digitalWrite( reset_pin, LOW );
    MsTimer2::start();    
  }

  /*
   * Monitora a tensÃ£o na porta analogica e
   * converter o valor de entrada para a faixa de 0 a 5 V.
   */
  volt = analogRead( 0 );
  volt = convertIntoVolts( volt );  


  /*  
   *  Bloco de cÃ³digo que verifica a mudanÃ§a do tempo, e caso haja mudanÃ§a,
   *  envia os dados monitorados pela porta serial e atualiza o tempo anterior para o tempo atual.
   */
  if(previous_time != time_){
    Serial.print( time_ );
    Serial.print( ";" );
    Serial.print( volt );
    previous_time = time_;
  } 

  
  /*
   * A interrupÃ§Ã£o de tempo Ã© desativada e as variÃ¡veis, de tempo
   * e de signal, sÃ£o modificadas para os valores iniciais. E o reset Ã© ativado para descarregar o capacitor
   */
  if(time_ == tal){
    MsTimer2::stop();
    time_ = 0;
    signal_code = ' ';
    digitalWrite( reset_pin, HIGH );
    delay(1000);
    Serial.print(END_TRANSMISSION);
  }
  
}


/*
 * FunÃ§Ã£o que converte os valores lidos na porta analÃ³gica 0 
 * em valores dentro da seguinte faixa:
 * De 0 atÃ© a tensÃ£o mÃ¡xima da fonte de alimentaÃ§Ã£o do circuito RC (e.g. 5V)
 */
float convertIntoVolts( float valor ){
  return (valor*4.95)/1023;
}


/*
 * FunÃ§Ã£o utilizada na interrupÃ§Ã£o interna para contabilizar o tempo transcorrido a partir do inÃ­cio do experimento
 */
void measurement() {
  time_ += 1;
}


/*
 * FunÃ§Ã£o que retÃ©m o fluxo do programa atÃ© que algum sinal seja recebido do sistema de monitoramento executado no raspberry pi
 */
char waitForRequest(char code){
  char _signal = ' ';
  while( _signal != code ){
    if( Serial.available() > 0 ){
      _signal = Serial.read();
    }
  }
  return _signal;
}



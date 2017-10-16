
#include <MsTimer2.h>

struct Data_experiment{
  int second;
  char separator = ';';
  float volt;
};

const char END_TRANSMISSION = '0';
const char START_EXPERIMENT = '1';
const char DURATION_EXPERIMENT = '2'; 
const float RESISTOR = 5e3;
const float CAPACITOR = 3300e-6;
const long TAU = 5*(RESISTOR*CAPACITOR);
const unsigned int RESET_PIN = 3;
Data_experiment seconds_and_volts[5];
int index = 0;
volatile  int time_ = 0;
int previous_time = 0;
float volt = 0.0;
char signal_code = ' ';

/*
 * Configura o intervalo de tempo em que os dados serão enviados
 * e ativa o reset para empedir que a corrente chegue até o 
 * capacitor antes do usuário iniciar o experimento.
 */
void setup() {
  pinMode( RESET_PIN, OUTPUT );
  Serial.begin( 14400 );
  MsTimer2::set( 1000, measurement_time );
  digitalWrite( RESET_PIN, HIGH );
}

void loop() {
  /*
   * estrutura de decisão que compara o signal_code com o codigo
   * para iniciar o experimento. caso sejam diferentes a função
   * waitForRequest aguarda o SGE enviar o codigo e. Quando o 
   * código é DURANTION_EXPERIMENT, envia o tempo de duração.
   * Quando o código é START_EXPERIMENT, desliga o dreno e
   * habilita a interrupção
   */
   if(signal_code != START_EXPERIMENT){
    waitForRequest(DURATION_EXPERIMENT);
    Serial.print(TAU);
    waitForRequest(START_EXPERIMENT);
    digitalWrite( RESET_PIN, LOW );
    MsTimer2::start();    
  }
  /*
   * volt recebe o valor percebido com o polling feito na
   * porta A0 e esse valor é convertido para a faixa de
   * tensão pretendida
   */
  volt = analogRead( 0 );
  volt = convertIntoVolts( volt );  
  /*
   * estrutura de decisão que compara o tempo anterior com
   * o tempo do experimento. caso tempo anterior seja menor
   * os dados em time_ e volt são enviados para o SGE
   * e previous_time recebe o valor de time_
   */
  if(previous_time < time_){
    seconds_and_volts[index].second = time_;
    seconds_and_volts[index].volt = volt;
    if(index < 4){
      index += 1; 
    }else{
      for(int i = 0; i <= index; i++){
        Serial.print(seconds_and_volts[i].second);
        Serial.print(seconds_and_volts[i].separator);
        Serial.print(seconds_and_volts[i].volt);
        Serial.print('|');
      }
      index = 0;
    }
    previous_time = time_;
  } 
  /*
   * estrutura de decisão que compara o tempo do experimento
   * com o tempo de duração estimado. caso sejam iguais as
   * variaveis time_ e signal_code recebem os valores iniciais
   * o aberto é aberto e o sinal de encerramento é enviado p/
   * o SMCD
   */
  if(time_ == TAU){
    if(index != 0){
      for(int i = 0; i < index; i++){
        Serial.print(seconds_and_volts[i].second);
        Serial.print(seconds_and_volts[i].separator);
        Serial.print(seconds_and_volts[i].volt);
        Serial.print('|');
      }
    }
    MsTimer2::stop();
    time_ = 0;
    signal_code = ' ';
    digitalWrite( RESET_PIN, HIGH );
    //delay(500);
    Serial.print(END_TRANSMISSION);
  }
  
}
  /*
   * Sub-rotina que converte o valor lido na porta A0 em 
   * outro valor dentro da faixa de 0 a 5
   */
float convertIntoVolts( float valor ){
  return (valor*5.0)/1023;
}
  /*
   * Rotina de interrupção que realiza a contagem do tempo
   * de execução do experimento
   */
void measurement_time() {
  time_ += 1;
}
  /*
   * sub-rotina que recebe o código de sinal e verifica
   * se ele está de acordo com o esperado
   */
void waitForRequest(char code){
  while( signal_code != code ){
    if( Serial.available() > 0 ){
      signal_code = Serial.read();
    }
  }
}

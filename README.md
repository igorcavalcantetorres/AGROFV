# Projeto Agrofotovoltaico uma interação entre energia solar fotovoltaica e cana-de-açúcar

O sistema agrofotovoltaico localiza-se na zona rural do município de Rio Largo/AL, com coordenadas: 9°27'52"S 35°49'41"W, elevação de 130,2m, com clima subúmido, em uma área de plantio de cana-de-açúcar, de propriedade da usina Santa Clotilde.
Coordenado pelo Campus de Engenharias e Ciências Agrárias (CECA), da Universidade Federal de Alagoas (UFAL), em parceria com a Fundação do Amparo à Pesquisa do Estado de Alagoas (FAPEAL), o sistema experimental agrofovoltaico é composto de 210 módulos fotovoltaicos policristalinos, de 335W, modelo 335P6K-36, da fabricante BYD, divididos em 14 conjuntos de módulos (conhecido como string), com cada string possuindo 15 módulos fotovoltaicos, eletricamente ligados em série. 
Os módulos fotovoltaicos foram apoiados em 7 estruturas metálicas de ferro fundido, cada uma com 7 metros de altura, inclinadas a 15°, orientadas à noroeste, com cada uma realizando o apoio mecânico de duas strings, conforme mostrado na Figura 1.

![image](https://github.com/user-attachments/assets/a99c8cdc-f49e-4580-8dbb-7ab69efe0b7b)

O Sistema possui potência de total de geração de 70,35 kWp (kilowatt-pico), com potência nominal de 70 kW (kilowatt), divididos em 2 dois inversores da marca Sungrow, sendo um de 30 kW e outro de 40 kW alocados num cubículo central em alvenaria, conectados à rede de distribuição em média tensão 13,8 kV (Quilovolts), através de uma subestação área de 75 kVa (quilovolt ampère), como mostrado na Figura 2.

![image](https://github.com/user-attachments/assets/2a17b3b8-baee-4e39-88c2-0a2fa0f9f975)

O encaminhamento do circuito em corrente contínua (CC), foi realizado através de eletrodutos Polietileno de Alta Densidade (PEAD) enterrados, com cada estrutura possuindo uma caixa de passagem de concreto. 
O sistema de proteção CC foi composto por dispositivos de proteção contra surtos (DPS), instalados junto a cada estrutura metálica e interligados à malha de aterramento principal, além da proteção interna dos inversores.

Os sistemas agrofotovoltaicos são construídos para serem adaptados a cultura agrícola a qual fazem parte, sendo seu desenvolvimento pensado em atender às necessidades das demandas de engenharia agrícola envolvida.

# Descrição da atividade experimental

Os dados foram coletados ao longo do período de 1 ano, entre setembro de 2022 a setembro de 2023, com a coleta dos dados sendo realizada ao começo de cada mês. As grandezas meteorológicas estudadas foram coletadas minuto a minuto, ao longo de 12 horas, durante o período das 6:00 horas às 18:00 horas. 
Após a coleta de dados, foi feita a importação dos dados e seu tratamento, levando em consideração fatores que poderiam influenciar na qualidade dos dados analisados, como:  problemas físico-químicos e oscilações e desligamentos da rede de distribuição elétrica. 
O mês de maio de 2023 foi o mês mais crítico, ficando 25 dias sem geração, por este motivo foi o mês escolhido para emprego dos modelos matemáticos. 
Os constantes desligamento e oscilações da rede de distribuição, levaram a perdas na geração de energia, estas perdas comprometeram os resultados do experimento, sendo um grande agravante para a determinação da real performance ratio (PR) do sistema fotovoltaico, uma vez que com o desligamento da rede, ou ao menos sua oscilação, houveram perdas dos dados cruciais para o entendimento dos aspectos de funcionamento da usina solar agrofotovoltaica. 
As informações foram organizadas em colunas, onde cada uma representa uma grandeza analisada. Após o tratamento inicial, realizou-se o diagnóstico e descarte dos dados inconsistentes, uma etapa crucial para assegurar a qualidade dos resultados obtidos. Este processo de triagem foi fundamental, pois permitiu eliminar inconsistências e preservar a integridade dos dados utilizados na análise.

Os instrumentos utilizados no experimento foram devidamente calibrados para garantir a alta confiabilidade dos dados coletados, assim como foram tomadas as devidas precauções, para atenuar erros de medições. 
Os instrumentos meteorológicos utilizados tiveram como finalidade o levantamento das seguintes grandezas: temperatura do ar (°C) e irradiância solar (W/m²) no plano inclinado. Na ligação após os inversores foi instalado um analisador de energia para estimar as grandezas elétricas geradas após conversão (CC/CA) conforme mostrado no fluxograma na Figura 3 a seguir.

![image](https://github.com/user-attachments/assets/077950a3-a911-4f7c-913f-f46ac71cce75).

# Piranômetro termopilha

O modelo instalado foi o B&W da fabricante EPPLEY, sendo um equipamento robusto capaz de realizar medições de irradiância global. Sua faixa espectral é de 295-2800 nm, saída 0-10 mV, analógico e sensibilidade aproximada de 8 μV / 〖Wm〗^(-2)
O piranômetro utilizado no experimento foi instalado junto às estruturas das strings 1 e 2, no mesmo plano de geração dos módulos fotovoltaicos, a 15° noroeste, realizando a aquisição de dados de irradiância solar (W/m²). 

# Sensor de temperatura do ar - HMP45C

O sensor foi devidamente instalado em área sombreada, inferior aos módulos fotovoltaico, como mostrado na Figura 10, fixado e calibrado para a realização da coleta de dados da temperatura do ar (°C).

# Datalogger

O data logger CR10X possui um programa módulo de função e controle, com um sensor de cronometragem interno, memória de 62 kB, 12 portas lógicas e resolução analógica de 0,33 μV. Integrado à um sistema carregamento autônomo, composto por uma bateria chumbo-ácido de 12 V, ligada a um pequeno módulo fotovoltaico. O data logger foi fixado à estrutura do agrofotovoltaico.

# Analisador de energia elétrica

O analisador de energia foi utilizado para obter os dados da geração solar fotovoltaica, sendo instalado junto ao quadro de distribuição da usina, com a principal informação fornecida sendo a quantidade de energia elétrica produzida (kWh). 
Composto por quatro garras, três para referência de tensão de cada fase e uma para o neutro, 4 bobinas flexíveis de referência, três para fases e uma para o neutro. O analisador DMI P1000R possui acurácia de 99% em seus componentes, sendo um instrumento de referência e alta confiabilidade (“ISSO - Análise e telemetria - Informações do Produto”, 2017).

# How to Cite - Como citar este repositório em trabalhos
Se você estiver desenvolvendo um trabalho científico, e utilizar dados e informações disponibilizados neste repositório, use a referência logo abaixo:

Torres, I.;Ferreira Junior, R. A.;Santos, M. A.;Souza, L. F. L.;Cavalcante, Márcio André Araújo. TÍTULO DO ARTIGO (INSERIR). (PERIÓDICO), (ANO), (VOLUME), (PÁGINAS), (DOI).

@article{Torres_2025,
  title={TÍTULO DO ARTIGO (INSERIR)},
  author={Torres, I. and Ferreira Junior, R. A. and Santos, M. A. and Souza, L. F. L. and Cavalcante, Márcio André Araújo},
  journal={},
  volume={},
  pages={3582-3593},
  year={2025},
  doi = {},
  publisher={IEEE},
}




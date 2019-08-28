### **Trabalho de métodos computacionais** - Felipe Nunes

    As instruções abaixo estão dividas nos módulos e para cada método do respectivo módulo, dá-se 
    o exemplo de entrada em JSON em seguida da explicação dos parâmetros utilizados no mesmo.

    As funções utilizadas pela API estão igualmente documentadas.
    Funções auxiliares estão dispostas no arquivo lib.py
    
    
## Roots

#### Bisection
    POST
    /roots/bisection
    
    {
        "funcao":"(x**3) + 5*x + 2",
        "a":"-100",
        "b":"50",
        "E":"0.00001"
    }
    
    "funcao" => Descrição da função com a utilização de parêntesis para determinar precedência.
    Devido a não utilização de algum tipo de Parser, não há suporte para funções trigonométricas
    ou logarítmicas, por exemplo.
    "a" => Intervalo numero 1
    "b" => Intervalo numero 2 
    "E" => Margem de erro, sem utilização da vírgula, substituindo-a por ponto.
    

    
#### False Position
    POST
    /roots/falseposition
    
    {
        "funcao":"(x**3) + 5*x + 2",
        "a":"-100",
        "b":"50",
        "E":"0.00001"
    }
    
    "funcao" => Descrição da função com a utilização de parêntesis para determinar precedência.
    Devido a não utilização de algum tipo de Parser, não há suporte para funções trigonométricas
    ou logarítmicas, por exemplo.
    "a" => Intervalo numero 1
    "b" => Intervalo numero 2
    "E" => Margem de erro, sem utilização da vírgula, substituindo-a por ponto.
       
#### Newton Raphson
    POST
    /roots/newtonraphson
    
    {
        "funcao":"(x**3) + 5*x + 2",
        "chute":"45",
        "E":"0.00001"
    }
    
    "funcao" => Descrição da função com a utilização de parêntesis para determinar precedência.
    Devido a não utilização de algum tipo de Parser, não há suporte para funções trigonométricas
    ou logarítmicas, por exemplo.
    "chute" => Chute inicial
    "E" => Margem de erro, sem utilização da vírgula, substituindo-a por ponto.  
    
#### Secant
    POST
    /roots/secant
    
    {
        "funcao":"(x**1) + 5**2 + 2",
        "xnmenos":"-115",
        "xn":"10",
        "E":"0.00001"
    }
    
    "funcao" => Descrição da função com a utilização de parêntesis para determinar precedência.
    Devido a não utilização de algum tipo de Parser, não há suporte para funções trigonométricas
    ou logarítmicas, por exemplo.
    "xnmenos" => Primeiro ponto por onde passará a reta secante
    "xn" => Segundo ponto por onde passará a reta secante
    "E" => Margem de erro, sem utilização da vírgula, substituindo-a por ponto. 

## Coefficients

#### Pearson, Kendall e Spearman.
    POST
    /coefficients/pearson
    /coefficients/kendall
    /coefficients/spearman
    
    {
    "dado1":"[86, 99, 99, 100, 100, 100, 110, 112, 113]",
    "dado2":"[0, 20, 28, 28, 50, 29, 7, 7, 6, 0]"
    }
    
    ps.: As listas devem ter o mesmo numero de dados, e podem ter numeros repetidos.
    "dado1" => Lista contendo os valores da primeira métrica. 
    "dado2" => Lista contendo os valores da segunda métrica. 

## Confidence Interval

#### With Standard Deviation
    POST
    /confidenceinterval/stddev        

    {
    "total":"500",
    "confianca":"95",
    "desvio":"5",
    "media":"100"
    }
    
    "total" => Numero total da amostra.
    "confianca" => Nivel de confiança exigido.
    "desvio" => Desvio Padrão da amostra.
    "media" => Média aritimética da amostra.
    
#### Without Standard Deviation
    POST
    /confidenceinterval/withoutstddev 
    
    {
    "dados":"[9, 8, 12, 7, 9, 6, 11, 6, 10, 9]",
    "porcentagem":"95"
    }     
    
    "dados" => Lista contendo a amostra.
    "confianca" => Nivel de confiança exigido.
    
#### Population Ratio
    POST
    /confidenceinterval/popratio
    
    {
    "sucessos":"160",
    "total":"200",
    "confianca":"160"
    }
    
    "sucessos": => Total de sucessos entre os casos da amostra.
    "total": => Total de casos da amostra.
    "confianca" => Nivel de confiança exigido.
     
## Resampling
    
#### Bootstrap
    POST
    /resampling/bootstrap
    
    {
    "dados":"[2.2, 2.5, 3.4, 6.7, 6.2, 8.2, 9.2, 10.1]",
    "repeticoes":"10"
    }
    
    "dados" => Lista contendo os dados da amostra.
    "repeticoes" => Numero de repetições exigidas.
    
#### JackKnife Average
    POST
    /resampling/jackknife/average
    
    {
    "dados":"[2.2, 2.5, 3.4, 6.7, 6.2, 8.2, 9.2, 10.1]"
    }
    
    "dados" => Lista contendo os dados da amostra.

#### JackKnife Variance
    POST
    /resampling/jackknife/variance
    
    {
    "dados":"[2.2, 2.5, 3.4, 6.7, 6.2, 8.2, 9.2, 10.1]"
    }
    
    "dados" => Lista contendo os dados da amostra.

#### JackKnife Standard Deviation
    POST
    /resampling/jackknife/variance
    
    {
    "dados":"[2.2, 2.5, 3.4, 6.7, 6.2, 8.2, 9.2, 10.1]"
    }
    
    "dados" => Lista contendo os dados da amostra.
                
#### JackKnife Confidence Interval
    POST
    /resampling/jackknife/confidenceinterval
    
    {
    "dados":"[2.2, 2.5, 3.4, 6.7, 6.2, 8.2, 9.2, 10.1]",
    "confianca":"95"
    }
    
    "dados" => Lista contendo os dados da amostra. 
    "confianca" => Nivel de confiança exigido.
    
## Regressions

#### Linear
    POST
    /regressions/linear
    
    {
    "dados1":"[122, 114, 86, 134, 146, 107, 68, 117, 71, 98]",
    "dados2":"[139, 126, 90, 144, 163, 136, 61, 62, 41, 120]"
    }         
    
    "dados1" => Lista contendo os valores da primeira entidade.                              
    "dados2" => Lista contendo os valores da segunda entidade.                              

#AULA 1 e 2
#Expressions
123*321
42**2
34-2*6
4 + 2 == 42
1 + sum(2,3)

#Sequences
seq(1,20)
seq(1, 20, by = 2)
seq(1, 20, length.out = 15)
seq(1, by = 0.4, length.out = 20)
seq(1, by = 0, length.out = 100) #or 
seq(1,1,length.out = 100)

#Vectors
a = c("L", 3, 3, T)
b = c(F, 4, 1, 7)
a
b

#a
names = c("Andre","Carolina","John","Pedro","Zé","Vânia")
grades = c(10,12,NaN,15,15,7)
names 
grades

#b
length(names) == length(grades)

#c
names[5]
grades[5]

#d
grades[3] = 13
grades

#Matrices
grades = sample(8:20, 20, replace=TRUE)
grades
#1
matrix_grades = matrix(grades,nrow=4,ncol=5)
matrix_grades
dim(matrix_grades)
#2
names = c("Andre","Carolina","John","Pedro")
grades = c("Exam1","Exam2","Exam3","Exam4","Exam5")
colnames(matrix_grades) = grades
rownames(matrix_grades) = names
matrix_grades
#3
matrix_grades[1,2]
matrix_grades["Andre","Exam2"]
matrix_grades[1,"Exam2"]
matrix_grades[1,]
matrix_grades["Andre",] 
matrix_grades[,"Exam2"]
matrix_grades[1:3,1:4]
#4
matrix_grades+1 #all grades increased by 1 value
matrix_grades*2 #all grades doubled
matrix_grades*matrix_grades 
matrix_grades%*%matrix_grades #imp since matrix[4,5] cant multiples by it 
matrix_grades%*%t(matrix_grades) #now we can
det(matrix_grades) #determinant of the matrix (error since it's NOT a square matrix)
det(matrix_grades[,1:4]) #how to transform it in a square matrix (make it with 4 col)
t(matrix_grades) #transposed matrix
solve(matrix_grades) #invert of the matrix (error since it's NOT a square matrix)
solve(matrix_grades[,2:5]) #other way to transform it in a square matrix (make it with 4 col)

#Control Structures
#1
ifelse(sqrt(9)<2,sqrt(9),0) #se a primeira condição for verdade, returna o 2º elemento
ifelse(sqrt(100)>9,sqrt(100),0) #se a primeira condição for falsa, returna o 3º elemento

x=12
if(is.numeric(x)) y=x*2 #se x for numérico então y = 2x
y

z=-1
if(z<0){x=abs(z);y=z*3} #se x for menor que zero ambas as seguintes acontecem
x
y

z=6
if(z<0) y=z*3 else y=z*5 #else acontece se a primeira condição for falsa
y

x=15
y=3
if(is.numeric(x))
  if(is.numeric(y) & y!=0) #se x e y foram ambos numérico e y for ≠ de 0
    z=x/y
z

x=letters[20]
if (is.numeric(x)) print('is numeric') else
  if(is.character(x)) print('is character')

x=90
ifelse(x<100,ifelse(x/2==trunc(x/2),x/2,0), #trunc = tirar a casa decimal de um nr
       ifelse(x/100==trunc(x/100),x/100,-1))

#2
for (i in 1:15) 
  if (i != 3)
  print (i)

#Functions
#1a
a = c(1,2,NA,4)
propna = function(v)
  {result = (sum(is.na(v))/length(v)) * 100
  print (result)}
propna (a)

#1b
b=c(1,2,3,4,5)
par = function (v) 
  {return(v[v%%2==0]) 
  }
par (b)

#2
convert_temp = function(value,to = 'C') {
if (to == 'C') {
    result = (value - 32) / 1.8
} else if (to == "F") {
    result = (value * 1.8) + 32
} else {
    stop('invalid conversion type')
  }    
   return (result) }

convert_temp (35,to ='F')

----
#AULA 3
  
install.packages("openxlsx")
install.packages("tidyverse")
install.packages("ggplot2")

#Ex 1
library(openxlsx)

data = read.xlsx("penguins.xlsx")
head(data)

#Ex 2
mean(data$flipper_length_mm,na.rm=TRUE)
sd(data$flipper_length_mm,na.rm=TRUE)

#Ex 3
freq_table = table(data$island)
freq_table #nr de penguins por ilha
prop.table(freq_table) #proporção do nr de penguins por ilha

#Ex 4
cor(na.omit(data$body_mass_g),na.omit(data$flipper_length_mm)) #high positive correlation

#Ex 5 (mean body mass per species)
install.packages("palmerpenguins")
library(tidyverse)
library(palmerpenguins)
penguins %>%
  group_by(species) %>%
  summarise(mean = mean(body_mass_g, na.rm=TRUE))

#Ex 6
library(ggplot2)
ggplot(penguins) +
  geom_bar(aes(x=island))

ggplot(penguins) +
  geom_point(aes(x = body_mass_g, y = flipper_length_mm)) + #gráfico "básico"
  theme_classic() + #alterar o fundo
  geom_smooth(aes(x = body_mass_g, y = flipper_length_mm), method = "lm", se = FALSE) + #regressão linear
  labs(title = "Scatter plot: Body Mass vs Flipper Length", x = "Body Mass (g)", y = "Flipper Length (mm)") #alterar título e nomes das variáveis

----
#AULA 4 
#Discrete Distributions
#ex2
#A
dbinom(x,size,prob)
#B
pbinom(x,size,prob) #p=cumulative
#C
Poisson 
#D
ppois(x,lamda)
#E
P(X <= x)

#ex3
dpois(x, lambda, log = FALSE)
#A P (X ≤ 5)
ppois(5,7)
#B P (X < 5) = P (X ≤ 4) = 1 - P (X > 5)
ppois(4,7)
#C P (4 ≤ X ≤ 16)
ppois(16,7)-ppois(3,7)

#ex4
dbinom(x, size, prob, log = FALSE)
#B i get 20, 25 or 30 times heads
dbinom(20,60,0.5)
dbinom(25,60,0.5)
dbinom(30,60,0.5)
#B ii get less than 30 times heads
pbinom(29,60,0.5)
#B iii get between 20 and 40 times heads
pbinom(40,60,0.5)-pbinom(19,60,0.5)

#ex5
#Nr 1: 1/6 | Nr 2: 1/3 | Nr 3: 1/3 | Nr 4: 1/6
pbinom(0,2,1/6)

#ex6: Prob of within 10 trials get less than 4 observations which prob of success is 0.6

#ex7
#P(X ≤ 5)
0.3669
#P(X < 5) = P(X <= 4)
0.1662
#P(X > 4) = 1 - P(X <= 4)
1-0.1662 
#P(X = 5) = P(X ≤ 5) - P(X <= 4)
0.3669-0.1662

#Continuous Distributions
#3
pf(3,4,300,lower.tail = FALSE) #a
pf(3,4,300) #b
pf(6,4,300)-pf(3,4,300) #c
#4
pchisq(3,4,lower.tail = FALSE) #a
pchisq(3,4) #b
pchisq(6,4)-pchisq(3,4) #c

#5 -> #normal distribution (cumulative distribution function)
pnorm(2) #P(x<=2) with N(0,1)
#the prob of a normal standard dist having values below or equal to 2 is 97,72%

pnorm(2, 1, 1) #P(x<=2) with N(1,1)
#the prob of a normal dist with mean and sd = 1 having values below or equal to 2 is 84,13%

pnorm(2, 1, 2) #P(x<=2) with N(1,2)
#the prob of a normal dist with mean = 1 and sd = 2 having values below or equal to 2 is 69,15%

#6 -> #normal distribution (quantile function)
qnorm(0.975) #P(X<=x)=0,975 with N(0,1)
#for a prob of 97,5%, a normal standard dist must have x = 1,96
#1,96 is the value of x that leaves 97,5% of the dist below it

qnorm(0.975, 1, 1) #P(X<=x)=0,975 with N(1,1)
#for a prob of 97,5%, a normal dist with mean = 1 and sd = 1 must have x = 2,96
#2,96 is the value of x that leaves 97,5% of the dist below it

qnorm(0.975, 1, 2) #PP(X<=x)=0,975 with N(1,2)
#for a prob of 97,5%, a normal dist with mean = 1 and sd = 2 must have x = 4,92
#4,92 is the value of x that leaves 97,5% of the dist below it

#7
qnorm(pnorm(2)) #pnorm: the prob of a the prob of a normal standard dist having values below or equal to 2 -> 97,72%
                #qnorm: then, with for a prob of 97,5%, a normal standard dist must have x = 2


#Extra -> criar um gráfico da função de distribuição normal
library(ggplot2)

values = seq(-10, 10, by = 0.01)
df = data.frame(x=values, density = dnorm(values, mean = 0, sd = 1))
ggplot(df, aes(x = x, y = density) + geom_line(color = "blue"))




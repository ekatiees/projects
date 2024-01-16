# Install packages
install.packages("car")
library(car)
install.packages("e1071")
library(e1071)
install.packages("nortest")
library(nortest)
install.packages("EnvStats")
library(EnvStats)
install.packages("twosamples")
library(twosamples)
install.packages("agricolae")
library(agricolae)
install.packages("lmtest")
library(lmtest)
install.packages("corrplot")
library(corrplot)
install.packages("MLmetrics")
library(MLmetrics)
install.packages("gap")
library(gap)
install.packages("leaps")
library(leaps)

# Load the dataset
install.packages("readr")
library(readr)
startups <- read_csv("Startups.csv")
View(startups)

names(startups) <- c("rnd", "administration", "marketing", "state", "profit")



# Descriptive Statistics -------------------------------------------------------
desc_stats <- function(variable) {
    print(summary(variable))
    cat("\nRange: ", max(variable)-min(variable),
    "\nIQR: ", IQR(variable),
    "\nStd: ", sd(variable),
    "\nCV: ", sd(variable)/mean(variable),
    "\nSkewness: ", skewness(variable),
    "\nKurtosis: ", kurtosis(variable))
}


# R&D expenses
desc_stats(startups$rnd)
## plots
hist(startups$rnd)
boxplot(startups$rnd)
qqPlot(startups$rnd)


# administration expenses
desc_stats(startups$administration)
## plots
hist(Startups$Administration)
boxplot(Startups$Administration)
qqPlot(Startups$Administration)


# marketing expenses
desc_stats(startups$marketing)
## plots
hist(Startups$Marketing.Spend)
boxplot(Startups$Marketing.Spend)
qqPlot(Startups$Marketing.Spend)


# profit
desc_stats(startups$profit)
## plots
hist(Startups$Profit)
boxplot(Startups$Profit)
qqPlot(Startups$Profit)





# Outliers ---------------------------------------------------------------------
iqr_rule <- function(variable) {
  subset(variable,
         variable > quantile(variable, 0.25)-1.5*IQR(variable) &
         variable < quantile(variable, 0.75)+1.5*IQR(variable))
}

z_score <- function(variable) {
  z1 <- (variable-mean(variable))/sd(variable)
  subset(z1, z1 > -3 & z1 < 3)
}

# R&D w/o outliers
rnd_wo_outliers_iqr <- iqr_rule(startups$rnd)
rnd_wo_outliers_z <- z_score(startups$rnd)
## check
cat("initial = ", length(startups$rnd),
    "\niqr_rule = ", length(rnd_wo_outliers_iqr),
    "\nz_score = ", length(rnd_wo_outliers_z))

# administration w/o outliers
adm_wo_outliers_iqr <- iqr_rule(startups$administration)
adm_wo_outliers_z <- z_score(startups$administration)
## check
cat("initial = ", length(startups$administration),
    "\niqr_rule = ", length(adm_wo_outliers_iqr),
    "\nz_score = ", length(adm_wo_outliers_z))

# marketing w/o outliers
mark_wo_outliers_iqr <- iqr_rule(startups$marketing)
mark_wo_outliers_z <- z_score(startups$marketing)
## check
cat("initial = ", length(startups$marketing),
    "\niqr_rule = ", length(mark_wo_outliers_iqr),
    "\nz_score = ", length(mark_wo_outliers_z))

# profit w/o outliers
profit_wo_outliers_iqr <- iqr_rule(startups$profit)
profit_wo_outliers_z <- z_score(startups$profit)
## check
cat("initial = ", length(startups$profit),
    "\niqr_rule = ", length(profit_wo_outliers_iqr),
    "\nz_score = ", length(profit_wo_outliers_z))





# Parameters estimation, confidence intervals ----------------------------------
# Check for normality
pearson.test(startups$rnd) # no
shapiro.test(startups$rnd) # no

pearson.test(startups$administration) # no
shapiro.test(startups$administration) # no

pearson.test(startups$marketing) # no
shapiro.test(startups$marketing) # no

pearson.test(startups$profit) # no
shapiro.test(startups$profit) # no


# Interval estimates
t.test(startups$rnd)
varTest(startups$rnd)

t.test(startups$administration)
varTest(startups$administration)

t.test(startups$marketing)
varTest(startups$marketing)

t.test(startups$profit)
varTest(startups$profit)


unique(startups$state)

nrow(subset(startups, startups$state == "California"))
prop.test(17, 50, correct = FALSE, conf.level = 0.95)
nrow(subset(startups, startups$state == "Florida"))
prop.test(16, 50, correct = FALSE, conf.level = 0.95)
nrow(subset(startups, startups$state == "New York"))
prop.test(17, 50, correct = FALSE, conf.level = 0.95)





# Hypothesis testing (significance lvl = 0.05) ---------------------------------

# Parametric statistical tests
# On average, a startup's profit is $112013 
t.test(startups$profit, mu = 112013, conf.level = 0.95) # accept H0

# The variance of profit against the average value is equal to 1624588173
varTest(startups$profit, sigma.squared = 1624588173, conf.level = 0.95)

# The average value of administration costs is equal to (or less than) the average value of marketing costs
t.test(startups$administration, startups$marketing, mu = 0, paired = TRUE, var.equal = TRUE, alternative = "less") # reject H0

# Average R&D costs equal to (or less than) average administration costs
t.test(startups$rnd, startups$administration, mu = 0, paired = TRUE, var.equal = TRUE, alternative = "less") # reject H0

# The shares of successful startups with profits > 100k are not equal in California and New York
California <- subset(startups, startups$state == "California")
NewYork <- subset(startups, startups$state == "New York")

nrow(subset(NewYork, NewYork$profit >= 100000))
nrow(subset(California, California$profit >= 100000))

prop.test(c(nrow(subset(NewYork, NewYork$profit >= 100000)),nrow(subset(California, California$profit >= 100000))), c(17,17), conf.level = 0.95, alternative = "two.sided")
# reject H0



# Nonparametric statistical tests
# Homogeneity criteria
ks.test(startups$administration, startups$marketing)
cvm_test(startups$administration, startups$marketing)

ks.test(startups$administration, startups$rnd)
cvm_test(startups$administration, startups$rnd)

ks.test(startups$rnd, startups$marketing)
cvm_test(startups$rnd, startups$marketing)

# Kraskell-Wallis criterion
kruskal.test(startups$profit, startups$state)
kruskal.test(startups$rnd, startups$state)
kruskal.test(startups$administration, startups$state)
kruskal.test(startups$marketing, startups$state)

# Mood criterion
Median.test(startups$profit, startups$state, alpha = 0.05, correct = TRUE)
Median.test(startups$rnd, startups$state, alpha = 0.05, correct = TRUE)
Median.test(startups$administration, startups$state, alpha = 0.05, correct = TRUE)
Median.test(startups$marketing, startups$state, alpha = 0.05, correct = TRUE)

# Analysis of variance --------------------------------------------------------- 
summary(aov(profit ~ state, data = startups))
shapiro.test(aov(profit ~ state, data = startups)$residuals)
t.test(aov(profit ~ state, data = startups)$residuals, mu=0)

dwtest(aov(profit ~ state, data = startups)$residuals, alternative = "two.sided")

bartlett.test(startups$profit, startups$state)





# Regression analysis (significance level 0.01) --------------------------------
# Dependency analysis
df <- startups[,-4]
cor(df, method = "pearson")
plot(df)

corrplot.mixed(cor(df, method = "pearson"), lower="circle", upper="number", tl.pos = "lt", diag="u")

# Paired model
model_1 <- lm(profit ~ rnd, data = df)
summary(model_1)

# --- Residuals check
# ------- Residuals are normally distributed
          pearson.test(model_1$residuals)
# ------- Expected value is zero
          t.test(model_1$residuals, mu=0)
# ------- Variance are equal (homoscedasticity)
          bptest(model_1, studentize = FALSE)
# ------- No autocorrelation
          #H0: first lvl autocorrelation coefficient is zero
          dwtest(model_1, alternative = "two.sided")
# --- Check the quality of the model
# ------- Average approximation error (5-7% good, up to 10% normal)
          MAPE(model_1$fitted.values, df$profit)*100


# Multiple model
summary(regsubsets(profit ~., data = df, nvmax = 3))
summary(regsubsets(profit ~., data = df, nvmax = 3))$adjr2

model_2 <- lm(profit ~ rnd+marketing, data = df)
summary(model_2) 

# --- Residuals check
# ------- Residuals are normally distributed
          pearson.test(model_2$residuals)
# ------- Expected value is zero
          t.test(model_2$residuals, mu=0)
# ------- Variance are equal (homoscedasticity)
          bptest(model_2, studentize = FALSE)
# ------- No autocorrelation
          #H0: first lvl autocorrelation coefficient is zero
          dwtest(model_2, alternative = "two.sided")
# --- Check the quality of the model
# ------- Average approximation error (5-7% good, up to 10% normal)
          MAPE(model_2$fitted.values, df$profit)*100
# ------- Statistical significance of pairwise linear regression
          vif(model_2)

predict(model_2, newdata = data.frame(rnd = 21000, marketing = 9500), interval = "prediction", level = 0.95)


# Multiple model considering qualitative variables
model_3 <- lm(profit ~ rnd+state, data = startups)
summary(model_3)

# --- Residuals check
# ------- Residuals are normally distributed
          pearson.test(model_3$residuals)
# ------- Expected value is zero
          t.test(model_3$residuals, mu=0)
# ------- Variance are equal (homoscedasticity)
          bptest(model_3, studentize = FALSE)
# ------- No autocorrelation
          #H0: first lvl autocorrelation coefficient is zero
          dwtest(model_3, alternative = "two.sided")
# --- Check the quality of the model
# ------- Average approximation error (5-7% good, up to 10% normal)
          MAPE(model_3$fitted.values, df$profit)*100
# ------- Statistical significance of pairwise linear regression
          vif(model_3)

b00 <- coef(model_3)[1]
b01 <- coef(model_3)[1]+coef(model_3)[3]
b02 <- coef(model_3)[1]+coef(model_3)[4]
b1 <- coef(model_3)[2]

plot(startups$rnd, startups$profit, col=as.numeric(as.factor(startups$state)))
abline(b00, b1, col=1)
abline(b01, b1, col=2)
abline(b02, b1, col=3)

s1 <- subset(startups, startups$state == "California")
s2 <- subset(startups, startups$state == "Florida")
s3 <- subset(startups, startups$state == "New York")

r1 <- lm(profit ~ rnd, data = s1)
r2 <- lm(profit ~ rnd, data = s2)
r3 <- lm(profit ~ rnd, data = s3)

plot(startups$rnd, startups$profit, col=as.numeric(as.factor(startups$state)))
abline(r1, col=1)
abline(r2, col=2)
abline(r3, col=3)

# Checking the significance of differences in the models
chow.test(s1$profit, s1$rnd, s2$profit, s2$rnd)
chow.test(s2$profit, s2$rnd, s3$profit, s3$rnd)
chow.test(s1$profit, s1$rnd, s3$profit, s3$rnd)

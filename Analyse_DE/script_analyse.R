library(kissDE)
setwd("~/ProjetS3/pipeline/Analyse_DE")

###### CONDITION R vs U
#table comptages bruts
myCounts=read.csv("~/ProjetS3/pipeline/COMP/Input_KissDE.csv", header=T, sep="\t")
head(myCounts)
myCountsR_U=subset(myCounts, select=c("Junction", "Lenght", "R2", "R3", "R4", "R5", "U2", "U3", "U4", "U5"))
#conditions et replicats
myConditionsR_U <- c(rep("condition_R", 4), rep("condition_U", 4))
myConditionsR_U
qualiteR_U=qualityControl(myCountsR_U, myConditionsR_U)
#test DE
resultsR_U <- diffExpressedVariants (myCountsR_U, myConditionsR_U, pvalue=1)
names(resultsR_U)
head(resultsR_U, n=3)
#exploitation des resulats
hist(resultsR_U$uncorrectedPVal, main = "Histogram of p-values",xlab = "p-values", breaks = 40)
hist(resultsR_U$correctedPVal, main = "Histogram of p-values",xlab = "p-values", breaks = 40)

table_finaleR_U=data.frame(resultsR_U$finalTable)
head(table_finaleR_U)
names(table_finaleR_U)

hist(table_finaleR_U$Adjusted_pvalue, main = "Histogram of p-values",xlab = "p-values", breaks = 40)
table(table_finaleR_U$Adjusted_pvalue < 0.05, useNA="always") #2 variants DE à 5%

#resSig=na.omit(pval_tabR_U)
#resSig=resSig[pval_tabR_U<0.05,]
#resSig=resSig[order(resSig$resultsR_U.correctedPVal),]
#nrow(resSig)


# CONDITION R vs C
#table comptages bruts
myCounts=read.csv("~/ProjetS3/pipeline/COMP/Input_KissDE.csv", header=T, sep="\t")
head(myCounts)
myCountsR_C=subset(myCounts, select=c("Junction", "Lenght", "R2", "R3", "R4", "R5", "C2", "C3", "C4", "C5"))
#conditions et replicats
myConditionsR_C <- c(rep("condition_R", 4), rep("condition_C", 4))
myConditionsR_C
qualiteR_C=qualityControl(myCountsR_C, myConditionsR_C)
#test DE
resultsR_C <- diffExpressedVariants (myCountsR_C, myConditionsR_C, pvalue=1)
names(resultsR_C)
head(resultsR_C, n=3)
#exploitation des resulats
hist(resultsR_C$uncorrectedPVal, main = "Histogram of p-values",xlab = "p-values", breaks = 40)
hist(resultsR_C$correctedPVal, main = "Histogram of p-values",xlab = "p-values", breaks = 40)

table_finaleR_C=data.frame(resultsR_C$finalTable)
head(table_finaleR_C)
names(table_finaleR_C)

hist(table_finaleR_C$Adjusted_pvalue, main = "Histogram of p-values",xlab = "p-values", breaks = 40)
table(table_finaleR_C$Adjusted_pvalue < 0.05, useNA="always") #7 variants DE à 5%


# CONDITION U vs C
#table comptages bruts
myCounts=read.csv("~/ProjetS3/pipeline/COMP/Input_KissDE.csv", header=T, sep="\t")
head(myCounts)
myCountsU_C=subset(myCounts, select=c("Junction", "Lenght", "U2", "U3", "U4", "U5", "C2", "C3", "C4", "C5"))
#conditions et replicats
myConditionsU_C <- c(rep("condition_U", 4), rep("condition_C", 4))
myConditionsU_C
qualiteU_C=qualityControl(myCountsU_C, myConditionsU_C)
#test DE
resultsU_C <- diffExpressedVariants (myCountsU_C, myConditionsU_C, pvalue=1)
names(resultsU_C)
head(resultsU_C, n=3)
#exploitation des resulats
hist(resultsU_C$uncorrectedPVal, main = "Histogram of p-values",xlab = "p-values", breaks = 40)
hist(resultsU_C$correctedPVal, main = "Histogram of p-values",xlab = "p-values", breaks = 40)

table_finaleU_C=data.frame(resultsU_C$finalTable)
head(table_finaleU_C)
names(table_finaleU_C)

hist(table_finaleU_C$Adjusted_pvalue, main = "Histogram of p-values",xlab = "p-values", breaks = 40)
table(table_finaleU_C$Adjusted_pvalue < 0.05, useNA="always") #3 variants DE à 5%





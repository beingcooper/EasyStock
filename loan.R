
z<-read.csv("hello7.csv", header=TRUE)
ind<-sample(nrow(z),nrow(z)*0.8)
z$OST_CDE_PERF_STAT<-as.factor(z$OST_CDE_PERF_STAT)

z$OST_CDE_REPR_FREQ<-as.factor(z$OST_CDE_REPR_FREQ)

z$OST_NUM_BILL_DAYS<-as.factor(z$OST_NUM_BILL_DAYS)

z$FAC_PCT_PNLTY_SPRD <- as.factor(z$FAC_PCT_PNLTY_SPRD)

z$FAC_NUM_MAX_CUR_OT <-as.factor(z$FAC_NUM_MAX_CUR_OT)

#z$OST_AMT_ORIGINAL<-as.factor(z$OST_AMT_ORIGINAL)
train_data<-z[ind,]
test_data<-z[-ind,!colnames(z) %in% c("OST_CDE_PERF_STAT")]
test_res<-z[-ind,colnames(z) %in% c("OST_CDE_PERF_STAT")]


#fit <- ctree(OST_CDE_PERF_STAT~., data=train_data)
fit<-randomForest(OST_CDE_PERF_STAT~., data=train_data)
x<-predict(fit,test_data)
print(importance(fit,2))
print(fit)

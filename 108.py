import random
import plotly.express as px
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go

count=[]

diceresult = []
for i in range(0,100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    diceresult.append(dice1+dice2)
    count.append(i)

mean=statistics.mean(diceresult)
standarddeviation=statistics.stdev(diceresult)
print ('mean',statistics.mean(diceresult))    
print ('median',statistics.median(diceresult))
print ('mode',statistics.mode(diceresult))
print ('standarddeviation',statistics.stdev(diceresult))

firststandarddeviationstart,firststandarddeviationend=mean-standarddeviation,mean+standarddeviation
secondstandarddeviationstart,secondstandarddeviationend=mean-(2*standarddeviation),mean+(2*standarddeviation)
thirdstandarddeviationstart,thirdstandarddeviationend=mean-(3*standarddeviation),(3*mean+standarddeviation)

listofdatawithinfirststandarddeviation=[result for result in diceresult if result>firststandarddeviationstart and result<firststandarddeviationend]
listofdatawithinsecondstandarddeviation=[result for result in diceresult if result>secondstandarddeviationstart and result<secondstandarddeviationend]
listofdatawithinthirdstandarddeviation=[result for result in diceresult if result>thirdstandarddeviationstart and result<thirdstandarddeviationend]
print('{}% of data lies within first standard deviation',format(len(listofdatawithinfirststandarddeviation)*100.0/len(diceresult)))
print('{}% of data lies within second standard deviation',format(len(listofdatawithinsecondstandarddeviation)*100.0/len(diceresult)))
print('{}% of data lies within third standard deviation',format(len(listofdatawithinthirdstandarddeviation)*100.0/len(diceresult)))

#fig=px.bar(x=diceresult,y=count,orientation='v')
fig=ff.create_distplot([diceresult],['Result'],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name='mean'))
fig.add_trace(go.Scatter(x=[firststandarddeviationstart,firststandarddeviationstart],y=[0,0.17],mode='lines',name='std1'))
fig.add_trace(go.Scatter(x=[firststandarddeviationend,firststandarddeviationend],y=[0,0.17],mode='lines',name='std1'))
fig.add_trace(go.Scatter(x=[secondstandarddeviationstart,secondstandarddeviationstart],y=[0,0.17],mode='lines',name='std2'))
fig.add_trace(go.Scatter(x=[secondstandarddeviationend,secondstandarddeviationend],y=[0,0.17],mode='lines',name='std2'))
fig.add_trace(go.Scatter(x=[thirdstandarddeviationstart,thirdstandarddeviationstart],y=[0,0.17],mode='lines',name='std3'))
fig.add_trace(go.Scatter(x=[thirdstandarddeviationend,thirdstandarddeviationend],y=[0,0.17],mode='lines',name='std3'))
fig.show()
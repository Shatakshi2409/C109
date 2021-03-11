import random
import plotly.express as px
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import pandas as pd
import csv

df=pd.read_csv('hw.csv')
hlist=df['Height(Inches)'].to_list()
wlist=df['Weight(Pounds)'].to_list()


hmean=statistics.mean(hlist)
hstandarddeviation=statistics.stdev(hlist)
wmean=statistics.mean(wlist)
wstandarddeviation=statistics.stdev(wlist)
print ('mean',statistics.mean(hlist))    
print ('median',statistics.median(hlist))
print ('mode',statistics.mode(hlist))
print ('hstandarddeviation',statistics.stdev(hlist))
print ('mean',statistics.mean(wlist))    
print ('median',statistics.median(wlist))
print ('mode',statistics.mode(wlist))
print ('wstandarddeviation',statistics.stdev(wlist))

firsthstandarddeviationstart,firsthstandarddeviationend=mean-hstandarddeviation,mean+hstandarddeviation
secondhstandarddeviationstart,secondhstandarddeviationend=mean-(2*hstandarddeviation),mean+(2*hstandarddeviation)
thirdhstandarddeviationstart,thirdhstandarddeviationend=mean-(3*hstandarddeviation),(3*mean+hstandarddeviation)
firstwstandarddeviationstart,firstwstandarddeviationend=mean-wstandarddeviation,mean+wstandarddeviation
secondwstandarddeviationstart,secondwstandarddeviationend=mean-(2*wstandarddeviation),mean+(2*wstandarddeviation)
thirdwstandarddeviationstart,thirdwstandarddeviationend=mean-(3*wstandarddeviation),(3*mean+wstandarddeviation)

listofdatawithinfirsthstandarddeviation=[result for result in hlist if result>firsthstandarddeviationstart and result<firsthstandarddeviationend]
listofdatawithinsecondhstandarddeviation=[result for result in hlist if result>secondhstandarddeviationstart and result<secondhstandarddeviationend]
listofdatawithinthirdhstandarddeviation=[result for result in hlist if result>thirdhstandarddeviationstart and result<thirdhstandarddeviationend]
print('{}% of data lies within first standard deviation',format(len(listofdatawithinfirsthstandarddeviation)*100.0/len(hlist)))
print('{}% of data lies within second standard deviation',format(len(listofdatawithinsecondhstandarddeviation)*100.0/len(hlist)))
print('{}% of data lies within third standard deviation',format(len(listofdatawithinthirdhstandarddeviation)*100.0/len(hlist)))

listofdatawithinfirstwstandarddeviation=[result for result in wlist if result>firstwstandarddeviationstart and result<firstwstandarddeviationend]
listofdatawithinsecondwstandarddeviation=[result for result in wlist if result>secondwstandarddeviationstart and result<secondwstandarddeviationend]
listofdatawithinthirdwstandarddeviation=[result for result in wlist if result>thirdwstandarddeviationstart and result<thirdwstandarddeviationend]
print('{}% of data lies within first standard deviation',format(len(listofdatawithinfirstwstandarddeviation)*100.0/len(wlist)))
print('{}% of data lies within second standard deviation',format(len(listofdatawithinsecondwstandarddeviation)*100.0/len(wlist)))
print('{}% of data lies within third standard deviation',format(len(listofdatawithinthirdwstandarddeviation)*100.0/len(wlist)))

#fig=px.bar(x=hlist,y=count,orientation='v')
fig=ff.create_distplot([hlist],['Result'],show_hist=False)
fig.add_trace(go.Scatter(x=[hmean,hmean],y=[0,0.17],mode='lines',name='hmean'))
fig.add_trace(go.Scatter(x=[firsthstandarddeviationstart,firsthstandarddeviationstart],y=[0,0.17],mode='lines',name='std1'))
fig.add_trace(go.Scatter(x=[firsthstandarddeviationend,firsthstandarddeviationend],y=[0,0.17],mode='lines',name='std1'))
fig.add_trace(go.Scatter(x=[secondhstandarddeviationstart,secondhstandarddeviationstart],y=[0,0.17],mode='lines',name='std2'))
fig.add_trace(go.Scatter(x=[secondhstandarddeviationend,secondhstandarddeviationend],y=[0,0.17],mode='lines',name='std2'))
fig.add_trace(go.Scatter(x=[thirdhstandarddeviationstart,thirdhstandarddeviationstart],y=[0,0.17],mode='lines',name='std3'))
fig.add_trace(go.Scatter(x=[thirdhstandarddeviationend,thirdhstandarddeviationend],y=[0,0.17],mode='lines',name='std3'))

fig=ff.create_distplot([wlist],['Result'],show_hist=False)
fig.add_trace(go.Scatter(x=[wmean,wmean],y=[0,0.17],mode='lines',name='wmean'))
fig.add_trace(go.Scatter(x=[firstwstandarddeviationstart,firstwstandarddeviationstart],y=[0,0.17],mode='lines',name='wstd1'))
fig.add_trace(go.Scatter(x=[firstwstandarddeviationend,firstwstandarddeviationend],y=[0,0.17],mode='lines',name='wstd1'))
fig.add_trace(go.Scatter(x=[secondwstandarddeviationstart,secondwstandarddeviationstart],y=[0,0.17],mode='lines',name='wstd2'))
fig.add_trace(go.Scatter(x=[secondwstandarddeviationend,secondwstandarddeviationend],y=[0,0.17],mode='lines',name='wstd2'))
fig.add_trace(go.Scatter(x=[thirdwstandarddeviationstart,thirdwstandarddeviationstart],y=[0,0.17],mode='lines',name='wstd3'))
fig.add_trace(go.Scatter(x=[thirdwstandarddeviationend,thirdwstandarddeviationend],y=[0,0.17],mode='lines',name='wstd3'))
fig.show()
### Test Script for a file found in the SDprox2 results from initial Parallel Simulations
from __future__ import division
import numpy
import matplotlib
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import scipy
from scipy import signal
from scipy import stats

Case = 'SDprox1_E_COM_I_COM'
EXCSLM = 1
EXCSR = 1

Inh90SR = 1
Inh180SR = 1
Inh270SR = 1
Inh90SLM = 1
Inh180SLM = 1
Inh270SLM = 1

EXC = 1
INH = 1

numExcThetaSyns = 27 # i.e. 3 connections so 9 synapses per connection
numInhThetaSyns = 8 # i.e. 2 connections so 4 synapses per connection
SaveExample = 1
randseed1 = 10 # if using fixed random seeds
randseed2 = 15

# HC Treshold Measurement Values
tstop = 10 # seconds
font_size = 13

Examples = numpy.load('NPYfiles/' + Case + '_ExampleHCModelParams.npy')
ExampleStrings = numpy.load('NPYfiles/' + Case + '_ExampleHCModelStrings.npy')
thetaSynMultiplier = numpy.array([0, 1, 2, 3])
prethetanoise = numpy.arange(0.00,0.11,0.01)

tstop = h.tstop/1000
dt = h.dt

for x2 in range(0,1):
	if Examples[0][x2] == 0:
		print(ExampleStrings[x2].decode("utf-8") + ' is empty')
		continue
	for n in prethetanoise:
		for y in range(0,4):
			print('Simulating... ' + str(ExampleStrings[x2]) + ' #' + str(y+1))
			ExampleString = ExampleStrings[x2].decode("utf-8")
			HCNumber = x2
			# Run Simulation of Example
			h.randomize_syns(5,2) # i.e. same random seeds when comparing runs
			h.f(Examples[0][x2],Examples[1][x2],Examples[2][x2],Examples[3][x2],SaveExample,randseed1,randseed2,1,INH*numInhThetaSyns*thetaSynMultiplier[y],EXC*numExcThetaSyns*thetaSynMultiplier[y],EXCSLM,EXCSR,Inh90SR,Inh180SR,Inh270SR,Inh90SLM,Inh180SLM,Inh270SLM,n) # i.e. same random seeds when comparing runs
			
			HC_Trace = numpy.fromfile("%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s" % ('model_',str(Examples[0][x2]),'_NumInh_',str(Examples[1][x2]),'_NumExc_',str(Examples[2][x2]),'_InhSpikes_',str(Examples[3][x2]),'_ExcSRSpikes_',str(Examples[3][x2]),'_ExcSLMSpikes_',str(9),'_NumExcCommon_',str(4),'_NumInhCommon_X',str(thetaSynMultiplier[y]),'_ThetaMultiplier_',str('%0.2f' %h.prethetanoise),'_prethetanoise.dat'),dtype=float)
			voltvec = HC_Trace[1:len(HC_Trace)]
			
			if y == 0:
				HC_Trace_Baseline = HC_Trace[10000:100001]
				HC_SpikeTimes_Baseline = numpy.zeros((len(HC_Trace),), dtype=numpy.float)
				for i in range(0,len(h.apctimes)): HC_SpikeTimes_Baseline[int(h.apctimes.x[i]/dt)] = h.apctimes.x[i]
				HC_SpikeTimes_Baseline = HC_SpikeTimes_Baseline[10000:100001]
				HC_SpikeTimes_Baseline2 = numpy.array(h.apctimes,dtype=numpy.float)
			elif y == 1:
				HC_Trace_Rhythm = HC_Trace[10000:100001]
				HC_SpikeTimes_Rhythm = numpy.zeros((len(HC_Trace),), dtype=numpy.float)
				for i in range(0,len(h.apctimes)): HC_SpikeTimes_Rhythm[int(h.apctimes.x[i]/dt)] = h.apctimes.x[i]
				HC_SpikeTimes_Rhythm = HC_SpikeTimes_Rhythm[10000:100001]
				HC_SpikeTimes_Rhythm2 = numpy.array(h.apctimes,dtype=numpy.float)
			elif y == 2:
				HC_Trace_X2Rhythm = HC_Trace[10000:100001]
				HC_SpikeTimes_X2Rhythm = numpy.zeros((len(HC_Trace),), dtype=numpy.float)
				for i in range(0,len(h.apctimes)): HC_SpikeTimes_X2Rhythm[int(h.apctimes.x[i]/dt)] = h.apctimes.x[i]
				HC_SpikeTimes_X2Rhythm = HC_SpikeTimes_X2Rhythm[10000:100001]
				HC_SpikeTimes_X2Rhythm2 = numpy.array(h.apctimes,dtype=numpy.float)
			elif y == 3:
				HC_Trace_X3Rhythm = HC_Trace[10000:100001]
				HC_SpikeTimes_X3Rhythm = numpy.zeros((len(HC_Trace),), dtype=numpy.float)
				for i in range(0,len(h.apctimes)): HC_SpikeTimes_X3Rhythm[int(h.apctimes.x[i]/dt)] = h.apctimes.x[i]
				HC_SpikeTimes_X3Rhythm = HC_SpikeTimes_X3Rhythm[10000:100001]
				HC_SpikeTimes_X3Rhythm2 = numpy.array(h.apctimes,dtype=numpy.float)
			
			timevec = numpy.arange(0,10000.1,0.1)
			if y == 0:
				f, axarr = matplotlib.pyplot.subplots(4, sharex=True)
				axarr[0].plot(timevec,voltvec,'b')
				axarr[0].set_title('Baseline High-Conductance',fontsize = font_size-2)
				# axarr[0].set_title("%s%s%s%s%s%s%s%s%s" % ('InhSyns: ',str(Examples[0][x]),', ExcSyns: ',str(Examples[1][x]),',\nInhSpikes: ',str(Examples[2][x]/tstop),'Hz, ExcSpikes: ',str(Examples[3][x]/tstop),'Hz'))
				axarr[0].set_ylim(-85,30)
				axarr[0].set_xlim(8000,10000)
				axarr[0].spines['right'].set_visible(False)
				axarr[0].spines['top'].set_visible(False)
				axarr[0].spines['bottom'].set_visible(False)
				for tic in axarr[0].xaxis.get_major_ticks():
					tic.tick1line.set_visible = tic.tick2line.set_visible = False
			if y == 1:
				axarr[1].plot(timevec,voltvec,'r')
				axarr[1].set_title('Theta Input X1',fontsize=font_size-2)
				axarr[1].set_ylim(-85,30)
				axarr[1].set_ylabel('Voltage (mV)     ',fontsize=font_size-2)
				axarr[1].set_xlim(8000,10000)
				axarr[1].spines['right'].set_visible(False)
				axarr[1].spines['top'].set_visible(False)
				axarr[1].spines['bottom'].set_visible(False)
				for tic in axarr[1].xaxis.get_major_ticks():
					tic.tick1line.set_visible = tic.tick2line.set_visible = False
			if y == 2:
				axarr[2].plot(timevec,voltvec,'g')
				axarr[2].set_title('Theta Input X2',fontsize=font_size-2)
				axarr[2].set_ylim(-85,30)
				axarr[2].set_xlim(8000,10000)
				axarr[2].spines['right'].set_visible(False)
				axarr[2].spines['top'].set_visible(False)
				axarr[2].spines['bottom'].set_visible(False)
				for tic in axarr[2].xaxis.get_major_ticks():
					tic.tick1line.set_visible = tic.tick2line.set_visible = False
			if y == 3:
				axarr[3].plot(timevec,voltvec,'c')
				axarr[3].set_title('Theta Input X3',fontsize=font_size-2)
				axarr[3].set_ylim(-85,30)
				axarr[3].set_xlim(8000,10000)
				axarr[3].set_xlabel('Time (ms)',fontsize=font_size-2)
				axarr[3].spines['right'].set_visible(False)
				axarr[3].spines['top'].set_visible(False)
				
				pyplot.savefig('PLOTfiles/' + Case + '_Trace_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.pdf', bbox_inches='tight')
				pyplot.savefig('PLOTfiles/' + Case + '_Trace_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.png', bbox_inches='tight')
				pyplot.gcf().clear()
				pyplot.cla()
				pyplot.clf()
				pyplot.close()
			if thetaSynMultiplier[y]>0:
				f2, axarr2 = matplotlib.pyplot.subplots(1)
				for j in range(0,int(h.excthetacount)):
					randind = int(h.EXCrandSRtheta.x[j])
					if randind == -1: randind = 0
					ThetaVec = numpy.array([],dtype=numpy.float)
					for q in range(0,len(h.ThetaSRexcprespiketrains[randind])): ThetaVec = numpy.append(ThetaVec,h.ThetaSRexcprespiketrains[randind].x[q])
					ThetaVec = numpy.array(ThetaVec,dtype=numpy.float)
					axarr2.vlines(ThetaVec,j+0.75,j+1.25,'g')
				for k in range(0,int(h.excthetacount)):
					randind = int(h.EXCrandSLMtheta.x[k])
					if randind == -1: randind = 0
					ThetaVec = numpy.array([],dtype=numpy.float)
					for q in range(0,len(h.ThetaSLMexcprespiketrains[randind])): ThetaVec = numpy.append(ThetaVec,h.ThetaSLMexcprespiketrains[randind].x[q])
					ThetaVec = numpy.array(ThetaVec,dtype=numpy.float)
					axarr2.vlines(ThetaVec,j+k+1.75,j+k+2.25,'c')
				for l in range(0,int(h.inhthetacount)):
					randind = int(h.randSRinhtheta90.x[l])
					if randind == -1: randind = 0
					ThetaVec = numpy.array([],dtype=numpy.float)
					for q in range(0,len(h.ThetaSRInh90prespiketrains[randind])): ThetaVec = numpy.append(ThetaVec,h.ThetaSRInh90prespiketrains[randind].x[q])
					ThetaVec = numpy.array(ThetaVec,dtype=numpy.float)
					axarr2.vlines(ThetaVec,l+j+k+2.75,l+j+k+3.25,'m')
				for m in range(0,int(h.inhthetacount)):
					randind = int(h.randSLMinhtheta90.x[m])
					if randind == -1: randind = 0
					ThetaVec = numpy.array([],dtype=numpy.float)
					for q in range(0,len(h.ThetaSLMInh90prespiketrains[randind])): ThetaVec = numpy.append(ThetaVec,h.ThetaSLMInh90prespiketrains[randind].x[q])
					ThetaVec = numpy.array(ThetaVec,dtype=numpy.float)
					axarr2.vlines(ThetaVec,m+l+j+k+3.75,m+l+j+k+4.25,'y')
				for n2 in range(0,int(h.inhthetacount)):
					randind = int(h.randSRinhtheta180.x[n2])
					if randind == -1: randind = 0
					ThetaVec = numpy.array([],dtype=numpy.float)
					for q in range(0,len(h.ThetaSRInh180prespiketrains[randind])): ThetaVec = numpy.append(ThetaVec,h.ThetaSRInh180prespiketrains[randind].x[q])
					ThetaVec = numpy.array(ThetaVec,dtype=numpy.float)
					axarr2.vlines(ThetaVec,n2+m+l+j+k+4.75,n2+m+l+j+k+5.25,'b')
				for o in range(0,int(h.inhthetacount)):
					randind = int(h.randSLMinhtheta180.x[o])
					if randind == -1: randind = 0
					ThetaVec = numpy.array([],dtype=numpy.float)
					for q in range(0,len(h.ThetaSLMInh180prespiketrains[randind])): ThetaVec = numpy.append(ThetaVec,h.ThetaSLMInh180prespiketrains[randind].x[q])
					ThetaVec = numpy.array(ThetaVec,dtype=numpy.float)
					axarr2.vlines(ThetaVec,o+n2+m+l+j+k+5.75,o+n2+m+l+j+k+6.25,'k')
				for p in range(0,int(h.inhthetacount)):
					randind = int(h.randSRinhtheta270.x[p])
					if randind == -1: randind = 0
					ThetaVec = numpy.array([],dtype=numpy.float)
					for q in range(0,len(h.ThetaSRInh270prespiketrains[randind])): ThetaVec = numpy.append(ThetaVec,h.ThetaSRInh270prespiketrains[randind].x[q])
					ThetaVec = numpy.array(ThetaVec,dtype=numpy.float)
					axarr2.vlines(ThetaVec,p+o+n2+m+l+j+k+6.75,p+o+n2+m+l+j+k+7.25,color='orange')
				for q2 in range(0,int(h.inhthetacount)):
					randind = int(h.randSLMinhtheta270.x[q2])
					if randind == -1: randind = 0
					ThetaVec = numpy.array([],dtype=numpy.float)
					for q in range(0,len(h.ThetaSLMInh270prespiketrains[randind])): ThetaVec = numpy.append(ThetaVec,h.ThetaSLMInh270prespiketrains[randind].x[q])
					ThetaVec = numpy.array(ThetaVec,dtype=numpy.float)
					axarr2.vlines(ThetaVec,q2+p+o+n2+m+l+j+k+6.75,q2+p+o+n2+m+l+j+k+7.25,color='r')
				axarr2.set_xlim(8000,10000)
				axarr2.set_ylim(0,q2+p+o+n2+m+l+j+k+8)
				axarr2.set_xlabel('Time (ms)',fontsize=font_size-4)
				axarr2.set_ylabel('CA3                   EC3                         Inhibition           ',fontsize=font_size-4)
				pyplot.savefig('PLOTfiles/' + Case + '_ThetaPresynapticSpikes_' + ExampleString + '_X' + str(y) + '_ThetaMultiplier_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.pdf', bbox_inches='tight')
				pyplot.savefig('PLOTfiles/' + Case + '_ThetaPresynapticSpikes_' + ExampleString + '_X' + str(y) + '_ThetaMultiplier_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.png', bbox_inches='tight')
				pyplot.gcf().clear()
				pyplot.cla()
				pyplot.clf()
				pyplot.close()
			
		f, axarr = matplotlib.pyplot.subplots(2, sharex=False)
		f1, Pxx_den1 = signal.welch(HC_SpikeTimes_Baseline, 1/(dt/1000), nperseg=25000)
		f2, Pxx_den2 = signal.welch(HC_SpikeTimes_Rhythm, 1/(dt/1000), nperseg=25000)
		f3, Pxx_den3 = signal.welch(HC_SpikeTimes_X2Rhythm, 1/(dt/1000), nperseg=25000)
		f4, Pxx_den4 = signal.welch(HC_SpikeTimes_X3Rhythm, 1/(dt/1000), nperseg=25000)
		numpy.save('NPYfiles/' + Case + '_SpikeTimesBaseline_' + str(HCNumber) + '_HCNumber_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.npy',HC_SpikeTimes_Baseline2)
		numpy.save('NPYfiles/' + Case + '_SpikeTimesRhythm_' + str(HCNumber) + '_HCNumber_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.npy',HC_SpikeTimes_Rhythm2)
		numpy.save('NPYfiles/' + Case + '_SpikeTimesX2Rhythm_' + str(HCNumber) + '_HCNumber_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.npy',HC_SpikeTimes_X2Rhythm2)
		numpy.save('NPYfiles/' + Case + '_SpikeTimesX3Rhythm_' + str(HCNumber) + '_HCNumber_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.npy',HC_SpikeTimes_X3Rhythm2)
		axarr[0].loglog(f1, Pxx_den1,'b')
		axarr[0].loglog(f2, Pxx_den2,'r')
		axarr[0].loglog(f3, Pxx_den3,'g')
		axarr[0].loglog(f4, Pxx_den4,'c')
		axarr[0].hlines(numpy.amax(Pxx_den4)+500,5,12,'k',linestyles='solid')
		axarr[0].text(5.05,numpy.amax(Pxx_den4)+1000,'Theta (5-12Hz)')
		axarr[0].axvline(numpy.array([5]),ymin=0,ymax=0.95,color='k',linestyle='solid')
		axarr[0].axvline(numpy.array([12]),ymin=0,ymax=0.95,color='k',linestyle='solid')
		axarr[0].axvline(numpy.array([8]),ymin=0,ymax=0.95,color='k',linestyle='dashed')
		axarr[0].set_xlim(0,100)
		axarr[0].set_xlabel('frequency (Hz)')
		axarr[0].set_ylabel(r'$PSD (Spikes^2 / Hz)$')
		axarr[0].spines['right'].set_visible(False)
		axarr[0].spines['top'].set_visible(False)
		
		ind = numpy.arange(8)
		width = 0.4
		Area1 = numpy.trapz(Pxx_den1[(f1>5) & (f1<12)],x=f1[(f1>5) & (f1<12)])
		Area2 = numpy.trapz(Pxx_den2[(f2>5) & (f2<12)],x=f2[(f2>5) & (f2<12)])
		Area3 = numpy.trapz(Pxx_den3[(f3>5) & (f3<12)],x=f3[(f3>5) & (f3<12)])
		Area4 = numpy.trapz(Pxx_den4[(f4>5) & (f4<12)],x=f4[(f4>5) & (f4<12)])
		e8Hz1 = Pxx_den1[f1==8]
		e8Hz2 = Pxx_den2[f2==8]
		e8Hz3 = Pxx_den3[f3==8]
		e8Hz4 = Pxx_den4[f4==8]
		axarr[1].bar(ind+width, [Area1, Area2, Area3, Area4, e8Hz1[0], e8Hz2[0], e8Hz3[0], e8Hz4[0]], width, color='k')
		axarr[1].set_xticks(ind+width)
		axarr[1].set_xticklabels(('Base\n(5-12Hz)','ThetaX1\n(5-12Hz)', 'ThetaX2\n(5-12Hz)', 'ThetaX3\n(5-12Hz)', 'Base\n(8Hz)','ThetaX1\n(8Hz)','ThetaX2\n(8Hz)','ThetaX3\n(8Hz)'),fontsize=font_size-3, fontweight='bold', rotation=45)
		axarr[1].set_ylabel('PSD Magnitude')
		axarr[1].set_xlim(0,8+width)
		axarr[1].spines['right'].set_visible(False)
		axarr[1].spines['top'].set_visible(False)
		pyplot.tight_layout()
		pyplot.savefig('PLOTfiles/' + Case + '_PSD_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.pdf', bbox_inches='tight')
		pyplot.savefig('PLOTfiles/' + Case + '_PSD_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.png', bbox_inches='tight')
		pyplot.gcf().clear()
		pyplot.cla()
		pyplot.clf()
		pyplot.close()
		
		# Instantaneous Frequency Analyses (Note this is converting the ISIs into seconds and then instantaneous frequencies)
		IF_Baseline = numpy.concatenate([numpy.array([0],dtype=numpy.float),1000/numpy.diff(HC_SpikeTimes_Baseline2)])
		IF_ThetaX1 = numpy.concatenate([numpy.array([0],dtype=numpy.float),1000/numpy.diff(HC_SpikeTimes_Rhythm2)])
		IF_ThetaX2 = numpy.concatenate([numpy.array([0],dtype=numpy.float),1000/numpy.diff(HC_SpikeTimes_X2Rhythm2)])
		IF_ThetaX3 = numpy.concatenate([numpy.array([0],dtype=numpy.float),1000/numpy.diff(HC_SpikeTimes_X3Rhythm2)])
		
		range_if = (0,100)
		heights1,bins1 = numpy.histogram(IF_Baseline,bins=100,range=range_if)
		heights2,bins2 = numpy.histogram(IF_ThetaX1,bins=100,range=range_if)
		heights3,bins3 = numpy.histogram(IF_ThetaX2,bins=100,range=range_if)
		heights4,bins4 = numpy.histogram(IF_ThetaX3,bins=100,range=range_if)
		
		# Normalize
		heights1 = heights1/float(sum(heights1))
		heights2 = heights2/float(sum(heights2))
		heights3 = heights3/float(sum(heights3))
		heights4 = heights4/float(sum(heights4))
		bin1=bins1[:-1]+numpy.diff(bins1)/2.
		bin2=bins2[:-1]+numpy.diff(bins2)/2.
		bin3=bins3[:-1]+numpy.diff(bins3)/2.
		bin4=bins4[:-1]+numpy.diff(bins4)/2.
		binMids1 = bin1[~numpy.isnan(bin1)]
		binMids2 = bin2[~numpy.isnan(bin2)]
		binMids3 = bin3[~numpy.isnan(bin3)]
		binMids4 = bin4[~numpy.isnan(bin4)]
		heights1 = heights1[~numpy.isnan(bin1)]
		heights2 = heights2[~numpy.isnan(bin2)]
		heights3 = heights3[~numpy.isnan(bin3)]
		heights4 = heights4[~numpy.isnan(bin4)]
		
		f, axarr = matplotlib.pyplot.subplots(2, sharex=False)
		axarr[0].semilogx(binMids1,heights1,'b')
		axarr[0].semilogx(binMids2,heights2,'r')
		axarr[0].semilogx(binMids3,heights3,'g')
		axarr[0].semilogx(binMids4,heights4,'c')
		axarr[0].vlines(numpy.array([4,12]),0,numpy.amax(heights4)+0.01,'k',linestyles='solid')
		axarr[0].vlines(numpy.array([8]),0,numpy.amax(heights4)+0.01,'k',linestyles='dashed')
		axarr[0].hlines(numpy.amax(heights4)+0.01,4,12,'k',linestyles='solid')
		axarr[0].text(4.3,numpy.amax(heights4)+0.02,'Theta (4-12Hz)')
		axarr[0].set_xlabel('Frequency (Hz)')
		axarr[0].set_ylabel('Probability')
		axarr[0].set_xlim(0,130)
		axarr[0].set_ylim(0,0.19)
		axarr[0].spines['right'].set_visible(False)
		axarr[0].spines['top'].set_visible(False)
		
		ind = numpy.arange(8)
		width = 0.4
		Area11 = numpy.trapz(heights1[(binMids1>4) & (binMids1<8)],x=binMids1[(binMids1>4) & (binMids1<8)])
		Area22 = numpy.trapz(heights2[(binMids2>4) & (binMids2<8)],x=binMids2[(binMids2>4) & (binMids2<8)])
		Area33 = numpy.trapz(heights3[(binMids3>4) & (binMids3<8)],x=binMids3[(binMids3>4) & (binMids3<8)])
		Area44 = numpy.trapz(heights4[(binMids4>4) & (binMids4<8)],x=binMids4[(binMids4>4) & (binMids4<8)])
		e8Hz11 = numpy.trapz(heights1[(binMids1>8) & (binMids1<12)],x=binMids1[(binMids1>8) & (binMids1<12)]) #IF NOT THIS TRY NUMPY.AMAX BETWEEN 7 AND 9
		e8Hz22 = numpy.trapz(heights2[(binMids2>8) & (binMids2<12)],x=binMids2[(binMids2>8) & (binMids2<12)])
		e8Hz33 = numpy.trapz(heights3[(binMids3>8) & (binMids3<12)],x=binMids3[(binMids3>8) & (binMids3<12)])
		e8Hz44 = numpy.trapz(heights4[(binMids4>8) & (binMids4<12)],x=binMids4[(binMids4>8) & (binMids4<12)])
		axarr[1].bar(ind+width, [Area11, Area22, Area33, Area44, e8Hz11, e8Hz22, e8Hz33, e8Hz44], width, color='k')
		axarr[1].set_xticks(ind+width)
		axarr[1].set_xticklabels(('Base\n(4-8Hz)','ThetaX1\n(4-8Hz)', 'ThetaX2\n(4-8Hz)', 'ThetaX3\n(4-8Hz)', 'Base\n(8-12Hz)','ThetaX1\n(8-12Hz)','ThetaX2\n(8-12Hz)','ThetaX3\n(8-12Hz)'),fontsize=font_size-3, fontweight='bold', rotation=45)
		axarr[1].set_ylabel('Probability')
		axarr[1].set_xlim(0,8+width)
		axarr[1].spines['right'].set_visible(False)
		axarr[1].spines['top'].set_visible(False)
		pyplot.tight_layout()
		pyplot.savefig('PLOTfiles/' + Case + '_IFDistribution_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.pdf', bbox_inches='tight')
		pyplot.savefig('PLOTfiles/' + Case + '_IFDistribution_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.png', bbox_inches='tight')
		pyplot.gcf().clear()
		pyplot.cla()
		pyplot.clf()
		pyplot.close()
		
		# Polar Distribution Plots
		STX0 = HC_SpikeTimes_Baseline2/125
		STX1 = HC_SpikeTimes_Rhythm2/125
		STX2 = HC_SpikeTimes_X2Rhythm2/125
		STX3 = HC_SpikeTimes_X3Rhythm2/125
		Rads_Baseline = 2*numpy.pi*(STX0-STX0.astype(int))
		Rads_1XRhythm = 2*numpy.pi*(STX1-STX1.astype(int))
		Rads_2XRhythm = 2*numpy.pi*(STX2-STX2.astype(int))
		Rads_3XRhythm = 2*numpy.pi*(STX3-STX3.astype(int))
		
		Rads_Baseline_Sorted = sorted(Rads_Baseline)
		Rads_1XRhythm_Sorted = sorted(Rads_1XRhythm)
		Rads_2XRhythm_Sorted = sorted(Rads_2XRhythm)
		Rads_3XRhythm_Sorted = sorted(Rads_3XRhythm)
		
		IF_Baseline_Sorted = [x for i, x in sorted(zip(Rads_Baseline,IF_Baseline))]
		IF_ThetaX1_Sorted = [x for i, x in sorted(zip(Rads_1XRhythm,IF_ThetaX1))]
		IF_ThetaX2_Sorted = [x for i, x in sorted(zip(Rads_2XRhythm,IF_ThetaX2))]
		IF_ThetaX3_Sorted = [x for i, x in sorted(zip(Rads_3XRhythm,IF_ThetaX3))]
		
		bin_size = 25
		range_if = (0,100)
		range_rads = (0,2*numpy.pi)
		
		heights11,be11 = numpy.histogram(Rads_Baseline,bins=bin_size,range=range_rads)
		bins11 = be11[:-1]+numpy.diff(be11)/2.
		PrefPhase_Baseline = bins11[heights11 == numpy.amax(heights11)]
		heights22,be22 = numpy.histogram(Rads_1XRhythm,bins=bin_size,range=range_rads)
		bins22 = be22[:-1]+numpy.diff(be22)/2.
		PrefPhase_ThetaX1 = bins22[heights22 == numpy.amax(heights22)]
		heights33,be33 = numpy.histogram(Rads_2XRhythm,bins=bin_size,range=range_rads)
		bins33 = be33[:-1]+numpy.diff(be33)/2.
		PrefPhase_ThetaX2 = bins33[heights33 == numpy.amax(heights33)]
		heights44,be44 = numpy.histogram(Rads_3XRhythm,bins=bin_size,range=range_rads)
		bins44 = be44[:-1]+numpy.diff(be44)/2.
		PrefPhase_ThetaX3 = bins44[heights44 == numpy.amax(heights44)]
		
		Rads_Baseline_MeanBins,be11,bn11 = scipy.stats.binned_statistic(Rads_Baseline_Sorted,Rads_Baseline_Sorted,statistic='mean',bins=bin_size,range=range_rads)
		_BMeans = Rads_Baseline_MeanBins
		Rads_Baseline_MeanBins = Rads_Baseline_MeanBins[~numpy.isnan(Rads_Baseline_MeanBins)]
		Rads_Baseline_MeanBins = numpy.append(Rads_Baseline_MeanBins,Rads_Baseline_MeanBins[0])
		Rads_1XRhythm_MeanBins,be21,bn21 = scipy.stats.binned_statistic(Rads_1XRhythm_Sorted,Rads_1XRhythm_Sorted,statistic='mean',bins=bin_size,range=range_rads)
		_1Means = Rads_1XRhythm_MeanBins
		Rads_1XRhythm_MeanBins = Rads_1XRhythm_MeanBins[~numpy.isnan(Rads_1XRhythm_MeanBins)]
		Rads_1XRhythm_MeanBins = numpy.append(Rads_1XRhythm_MeanBins,Rads_1XRhythm_MeanBins[0])
		Rads_2XRhythm_MeanBins,be31,bn31 = scipy.stats.binned_statistic(Rads_2XRhythm_Sorted,Rads_2XRhythm_Sorted,statistic='mean',bins=bin_size,range=range_rads)
		_2Means = Rads_2XRhythm_MeanBins
		Rads_2XRhythm_MeanBins = Rads_2XRhythm_MeanBins[~numpy.isnan(Rads_2XRhythm_MeanBins)]
		Rads_2XRhythm_MeanBins = numpy.append(Rads_2XRhythm_MeanBins,Rads_2XRhythm_MeanBins[0])
		Rads_3XRhythm_MeanBins,be41,bn41 = scipy.stats.binned_statistic(Rads_3XRhythm_Sorted,Rads_3XRhythm_Sorted,statistic='mean',bins=bin_size,range=range_rads)
		_3Means = Rads_3XRhythm_MeanBins
		Rads_3XRhythm_MeanBins = Rads_3XRhythm_MeanBins[~numpy.isnan(Rads_3XRhythm_MeanBins)]
		Rads_3XRhythm_MeanBins = numpy.append(Rads_3XRhythm_MeanBins,Rads_3XRhythm_MeanBins[0])
		
		IF_Baseline_MeanBins,be12,bn12 = scipy.stats.binned_statistic(Rads_Baseline_Sorted,IF_Baseline_Sorted,statistic='mean',bins=bin_size,range=range_rads)
		IF_Baseline_MeanBins = IF_Baseline_MeanBins[~numpy.isnan(_BMeans)]
		IF_Baseline_MeanBins = numpy.append(IF_Baseline_MeanBins,IF_Baseline_MeanBins[0])
		IF_1XRhythm_MeanBins,be22,bn22 = scipy.stats.binned_statistic(Rads_1XRhythm_Sorted,IF_ThetaX1_Sorted,statistic='mean',bins=bin_size,range=range_rads)
		IF_1XRhythm_MeanBins = IF_1XRhythm_MeanBins[~numpy.isnan(_1Means)]
		IF_1XRhythm_MeanBins = numpy.append(IF_1XRhythm_MeanBins,IF_1XRhythm_MeanBins[0])
		IF_2XRhythm_MeanBins,be32,bn32 = scipy.stats.binned_statistic(Rads_2XRhythm_Sorted,IF_ThetaX2_Sorted,statistic='mean',bins=bin_size,range=range_rads)
		IF_2XRhythm_MeanBins = IF_2XRhythm_MeanBins[~numpy.isnan(_2Means)]
		IF_2XRhythm_MeanBins = numpy.append(IF_2XRhythm_MeanBins,IF_2XRhythm_MeanBins[0])
		IF_3XRhythm_MeanBins,be42,bn42 = scipy.stats.binned_statistic(Rads_3XRhythm_Sorted,IF_ThetaX3_Sorted,statistic='mean',bins=bin_size,range=range_rads)
		IF_3XRhythm_MeanBins = IF_3XRhythm_MeanBins[~numpy.isnan(_3Means)]
		IF_3XRhythm_MeanBins = numpy.append(IF_3XRhythm_MeanBins,IF_3XRhythm_MeanBins[0])
		
		IF_Baseline_MinsBins,be111,bn111 = scipy.stats.binned_statistic(Rads_Baseline_Sorted,IF_Baseline_Sorted,statistic='min',bins=bin_size,range=range_rads)
		IF_Baseline_MinsBins = IF_Baseline_MinsBins[~numpy.isnan(_BMeans)]
		IF_Baseline_MinsBins = numpy.append(IF_Baseline_MinsBins,IF_Baseline_MinsBins[0])
		IF_1XRhythm_MinsBins,be211,bn211 = scipy.stats.binned_statistic(Rads_1XRhythm_Sorted,IF_ThetaX1_Sorted,statistic='min',bins=bin_size,range=range_rads)
		IF_1XRhythm_MinsBins = IF_1XRhythm_MinsBins[~numpy.isnan(_1Means)]
		IF_1XRhythm_MinsBins = numpy.append(IF_1XRhythm_MinsBins,IF_1XRhythm_MinsBins[0])
		IF_2XRhythm_MinsBins,be311,bn311 = scipy.stats.binned_statistic(Rads_2XRhythm_Sorted,IF_ThetaX2_Sorted,statistic='min',bins=bin_size,range=range_rads)
		IF_2XRhythm_MinsBins = IF_2XRhythm_MinsBins[~numpy.isnan(_2Means)]
		IF_2XRhythm_MinsBins = numpy.append(IF_2XRhythm_MinsBins,IF_2XRhythm_MinsBins[0])
		IF_3XRhythm_MinsBins,be411,bn411 = scipy.stats.binned_statistic(Rads_3XRhythm_Sorted,IF_ThetaX3_Sorted,statistic='min',bins=bin_size,range=range_rads)
		IF_3XRhythm_MinsBins = IF_3XRhythm_MinsBins[~numpy.isnan(_3Means)]
		IF_3XRhythm_MinsBins = numpy.append(IF_3XRhythm_MinsBins,IF_3XRhythm_MinsBins[0])
		
		IF_Baseline_MaxBins,be111,bn111 = scipy.stats.binned_statistic(Rads_Baseline_Sorted,IF_Baseline_Sorted,statistic='max',bins=bin_size,range=range_rads)
		IF_Baseline_MaxBins = IF_Baseline_MaxBins[~numpy.isnan(_BMeans)]
		IF_Baseline_MaxBins = numpy.append(IF_Baseline_MaxBins,IF_Baseline_MaxBins[0])
		IF_1XRhythm_MaxBins,be211,bn211 = scipy.stats.binned_statistic(Rads_1XRhythm_Sorted,IF_ThetaX1_Sorted,statistic='max',bins=bin_size,range=range_rads)
		IF_1XRhythm_MaxBins = IF_1XRhythm_MaxBins[~numpy.isnan(_1Means)]
		IF_1XRhythm_MaxBins = numpy.append(IF_1XRhythm_MaxBins,IF_1XRhythm_MaxBins[0])
		IF_2XRhythm_MaxBins,be311,bn311 = scipy.stats.binned_statistic(Rads_2XRhythm_Sorted,IF_ThetaX2_Sorted,statistic='max',bins=bin_size,range=range_rads)
		IF_2XRhythm_MaxBins = IF_2XRhythm_MaxBins[~numpy.isnan(_2Means)]
		IF_2XRhythm_MaxBins = numpy.append(IF_2XRhythm_MaxBins,IF_2XRhythm_MaxBins[0])
		IF_3XRhythm_MaxBins,be411,bn411 = scipy.stats.binned_statistic(Rads_3XRhythm_Sorted,IF_ThetaX3_Sorted,statistic='max',bins=bin_size,range=range_rads)
		IF_3XRhythm_MaxBins = IF_3XRhythm_MaxBins[~numpy.isnan(_3Means)]
		IF_3XRhythm_MaxBins = numpy.append(IF_3XRhythm_MaxBins,IF_3XRhythm_MaxBins[0])
		
		IF_Baseline_StdBins,be111,bn111 = scipy.stats.binned_statistic(Rads_Baseline_Sorted,IF_Baseline_Sorted,statistic='std',bins=bin_size,range=range_rads)
		IF_Baseline_StdBins = IF_Baseline_StdBins[~numpy.isnan(_BMeans)]
		IF_Baseline_StdBins = numpy.append(IF_Baseline_StdBins,IF_Baseline_StdBins[0])
		IF_1XRhythm_StdBins,be211,bn211 = scipy.stats.binned_statistic(Rads_1XRhythm_Sorted,IF_ThetaX1_Sorted,statistic='std',bins=bin_size,range=range_rads)
		IF_1XRhythm_StdBins = IF_1XRhythm_StdBins[~numpy.isnan(_1Means)]
		IF_1XRhythm_StdBins = numpy.append(IF_1XRhythm_StdBins,IF_1XRhythm_StdBins[0])
		IF_2XRhythm_StdBins,be311,bn311 = scipy.stats.binned_statistic(Rads_2XRhythm_Sorted,IF_ThetaX2_Sorted,statistic='std',bins=bin_size,range=range_rads)
		IF_2XRhythm_StdBins = IF_2XRhythm_StdBins[~numpy.isnan(_2Means)]
		IF_2XRhythm_StdBins = numpy.append(IF_2XRhythm_StdBins,IF_2XRhythm_StdBins[0])
		IF_3XRhythm_StdBins,be411,bn411 = scipy.stats.binned_statistic(Rads_3XRhythm_Sorted,IF_ThetaX3_Sorted,statistic='std',bins=bin_size,range=range_rads)
		IF_3XRhythm_StdBins = IF_3XRhythm_StdBins[~numpy.isnan(_3Means)]
		IF_3XRhythm_StdBins = numpy.append(IF_3XRhythm_StdBins,IF_3XRhythm_StdBins[0])
		
		axarr = pyplot.subplot(111, projection='polar')
		axarr.plot(Rads_Baseline_Sorted,IF_Baseline_Sorted,'b',label='Baseline')
		axarr.plot(Rads_1XRhythm_Sorted,IF_ThetaX1_Sorted,'r',label='ThetaX1')
		axarr.plot(Rads_2XRhythm_Sorted,IF_ThetaX2_Sorted,'g',label='ThetaX2')
		axarr.plot(Rads_3XRhythm_Sorted,IF_ThetaX3_Sorted,'c',label='ThetaX3')
		position = 292.5
		axarr._r_label_position._t = (position, 0)
		axarr._r_label_position.invalidate()
		axarr.set_xticklabels(['0$^\circ$', '45$^\circ$', '90$^\circ$\nPeak', '135$^\circ$', '180$^\circ$', '225$^\circ$', '270$^\circ$\nTrough', '315$^\circ$'])
		# axarr.legend(loc=1)
		pyplot.tight_layout()
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlot_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.pdf', bbox_inches='tight')
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlot_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.png', bbox_inches='tight')
		pyplot.gcf().clear()
		pyplot.cla()
		pyplot.clf()
		pyplot.close()
		
		axarr = pyplot.subplot(111, projection='polar')
		axarr.plot(Rads_Baseline_MeanBins,IF_Baseline_MeanBins,'b',label='Baseline')
		# axarr.fill_between(Rads_Baseline_MeanBins,IF_Baseline_MinsBins,IF_Baseline_MaxBins,alpha=0.5, edgecolor='b', facecolor='b')
		axarr.fill_between(Rads_Baseline_MeanBins,numpy.clip(IF_Baseline_MeanBins-IF_Baseline_StdBins,0,1000),numpy.clip(IF_Baseline_MeanBins+IF_Baseline_StdBins,0,1000),alpha=0.5, edgecolor='b', facecolor='b')
		axarr.plot(Rads_1XRhythm_MeanBins,IF_1XRhythm_MeanBins,'r',label='ThetaX1')
		# axarr.fill_between(Rads_1XRhythm_MeanBins,IF_1XRhythm_MinsBins,IF_1XRhythm_MaxBins,alpha=0.5, edgecolor='r', facecolor='r')
		axarr.fill_between(Rads_1XRhythm_MeanBins,numpy.clip(IF_1XRhythm_MeanBins-IF_1XRhythm_StdBins,0,1000),numpy.clip(IF_1XRhythm_MeanBins+IF_1XRhythm_StdBins,0,1000),alpha=0.5, edgecolor='r', facecolor='r')
		axarr.plot(Rads_2XRhythm_MeanBins,IF_2XRhythm_MeanBins,'g',label='ThetaX2')
		# axarr.fill_between(Rads_2XRhythm_MeanBins,IF_2XRhythm_MinsBins,IF_2XRhythm_MaxBins,alpha=0.5, edgecolor='g', facecolor='g')
		axarr.fill_between(Rads_2XRhythm_MeanBins,numpy.clip(IF_2XRhythm_MeanBins-IF_2XRhythm_StdBins,0,1000),numpy.clip(IF_2XRhythm_MeanBins+IF_2XRhythm_StdBins,0,1000),alpha=0.5, edgecolor='g', facecolor='g')
		axarr.plot(Rads_3XRhythm_MeanBins,IF_3XRhythm_MeanBins,'c',label='ThetaX3')
		# axarr.fill_between(Rads_3XRhythm_MeanBins,IF_3XRhythm_MinsBins,IF_3XRhythm_MaxBins,alpha=0.5, edgecolor='c', facecolor='c')
		axarr.fill_between(Rads_3XRhythm_MeanBins,numpy.clip(IF_3XRhythm_MeanBins-IF_3XRhythm_StdBins,0,1000),numpy.clip(IF_3XRhythm_MeanBins+IF_3XRhythm_StdBins,0,1000),alpha=0.5, edgecolor='c', facecolor='c')
		position = 292.5
		axarr._r_label_position._t = (position, 0)
		axarr._r_label_position.invalidate()
		axarr.set_xticklabels(['0$^\circ$', '45$^\circ$', '90$^\circ$\nPeak', '135$^\circ$', '180$^\circ$', '225$^\circ$', '270$^\circ$\nTrough', '315$^\circ$'])
		# axarr.legend(loc=1)
		pyplot.tight_layout()
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlotBinned_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.pdf', bbox_inches='tight')
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlotBinned_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.png', bbox_inches='tight')
		pyplot.gcf().clear()
		pyplot.cla()
		pyplot.clf()
		pyplot.close()
		
		axarr = pyplot.subplot(111, projection='polar')
		axarr.plot(Rads_Baseline_MeanBins,IF_Baseline_MeanBins,'b',label='Baseline')
		# axarr.fill_between(Rads_Baseline_MeanBins,IF_Baseline_MinsBins,IF_Baseline_MaxBins,alpha=0.5, edgecolor='b', facecolor='b')
		axarr.fill_between(Rads_Baseline_MeanBins,numpy.clip(IF_Baseline_MeanBins-IF_Baseline_StdBins,0,1000),numpy.clip(IF_Baseline_MeanBins+IF_Baseline_StdBins,0,1000),alpha=0.5, edgecolor='b', facecolor='b')
		position = 292.5
		bottom = numpy.amax(numpy.clip(IF_Baseline_MeanBins+IF_Baseline_StdBins,0,1000))+5
		width = range_rads[1]/(bin_size+1)
		axarr.bar(_BMeans, heights11, width=width, bottom=bottom,color='b')
		# for ph in range(0,len(PrefPhase_Baseline)):
		#     axarr.annotate(' ', xy=(PrefPhase_Baseline[ph], numpy.amax(numpy.clip(IF_Baseline_MeanBins+IF_Baseline_StdBins,0,1000))), xytext=(0, 0),arrowprops=dict(facecolor='black', shrink=0.05),)
		axarr._r_label_position._t = (position, 0)
		axarr._r_label_position.invalidate()
		axarr.set_xticklabels(['0$^\circ$', '45$^\circ$', '90$^\circ$\nPeak', '135$^\circ$', '180$^\circ$', '225$^\circ$', '270$^\circ$\nTrough', '315$^\circ$'])
		# axarr.legend(loc=1)
		pyplot.tight_layout()
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlotBinnedBaseline_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.pdf', bbox_inches='tight')
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlotBinnedBaseline_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.png', bbox_inches='tight')
		pyplot.gcf().clear()
		pyplot.cla()
		pyplot.clf()
		pyplot.close()
		
		axarr = pyplot.subplot(111, projection='polar')
		axarr.plot(Rads_1XRhythm_MeanBins,IF_1XRhythm_MeanBins,'r',label='ThetaX1')
		# axarr.fill_between(Rads_1XRhythm_MeanBins,IF_1XRhythm_MinsBins,IF_1XRhythm_MaxBins,alpha=0.5, edgecolor='r', facecolor='r')
		axarr.fill_between(Rads_1XRhythm_MeanBins,numpy.clip(IF_1XRhythm_MeanBins-IF_1XRhythm_StdBins,0,1000),numpy.clip(IF_1XRhythm_MeanBins+IF_1XRhythm_StdBins,0,1000),alpha=0.5, edgecolor='r', facecolor='r')
		position = 292.5
		bottom = numpy.amax(numpy.clip(IF_1XRhythm_MeanBins+IF_1XRhythm_StdBins,0,1000))+5
		width = range_rads[1]/(bin_size+1)
		axarr.bar(_1Means, heights22, width=width, bottom=bottom,color='r')
		# for ph in range(0,len(PrefPhase_ThetaX1)):
		#     axarr.annotate(' ', xy=(PrefPhase_ThetaX1[ph], numpy.amax(numpy.clip(IF_1XRhythm_MeanBins+IF_1XRhythm_StdBins,0,1000))), xytext=(0, 0),arrowprops=dict(facecolor='black', shrink=0.05),)
		axarr._r_label_position._t = (position, 0)
		axarr._r_label_position.invalidate()
		axarr.set_xticklabels(['0$^\circ$', '45$^\circ$', '90$^\circ$\nPeak', '135$^\circ$', '180$^\circ$', '225$^\circ$', '270$^\circ$\nTrough', '315$^\circ$'])
		# axarr.legend(loc=1)
		pyplot.tight_layout()
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlotBinned1XTheta_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.pdf', bbox_inches='tight')
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlotBinned1XTheta_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.png', bbox_inches='tight')
		pyplot.gcf().clear()
		pyplot.cla()
		pyplot.clf()
		pyplot.close()
		
		axarr = pyplot.subplot(111, projection='polar')
		axarr.plot(Rads_2XRhythm_MeanBins,IF_2XRhythm_MeanBins,'g',label='ThetaX2')
		# axarr.fill_between(Rads_2XRhythm_MeanBins,IF_2XRhythm_MinsBins,IF_2XRhythm_MaxBins,alpha=0.5, edgecolor='g', facecolor='g')
		axarr.fill_between(Rads_2XRhythm_MeanBins,numpy.clip(IF_2XRhythm_MeanBins-IF_2XRhythm_StdBins,0,1000),numpy.clip(IF_2XRhythm_MeanBins+IF_2XRhythm_StdBins,0,1000),alpha=0.5, edgecolor='g', facecolor='g')
		position = 292.5
		bottom = numpy.amax(numpy.clip(IF_2XRhythm_MeanBins+IF_2XRhythm_StdBins,0,1000))+5
		width = range_rads[1]/(bin_size+1)
		axarr.bar(_2Means, heights33, width=width, bottom=bottom,color='g')
		# for ph in range(0,len(PrefPhase_ThetaX2)):
		#     axarr.annotate(' ', xy=(PrefPhase_ThetaX2[ph], numpy.amax(numpy.clip(IF_2XRhythm_MeanBins+IF_2XRhythm_StdBins,0,1000))), xytext=(0, 0),arrowprops=dict(facecolor='black', shrink=0.05),)
		axarr._r_label_position._t = (position, 0)
		axarr._r_label_position.invalidate()
		axarr.set_xticklabels(['0$^\circ$', '45$^\circ$', '90$^\circ$\nPeak', '135$^\circ$', '180$^\circ$', '225$^\circ$', '270$^\circ$\nTrough', '315$^\circ$'])
		# axarr.legend(loc=1)
		pyplot.tight_layout()
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlotBinned2XTheta_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.pdf', bbox_inches='tight')
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlotBinned2XTheta_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.png', bbox_inches='tight')
		pyplot.gcf().clear()
		pyplot.cla()
		pyplot.clf()
		pyplot.close()
		
		axarr = pyplot.subplot(111, projection='polar')
		axarr.plot(Rads_3XRhythm_MeanBins,IF_3XRhythm_MeanBins,'c',label='ThetaX3')
		# axarr.fill_between(Rads_3XRhythm_MeanBins,IF_3XRhythm_MinsBins,IF_3XRhythm_MaxBins,alpha=0.5, edgecolor='c', facecolor='c')
		axarr.fill_between(Rads_3XRhythm_MeanBins,numpy.clip(IF_3XRhythm_MeanBins-IF_3XRhythm_StdBins,0,1000),numpy.clip(IF_3XRhythm_MeanBins+IF_3XRhythm_StdBins,0,1000),alpha=0.5, edgecolor='c', facecolor='c')
		position = 292.5
		bottom = numpy.amax(numpy.clip(IF_3XRhythm_MeanBins+IF_3XRhythm_StdBins,0,1000))+5
		width = range_rads[1]/(bin_size+1)
		axarr.bar(_3Means, heights44, width=width, bottom=bottom,color='c')
		# for ph in range(0,len(PrefPhase_ThetaX3)):
		#     axarr.annotate(' ', xy=(PrefPhase_ThetaX3[ph], numpy.amax(numpy.clip(IF_3XRhythm_MeanBins+IF_3XRhythm_StdBins,0,1000))), xytext=(0, 0),arrowprops=dict(facecolor='black', shrink=0.05),)
		axarr._r_label_position._t = (position, 0)
		axarr._r_label_position.invalidate()
		axarr.set_xticklabels(['0$^\circ$', '45$^\circ$', '90$^\circ$\nPeak', '135$^\circ$', '180$^\circ$', '225$^\circ$', '270$^\circ$\nTrough', '315$^\circ$'])
		# axarr.legend(loc=1)
		pyplot.tight_layout()
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlotBinned3XTheta_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.pdf', bbox_inches='tight')
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlotBinned3XTheta_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.png', bbox_inches='tight')
		pyplot.gcf().clear()
		pyplot.cla()
		pyplot.clf()
		pyplot.close()
	
	numpy.save('NPYfiles/' + Case + '_Areas_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.npy',numpy.array([Area1,Area2,Area3,Area4],dtype=numpy.float))
	numpy.save('NPYfiles/' + Case + '_e8Hz_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.npy',numpy.array([e8Hz1,e8Hz2,e8Hz3,e8Hz4],dtype=numpy.float))

# LNI_LNE_LIS_LES
# HNI_LNE_LIS_LES
# LNI_HNE_LIS_LES
# HNI_HNE_LIS_LES
# LNI_LNE_HIS_LES
# HNI_LNE_HIS_LES
# LNI_HNE_HIS_LES
# HNI_HNE_HIS_LES
# LNI_LNE_LIS_HES
# HNI_LNE_LIS_HES
# LNI_HNE_LIS_HES
# HNI_HNE_LIS_HES
# LNI_LNE_HIS_HES
# HNI_LNE_HIS_HES
# LNI_HNE_HIS_HES
# HNI_HNE_HIS_HES

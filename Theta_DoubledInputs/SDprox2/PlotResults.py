### Test Script for a file found in the SDprox2 results from initial Parallel Simulations
from __future__ import division
import numpy
import matplotlib
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import scipy
from scipy import signal
from scipy import stats

Case = 'SDprox2_E_COM_I_COM'
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
thetaSynMultiplier = numpy.array([0, 1, 1, 1, 1, 1, 1, 1, 1, 1])
prethetanoise = numpy.array([0.01])

tstop = h.tstop/1000
dt = h.dt

for x2 in range(0,1):
	if Examples[0][x2] == 0:
		print(ExampleStrings[x2].decode("utf-8") + ' is empty')
		continue
	for n in prethetanoise:
		for y in range(0,10):
			print('Simulating... ' + str(ExampleStrings[x2].decode("utf-8")) + ' #' + str(y+1))
			if y == 1:
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
			elif y == 2:
				EXCSLM = 1
				EXCSR = 2
				Inh90SR = 1
				Inh180SR = 1
				Inh270SR = 1
				Inh90SLM = 1
				Inh180SLM = 1
				Inh270SLM = 1
				EXC = 1
				INH = 1
			elif y == 3:
				EXCSLM = 2
				EXCSR = 1
				Inh90SR = 1
				Inh180SR = 1
				Inh270SR = 1
				Inh90SLM = 1
				Inh180SLM = 1
				Inh270SLM = 1
				EXC = 1
				INH = 1
			elif y == 4:
				EXCSLM = 1
				EXCSR = 1
				Inh90SR = 2
				Inh180SR = 1
				Inh270SR = 1
				Inh90SLM = 1
				Inh180SLM = 1
				Inh270SLM = 1
				EXC = 1
				INH = 1
			elif y == 5:
				EXCSLM = 1
				EXCSR = 1
				Inh90SR = 1
				Inh180SR = 2
				Inh270SR = 1
				Inh90SLM = 1
				Inh180SLM = 1
				Inh270SLM = 1
				EXC = 1
				INH = 1
			elif y == 6:
				EXCSLM = 1
				EXCSR = 1
				Inh90SR = 1
				Inh180SR = 1
				Inh270SR = 2
				Inh90SLM = 1
				Inh180SLM = 1
				Inh270SLM = 1
				EXC = 1
				INH = 1
			elif y == 7:
				EXCSLM = 1
				EXCSR = 1
				Inh90SR = 1
				Inh180SR = 1
				Inh270SR = 1
				Inh90SLM = 2
				Inh180SLM = 1
				Inh270SLM = 1
				EXC = 1
				INH = 1
			elif y == 8:
				EXCSLM = 1
				EXCSR = 1
				Inh90SR = 1
				Inh180SR = 1
				Inh270SR = 1
				Inh90SLM = 1
				Inh180SLM = 2
				Inh270SLM = 1
				EXC = 1
				INH = 1
			elif y == 9:
				EXCSLM = 1
				EXCSR = 1
				Inh90SR = 1
				Inh180SR = 1
				Inh270SR = 1
				Inh90SLM = 1
				Inh180SLM = 1
				Inh270SLM = 2
				EXC = 1
				INH = 1
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
				HC_Trace_CA3Removed = HC_Trace[10000:100001]
				HC_SpikeTimes_CA3Removed = numpy.zeros((len(HC_Trace),), dtype=numpy.float)
				for i in range(0,len(h.apctimes)): HC_SpikeTimes_CA3Removed[int(h.apctimes.x[i]/dt)] = h.apctimes.x[i]
				HC_SpikeTimes_CA3Removed = HC_SpikeTimes_CA3Removed[10000:100001]
				HC_SpikeTimes_CA3Removed2 = numpy.array(h.apctimes,dtype=numpy.float)
			elif y == 3:
				HC_Trace_EC3Removed = HC_Trace[10000:100001]
				HC_SpikeTimes_EC3Removed = numpy.zeros((len(HC_Trace),), dtype=numpy.float)
				for i in range(0,len(h.apctimes)): HC_SpikeTimes_EC3Removed[int(h.apctimes.x[i]/dt)] = h.apctimes.x[i]
				HC_SpikeTimes_EC3Removed = HC_SpikeTimes_EC3Removed[10000:100001]
				HC_SpikeTimes_EC3Removed2 = numpy.array(h.apctimes,dtype=numpy.float)
			elif y == 4:
				HC_Trace_SR90Removed = HC_Trace[10000:100001]
				HC_SpikeTimes_SR90Removed = numpy.zeros((len(HC_Trace),), dtype=numpy.float)
				for i in range(0,len(h.apctimes)): HC_SpikeTimes_SR90Removed[int(h.apctimes.x[i]/dt)] = h.apctimes.x[i]
				HC_SpikeTimes_SR90Removed = HC_SpikeTimes_SR90Removed[10000:100001]
				HC_SpikeTimes_SR90Removed2 = numpy.array(h.apctimes,dtype=numpy.float)
			elif y == 5:
				HC_Trace_SR180Removed = HC_Trace[10000:100001]
				HC_SpikeTimes_SR180Removed = numpy.zeros((len(HC_Trace),), dtype=numpy.float)
				for i in range(0,len(h.apctimes)): HC_SpikeTimes_SR180Removed[int(h.apctimes.x[i]/dt)] = h.apctimes.x[i]
				HC_SpikeTimes_SR180Removed = HC_SpikeTimes_SR180Removed[10000:100001]
				HC_SpikeTimes_SR180Removed2 = numpy.array(h.apctimes,dtype=numpy.float)
			elif y == 6:
				HC_Trace_SR270Removed = HC_Trace[10000:100001]
				HC_SpikeTimes_SR270Removed = numpy.zeros((len(HC_Trace),), dtype=numpy.float)
				for i in range(0,len(h.apctimes)): HC_SpikeTimes_SR270Removed[int(h.apctimes.x[i]/dt)] = h.apctimes.x[i]
				HC_SpikeTimes_SR270Removed = HC_SpikeTimes_SR270Removed[10000:100001]
				HC_SpikeTimes_SR270Removed2 = numpy.array(h.apctimes,dtype=numpy.float)
			elif y == 7:
				HC_Trace_SLM90Removed = HC_Trace[10000:100001]
				HC_SpikeTimes_SLM90Removed = numpy.zeros((len(HC_Trace),), dtype=numpy.float)
				for i in range(0,len(h.apctimes)): HC_SpikeTimes_SLM90Removed[int(h.apctimes.x[i]/dt)] = h.apctimes.x[i]
				HC_SpikeTimes_SLM90Removed = HC_SpikeTimes_SLM90Removed[10000:100001]
				HC_SpikeTimes_SLM90Removed2 = numpy.array(h.apctimes,dtype=numpy.float)
			elif y == 8:
				HC_Trace_SLM180Removed = HC_Trace[10000:100001]
				HC_SpikeTimes_SLM180Removed = numpy.zeros((len(HC_Trace),), dtype=numpy.float)
				for i in range(0,len(h.apctimes)): HC_SpikeTimes_SLM180Removed[int(h.apctimes.x[i]/dt)] = h.apctimes.x[i]
				HC_SpikeTimes_SLM180Removed = HC_SpikeTimes_SLM180Removed[10000:100001]
				HC_SpikeTimes_SLM180Removed2 = numpy.array(h.apctimes,dtype=numpy.float)
			elif y == 9:
				HC_Trace_SLM270Removed = HC_Trace[10000:100001]
				HC_SpikeTimes_SLM270Removed = numpy.zeros((len(HC_Trace),), dtype=numpy.float)
				for i in range(0,len(h.apctimes)): HC_SpikeTimes_SLM270Removed[int(h.apctimes.x[i]/dt)] = h.apctimes.x[i]
				HC_SpikeTimes_SLM270Removed = HC_SpikeTimes_SLM270Removed[10000:100001]
				HC_SpikeTimes_SLM270Removed2 = numpy.array(h.apctimes,dtype=numpy.float)
			
			timevec = numpy.arange(0,10000.1,0.1)
			if y == 0:
				f, axarr = matplotlib.pyplot.subplots(10, sharex=True)
				axarr[0].plot(timevec,voltvec,'lightblue',label='Base')
				axarr[0].set_ylim(-85,30)
				axarr[0].set_xlim(8000,10000)
				axarr[0].spines['right'].set_visible(False)
				axarr[0].spines['top'].set_visible(False)
				axarr[0].spines['bottom'].set_visible(False)
				for tic in axarr[0].xaxis.get_major_ticks():
					tic.tick1line.set_visible = tic.tick2line.set_visible = False
				leg = axarr[0].legend(loc="upper right", handlelength=0, handletextpad=0, fancybox=True)
				leg.get_frame().set_alpha(1)
				for item in leg.legendHandles:
					item.set_visible(False)
			if y == 1:
				axarr[1].plot(timevec,voltvec,'tomato',label='X1 Theta')
				axarr[1].set_ylim(-85,30)
				axarr[1].set_xlim(8000,10000)
				axarr[1].spines['right'].set_visible(False)
				axarr[1].spines['top'].set_visible(False)
				axarr[1].spines['bottom'].set_visible(False)
				for tic in axarr[1].xaxis.get_major_ticks():
					tic.tick1line.set_visible = tic.tick2line.set_visible = False
				leg = axarr[1].legend(loc="upper right", handlelength=0, handletextpad=0, fancybox=True)
				leg.get_frame().set_alpha(1)
				for item in leg.legendHandles:
					item.set_visible(False)
			if y == 2:
				axarr[2].plot(timevec,voltvec,'g',label=r'$2 \times$CA3')
				axarr[2].set_ylim(-85,30)
				axarr[2].set_xlim(8000,10000)
				axarr[2].spines['right'].set_visible(False)
				axarr[2].spines['top'].set_visible(False)
				axarr[2].spines['bottom'].set_visible(False)
				for tic in axarr[2].xaxis.get_major_ticks():
					tic.tick1line.set_visible = tic.tick2line.set_visible = False
				leg = axarr[2].legend(loc="upper right", handlelength=0, handletextpad=0, fancybox=True)
				leg.get_frame().set_alpha(1)
				for item in leg.legendHandles:
					item.set_visible(False)
			if y == 3:
				axarr[3].plot(timevec,voltvec,'c',label=r'$2 \times$EC3')
				axarr[3].set_ylim(-85,30)
				axarr[3].set_xlim(8000,10000)
				axarr[3].set_ylabel('Voltage (mV)         ',fontsize=font_size-2)
				axarr[3].spines['right'].set_visible(False)
				axarr[3].spines['top'].set_visible(False)
				axarr[3].spines['bottom'].set_visible(False)
				for tic in axarr[3].xaxis.get_major_ticks():
					tic.tick1line.set_visible = tic.tick2line.set_visible = False
				leg = axarr[3].legend(loc="upper right", handlelength=0, handletextpad=0, fancybox=True)
				leg.get_frame().set_alpha(1)
				for item in leg.legendHandles:
					item.set_visible(False)
			if y == 4:
				axarr[4].plot(timevec,voltvec,'m',label=r'$2 \times$SR90')
				axarr[4].set_ylim(-85,30)
				axarr[4].set_xlim(8000,10000)
				axarr[4].spines['right'].set_visible(False)
				axarr[4].spines['top'].set_visible(False)
				axarr[4].spines['bottom'].set_visible(False)
				for tic in axarr[4].xaxis.get_major_ticks():
					tic.tick1line.set_visible = tic.tick2line.set_visible = False
				leg = axarr[4].legend(loc="upper right", handlelength=0, handletextpad=0, fancybox=True)
				leg.get_frame().set_alpha(1)
				for item in leg.legendHandles:
					item.set_visible(False)
			if y == 5:
				axarr[5].plot(timevec,voltvec,'y',label=r'$2 \times$SR180')
				axarr[5].set_ylim(-85,30)
				axarr[5].set_xlim(8000,10000)
				axarr[5].spines['right'].set_visible(False)
				axarr[5].spines['top'].set_visible(False)
				axarr[5].spines['bottom'].set_visible(False)
				for tic in axarr[5].xaxis.get_major_ticks():
					tic.tick1line.set_visible = tic.tick2line.set_visible = False
				leg = axarr[5].legend(loc="upper right", handlelength=0, handletextpad=0, fancybox=True)
				leg.get_frame().set_alpha(1)
				for item in leg.legendHandles:
					item.set_visible(False)
			if y == 6:
				axarr[6].plot(timevec,voltvec,'b',label=r'$2 \times$SR270')
				axarr[6].set_ylim(-85,30)
				axarr[6].set_xlim(8000,10000)
				axarr[6].spines['right'].set_visible(False)
				axarr[6].spines['top'].set_visible(False)
				axarr[6].spines['bottom'].set_visible(False)
				for tic in axarr[6].xaxis.get_major_ticks():
					tic.tick1line.set_visible = tic.tick2line.set_visible = False
				leg = axarr[6].legend(loc="upper right", handlelength=0, handletextpad=0, fancybox=True)
				leg.get_frame().set_alpha(1)
				for item in leg.legendHandles:
					item.set_visible(False)
			if y == 7:
				axarr[7].plot(timevec,voltvec,'k',label=r'$2 \times$SLM90')
				axarr[7].set_ylim(-85,30)
				axarr[7].set_xlim(8000,10000)
				axarr[7].spines['right'].set_visible(False)
				axarr[7].spines['top'].set_visible(False)
				axarr[7].spines['bottom'].set_visible(False)
				for tic in axarr[7].xaxis.get_major_ticks():
					tic.tick1line.set_visible = tic.tick2line.set_visible = False
				leg = axarr[7].legend(loc="upper right", handlelength=0, handletextpad=0, fancybox=True)
				leg.get_frame().set_alpha(1)
				for item in leg.legendHandles:
					item.set_visible(False)
			if y == 8:
				axarr[8].plot(timevec,voltvec,'orange',label=r'$2 \times$SLM180')
				axarr[8].set_ylim(-85,30)
				axarr[8].set_xlim(8000,10000)
				axarr[8].spines['right'].set_visible(False)
				axarr[8].spines['top'].set_visible(False)
				axarr[8].spines['bottom'].set_visible(False)
				for tic in axarr[8].xaxis.get_major_ticks():
					tic.tick1line.set_visible = tic.tick2line.set_visible = False
				leg = axarr[8].legend(loc="upper right", handlelength=0, handletextpad=0, fancybox=True)
				leg.get_frame().set_alpha(1)
				for item in leg.legendHandles:
					item.set_visible(False)
			if y == 9:
				axarr[9].plot(timevec,voltvec,'r',label=r'$2 \times$SLM270')
				axarr[9].set_ylim(-85,30)
				axarr[9].set_xlim(8000,10000)
				axarr[9].set_xlabel('Time (ms)',fontsize=font_size-2)
				axarr[9].spines['right'].set_visible(False)
				axarr[9].spines['top'].set_visible(False)
				leg = axarr[9].legend(loc="upper right", handlelength=0, handletextpad=0, fancybox=True)
				leg.get_frame().set_alpha(1)
				for item in leg.legendHandles:
					item.set_visible(False)
				
				pyplot.savefig('PLOTfiles/' + Case + '_Trace_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.pdf', bbox_inches='tight')
				pyplot.savefig('PLOTfiles/' + Case + '_Trace_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.png', bbox_inches='tight')
				pyplot.gcf().clear()
				pyplot.cla()
				pyplot.clf()
				pyplot.close()
		f, axarr = matplotlib.pyplot.subplots(2, sharex=False)
		f1, Pxx_den1 = signal.welch(HC_SpikeTimes_Baseline, 1/(dt/1000), nperseg=25000)
		f2, Pxx_den2 = signal.welch(HC_SpikeTimes_Rhythm, 1/(dt/1000), nperseg=25000)
		f3, Pxx_den3 = signal.welch(HC_SpikeTimes_CA3Removed, 1/(dt/1000), nperseg=25000)
		f4, Pxx_den4 = signal.welch(HC_SpikeTimes_EC3Removed, 1/(dt/1000), nperseg=25000)
		f5, Pxx_den5 = signal.welch(HC_SpikeTimes_SR90Removed, 1/(dt/1000), nperseg=25000)
		f6, Pxx_den6 = signal.welch(HC_SpikeTimes_SR180Removed, 1/(dt/1000), nperseg=25000)
		f7, Pxx_den7 = signal.welch(HC_SpikeTimes_SR270Removed, 1/(dt/1000), nperseg=25000)
		f8, Pxx_den8 = signal.welch(HC_SpikeTimes_SLM90Removed, 1/(dt/1000), nperseg=25000)
		f9, Pxx_den9 = signal.welch(HC_SpikeTimes_SLM180Removed, 1/(dt/1000), nperseg=25000)
		f10, Pxx_den10 = signal.welch(HC_SpikeTimes_SLM270Removed, 1/(dt/1000), nperseg=25000)
		numpy.save('NPYfiles/' + Case + '_SpikeTimesBaseline_' + str(HCNumber) + '_HCNumber_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.npy',HC_SpikeTimes_Baseline2)
		numpy.save('NPYfiles/' + Case + '_SpikeTimesRhythm_' + str(HCNumber) + '_HCNumber_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.npy',HC_SpikeTimes_Rhythm2)
		numpy.save('NPYfiles/' + Case + '_SpikeTimesRhythm_' + str(HCNumber) + '_HCNumber_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.npy',HC_SpikeTimes_CA3Removed2)
		numpy.save('NPYfiles/' + Case + '_SpikeTimesRhythm_' + str(HCNumber) + '_HCNumber_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.npy',HC_SpikeTimes_EC3Removed2)
		numpy.save('NPYfiles/' + Case + '_SpikeTimesRhythm_' + str(HCNumber) + '_HCNumber_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.npy',HC_SpikeTimes_SR90Removed2)
		numpy.save('NPYfiles/' + Case + '_SpikeTimesRhythm_' + str(HCNumber) + '_HCNumber_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.npy',HC_SpikeTimes_SR180Removed2)
		numpy.save('NPYfiles/' + Case + '_SpikeTimesRhythm_' + str(HCNumber) + '_HCNumber_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.npy',HC_SpikeTimes_SR270Removed2)
		numpy.save('NPYfiles/' + Case + '_SpikeTimesRhythm_' + str(HCNumber) + '_HCNumber_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.npy',HC_SpikeTimes_SLM90Removed2)
		numpy.save('NPYfiles/' + Case + '_SpikeTimesRhythm_' + str(HCNumber) + '_HCNumber_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.npy',HC_SpikeTimes_SLM180Removed2)
		numpy.save('NPYfiles/' + Case + '_SpikeTimesRhythm_' + str(HCNumber) + '_HCNumber_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.npy',HC_SpikeTimes_SLM270Removed2)
		axarr[0].loglog(f1, Pxx_den1,color='lightblue')
		axarr[0].loglog(f2, Pxx_den2,color='tomato')
		axarr[0].loglog(f3, Pxx_den3,'g')
		axarr[0].loglog(f4, Pxx_den4,'c')
		axarr[0].loglog(f5, Pxx_den5,'m')
		axarr[0].loglog(f6, Pxx_den6,'y')
		axarr[0].loglog(f7, Pxx_den7,'b')
		axarr[0].loglog(f8, Pxx_den8,'k')
		axarr[0].loglog(f9, Pxx_den9,color='orange')
		axarr[0].loglog(f10, Pxx_den10,'r')
		axarr[0].hlines(numpy.amax(Pxx_den2)+500,5,12,'k',linestyles='solid')
		axarr[0].text(5.05,numpy.amax(Pxx_den2)+1000,'Theta (5-12Hz)')
		axarr[0].axvline(numpy.array([5]),ymin=0,ymax=0.95,color='k',linestyle='solid')
		axarr[0].axvline(numpy.array([12]),ymin=0,ymax=0.95,color='k',linestyle='solid')
		axarr[0].axvline(numpy.array([8]),ymin=0,ymax=0.95,color='k',linestyle='dashed')
		axarr[0].set_xlim(0,100)
		axarr[0].set_xlabel('frequency (Hz)')
		axarr[0].set_ylabel(r'$PSD (Spikes^2 / Hz)$')
		axarr[0].spines['right'].set_visible(False)
		axarr[0].spines['top'].set_visible(False)
		
		ind = numpy.arange(10)
		width = 0.4
		Area1 = numpy.trapz(Pxx_den1[(f1>5) & (f1<12)],x=f1[(f1>5) & (f1<12)])
		Area2 = numpy.trapz(Pxx_den2[(f2>5) & (f2<12)],x=f2[(f2>5) & (f2<12)])
		Area3 = numpy.trapz(Pxx_den3[(f3>5) & (f3<12)],x=f3[(f3>5) & (f3<12)])
		Area4 = numpy.trapz(Pxx_den4[(f4>5) & (f4<12)],x=f4[(f4>5) & (f4<12)])
		Area5 = numpy.trapz(Pxx_den5[(f5>5) & (f5<12)],x=f5[(f5>5) & (f5<12)])
		Area6 = numpy.trapz(Pxx_den6[(f6>5) & (f6<12)],x=f6[(f6>5) & (f6<12)])
		Area7 = numpy.trapz(Pxx_den7[(f7>5) & (f7<12)],x=f7[(f7>5) & (f7<12)])
		Area8 = numpy.trapz(Pxx_den8[(f8>5) & (f8<12)],x=f8[(f8>5) & (f8<12)])
		Area9 = numpy.trapz(Pxx_den9[(f9>5) & (f9<12)],x=f9[(f9>5) & (f9<12)])
		Area10 = numpy.trapz(Pxx_den8[(f10>5) & (f10<12)],x=f10[(f10>5) & (f10<12)])
		e8Hz1 = Pxx_den1[f1==8]
		e8Hz2 = Pxx_den2[f2==8]
		e8Hz3 = Pxx_den3[f3==8]
		e8Hz4 = Pxx_den4[f4==8]
		e8Hz5 = Pxx_den5[f5==8]
		e8Hz6 = Pxx_den6[f6==8]
		e8Hz7 = Pxx_den7[f7==8]
		e8Hz8 = Pxx_den8[f8==8]
		e8Hz9 = Pxx_den9[f9==8]
		e8Hz10 = Pxx_den10[f10==8]
		axarr[1].bar(ind+width, [e8Hz1[0], e8Hz2[0], e8Hz3[0], e8Hz4[0], e8Hz5[0], e8Hz6[0], e8Hz7[0], e8Hz8[0], e8Hz9[0], e8Hz10[0]], width, color='k')
		axarr[1].set_xticks(ind+width)
		axarr[1].set_xticklabels(('Base','X1 Theta',r'$2 \times$CA3',r'$2 \times$EC3',r'$2 \times$SR90',r'$2 \times$SR180',r'$2 \times$SR270',r'$2 \times$SLM90',r'$2 \times$SLM180',r'$2 \times$SLM270'),fontsize=font_size-3, fontweight='bold', rotation=45)
		axarr[1].set_ylabel('PSD Magnitude At 8Hz')
		axarr[1].set_xlim(0,10+width)
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
		IF_CA3Removed = numpy.concatenate([numpy.array([0],dtype=numpy.float),1000/numpy.diff(HC_SpikeTimes_CA3Removed2)])
		IF_EC3Removed = numpy.concatenate([numpy.array([0],dtype=numpy.float),1000/numpy.diff(HC_SpikeTimes_EC3Removed2)])
		IF_SR90Removed = numpy.concatenate([numpy.array([0],dtype=numpy.float),1000/numpy.diff(HC_SpikeTimes_SR90Removed2)])
		IF_SR180Removed = numpy.concatenate([numpy.array([0],dtype=numpy.float),1000/numpy.diff(HC_SpikeTimes_SR180Removed2)])
		IF_SR270Removed = numpy.concatenate([numpy.array([0],dtype=numpy.float),1000/numpy.diff(HC_SpikeTimes_SR270Removed2)])
		IF_SLM90Removed = numpy.concatenate([numpy.array([0],dtype=numpy.float),1000/numpy.diff(HC_SpikeTimes_SLM90Removed2)])
		IF_SLM180Removed = numpy.concatenate([numpy.array([0],dtype=numpy.float),1000/numpy.diff(HC_SpikeTimes_SLM180Removed2)])
		IF_SLM270Removed = numpy.concatenate([numpy.array([0],dtype=numpy.float),1000/numpy.diff(HC_SpikeTimes_SLM270Removed2)])
		
		range_if = (0,100)
		heights1,bins1 = numpy.histogram(IF_Baseline,bins=100,range=range_if)
		heights2,bins2 = numpy.histogram(IF_ThetaX1,bins=100,range=range_if)
		heights3,bins3 = numpy.histogram(IF_CA3Removed,bins=100,range=range_if)
		heights4,bins4 = numpy.histogram(IF_EC3Removed,bins=100,range=range_if)
		heights5,bins5 = numpy.histogram(IF_SR90Removed,bins=100,range=range_if)
		heights6,bins6 = numpy.histogram(IF_SR180Removed,bins=100,range=range_if)
		heights7,bins7 = numpy.histogram(IF_SR270Removed,bins=100,range=range_if)
		heights8,bins8 = numpy.histogram(IF_SLM90Removed,bins=100,range=range_if)
		heights9,bins9 = numpy.histogram(IF_SLM180Removed,bins=100,range=range_if)
		heights10,bins10 = numpy.histogram(IF_SLM270Removed,bins=100,range=range_if)
		
		# Normalize
		heights1 = heights1/float(sum(heights1))
		heights2 = heights2/float(sum(heights2))
		heights3 = heights3/float(sum(heights3))
		heights4 = heights4/float(sum(heights4))
		heights5 = heights5/float(sum(heights5))
		heights6 = heights6/float(sum(heights6))
		heights7 = heights7/float(sum(heights7))
		heights8 = heights8/float(sum(heights8))
		heights9 = heights9/float(sum(heights9))
		heights10 = heights10/float(sum(heights10))
		bin1=bins1[:-1]+numpy.diff(bins1)/2.
		bin2=bins2[:-1]+numpy.diff(bins2)/2.
		bin3=bins3[:-1]+numpy.diff(bins3)/2.
		bin4=bins4[:-1]+numpy.diff(bins4)/2.
		bin5=bins5[:-1]+numpy.diff(bins5)/2.
		bin6=bins6[:-1]+numpy.diff(bins6)/2.
		bin7=bins7[:-1]+numpy.diff(bins7)/2.
		bin8=bins8[:-1]+numpy.diff(bins8)/2.
		bin9=bins9[:-1]+numpy.diff(bins9)/2.
		bin10=bins10[:-1]+numpy.diff(bins10)/2.
		binMids1 = bin1[~numpy.isnan(bin1)]
		binMids2 = bin2[~numpy.isnan(bin2)]
		binMids3 = bin3[~numpy.isnan(bin3)]
		binMids4 = bin4[~numpy.isnan(bin4)]
		binMids5 = bin5[~numpy.isnan(bin5)]
		binMids6 = bin6[~numpy.isnan(bin6)]
		binMids7 = bin7[~numpy.isnan(bin7)]
		binMids8 = bin8[~numpy.isnan(bin8)]
		binMids9 = bin9[~numpy.isnan(bin9)]
		binMids10 = bin10[~numpy.isnan(bin10)]
		heights1 = heights1[~numpy.isnan(bin1)]
		heights2 = heights2[~numpy.isnan(bin2)]
		heights3 = heights3[~numpy.isnan(bin3)]
		heights4 = heights4[~numpy.isnan(bin4)]
		heights5 = heights5[~numpy.isnan(bin5)]
		heights6 = heights6[~numpy.isnan(bin6)]
		heights7 = heights7[~numpy.isnan(bin7)]
		heights8 = heights8[~numpy.isnan(bin8)]
		heights9 = heights9[~numpy.isnan(bin9)]
		heights10 = heights10[~numpy.isnan(bin10)]
		
		f, axarr = matplotlib.pyplot.subplots(2, sharex=False)
		axarr[0].semilogx(binMids1,heights1,color='lightblue')
		axarr[0].semilogx(binMids2,heights2,color='tomato')
		axarr[0].semilogx(binMids3,heights3,'g')
		axarr[0].semilogx(binMids4,heights4,'c')
		axarr[0].semilogx(binMids5,heights5,'m')
		axarr[0].semilogx(binMids6,heights6,'y')
		axarr[0].semilogx(binMids7,heights7,'b')
		axarr[0].semilogx(binMids8,heights8,'k')
		axarr[0].semilogx(binMids9,heights9,color='orange')
		axarr[0].semilogx(binMids10,heights10,'r')
		axarr[0].vlines(numpy.array([4,12]),0,numpy.amax(heights2)+0.01,'k',linestyles='solid')
		axarr[0].vlines(numpy.array([8]),0,numpy.amax(heights2)+0.01,'k',linestyles='dashed')
		axarr[0].hlines(numpy.amax(heights2)+0.01,4,12,'k',linestyles='solid')
		axarr[0].text(4.3,numpy.amax(heights2)+0.02,'Theta (4-12Hz)')
		axarr[0].set_xlabel('Frequency (Hz)')
		axarr[0].set_ylabel('Probability')
		axarr[0].set_xlim(0,130)
		axarr[0].set_ylim(0,0.19)
		axarr[0].spines['right'].set_visible(False)
		axarr[0].spines['top'].set_visible(False)
		
		ind = numpy.arange(10)
		width = 0.4
		Area11 = numpy.trapz(heights1[(binMids1>4) & (binMids1<8)],x=binMids1[(binMids1>4) & (binMids1<8)])
		Area22 = numpy.trapz(heights2[(binMids2>4) & (binMids2<8)],x=binMids2[(binMids2>4) & (binMids2<8)])
		Area33 = numpy.trapz(heights3[(binMids3>4) & (binMids3<8)],x=binMids3[(binMids3>4) & (binMids3<8)])
		Area44 = numpy.trapz(heights4[(binMids4>4) & (binMids4<8)],x=binMids4[(binMids4>4) & (binMids4<8)])
		Area55 = numpy.trapz(heights5[(binMids5>4) & (binMids5<8)],x=binMids5[(binMids5>4) & (binMids5<8)])
		Area66 = numpy.trapz(heights6[(binMids6>4) & (binMids6<8)],x=binMids6[(binMids6>4) & (binMids6<8)])
		Area77 = numpy.trapz(heights7[(binMids7>4) & (binMids7<8)],x=binMids7[(binMids7>4) & (binMids7<8)])
		Area88 = numpy.trapz(heights8[(binMids8>4) & (binMids8<8)],x=binMids8[(binMids8>4) & (binMids8<8)])
		Area99 = numpy.trapz(heights9[(binMids9>4) & (binMids9<8)],x=binMids9[(binMids9>4) & (binMids9<8)])
		Area1010 = numpy.trapz(heights10[(binMids10>4) & (binMids10<8)],x=binMids10[(binMids10>4) & (binMids10<8)])
		e8Hz11 = numpy.trapz(heights1[(binMids1>8) & (binMids1<12)],x=binMids1[(binMids1>8) & (binMids1<12)]) #IF NOT THIS TRY NUMPY.AMAX BETWEEN 7 AND 9
		e8Hz22 = numpy.trapz(heights2[(binMids2>8) & (binMids2<12)],x=binMids2[(binMids2>8) & (binMids2<12)])
		e8Hz33 = numpy.trapz(heights3[(binMids3>8) & (binMids3<12)],x=binMids3[(binMids3>8) & (binMids3<12)])
		e8Hz44 = numpy.trapz(heights4[(binMids4>8) & (binMids4<12)],x=binMids4[(binMids4>8) & (binMids4<12)])
		e8Hz55 = numpy.trapz(heights5[(binMids5>8) & (binMids5<12)],x=binMids5[(binMids5>8) & (binMids5<12)])
		e8Hz66 = numpy.trapz(heights6[(binMids6>8) & (binMids6<12)],x=binMids6[(binMids6>8) & (binMids6<12)])
		e8Hz77 = numpy.trapz(heights7[(binMids7>8) & (binMids7<12)],x=binMids7[(binMids7>8) & (binMids7<12)])
		e8Hz88 = numpy.trapz(heights8[(binMids8>8) & (binMids8<12)],x=binMids8[(binMids8>8) & (binMids8<12)])
		e8Hz99 = numpy.trapz(heights9[(binMids9>8) & (binMids9<12)],x=binMids9[(binMids9>8) & (binMids9<12)])
		e8Hz1010 = numpy.trapz(heights10[(binMids10>8) & (binMids10<12)],x=binMids10[(binMids10>8) & (binMids10<12)])
		axarr[1].bar(ind+width, [e8Hz11, e8Hz22, e8Hz33, e8Hz44, e8Hz55, e8Hz66, e8Hz77, e8Hz88, e8Hz99, e8Hz1010], width, color='k')
		axarr[1].set_xticks(ind+width)
		axarr[1].set_xticklabels(('Base','X1 Theta',r'$2 \times$CA3',r'$2 \times$EC3',r'$2 \times$SR90',r'$2 \times$SR180',r'$2 \times$SR270',r'$2 \times$SLM90',r'$2 \times$SLM180',r'$2 \times$SLM270'),fontsize=font_size-3, fontweight='bold', rotation=45)
		axarr[1].set_ylabel('Probability At 8-12Hz')
		axarr[1].set_xlim(0,10+width)
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
		STX2 = HC_SpikeTimes_CA3Removed2/125
		STX3 = HC_SpikeTimes_EC3Removed2/125
		STX4 = HC_SpikeTimes_SR90Removed2/125
		STX5 = HC_SpikeTimes_SR180Removed2/125
		STX6 = HC_SpikeTimes_SR270Removed2/125
		STX7 = HC_SpikeTimes_SLM90Removed2/125
		STX8 = HC_SpikeTimes_SLM180Removed2/125
		STX9 = HC_SpikeTimes_SLM270Removed2/125
		Rads_Baseline = 2*numpy.pi*(STX0-STX0.astype(int))
		Rads_1XRhythm = 2*numpy.pi*(STX1-STX1.astype(int))
		Rads_CA3Removed = 2*numpy.pi*(STX2-STX2.astype(int))
		Rads_EC3Removed = 2*numpy.pi*(STX3-STX3.astype(int))
		Rads_SR90Removed = 2*numpy.pi*(STX4-STX4.astype(int))
		Rads_SR180Removed = 2*numpy.pi*(STX5-STX5.astype(int))
		Rads_SR270Removed = 2*numpy.pi*(STX6-STX6.astype(int))
		Rads_SLM90Removed = 2*numpy.pi*(STX7-STX7.astype(int))
		Rads_SLM180Removed = 2*numpy.pi*(STX8-STX8.astype(int))
		Rads_SLM270Removed = 2*numpy.pi*(STX9-STX9.astype(int))
		
		bin_size = 25
		range_if = (0,100)
		range_rads = (0,2*numpy.pi)
		
		heights11,be11 = numpy.histogram(Rads_Baseline,bins=bin_size,range=range_rads)
		bins11 = be11[:-1]+numpy.diff(be11)/2.
		PrefPhase_Baseline = bins11[heights11 == numpy.amax(heights11)]
		heights22,be22 = numpy.histogram(Rads_1XRhythm,bins=bin_size,range=range_rads)
		bins22 = be22[:-1]+numpy.diff(be22)/2.
		PrefPhase_ThetaX1 = bins22[heights22 == numpy.amax(heights22)]
		heights33,be33 = numpy.histogram(Rads_CA3Removed,bins=bin_size,range=range_rads)
		bins33 = be33[:-1]+numpy.diff(be33)/2.
		PrefPhase_CA3Removed = bins33[heights33 == numpy.amax(heights33)]
		heights44,be44 = numpy.histogram(Rads_EC3Removed,bins=bin_size,range=range_rads)
		bins44 = be44[:-1]+numpy.diff(be44)/2.
		PrefPhase_EC3Removed = bins44[heights44 == numpy.amax(heights44)]
		heights55,be55 = numpy.histogram(Rads_SR90Removed,bins=bin_size,range=range_rads)
		bins55 = be55[:-1]+numpy.diff(be55)/2.
		PrefPhase_SR90Removed = bins55[heights55 == numpy.amax(heights55)]
		heights66,be66 = numpy.histogram(Rads_SR180Removed,bins=bin_size,range=range_rads)
		bins66 = be66[:-1]+numpy.diff(be66)/2.
		PrefPhase_SR180Removed = bins66[heights66 == numpy.amax(heights66)]
		heights77,be77 = numpy.histogram(Rads_SR270Removed,bins=bin_size,range=range_rads)
		bins77 = be77[:-1]+numpy.diff(be77)/2.
		PrefPhase_SR270Removed = bins77[heights77 == numpy.amax(heights77)]
		heights88,be88 = numpy.histogram(Rads_SLM90Removed,bins=bin_size,range=range_rads)
		bins88 = be88[:-1]+numpy.diff(be88)/2.
		PrefPhase_SLM90Removed = bins88[heights88 == numpy.amax(heights88)]
		heights99,be99 = numpy.histogram(Rads_SLM180Removed,bins=bin_size,range=range_rads)
		bins99 = be99[:-1]+numpy.diff(be99)/2.
		PrefPhase_SLM180Removed = bins99[heights99 == numpy.amax(heights99)]
		heights1010,be1010 = numpy.histogram(Rads_SLM270Removed,bins=bin_size,range=range_rads)
		bins1010 = be1010[:-1]+numpy.diff(be1010)/2.
		PrefPhase_SLM270Removed = bins88[heights1010 == numpy.amax(heights1010)]
		
		Rads_Baseline_Sorted = sorted(Rads_Baseline)
		Rads_1XRhythm_Sorted = sorted(Rads_1XRhythm)
		Rads_CA3Removed_Sorted = sorted(Rads_CA3Removed)
		Rads_EC3Removed_Sorted = sorted(Rads_EC3Removed)
		Rads_SR90Removed_Sorted = sorted(Rads_SR90Removed)
		Rads_SR180Removed_Sorted = sorted(Rads_SR180Removed)
		Rads_SR270Removed_Sorted = sorted(Rads_SR270Removed)
		Rads_SLM90Removed_Sorted = sorted(Rads_SLM90Removed)
		Rads_SLM180Removed_Sorted = sorted(Rads_SLM180Removed)
		Rads_SLM270Removed_Sorted = sorted(Rads_SLM270Removed)
		
		IF_Baseline_Sorted = [x for i, x in sorted(zip(Rads_Baseline,IF_Baseline))]
		IF_ThetaX1_Sorted = [x for i, x in sorted(zip(Rads_1XRhythm,IF_ThetaX1))]
		IF_CA3Removed_Sorted = [x for i, x in sorted(zip(Rads_CA3Removed,IF_CA3Removed))]
		IF_EC3Removed_Sorted = [x for i, x in sorted(zip(Rads_EC3Removed,IF_EC3Removed))]
		IF_SR90Removed_Sorted = [x for i, x in sorted(zip(Rads_SR90Removed,IF_SR90Removed))]
		IF_SR180Removed_Sorted = [x for i, x in sorted(zip(Rads_SR180Removed,IF_SR180Removed))]
		IF_SR270Removed_Sorted = [x for i, x in sorted(zip(Rads_SR270Removed,IF_SR270Removed))]
		IF_SLM90Removed_Sorted = [x for i, x in sorted(zip(Rads_SLM90Removed,IF_SLM90Removed))]
		IF_SLM180Removed_Sorted = [x for i, x in sorted(zip(Rads_SLM180Removed,IF_SLM180Removed))]
		IF_SLM270Removed_Sorted = [x for i, x in sorted(zip(Rads_SLM270Removed,IF_SLM270Removed))]
		
		Rads_Baseline_MeanBins,be11,bn11 = scipy.stats.binned_statistic(Rads_Baseline_Sorted,Rads_Baseline_Sorted,statistic='mean',bins=bin_size,range=range_rads)
		_BMeans = Rads_Baseline_MeanBins
		Rads_Baseline_MeanBins = Rads_Baseline_MeanBins[~numpy.isnan(Rads_Baseline_MeanBins)]
		Rads_Baseline_MeanBins = numpy.append(Rads_Baseline_MeanBins,Rads_Baseline_MeanBins[0])
		Rads_1XRhythm_MeanBins,be21,bn21 = scipy.stats.binned_statistic(Rads_1XRhythm_Sorted,Rads_1XRhythm_Sorted,statistic='mean',bins=bin_size,range=range_rads)
		_1Means = Rads_1XRhythm_MeanBins
		Rads_1XRhythm_MeanBins = Rads_1XRhythm_MeanBins[~numpy.isnan(Rads_1XRhythm_MeanBins)]
		Rads_1XRhythm_MeanBins = numpy.append(Rads_1XRhythm_MeanBins,Rads_1XRhythm_MeanBins[0])
		Rads_CA3Removed_MeanBins,be31,bn31 = scipy.stats.binned_statistic(Rads_CA3Removed_Sorted,Rads_CA3Removed_Sorted,statistic='mean',bins=bin_size,range=range_rads)
		_2Means = Rads_CA3Removed_MeanBins
		Rads_CA3Removed_MeanBins = Rads_CA3Removed_MeanBins[~numpy.isnan(Rads_CA3Removed_MeanBins)]
		Rads_CA3Removed_MeanBins = numpy.append(Rads_CA3Removed_MeanBins,Rads_CA3Removed_MeanBins[0])
		Rads_EC3Removed_MeanBins,be41,bn41 = scipy.stats.binned_statistic(Rads_EC3Removed_Sorted,Rads_EC3Removed_Sorted,statistic='mean',bins=bin_size,range=range_rads)
		_3Means = Rads_EC3Removed_MeanBins
		Rads_EC3Removed_MeanBins = Rads_EC3Removed_MeanBins[~numpy.isnan(Rads_EC3Removed_MeanBins)]
		Rads_EC3Removed_MeanBins = numpy.append(Rads_EC3Removed_MeanBins,Rads_EC3Removed_MeanBins[0])
		Rads_SR90Removed_MeanBins,be51,bn51 = scipy.stats.binned_statistic(Rads_SR90Removed_Sorted,Rads_SR90Removed_Sorted,statistic='mean',bins=bin_size,range=range_rads)
		_4Means = Rads_SR90Removed_MeanBins
		Rads_SR90Removed_MeanBins = Rads_SR90Removed_MeanBins[~numpy.isnan(Rads_SR90Removed_MeanBins)]
		Rads_SR90Removed_MeanBins = numpy.append(Rads_SR90Removed_MeanBins,Rads_SR90Removed_MeanBins[0])
		Rads_SR180Removed_MeanBins,be61,bn61 = scipy.stats.binned_statistic(Rads_SR180Removed_Sorted,Rads_SR180Removed_Sorted,statistic='mean',bins=bin_size,range=range_rads)
		_5Means = Rads_SR180Removed_MeanBins
		Rads_SR180Removed_MeanBins = Rads_SR180Removed_MeanBins[~numpy.isnan(Rads_SR180Removed_MeanBins)]
		Rads_SR180Removed_MeanBins = numpy.append(Rads_SR180Removed_MeanBins,Rads_SR180Removed_MeanBins[0])
		Rads_SR270Removed_MeanBins,be71,bn71 = scipy.stats.binned_statistic(Rads_SR270Removed_Sorted,Rads_SR270Removed_Sorted,statistic='mean',bins=bin_size,range=range_rads)
		_6Means = Rads_SR270Removed_MeanBins
		Rads_SR270Removed_MeanBins = Rads_SR270Removed_MeanBins[~numpy.isnan(Rads_SR270Removed_MeanBins)]
		Rads_SR270Removed_MeanBins = numpy.append(Rads_SR270Removed_MeanBins,Rads_SR270Removed_MeanBins[0])
		Rads_SLM90Removed_MeanBins,be81,bn81 = scipy.stats.binned_statistic(Rads_SLM90Removed_Sorted,Rads_SLM90Removed_Sorted,statistic='mean',bins=bin_size,range=range_rads)
		_7Means = Rads_SLM90Removed_MeanBins
		Rads_SLM90Removed_MeanBins = Rads_SLM90Removed_MeanBins[~numpy.isnan(Rads_SLM90Removed_MeanBins)]
		Rads_SLM90Removed_MeanBins = numpy.append(Rads_SLM90Removed_MeanBins,Rads_SLM90Removed_MeanBins[0])
		Rads_SLM180Removed_MeanBins,be91,bn91 = scipy.stats.binned_statistic(Rads_SLM180Removed_Sorted,Rads_SLM180Removed_Sorted,statistic='mean',bins=bin_size,range=range_rads)
		_8Means = Rads_SLM180Removed_MeanBins
		Rads_SLM180Removed_MeanBins = Rads_SLM180Removed_MeanBins[~numpy.isnan(Rads_SLM180Removed_MeanBins)]
		Rads_SLM180Removed_MeanBins = numpy.append(Rads_SLM180Removed_MeanBins,Rads_SLM180Removed_MeanBins[0])
		Rads_SLM270Removed_MeanBins,be101,bn101 = scipy.stats.binned_statistic(Rads_SLM270Removed_Sorted,Rads_SLM270Removed_Sorted,statistic='mean',bins=bin_size,range=range_rads)
		_9Means = Rads_SLM270Removed_MeanBins
		Rads_SLM270Removed_MeanBins = Rads_SLM270Removed_MeanBins[~numpy.isnan(Rads_SLM270Removed_MeanBins)]
		Rads_SLM270Removed_MeanBins = numpy.append(Rads_SLM270Removed_MeanBins,Rads_SLM270Removed_MeanBins[0])
		
		IF_Baseline_MeanBins,be12,bn12 = scipy.stats.binned_statistic(Rads_Baseline_Sorted,IF_Baseline_Sorted,statistic='mean',bins=bin_size,range=range_rads)
		IF_Baseline_MeanBins = IF_Baseline_MeanBins[~numpy.isnan(_BMeans)]
		IF_Baseline_MeanBins = numpy.append(IF_Baseline_MeanBins,IF_Baseline_MeanBins[0])
		IF_1XRhythm_MeanBins,be22,bn22 = scipy.stats.binned_statistic(Rads_1XRhythm_Sorted,IF_ThetaX1_Sorted,statistic='mean',bins=bin_size,range=range_rads)
		IF_1XRhythm_MeanBins = IF_1XRhythm_MeanBins[~numpy.isnan(_1Means)]
		IF_1XRhythm_MeanBins = numpy.append(IF_1XRhythm_MeanBins,IF_1XRhythm_MeanBins[0])
		IF_CA3Removed_MeanBins,be32,bn32 = scipy.stats.binned_statistic(Rads_CA3Removed_Sorted,IF_CA3Removed_Sorted,statistic='mean',bins=bin_size,range=range_rads)
		IF_CA3Removed_MeanBins = IF_CA3Removed_MeanBins[~numpy.isnan(_2Means)]
		IF_CA3Removed_MeanBins = numpy.append(IF_CA3Removed_MeanBins,IF_CA3Removed_MeanBins[0])
		IF_EC3Removed_MeanBins,be42,bn42 = scipy.stats.binned_statistic(Rads_EC3Removed_Sorted,IF_EC3Removed_Sorted,statistic='mean',bins=bin_size,range=range_rads)
		IF_EC3Removed_MeanBins = IF_EC3Removed_MeanBins[~numpy.isnan(_3Means)]
		IF_EC3Removed_MeanBins = numpy.append(IF_EC3Removed_MeanBins,IF_EC3Removed_MeanBins[0])
		IF_SR90Removed_MeanBins,be52,bn52 = scipy.stats.binned_statistic(Rads_SR90Removed_Sorted,IF_SR90Removed_Sorted,statistic='mean',bins=bin_size,range=range_rads)
		IF_SR90Removed_MeanBins = IF_SR90Removed_MeanBins[~numpy.isnan(_4Means)]
		IF_SR90Removed_MeanBins = numpy.append(IF_SR90Removed_MeanBins,IF_SR90Removed_MeanBins[0])
		IF_SR180Removed_MeanBins,be62,bn62 = scipy.stats.binned_statistic(Rads_SR180Removed_Sorted,IF_SR180Removed_Sorted,statistic='mean',bins=bin_size,range=range_rads)
		IF_SR180Removed_MeanBins = IF_SR180Removed_MeanBins[~numpy.isnan(_5Means)]
		IF_SR180Removed_MeanBins = numpy.append(IF_SR180Removed_MeanBins,IF_SR180Removed_MeanBins[0])
		IF_SR270Removed_MeanBins,be72,bn72 = scipy.stats.binned_statistic(Rads_SR270Removed_Sorted,IF_SR270Removed_Sorted,statistic='mean',bins=bin_size,range=range_rads)
		IF_SR270Removed_MeanBins = IF_SR270Removed_MeanBins[~numpy.isnan(_6Means)]
		IF_SR270Removed_MeanBins = numpy.append(IF_SR270Removed_MeanBins,IF_SR270Removed_MeanBins[0])
		IF_SLM90Removed_MeanBins,be82,bn82 = scipy.stats.binned_statistic(Rads_SLM90Removed_Sorted,IF_SLM90Removed_Sorted,statistic='mean',bins=bin_size,range=range_rads)
		IF_SLM90Removed_MeanBins = IF_SLM90Removed_MeanBins[~numpy.isnan(_7Means)]
		IF_SLM90Removed_MeanBins = numpy.append(IF_SLM90Removed_MeanBins,IF_SLM90Removed_MeanBins[0])
		IF_SLM180Removed_MeanBins,be92,bn92 = scipy.stats.binned_statistic(Rads_SLM180Removed_Sorted,IF_SLM180Removed_Sorted,statistic='mean',bins=bin_size,range=range_rads)
		IF_SLM180Removed_MeanBins = IF_SLM180Removed_MeanBins[~numpy.isnan(_8Means)]
		IF_SLM180Removed_MeanBins = numpy.append(IF_SLM180Removed_MeanBins,IF_SLM180Removed_MeanBins[0])
		IF_SLM270Removed_MeanBins,be102,bn102 = scipy.stats.binned_statistic(Rads_SLM270Removed_Sorted,IF_SLM270Removed_Sorted,statistic='mean',bins=bin_size,range=range_rads)
		IF_SLM270Removed_MeanBins = IF_SLM270Removed_MeanBins[~numpy.isnan(_9Means)]
		IF_SLM270Removed_MeanBins = numpy.append(IF_SLM270Removed_MeanBins,IF_SLM270Removed_MeanBins[0])
		
		IF_Baseline_MinsBins,be111,bn111 = scipy.stats.binned_statistic(Rads_Baseline_Sorted,IF_Baseline_Sorted,statistic='min',bins=bin_size,range=range_rads)
		IF_Baseline_MinsBins = IF_Baseline_MinsBins[~numpy.isnan(_BMeans)]
		IF_Baseline_MinsBins = numpy.append(IF_Baseline_MinsBins,IF_Baseline_MinsBins[0])
		IF_1XRhythm_MinsBins,be211,bn211 = scipy.stats.binned_statistic(Rads_1XRhythm_Sorted,IF_ThetaX1_Sorted,statistic='min',bins=bin_size,range=range_rads)
		IF_1XRhythm_MinsBins = IF_1XRhythm_MinsBins[~numpy.isnan(_1Means)]
		IF_1XRhythm_MinsBins = numpy.append(IF_1XRhythm_MinsBins,IF_1XRhythm_MinsBins[0])
		IF_CA3Removed_MinsBins,be32,bn32 = scipy.stats.binned_statistic(Rads_CA3Removed_Sorted,IF_CA3Removed_Sorted,statistic='min',bins=bin_size,range=range_rads)
		IF_CA3Removed_MinsBins = IF_CA3Removed_MinsBins[~numpy.isnan(_2Means)]
		IF_CA3Removed_MinsBins = numpy.append(IF_CA3Removed_MinsBins,IF_CA3Removed_MinsBins[0])
		IF_EC3Removed_MinsBins,be42,bn42 = scipy.stats.binned_statistic(Rads_EC3Removed_Sorted,IF_EC3Removed_Sorted,statistic='min',bins=bin_size,range=range_rads)
		IF_EC3Removed_MinsBins = IF_EC3Removed_MinsBins[~numpy.isnan(_3Means)]
		IF_EC3Removed_MinsBins = numpy.append(IF_EC3Removed_MinsBins,IF_EC3Removed_MinsBins[0])
		IF_SR90Removed_MinsBins,be52,bn52 = scipy.stats.binned_statistic(Rads_SR90Removed_Sorted,IF_SR90Removed_Sorted,statistic='min',bins=bin_size,range=range_rads)
		IF_SR90Removed_MinsBins = IF_SR90Removed_MinsBins[~numpy.isnan(_4Means)]
		IF_SR90Removed_MinsBins = numpy.append(IF_SR90Removed_MinsBins,IF_SR90Removed_MinsBins[0])
		IF_SR180Removed_MinsBins,be62,bn62 = scipy.stats.binned_statistic(Rads_SR180Removed_Sorted,IF_SR180Removed_Sorted,statistic='min',bins=bin_size,range=range_rads)
		IF_SR180Removed_MinsBins = IF_SR180Removed_MinsBins[~numpy.isnan(_5Means)]
		IF_SR180Removed_MinsBins = numpy.append(IF_SR180Removed_MinsBins,IF_SR180Removed_MinsBins[0])
		IF_SR270Removed_MinsBins,be72,bn72 = scipy.stats.binned_statistic(Rads_SR270Removed_Sorted,IF_SR270Removed_Sorted,statistic='min',bins=bin_size,range=range_rads)
		IF_SR270Removed_MinsBins = IF_SR270Removed_MinsBins[~numpy.isnan(_6Means)]
		IF_SR270Removed_MinsBins = numpy.append(IF_SR270Removed_MinsBins,IF_SR270Removed_MinsBins[0])
		IF_SLM90Removed_MinsBins,be82,bn82 = scipy.stats.binned_statistic(Rads_SLM90Removed_Sorted,IF_SLM90Removed_Sorted,statistic='min',bins=bin_size,range=range_rads)
		IF_SLM90Removed_MinsBins = IF_SLM90Removed_MinsBins[~numpy.isnan(_7Means)]
		IF_SLM90Removed_MinsBins = numpy.append(IF_SLM90Removed_MinsBins,IF_SLM90Removed_MinsBins[0])
		IF_SLM180Removed_MinsBins,be92,bn92 = scipy.stats.binned_statistic(Rads_SLM180Removed_Sorted,IF_SLM180Removed_Sorted,statistic='min',bins=bin_size,range=range_rads)
		IF_SLM180Removed_MinsBins = IF_SLM180Removed_MinsBins[~numpy.isnan(_8Means)]
		IF_SLM180Removed_MinsBins = numpy.append(IF_SLM180Removed_MinsBins,IF_SLM180Removed_MinsBins[0])
		IF_SLM270Removed_MinsBins,be102,bn102 = scipy.stats.binned_statistic(Rads_SLM270Removed_Sorted,IF_SLM270Removed_Sorted,statistic='min',bins=bin_size,range=range_rads)
		IF_SLM270Removed_MinsBins = IF_SLM270Removed_MinsBins[~numpy.isnan(_9Means)]
		IF_SLM270Removed_MinsBins = numpy.append(IF_SLM270Removed_MinsBins,IF_SLM270Removed_MinsBins[0])
		
		IF_Baseline_MaxBins,be111,bn111 = scipy.stats.binned_statistic(Rads_Baseline_Sorted,IF_Baseline_Sorted,statistic='max',bins=bin_size,range=range_rads)
		IF_Baseline_MaxBins = IF_Baseline_MaxBins[~numpy.isnan(_BMeans)]
		IF_Baseline_MaxBins = numpy.append(IF_Baseline_MaxBins,IF_Baseline_MaxBins[0])
		IF_1XRhythm_MaxBins,be211,bn211 = scipy.stats.binned_statistic(Rads_1XRhythm_Sorted,IF_ThetaX1_Sorted,statistic='max',bins=bin_size,range=range_rads)
		IF_1XRhythm_MaxBins = IF_1XRhythm_MaxBins[~numpy.isnan(_1Means)]
		IF_1XRhythm_MaxBins = numpy.append(IF_1XRhythm_MaxBins,IF_1XRhythm_MaxBins[0])
		IF_CA3Removed_MaxBins,be32,bn32 = scipy.stats.binned_statistic(Rads_CA3Removed_Sorted,IF_CA3Removed_Sorted,statistic='max',bins=bin_size,range=range_rads)
		IF_CA3Removed_MaxBins = IF_CA3Removed_MaxBins[~numpy.isnan(_2Means)]
		IF_CA3Removed_MaxBins = numpy.append(IF_CA3Removed_MaxBins,IF_CA3Removed_MaxBins[0])
		IF_EC3Removed_MaxBins,be42,bn42 = scipy.stats.binned_statistic(Rads_EC3Removed_Sorted,IF_EC3Removed_Sorted,statistic='max',bins=bin_size,range=range_rads)
		IF_EC3Removed_MaxBins = IF_EC3Removed_MaxBins[~numpy.isnan(_3Means)]
		IF_EC3Removed_MaxBins = numpy.append(IF_EC3Removed_MaxBins,IF_EC3Removed_MaxBins[0])
		IF_SR90Removed_MaxBins,be52,bn52 = scipy.stats.binned_statistic(Rads_SR90Removed_Sorted,IF_SR90Removed_Sorted,statistic='max',bins=bin_size,range=range_rads)
		IF_SR90Removed_MaxBins = IF_SR90Removed_MaxBins[~numpy.isnan(_4Means)]
		IF_SR90Removed_MaxBins = numpy.append(IF_SR90Removed_MaxBins,IF_SR90Removed_MaxBins[0])
		IF_SR180Removed_MaxBins,be62,bn62 = scipy.stats.binned_statistic(Rads_SR180Removed_Sorted,IF_SR180Removed_Sorted,statistic='max',bins=bin_size,range=range_rads)
		IF_SR180Removed_MaxBins = IF_SR180Removed_MaxBins[~numpy.isnan(_5Means)]
		IF_SR180Removed_MaxBins = numpy.append(IF_SR180Removed_MaxBins,IF_SR180Removed_MaxBins[0])
		IF_SR270Removed_MaxBins,be72,bn72 = scipy.stats.binned_statistic(Rads_SR270Removed_Sorted,IF_SR270Removed_Sorted,statistic='max',bins=bin_size,range=range_rads)
		IF_SR270Removed_MaxBins = IF_SR270Removed_MaxBins[~numpy.isnan(_6Means)]
		IF_SR270Removed_MaxBins = numpy.append(IF_SR270Removed_MaxBins,IF_SR270Removed_MaxBins[0])
		IF_SLM90Removed_MaxBins,be82,bn82 = scipy.stats.binned_statistic(Rads_SLM90Removed_Sorted,IF_SLM90Removed_Sorted,statistic='max',bins=bin_size,range=range_rads)
		IF_SLM90Removed_MaxBins = IF_SLM90Removed_MaxBins[~numpy.isnan(_7Means)]
		IF_SLM90Removed_MaxBins = numpy.append(IF_SLM90Removed_MaxBins,IF_SLM90Removed_MaxBins[0])
		IF_SLM180Removed_MaxBins,be92,bn92 = scipy.stats.binned_statistic(Rads_SLM180Removed_Sorted,IF_SLM180Removed_Sorted,statistic='max',bins=bin_size,range=range_rads)
		IF_SLM180Removed_MaxBins = IF_SLM180Removed_MaxBins[~numpy.isnan(_8Means)]
		IF_SLM180Removed_MaxBins = numpy.append(IF_SLM180Removed_MaxBins,IF_SLM180Removed_MaxBins[0])
		IF_SLM270Removed_MaxBins,be102,bn102 = scipy.stats.binned_statistic(Rads_SLM270Removed_Sorted,IF_SLM270Removed_Sorted,statistic='max',bins=bin_size,range=range_rads)
		IF_SLM270Removed_MaxBins = IF_SLM270Removed_MaxBins[~numpy.isnan(_9Means)]
		IF_SLM270Removed_MaxBins = numpy.append(IF_SLM270Removed_MaxBins,IF_SLM270Removed_MaxBins[0])
		
		IF_Baseline_StdBins,be111,bn111 = scipy.stats.binned_statistic(Rads_Baseline_Sorted,IF_Baseline_Sorted,statistic='std',bins=bin_size,range=range_rads)
		IF_Baseline_StdBins = IF_Baseline_StdBins[~numpy.isnan(_BMeans)]
		IF_Baseline_StdBins = numpy.append(IF_Baseline_StdBins,IF_Baseline_StdBins[0])
		IF_1XRhythm_StdBins,be211,bn211 = scipy.stats.binned_statistic(Rads_1XRhythm_Sorted,IF_ThetaX1_Sorted,statistic='std',bins=bin_size,range=range_rads)
		IF_1XRhythm_StdBins = IF_1XRhythm_StdBins[~numpy.isnan(_1Means)]
		IF_1XRhythm_StdBins = numpy.append(IF_1XRhythm_StdBins,IF_1XRhythm_StdBins[0])
		IF_CA3Removed_StdBins,be32,bn32 = scipy.stats.binned_statistic(Rads_CA3Removed_Sorted,IF_CA3Removed_Sorted,statistic='std',bins=bin_size,range=range_rads)
		IF_CA3Removed_StdBins = IF_CA3Removed_StdBins[~numpy.isnan(_2Means)]
		IF_CA3Removed_StdBins = numpy.append(IF_CA3Removed_StdBins,IF_CA3Removed_StdBins[0])
		IF_EC3Removed_StdBins,be42,bn42 = scipy.stats.binned_statistic(Rads_EC3Removed_Sorted,IF_EC3Removed_Sorted,statistic='std',bins=bin_size,range=range_rads)
		IF_EC3Removed_StdBins = IF_EC3Removed_StdBins[~numpy.isnan(_3Means)]
		IF_EC3Removed_StdBins = numpy.append(IF_EC3Removed_StdBins,IF_EC3Removed_StdBins[0])
		IF_SR90Removed_StdBins,be52,bn52 = scipy.stats.binned_statistic(Rads_SR90Removed_Sorted,IF_SR90Removed_Sorted,statistic='std',bins=bin_size,range=range_rads)
		IF_SR90Removed_StdBins = IF_SR90Removed_StdBins[~numpy.isnan(_4Means)]
		IF_SR90Removed_StdBins = numpy.append(IF_SR90Removed_StdBins,IF_SR90Removed_StdBins[0])
		IF_SR180Removed_StdBins,be62,bn62 = scipy.stats.binned_statistic(Rads_SR180Removed_Sorted,IF_SR180Removed_Sorted,statistic='std',bins=bin_size,range=range_rads)
		IF_SR180Removed_StdBins = IF_SR180Removed_StdBins[~numpy.isnan(_5Means)]
		IF_SR180Removed_StdBins = numpy.append(IF_SR180Removed_StdBins,IF_SR180Removed_StdBins[0])
		IF_SR270Removed_StdBins,be72,bn72 = scipy.stats.binned_statistic(Rads_SR270Removed_Sorted,IF_SR270Removed_Sorted,statistic='std',bins=bin_size,range=range_rads)
		IF_SR270Removed_StdBins = IF_SR270Removed_StdBins[~numpy.isnan(_6Means)]
		IF_SR270Removed_StdBins = numpy.append(IF_SR270Removed_StdBins,IF_SR270Removed_StdBins[0])
		IF_SLM90Removed_StdBins,be82,bn82 = scipy.stats.binned_statistic(Rads_SLM90Removed_Sorted,IF_SLM90Removed_Sorted,statistic='std',bins=bin_size,range=range_rads)
		IF_SLM90Removed_StdBins = IF_SLM90Removed_StdBins[~numpy.isnan(_7Means)]
		IF_SLM90Removed_StdBins = numpy.append(IF_SLM90Removed_StdBins,IF_SLM90Removed_StdBins[0])
		IF_SLM180Removed_StdBins,be92,bn92 = scipy.stats.binned_statistic(Rads_SLM180Removed_Sorted,IF_SLM180Removed_Sorted,statistic='std',bins=bin_size,range=range_rads)
		IF_SLM180Removed_StdBins = IF_SLM180Removed_StdBins[~numpy.isnan(_8Means)]
		IF_SLM180Removed_StdBins = numpy.append(IF_SLM180Removed_StdBins,IF_SLM180Removed_StdBins[0])
		IF_SLM270Removed_StdBins,be102,bn102 = scipy.stats.binned_statistic(Rads_SLM270Removed_Sorted,IF_SLM270Removed_Sorted,statistic='std',bins=bin_size,range=range_rads)
		IF_SLM270Removed_StdBins = IF_SLM270Removed_StdBins[~numpy.isnan(_9Means)]
		IF_SLM270Removed_StdBins = numpy.append(IF_SLM270Removed_StdBins,IF_SLM270Removed_StdBins[0])
		
		axarr = pyplot.subplot(111, projection='polar')
		axarr.plot(Rads_Baseline_Sorted,IF_Baseline_Sorted,color='lightblue',label='Base')
		axarr.plot(Rads_1XRhythm_Sorted,IF_ThetaX1_Sorted,color='tomato',label='Theta')
		axarr.plot(Rads_CA3Removed_Sorted,IF_CA3Removed_Sorted,'g',label=r'$2 \times$CA3')
		axarr.plot(Rads_EC3Removed_Sorted,IF_EC3Removed_Sorted,'c',label=r'$2 \times$EC3')
		axarr.plot(Rads_SR90Removed_Sorted,IF_SR90Removed_Sorted,'m',label=r'$2 \times$SR90')
		axarr.plot(Rads_SR180Removed_Sorted,IF_SR180Removed_Sorted,'y',label=r'$2 \times$SR180')
		axarr.plot(Rads_SR270Removed_Sorted,IF_SR270Removed_Sorted,'b',label=r'$2 \times$SR270')
		axarr.plot(Rads_SLM90Removed_Sorted,IF_SLM90Removed_Sorted,'k',label=r'$2 \times$SLM90')
		axarr.plot(Rads_SLM180Removed_Sorted,IF_SLM180Removed_Sorted,color='orange',label=r'$2 \times$SLM180')
		axarr.plot(Rads_SLM270Removed_Sorted,IF_SLM270Removed_Sorted,'r',label=r'$2 \times$SLM270')
		position = 292.5
		axarr._r_label_position._t = (position, 0)
		axarr._r_label_position.invalidate()
		axarr.set_xticklabels(['0$^\circ$', '45$^\circ$', '90$^\circ$\nPeak', '135$^\circ$', '180$^\circ$', '225$^\circ$', '270$^\circ$\nTrough', '315$^\circ$'])
		pyplot.tight_layout()
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlot_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.pdf', bbox_inches='tight')
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlot_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.png', bbox_inches='tight')
		pyplot.gcf().clear()
		pyplot.cla()
		pyplot.clf()
		pyplot.close()
		
		axarr = pyplot.subplot(111, projection='polar')
		axarr.plot(Rads_Baseline_MeanBins,IF_Baseline_MeanBins,color='lightblue',label='Base')
		axarr.fill_between(Rads_Baseline_MeanBins,numpy.clip(IF_Baseline_MeanBins-IF_Baseline_StdBins,0,1000),numpy.clip(IF_Baseline_MeanBins+IF_Baseline_StdBins,0,1000),alpha=0.5, edgecolor='lightblue', facecolor='lightblue')
		axarr.plot(Rads_1XRhythm_MeanBins,IF_1XRhythm_MeanBins,color='tomato',label='X1 Theta')
		axarr.fill_between(Rads_1XRhythm_MeanBins,numpy.clip(IF_1XRhythm_MeanBins-IF_1XRhythm_StdBins,0,1000),numpy.clip(IF_1XRhythm_MeanBins+IF_1XRhythm_StdBins,0,1000),alpha=0.5, edgecolor='tomato', facecolor='tomato')
		axarr.plot(Rads_CA3Removed_MeanBins,IF_CA3Removed_MeanBins,'g',label=r'$2 \times$CA3')
		axarr.fill_between(Rads_CA3Removed_MeanBins,numpy.clip(IF_CA3Removed_MeanBins-IF_CA3Removed_StdBins,0,1000),numpy.clip(IF_CA3Removed_MeanBins+IF_CA3Removed_StdBins,0,1000),alpha=0.5, edgecolor='g', facecolor='g')
		axarr.plot(Rads_EC3Removed_MeanBins,IF_EC3Removed_MeanBins,'c',label=r'$2 \times$EC3')
		axarr.fill_between(Rads_EC3Removed_MeanBins,numpy.clip(IF_EC3Removed_MeanBins-IF_EC3Removed_StdBins,0,1000),numpy.clip(IF_EC3Removed_MeanBins+IF_EC3Removed_StdBins,0,1000),alpha=0.5, edgecolor='c', facecolor='c')
		axarr.plot(Rads_SR90Removed_MeanBins,IF_SR90Removed_MeanBins,'m',label=r'$2 \times$SR90')
		axarr.fill_between(Rads_SR90Removed_MeanBins,numpy.clip(IF_SR90Removed_MeanBins-IF_SR90Removed_StdBins,0,1000),numpy.clip(IF_SR90Removed_MeanBins+IF_SR90Removed_StdBins,0,1000),alpha=0.5, edgecolor='m', facecolor='m')
		axarr.plot(Rads_SR180Removed_MeanBins,IF_SR180Removed_MeanBins,'y',label=r'$2 \times$SR180')
		axarr.fill_between(Rads_SR180Removed_MeanBins,numpy.clip(IF_SR180Removed_MeanBins-IF_SR180Removed_StdBins,0,1000),numpy.clip(IF_SR180Removed_MeanBins+IF_SR180Removed_StdBins,0,1000),alpha=0.5, edgecolor='y', facecolor='y')
		axarr.plot(Rads_SR270Removed_MeanBins,IF_SR270Removed_MeanBins,'b',label=r'$2 \times$SR270')
		axarr.fill_between(Rads_SR270Removed_MeanBins,numpy.clip(IF_SR270Removed_MeanBins-IF_SR270Removed_StdBins,0,1000),numpy.clip(IF_SR270Removed_MeanBins+IF_SR270Removed_StdBins,0,1000),alpha=0.5, edgecolor='b', facecolor='b')
		axarr.plot(Rads_SLM90Removed_MeanBins,IF_SLM90Removed_MeanBins,'k',label=r'$2 \times$SLM90')
		axarr.fill_between(Rads_SLM90Removed_MeanBins,numpy.clip(IF_SLM90Removed_MeanBins-IF_SLM90Removed_StdBins,0,1000),numpy.clip(IF_SLM90Removed_MeanBins+IF_SLM90Removed_StdBins,0,1000),alpha=0.5, edgecolor='k', facecolor='k')
		axarr.plot(Rads_SLM180Removed_MeanBins,IF_SLM180Removed_MeanBins,color='orange',label=r'$2 \times$SLM180')
		axarr.fill_between(Rads_SLM180Removed_MeanBins,numpy.clip(IF_SLM180Removed_MeanBins-IF_SLM180Removed_StdBins,0,1000),numpy.clip(IF_SLM180Removed_MeanBins+IF_SLM180Removed_StdBins,0,1000),alpha=0.5, edgecolor='orange', facecolor='orange')
		axarr.plot(Rads_SLM270Removed_MeanBins,IF_SLM270Removed_MeanBins,'r',label=r'$2 \times$SLM270')
		axarr.fill_between(Rads_SLM270Removed_MeanBins,numpy.clip(IF_SLM270Removed_MeanBins-IF_SLM270Removed_StdBins,0,1000),numpy.clip(IF_SLM270Removed_MeanBins+IF_SLM270Removed_StdBins,0,1000),alpha=0.5, edgecolor='r', facecolor='r')
		position = 292.5
		axarr._r_label_position._t = (position, 0)
		axarr._r_label_position.invalidate()
		axarr.set_xticklabels(['0$^\circ$', '45$^\circ$', '90$^\circ$\nPeak', '135$^\circ$', '180$^\circ$', '225$^\circ$', '270$^\circ$\nTrough', '315$^\circ$'])
		pyplot.tight_layout()
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlotBinned_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.pdf', bbox_inches='tight')
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlotBinned_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.png', bbox_inches='tight')
		pyplot.gcf().clear()
		pyplot.cla()
		pyplot.clf()
		pyplot.close()
		
		axarr = pyplot.subplot(111, projection='polar')
		axarr.plot(Rads_Baseline_MeanBins,IF_Baseline_MeanBins,color='lightblue',label='Base')
		axarr.fill_between(Rads_Baseline_MeanBins,numpy.clip(IF_Baseline_MeanBins-IF_Baseline_StdBins,0,1000),numpy.clip(IF_Baseline_MeanBins+IF_Baseline_StdBins,0,1000),alpha=0.5, edgecolor='lightblue', facecolor='lightblue')
		position = 292.5
		axarr._r_label_position._t = (position, 0)
		axarr._r_label_position.invalidate()
		bottom = numpy.amax(numpy.clip(IF_Baseline_MeanBins+IF_Baseline_StdBins,0,1000))+5
		width = range_rads[1]/(bin_size+1)
		axarr.bar(_BMeans, heights11, width=width, bottom=bottom,color='lightblue')
		# for ph in range(0,len(PrefPhase_Baseline)):
		#     axarr.annotate(' ', xy=(PrefPhase_Baseline[ph], numpy.amax(numpy.clip(IF_Baseline_MeanBins+IF_Baseline_StdBins,0,1000))), xytext=(0, 0),arrowprops=dict(facecolor='black', shrink=0.05),)
		axarr.set_xticklabels(['0$^\circ$', '45$^\circ$', '90$^\circ$\nPeak', '135$^\circ$', '180$^\circ$', '225$^\circ$', '270$^\circ$\nTrough', '315$^\circ$'])
		pyplot.tight_layout()
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlotBinnedBaseline_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.pdf', bbox_inches='tight')
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlotBinnedBaseline_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.png', bbox_inches='tight')
		pyplot.gcf().clear()
		pyplot.cla()
		pyplot.clf()
		pyplot.close()
		
		axarr = pyplot.subplot(111, projection='polar')
		axarr.plot(Rads_1XRhythm_MeanBins,IF_1XRhythm_MeanBins,color='tomato',label='X1 Theta')
		axarr.fill_between(Rads_1XRhythm_MeanBins,numpy.clip(IF_1XRhythm_MeanBins-IF_1XRhythm_StdBins,0,1000),numpy.clip(IF_1XRhythm_MeanBins+IF_1XRhythm_StdBins,0,1000),alpha=0.5, edgecolor='tomato', facecolor='tomato')
		position = 292.5
		axarr._r_label_position._t = (position, 0)
		axarr._r_label_position.invalidate()
		bottom = numpy.amax(numpy.clip(IF_1XRhythm_MeanBins+IF_1XRhythm_StdBins,0,1000))+5
		width = range_rads[1]/(bin_size+1)
		axarr.bar(_1Means, heights22, width=width, bottom=bottom,color='tomato')
		# for ph in range(0,len(PrefPhase_ThetaX1)):
		#     axarr.annotate(' ', xy=(PrefPhase_ThetaX1[ph], numpy.amax(numpy.clip(IF_1XRhythm_MeanBins+IF_1XRhythm_StdBins,0,1000))), xytext=(0, 0),arrowprops=dict(facecolor='black', shrink=0.05),)
		axarr.set_xticklabels(['0$^\circ$', '45$^\circ$', '90$^\circ$\nPeak', '135$^\circ$', '180$^\circ$', '225$^\circ$', '270$^\circ$\nTrough', '315$^\circ$'])
		pyplot.tight_layout()
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlotBinned1XTheta_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.pdf', bbox_inches='tight')
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlotBinned1XTheta_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.png', bbox_inches='tight')
		pyplot.gcf().clear()
		pyplot.cla()
		pyplot.clf()
		pyplot.close()
	
		axarr = pyplot.subplot(111, projection='polar')
		axarr.plot(Rads_CA3Removed_MeanBins,IF_CA3Removed_MeanBins,'g',label=r'$2 \times$CA3')
		axarr.fill_between(Rads_CA3Removed_MeanBins,numpy.clip(IF_CA3Removed_MeanBins-IF_CA3Removed_StdBins,0,1000),numpy.clip(IF_CA3Removed_MeanBins+IF_CA3Removed_StdBins,0,1000),alpha=0.5, edgecolor='g', facecolor='g')
		position = 292.5
		axarr._r_label_position._t = (position, 0)
		axarr._r_label_position.invalidate()
		bottom = numpy.amax(numpy.clip(IF_CA3Removed_MeanBins+IF_CA3Removed_StdBins,0,1000))+5
		width = range_rads[1]/(bin_size+1)
		axarr.bar(_2Means, heights33, width=width, bottom=bottom,color='g')
		# for ph in range(0,len(PrefPhase_CA3Removed)):
		#     axarr.annotate(' ', xy=(PrefPhase_CA3Removed[ph], numpy.amax(numpy.clip(IF_CA3Removed_MeanBins+IF_CA3Removed_StdBins,0,1000))), xytext=(0, 0),arrowprops=dict(facecolor='black', shrink=0.05),)
		axarr.set_xticklabels(['0$^\circ$', '45$^\circ$', '90$^\circ$\nPeak', '135$^\circ$', '180$^\circ$', '225$^\circ$', '270$^\circ$\nTrough', '315$^\circ$'])
		pyplot.tight_layout()
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlotBinnedCA3Doubled_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.pdf', bbox_inches='tight')
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlotBinnedCA3Doubled_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.png', bbox_inches='tight')
		pyplot.gcf().clear()
		pyplot.cla()
		pyplot.clf()
		pyplot.close()
	
		axarr = pyplot.subplot(111, projection='polar')
		axarr.plot(Rads_EC3Removed_MeanBins,IF_EC3Removed_MeanBins,'c',label=r'$2 \times$EC3')
		axarr.fill_between(Rads_EC3Removed_MeanBins,numpy.clip(IF_EC3Removed_MeanBins-IF_EC3Removed_StdBins,0,1000),numpy.clip(IF_EC3Removed_MeanBins+IF_EC3Removed_StdBins,0,1000),alpha=0.5, edgecolor='c', facecolor='c')
		position = 292.5
		axarr._r_label_position._t = (position, 0)
		axarr._r_label_position.invalidate()
		bottom = numpy.amax(numpy.clip(IF_EC3Removed_MeanBins+IF_EC3Removed_StdBins,0,1000))+5
		width = range_rads[1]/(bin_size+1)
		axarr.bar(_3Means, heights44, width=width, bottom=bottom,color='c')
		# for ph in range(0,len(PrefPhase_EC3Removed)):
		#     axarr.annotate(' ', xy=(PrefPhase_EC3Removed[ph], numpy.amax(numpy.clip(IF_EC3Removed_MeanBins+IF_EC3Removed_StdBins,0,1000))), xytext=(0, 0),arrowprops=dict(facecolor='black', shrink=0.05),)
		axarr.set_xticklabels(['0$^\circ$', '45$^\circ$', '90$^\circ$\nPeak', '135$^\circ$', '180$^\circ$', '225$^\circ$', '270$^\circ$\nTrough', '315$^\circ$'])
		pyplot.tight_layout()
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlotBinnedEC3Doubled_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.pdf', bbox_inches='tight')
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlotBinnedEC3Doubled_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.png', bbox_inches='tight')
		pyplot.gcf().clear()
		pyplot.cla()
		pyplot.clf()
		pyplot.close()
	
		axarr = pyplot.subplot(111, projection='polar')
		axarr.plot(Rads_SR90Removed_MeanBins,IF_SR90Removed_MeanBins,'m',label=r'$2 \times$SR90')
		axarr.fill_between(Rads_SR90Removed_MeanBins,numpy.clip(IF_SR90Removed_MeanBins-IF_SR90Removed_StdBins,0,1000),numpy.clip(IF_SR90Removed_MeanBins+IF_SR90Removed_StdBins,0,1000),alpha=0.5, edgecolor='m', facecolor='m')
		position = 292.5
		axarr._r_label_position._t = (position, 0)
		axarr._r_label_position.invalidate()
		bottom = numpy.amax(numpy.clip(IF_SR90Removed_MeanBins+IF_SR90Removed_StdBins,0,1000))+5
		width = range_rads[1]/(bin_size+1)
		axarr.bar(_4Means, heights55, width=width, bottom=bottom,color='m')
		# for ph in range(0,len(PrefPhase_OLMRemoved)):
		#     axarr.annotate(' ', xy=(PrefPhase_OLMRemoved[ph], numpy.amax(numpy.clip(IF_OLMRemoved_MeanBins+IF_OLMRemoved_StdBins,0,1000))), xytext=(0, 0),arrowprops=dict(facecolor='black', shrink=0.05),)
		axarr.set_xticklabels(['0$^\circ$', '45$^\circ$', '90$^\circ$\nPeak', '135$^\circ$', '180$^\circ$', '225$^\circ$', '270$^\circ$\nTrough', '315$^\circ$'])
		pyplot.tight_layout()
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlotBinnedSR90Doubled_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.pdf', bbox_inches='tight')
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlotBinnedSR90Doubled_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.png', bbox_inches='tight')
		pyplot.gcf().clear()
		pyplot.cla()
		pyplot.clf()
		pyplot.close()
	
		axarr = pyplot.subplot(111, projection='polar')
		axarr.plot(Rads_SR180Removed_MeanBins,IF_SR180Removed_MeanBins,'y',label=r'$2 \times$SR180')
		axarr.fill_between(Rads_SR180Removed_MeanBins,numpy.clip(IF_SR180Removed_MeanBins-IF_SR180Removed_StdBins,0,1000),numpy.clip(IF_SR180Removed_MeanBins+IF_SR180Removed_StdBins,0,1000),alpha=0.5, edgecolor='y', facecolor='y')
		position = 292.5
		axarr._r_label_position._t = (position, 0)
		axarr._r_label_position.invalidate()
		bottom = numpy.amax(numpy.clip(IF_SR180Removed_MeanBins+IF_SR180Removed_StdBins,0,1000))+5
		width = range_rads[1]/(bin_size+1)
		axarr.bar(_5Means, heights66, width=width, bottom=bottom,color='y')
		# for ph in range(0,len(PrefPhase_IS2NGFRemoved)):
		#     axarr.annotate(' ', xy=(PrefPhase_IS2NGFRemoved[ph], numpy.amax(numpy.clip(IF_IS2NGFRemoved_MeanBins+IF_IS2NGFRemoved_StdBins,0,1000))), xytext=(0, 0),arrowprops=dict(facecolor='black', shrink=0.05),)
		axarr.set_xticklabels(['0$^\circ$', '45$^\circ$', '90$^\circ$\nPeak', '135$^\circ$', '180$^\circ$', '225$^\circ$', '270$^\circ$\nTrough', '315$^\circ$'])
		pyplot.tight_layout()
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlotBinnedSR180Doubled_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.pdf', bbox_inches='tight')
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlotBinnedSR180Doubled_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.png', bbox_inches='tight')
		pyplot.gcf().clear()
		pyplot.cla()
		pyplot.clf()
		pyplot.close()
	
		axarr = pyplot.subplot(111, projection='polar')
		axarr.plot(Rads_SR270Removed_MeanBins,IF_SR270Removed_MeanBins,'b',label=r'$2 \times$SR270')
		axarr.fill_between(Rads_SR270Removed_MeanBins,numpy.clip(IF_SR270Removed_MeanBins-IF_SR270Removed_StdBins,0,1000),numpy.clip(IF_SR270Removed_MeanBins+IF_SR270Removed_StdBins,0,1000),alpha=0.5, edgecolor='b', facecolor='b')
		position = 292.5
		axarr._r_label_position._t = (position, 0)
		axarr._r_label_position.invalidate()
		bottom = numpy.amax(numpy.clip(IF_SR270Removed_MeanBins+IF_SR270Removed_StdBins,0,1000))+5
		width = range_rads[1]/(bin_size+1)
		axarr.bar(_6Means, heights77, width=width, bottom=bottom,color='b')
		# for ph in range(0,len(PrefPhase_BISRemoved)):
		#     axarr.annotate(' ', xy=(PrefPhase_BISRemoved[ph], numpy.amax(numpy.clip(IF_BISRemoved_MeanBins+IF_BISRemoved_StdBins,0,1000))), xytext=(0, 0),arrowprops=dict(facecolor='black', shrink=0.05),)
		axarr.set_xticklabels(['0$^\circ$', '45$^\circ$', '90$^\circ$\nPeak', '135$^\circ$', '180$^\circ$', '225$^\circ$', '270$^\circ$\nTrough', '315$^\circ$'])
		pyplot.tight_layout()
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlotBinnedSR270Doubled_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.pdf', bbox_inches='tight')
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlotBinnedSR270Doubled_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.png', bbox_inches='tight')
		pyplot.gcf().clear()
		pyplot.cla()
		pyplot.clf()
		pyplot.close()
	
		axarr = pyplot.subplot(111, projection='polar')
		axarr.plot(Rads_SLM90Removed_MeanBins,IF_SLM90Removed_MeanBins,'k',label=r'$2 \times$SLM90')
		axarr.fill_between(Rads_SLM90Removed_MeanBins,numpy.clip(IF_SLM90Removed_MeanBins-IF_SLM90Removed_StdBins,0,1000),numpy.clip(IF_SLM90Removed_MeanBins+IF_SLM90Removed_StdBins,0,1000),alpha=0.5, edgecolor='k', facecolor='k')
		position = 292.5
		axarr._r_label_position._t = (position, 0)
		axarr._r_label_position.invalidate()
		bottom = numpy.amax(numpy.clip(IF_SLM90Removed_MeanBins+IF_SLM90Removed_StdBins,0,1000))+5
		width = range_rads[1]/(bin_size+1)
		axarr.bar(_7Means, heights88, width=width, bottom=bottom,color='k')
		# for ph in range(0,len(PrefPhase_IS1Removed)):
		#     axarr.annotate(' ', xy=(PrefPhase_IS1Removed[ph], numpy.amax(numpy.clip(IF_IS1Removed_MeanBins+IF_IS1Removed_StdBins,0,1000))), xytext=(0, 0),arrowprops=dict(facecolor='black', shrink=0.05),)
		axarr.set_xticklabels(['0$^\circ$', '45$^\circ$', '90$^\circ$\nPeak', '135$^\circ$', '180$^\circ$', '225$^\circ$', '270$^\circ$\nTrough', '315$^\circ$'])
		pyplot.tight_layout()
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlotBinnedSLM90Doubled_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.pdf', bbox_inches='tight')
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlotBinnedSLM90Doubled_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.png', bbox_inches='tight')
		pyplot.gcf().clear()
		pyplot.cla()
		pyplot.clf()
		pyplot.close()
	
		axarr = pyplot.subplot(111, projection='polar')
		axarr.plot(Rads_SLM180Removed_MeanBins,IF_SLM180Removed_MeanBins,color='orange',label=r'$2 \times$SLM180')
		axarr.fill_between(Rads_SLM180Removed_MeanBins,numpy.clip(IF_SLM180Removed_MeanBins-IF_SLM180Removed_StdBins,0,1000),numpy.clip(IF_SLM180Removed_MeanBins+IF_SLM180Removed_StdBins,0,1000),alpha=0.5, edgecolor='orange', facecolor='orange')
		position = 292.5
		axarr._r_label_position._t = (position, 0)
		axarr._r_label_position.invalidate()
		bottom = numpy.amax(numpy.clip(IF_SLM180Removed_MeanBins+IF_SLM180Removed_StdBins,0,1000))+5
		width = range_rads[1]/(bin_size+1)
		axarr.bar(_8Means, heights99, width=width, bottom=bottom,color='orange')
		# for ph in range(0,len(PrefPhase_IS1Removed)):
		#     axarr.annotate(' ', xy=(PrefPhase_IS1Removed[ph], numpy.amax(numpy.clip(IF_IS1Removed_MeanBins+IF_IS1Removed_StdBins,0,1000))), xytext=(0, 0),arrowprops=dict(facecolor='black', shrink=0.05),)
		axarr.set_xticklabels(['0$^\circ$', '45$^\circ$', '90$^\circ$\nPeak', '135$^\circ$', '180$^\circ$', '225$^\circ$', '270$^\circ$\nTrough', '315$^\circ$'])
		pyplot.tight_layout()
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlotBinnedSLM180Doubled_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.pdf', bbox_inches='tight')
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlotBinnedSLM180Doubled_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.png', bbox_inches='tight')
		pyplot.gcf().clear()
		pyplot.cla()
		pyplot.clf()
		pyplot.close()
	
		axarr = pyplot.subplot(111, projection='polar')
		axarr.plot(Rads_SLM270Removed_MeanBins,IF_SLM270Removed_MeanBins,'r',label=r'$2 \times$SLM270')
		axarr.fill_between(Rads_SLM270Removed_MeanBins,numpy.clip(IF_SLM270Removed_MeanBins-IF_SLM270Removed_StdBins,0,1000),numpy.clip(IF_SLM270Removed_MeanBins+IF_SLM270Removed_StdBins,0,1000),alpha=0.5, edgecolor='r', facecolor='r')
		position = 292.5
		axarr._r_label_position._t = (position, 0)
		axarr._r_label_position.invalidate()
		bottom = numpy.amax(numpy.clip(IF_SLM270Removed_MeanBins+IF_SLM270Removed_StdBins,0,1000))+5
		width = range_rads[1]/(bin_size+1)
		axarr.bar(_9Means, heights1010, width=width, bottom=bottom,color='r')
		# for ph in range(0,len(PrefPhase_IS1Removed)):
		#     axarr.annotate(' ', xy=(PrefPhase_IS1Removed[ph], numpy.amax(numpy.clip(IF_IS1Removed_MeanBins+IF_IS1Removed_StdBins,0,1000))), xytext=(0, 0),arrowprops=dict(facecolor='black', shrink=0.05),)
		axarr.set_xticklabels(['0$^\circ$', '45$^\circ$', '90$^\circ$\nPeak', '135$^\circ$', '180$^\circ$', '225$^\circ$', '270$^\circ$\nTrough', '315$^\circ$'])
		pyplot.tight_layout()
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlotBinnedSLM270Doubled_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.pdf', bbox_inches='tight')
		pyplot.savefig('PLOTfiles/' + Case + '_PolarPlotBinnedSLM270Doubled_' + ExampleString + '_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.png', bbox_inches='tight')
		pyplot.gcf().clear()
		pyplot.cla()
		pyplot.clf()
		pyplot.close()
	
	numpy.save('NPYfiles/' + Case + '_Areas_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.npy',numpy.array([Area1,Area2,Area3,Area4,Area5,Area6,Area7,Area8,Area9,Area10],dtype=numpy.float))
	numpy.save('NPYfiles/' + Case + '_e8Hz_' + str('%0.2f' %h.prethetanoise) + '_prethetanoise.npy',numpy.array([e8Hz1,e8Hz2,e8Hz3,e8Hz4,e8Hz5,e8Hz6,e8Hz7,e8Hz8,e8Hz9,e8Hz10],dtype=numpy.float))

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

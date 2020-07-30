import neuron
from neuron import h

h.load_file("SynParamSearch.hoc")
exec(open("PlotResults.py").read())
h.quit()

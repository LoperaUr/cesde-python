import matplotlib.pyplot as pyplot
import numpy

## gráfica histograma
datos = numpy.random.rand(1000)

pyplot.hist(datos, bins=30, edgecolor="black", color="white")
pyplot.show()

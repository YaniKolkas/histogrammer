import csv
import numpy
import matplotlib


measurements = dict()
measurement_file = 'Measurements.csv'

with open(measurement_file) as f:
    csv_reader = csv.reader(f, delimiter=';')

    header = next(csv_reader)
    number_of_columns = len(header)

    for name in header:
        measurements[name] = list()

    for row in csv_reader:
        index = 0
        for item in header:
            try:
                converted_value = float(row[index])
                measurements[item].append(converted_value)
            except ValueError:
                print "Found non-convertable value row {} column {}".format(item, index)
            index += 1

for item in measurements:
    parameter_list = measurements[item]
    average = numpy.average(parameter_list)
    stdev = numpy.std(parameter_list)
    print "{} average value = {} stdev = {}".format(item, average, stdev )


data_vreg_nom = measurements['V_reg_VddNom_']


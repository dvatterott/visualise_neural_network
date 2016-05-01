from matplotlib import pyplot as plt
import numpy as np
from math import cos, sin, atan

class Neuron():
    def __init__(self, x, y, weight=[]):
        self.x = x
        self.y = y
        if weight: self.weight = weight

    def draw(self,texter):
        circle = plt.Circle((self.x, self.y), radius=neuron_radius, fill=False)
        text = plt.annotate(texter,(self.x,self.y),size='large',ha='center',va='center')
        plt.gca().add_patch(circle)

class Layer():
    def __init__(self, network, number_of_neurons,text,weights=[]):
        self.previous_layer = self.__get_previous_layer(network)
        self.y = self.__calculate_layer_y_position()
        self.neurons = self.__intialise_neurons(number_of_neurons, weights)
        self.text = text

    def __intialise_neurons(self, number_of_neurons,weights):
        neurons = []
        x = self.__calculate_left_margin_so_layer_is_centered(number_of_neurons)
        for iteration in xrange(number_of_neurons):
            if weights: 
                neuron = Neuron(x,self.y,weight = weights[iteration])
            else:
                neuron = Neuron(x, self.y,weight = 'no')
            neurons.append(neuron)
            x += horizontal_distance_between_neurons
        return neurons

    def __calculate_left_margin_so_layer_is_centered(self, number_of_neurons):
        return horizontal_distance_between_neurons * (number_of_neurons_in_widest_layer - number_of_neurons) / 2

    def __calculate_layer_y_position(self):
        if self.previous_layer:
            return self.previous_layer.y + vertical_distance_between_layers
        else:
            return 0

    def __get_previous_layer(self, network):
        if len(network.layers) > 0:
            return network.layers[-1]
        else:
            return None

    def __line_between_two_neurons(self, neuron1, neuron2,weight=[]):
        angle = atan((neuron2.x - neuron1.x) / float(neuron2.y - neuron1.y))
        x_adjustment = neuron_radius * sin(angle)
        y_adjustment = neuron_radius * cos(angle)
        line = plt.Line2D((neuron1.x - x_adjustment, neuron2.x + x_adjustment), (neuron1.y - y_adjustment, neuron2.y + y_adjustment),color='k')
        plt.gca().add_line(line)
        if weight: 
            if neuron1.x < 8: 
                text = plt.text((neuron1.x+neuron2.x)/2,(neuron1.y+neuron2.y)/2,weight[0],size='large',ha='right')
            if neuron1.x > 8:
                text = plt.text((neuron1.x+neuron2.x)/2,(neuron1.y+neuron2.y)/2,weight[1],size='large',ha='left')
            if neuron1.x == 8: text = plt.text((neuron1.x+neuron2.x)/2,(neuron1.y+neuron2.y)/2,weight,size='large',ha='center')
            
    def draw(self,text):
        for neuron,texter in zip(self.neurons,text):
            neuron.draw(texter)
            if self.previous_layer:
                for i,previous_layer_neuron in enumerate(self.previous_layer.neurons):
                    if previous_layer_neuron.weight == 'no':
                        self.__line_between_two_neurons(neuron, previous_layer_neuron, weight=[])
                    elif np.size(previous_layer_neuron.weight) < 2:
                        self.__line_between_two_neurons(neuron, previous_layer_neuron, weight=previous_layer_neuron.weight)
                    else:
                        self.__line_between_two_neurons(neuron, previous_layer_neuron, weight=previous_layer_neuron.weight)
                        
                        
class NeuralNetwork():
    def __init__(self):
        self.layers = []

    def add_layer(self, number_of_neurons,text,weights=[]):
        layer = Layer(self, number_of_neurons,text,weights=weights)
        self.layers.append(layer)
        
    def draw(self):
        plt.figure(figsize=(8,8))
        for layer in self.layers:
            layer.draw(layer.text)
        plt.axis('scaled')
        plt.xticks([])
        plt.yticks([])
        plt.show()

vertical_distance_between_layers = 6
horizontal_distance_between_neurons = 8
neuron_radius = 1.5
number_of_neurons_in_widest_layer = 3
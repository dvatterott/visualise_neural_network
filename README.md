# Visualise Neural Network
Generates a static diagram of a neural network, where each neuron is connected to every neuron in the previous layer.

For example, this code:

    network = NeuralNetwork()
    network.add_layer(3)
    network.add_layer(4)
    network.add_layer(1)
    network.draw()

Will generate this diagram:

![Diagram of a neural network with 3 neurons in the first layer, 4 neurons in the second layer and 1 neuron in the 3rd layer](http://i.stack.imgur.com/8oxCO.png)

[4/24/16] - dvatterott
I forked this repository from miloharper/visualise-neural-network. I made the repository into a python package and renamed it (for importing into python). I also added some code for labeling the neurons and weights. 

Each neuron now requires a name (sorry...the code above will not work with my changes). 
The weights take an optional label. 

Here's an example of code to draw a network with one Output neuron and two Input neurons. The Weights between the Input and Output neurons are labeled. 

    from visualise_neural_network import NeuralNetwork

    network = NeuralNetwork()
    network.add_layer(2,['Input A','Input B'],['Weight A','Weight B'])
    network.add_layer(1,['Output'])
    network.draw()

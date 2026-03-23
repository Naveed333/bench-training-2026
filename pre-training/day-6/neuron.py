import math
import random

# ─────────────────────────────────────────────
# ACTIVATION FUNCTIONS
# ─────────────────────────────────────────────

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def relu(x):
    return max(0.0, x)


# ─────────────────────────────────────────────
# PART 1 — SINGLE NEURON
# ─────────────────────────────────────────────

class Neuron:
    def __init__(self, n_inputs, activation="sigmoid"):
        # Each weight controls how much a specific input influences the output.
        # A high weight means that input matters a lot; near-zero means it barely matters.
        self.weights = [random.uniform(-1, 1) for _ in range(n_inputs)]

        # Bias shifts the activation threshold up or down independently of inputs.
        # Without bias the neuron can only fire when inputs push it over zero.
        self.bias = random.uniform(-1, 1)

        self.activation = activation

    def forward(self, inputs):
        if len(inputs) != len(self.weights):
            raise ValueError(f"Expected {len(self.weights)} inputs, got {len(inputs)}")

        # Weighted sum: multiply each input by its weight and add them all up
        z = sum(w * x for w, x in zip(self.weights, inputs)) + self.bias

        # Pass through activation function
        if self.activation == "sigmoid":
            return sigmoid(z)
        elif self.activation == "relu":
            return relu(z)
        else:
            raise ValueError(f"Unknown activation: {self.activation}")


# ─────────────────────────────────────────────
# PART 2 — DENSE LAYER
# ─────────────────────────────────────────────

class DenseLayer:
    def __init__(self, n_inputs, n_neurons, activation="sigmoid"):
        # A layer is just a collection of neurons — each neuron gets all inputs
        self.neurons = [Neuron(n_inputs, activation) for _ in range(n_neurons)]

    def forward(self, inputs):
        # Each neuron independently processes the same inputs
        # Returns one output value per neuron
        return [neuron.forward(inputs) for neuron in self.neurons]


# ─────────────────────────────────────────────
# PART 3 — TINY NETWORK (manually set weights)
# ─────────────────────────────────────────────

class TinyNetwork:
    def __init__(self):
        # Layer 1: 3 inputs → 4 neurons (hidden layer)
        self.layer1 = DenseLayer(n_inputs=3, n_neurons=4, activation="relu")

        # Layer 2: 4 inputs (from layer1 output) → 2 neurons (output layer)
        self.layer2 = DenseLayer(n_inputs=4, n_neurons=2, activation="sigmoid")

        # Manually set weights so results are deterministic and explainable
        # Layer 1 weights — shape: (4 neurons) x (3 weights each)
        manual_w1 = [
            [0.5,  -0.3,  0.8],   # neuron 0
            [-0.4,  0.6,  0.2],   # neuron 1
            [0.7,   0.1, -0.5],   # neuron 2
            [-0.2,  0.9,  0.4],   # neuron 3
        ]
        manual_b1 = [0.1, -0.1, 0.2, -0.2]

        for i, neuron in enumerate(self.layer1.neurons):
            neuron.weights = manual_w1[i]
            neuron.bias = manual_b1[i]

        # Layer 2 weights — shape: (2 neurons) x (4 weights each)
        manual_w2 = [
            [0.3, -0.5,  0.7, -0.1],  # neuron 0
            [-0.6,  0.4, -0.3,  0.8], # neuron 1
        ]
        manual_b2 = [0.05, -0.05]

        for i, neuron in enumerate(self.layer2.neurons):
            neuron.weights = manual_w2[i]
            neuron.bias = manual_b2[i]

    def forward(self, inputs):
        # Pass inputs through layer 1, then feed output into layer 2
        hidden = self.layer1.forward(inputs)
        output = self.layer2.forward(hidden)
        return hidden, output


# ─────────────────────────────────────────────
# MAIN — RUN THE NETWORK
# ─────────────────────────────────────────────

if __name__ == "__main__":
    sample_input = [0.5, -0.3, 0.8]

    print("=" * 50)
    print("  PART 1 — Single Neuron")
    print("=" * 50)
    n_sigmoid = Neuron(n_inputs=3, activation="sigmoid")
    n_relu    = Neuron(n_inputs=3, activation="relu")
    n_sigmoid.weights = [0.5, -0.3, 0.8]
    n_sigmoid.bias    = 0.1
    n_relu.weights    = [0.5, -0.3, 0.8]
    n_relu.bias       = 0.1

    print(f"  Input        : {sample_input}")
    print(f"  Sigmoid out  : {n_sigmoid.forward(sample_input):.6f}")
    print(f"  ReLU out     : {n_relu.forward(sample_input):.6f}")

    print("\n" + "=" * 50)
    print("  PART 2 — Dense Layer (3 inputs → 4 neurons)")
    print("=" * 50)
    layer = DenseLayer(n_inputs=3, n_neurons=4, activation="relu")
    layer_out = layer.forward(sample_input)
    print(f"  Input  : {sample_input}")
    print(f"  Output : {[round(v, 6) for v in layer_out]}")

    print("\n" + "=" * 50)
    print("  PART 3 — Tiny Network (3→4→2)")
    print("=" * 50)
    net = TinyNetwork()
    hidden_out, final_out = net.forward(sample_input)
    print(f"  Input        : {sample_input}")
    print(f"  Hidden (ReLU): {[round(v, 6) for v in hidden_out]}")
    print(f"  Output (Sig) : {[round(v, 6) for v in final_out]}")
   
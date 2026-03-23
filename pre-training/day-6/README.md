# Day 6 – Build a Neuron from Scratch (No NumPy, No PyTorch)

## Script

- `neuron.py` — Implements a single neuron, a dense layer, and a tiny 2-layer network using pure Python

```
python neuron.py
```



## Part 4 – Explanations

### What does each weight represent?
Each weight controls how much one specific input influences the neuron's output.
A large positive weight amplifies that input; a large negative weight suppresses it.
A near-zero weight means the neuron mostly ignores that input.

### What does the bias do?
The bias shifts the activation threshold independently of the inputs.
Without it, a neuron can only fire when the weighted inputs push it past zero.
With bias, the neuron can fire even when all inputs are zero, or stay silent even when inputs are high.

### What changes if you use ReLU vs Sigmoid?

| | Sigmoid | ReLU |
|---|---|---|
| **Output range** | (0, 1) | (0, ∞) |
| **Use case** | Output layer, probabilities | Hidden layers |
| **Vanishing gradient** | Can cause it in deep nets | Avoids it |
| **Dead neurons** | No | Yes, if weights go too negative, neuron always outputs 0 |

In this network: **ReLU** is used in the hidden layer (layer 1) and **Sigmoid** in the output layer (layer 2).

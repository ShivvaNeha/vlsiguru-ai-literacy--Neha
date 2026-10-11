**Mission 7 — What actually runs AI?**
Objective: Understand the hardware behind AI systems.
Step 1: Answer the seven questions
1. What is a CPU?
A Central Processing Unit is a general-purpose processor that executes instructions and handles a wide variety of tasks. It is good at sequential work, control logic, operating-system tasks and coordinating other components.
2. What is a GPU, and why is it useful for AI?
A Graphics Processing Unit has many processing units designed to handle large amounts of parallel work. It is useful for AI workloads such as matrix multiplication and tensor operations, which occur extensively in neural networks.
3. What is an NPU or AI accelerator?
A Neural Processing Unit or AI accelerator is specialised hardware designed to execute common AI operations efficiently. It can improve performance per watt for supported workloads.
4. What is parallel computation?
Parallel computation means performing multiple computations at the same time. For example, instead of calculating thousands of independent values one by one, a suitable system can calculate many of them simultaneously.
5. Why does AI depend on compute and memory?
AI models perform many mathematical operations and need access to model parameters, input data and intermediate results. Computing capacity affects how quickly operations execute, while memory capacity and bandwidth affect how efficiently data reaches the processors.
6. Training versus inference
Training	Inference
The model learns from data by adjusting its parameters.	A trained model generates predictions or outputs.
Usually involves forward computation, loss calculation and parameter updates.	Uses the trained parameters to process new inputs.
Often requires substantial compute and memory.	Resource requirements depend on model size, input and workload.
7. Draw the hardware diagram
AI Application
Chatbot, image recognition or coding assistant

AI Model
Neural network and its parameters

Software / Framework
Model execution and tensor operations

Compute Hardware
CPU • GPU • AI accelerator

Memory
Stores model parameters, inputs and intermediate data

Simplified conceptual view: software schedules computation on processors, which read and write memory.

Step 2: Choose one real AI workload
Workload: Image recognition in a factory.
A factory may use a deep-learning model to identify defective components in images. A GPU or specialised AI accelerator can be useful when many images must be processed quickly. A CPU may handle image input, application logic and communication with other systems. The appropriate hardware depends on model size, throughput, latency, power consumption and cost.
Submission: Answers to all seven questions, the hardware diagram and one workload example.
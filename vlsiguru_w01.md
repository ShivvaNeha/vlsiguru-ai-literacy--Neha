**Mission 4 — Make AI explain itself, then test it**
Objective: Understand how a Large Language Model (LLM) produces an answer.
Step 1: Ask your AI assistant
Prompt 1:
Explain how an LLM produces an answer to my prompt. Copy prompt

Prompt 2:
Now explain it to me as a beginner using a simple example. Copy prompt

Step 2: Write your own explanation
An LLM is an AI model trained on large amounts of data. When a user enters a prompt, the model processes the text as tokens and uses the context to calculate probabilities for possible next tokens. It generates an answer token by token until the response ends.
For example, if I ask, "The capital of India is...", the model may assign a high probability to the token "New" followed by "Delhi". It continues generating the response based on the context.
An LLM does not simply retrieve a verified fact for every question. It generates responses based on learned patterns and the current context, so its answers can be incorrect.
Step 3: Verify two important claims
Claim	Verification source
LLMs generate text using token probabilities and next-token prediction.	Hugging Face LLM Course
Generative AI models can produce incorrect or misleading information.	NIST AI Risk Management Framework
Read the relevant sections and record what each source actually supports.
Step 4: Record one strength and one clarification
Use the following as a guide, and adjust it to reflect your own investigation:
- What AI explained well: It explained token-by-token generation using a simple example.
- What needed clarification: Saying that an LLM always selects the single most probable next word is misleading. Models may use different decoding strategies, and the generated units are tokens, not necessarily whole words.
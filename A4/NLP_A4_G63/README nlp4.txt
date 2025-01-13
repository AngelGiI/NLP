Welcome to Assignment 4 of Natural Language Processing!

We'll be using PyTorch for this assignment. If you're not familiar with PyTorch, or if you would like to review some of the fundamentals of PyTorch, there is a review notebook linked in the assignment. The Thursday TA sessions on May 11 will also go through this and answer questions. 


To create a working environment for this assignment, please run:

# 1. Create an environment with dependencies specified in local_env.yml (note that this can take some time depending on your laptop):
    
    conda env create -f local_env.yml

# 2. Activate the new environment:
    
    conda activate nlp_a4
    

# To deactivate an active environment, use
    
    conda deactivate





In essence, gradient descent is an optimization algorithm commonly used in machine learning, including neural networks. It involves iteratively adjusting the parameters of a model in the direction of steepest descent of a loss function, which measures the model's performance. This process allows the model to learn and improve its predictions over time. In the context of natural language processing (NLP), gradient descent can be applied to tasks such as sentiment analysis, text classification, or machine translation, where the goal is to find optimal parameter values that minimize the discrepancy between predicted and expected outputs, thus enhancing the accuracy and effectiveness of the NLP model.

Stochastic gradient descent (SGD) is a variant of the gradient descent optimization algorithm used in machine learning. Unlike traditional gradient descent, which computes the gradient using the entire training dataset, SGD updates the model parameters using a random subset (or a single sample) of the training data at each iteration. This randomness introduces noise, but it allows for faster convergence and makes SGD particularly useful for large-scale NLP tasks where the training data can be massive, as it enables the model to process and learn from smaller, manageable batches of data at a time.

Stochastic gradient descent (SGD) is a variant of the gradient descent algorithm commonly used in machine learning, including natural language processing (NLP) tasks. Unlike traditional gradient descent, which computes the gradient over the entire dataset, SGD randomly selects a subset (or mini-batch) of training examples to calculate the gradient at each iteration. This random sampling introduces noise but allows for faster computation and potentially better generalization, making SGD particularly useful in NLP tasks where large datasets are involved and computational efficiency is important.
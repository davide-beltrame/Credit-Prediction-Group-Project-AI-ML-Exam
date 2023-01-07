# **Group Project 268701**
## **Artificial Intelligence & Machine Learning 2022 - 2023**

### *Group Members:*
- Davide Beltrame, 268701
- Demetrio Francesco Cardile, 267281
- Mariasole Mohn, 268651

## **1) Introduction**
We have received bank details and credit-related data from the greatest financial company in the world: 
we need to help develop targeted products for their users by dividing them into 
three credit score brackets: Poor, Standard and Good. 
In the following sections we will explain how we thought of an efficient data-driven solution to tackle this problem.

## **2) Methods**

### **2.1) Required libraries and packages:**
Before running our project, install Python 3 and execute the following commands on a shell (N.B.: if your are working in a conda environment, substitute *pip* with *conda*):
> `pip install numpy`  
> `pip install pandas`  
> `pip install matplotlib`  
> `pip install seaborn`  
> `pip install sklearn`  
> `pip install xgboost`  
> `pip install python-time`  

### **2.2) Workflow**
Through exploratory data analysis we perform a deep analysis of the dataset, highlighting some interesting features, 
and trying to extrapolate as much information as possible from data.
First of all, we get a general understanding of the dataset using ad hoc *pandas* methods in order to discover its size,
the type of variables that it contains and the number of null values.
Although it may be conceived as data cleaning, we will handle missing values in exploratory data analysis 
in order to plot data and have a better understanding through visualization. 
The following strategy to handle missing values is adopted: missing values are replaced by the mode, 
both in the case of categorical and numerical data. 
To get further insights on data, we show the most interesting statistical features for each numerical variable,
such as mean, standard deviation, quartiles, minimum and maximum.
After some observations on categorical variables, given by bar plots and histograms, we remove outliers and 
eliminate the ID column, useless for statistical purposes (it is used solely to differentiate every data point).

Before any consideration over the methods we are going to use for this classification problem (our classifiers), 
we remark the importance of splitting our data into three different sets:
- Training set: as its name suggests, it is used to train the classifier. It makes up for 75% of the data points.
- Validation set. Normally, we would use this to evaluate our model and tune our hyperparameters; but in our approach
to the problem, we tune them in the training phase and we test once on the test set.
- Test set. 25% of the data points are in it.

In order to choose our models, we had to make a choice among the classification methods we have studied:
- K-Nearest Neighbours (KNN)
- Support Vector Machine (SVM)
- Kernel SVM
- Classification and Regression Tree (CART)
- Random Forests
- Artificial Neural Network (ANN)
- XGBoost

We excluded Logistic Regression because the default model is limited to binary classification problems. 
By searching on the web, we found out that an option could have been to transform the problem into a 
multiple binary classification problem. 
Nevertheless, we decided not to proceed in this way. Firstly because other more complex models would have 
very likely performed better and secondly because it seemed a process too long and complex.

Furthermore, we favoured Kernel SVM over SVM because we cannot assume linearly separable data points (a necessary condition for using appropriately linear SVM).

## **3) Experimental Design**
After building our models by calling the *sklearn* functions, we have performed the task of **hyperparameter tuning**.
Hyperparameters are the hidden (not human-interpretable) variables that determine the network structure and how the network is trained. 
Thus, the process of hyperparameter tuning has the goal of finding the best settings for the ML algorithm, that is 
the setting of hyperparameters producing the highest accuracy and lowest error rate. 
To achieve this task, we use for each model the **grid search algorithm**.
Grid search exhaustively enumerates all combinations of hyperparameters and evaluates each combination. 
Depending on the available computational resources, the nature of the learning algorithm and size of the problem,
each evaluation may take considerable time. Thus, the overall optimization process is time-consuming.

### **3.1) Evaluation metrics**
In order to determine the best models in our results, we decided to choose accuracy.

### **3.1) Hyperparameter tuning**
### K-Nearest Neighbours (KNN)
In KNN, the choices of hyperparameters are: 
- The number of neighbours: a value chosen among the set [3,5,8,10].
- The weights: a value that can vary from "uniform", where all points in each neighborhood are weighted equally,
to "distance", where closer neighbors will have a greater influence on a data point than further ones.
- The distance metric: a set of distance metrics, where not all distance metrics are taken into account
in order to reduce the computational time.

### Kernel Support Vector Machine (Kernel SVM)
In Kernel SVM, we've taken into account 3 hyperparameters:
- The kernel, which specifies the kernel type to be used in the algorithm. 
The choices are among ['linear', 'rbf', 'poly', 'sigmoid'].
- The C parameter, which adds a 'penalty' for each misclassified data point. If c is small, the penalty for 
misclassified points is low so the decision boundary has large margin while if c is large, the number of 
misclassified examples are minimized due to high penalty.
- max iterator: the limit of iterations. We set the value to 1500, so as to stop the iterations 
before convergence (time issue)

### XGBoost
XGBoost is a very powerful algorithm which provides a large range of hyperparameters. 
However, because of the limited power of our computers and because of the huge time it would have taken 
to tune all of them, we've decided to focus on the main ones:
- The maximum depth, which defines the maximum depth of a tree (this value controls over-fitting,
as higher depth will allow model to learn patterns very specific to a particular sample).
- The learning rate, which makes the model more robust by shrinking the weights on each step. 
In general, optimal values for the learning rate are in the range [0.1, 0.3]

### Classification and Regression Tree (CART)
To build the CART model, we've considered 3 hyperparameters in the tuning:
- maximum depth: the maximum depth of the tree (recall that a higher tree is more likely to overfit)
- minimum samples leaf: the minimum number of samples required to be at a leaf node
- maximum features: the number of features to consider when looking for the best split 

### Artificial Neural Network (ANN)
In building the ANN model we've tuned:
- The activation function, either 'logistic' or 'relu'.
- The learning rate_init, which is the initial learning rate used. It controls the step-size in updating the weights
It is important to state that among the hyperparameters we did not include any solver for weights optimization. 
In particular, the default one - namely “adam”, which refers to a stochastic gradient-based optimizer,
works perfectly fine with large datasets. 

## **4) Results**

Confusion matrices

Accuracy

Time complexity

- Main finding(s): report your final results and what you might conclude from your work 
- Include at least one placeholder figure and/or table for communicating your findings 
- All the figures containing results should be generated from the code.

## **5) Conclusions**
- Summarize in one paragraph the take-away point from your work.
- Include one paragraph to explain what questions may not be fully answered by your work as well as natural next steps for this direction of future work
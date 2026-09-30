# Machine Learning

This repository is a collection of small, practical machine-learning lessons. Each topic has Python examples, and most include both a Jupyter notebook and a Python script. The notebooks are a good place to start: run the cells in order, inspect the output, and change one thing at a time.

You do not need to know machine learning before you begin. Basic Python, variables, lists, and functions will help. The examples use `pandas` and `NumPy` to work with data, `scikit-learn` to train models, and `matplotlib` to make plots.

## Suggested learning path

Follow the topics in this order. The first lessons introduce prediction and model training; the final lessons explore unsupervised learning, where examples do not come with a target answer.

1. [Gradient descent](Gradient_discent/Gradient_discent_python.ipynb) - see how repeated parameter updates can reduce a model's error.
2. [Simple linear regression](Simple%20Linear%20Regression/Python/simple_linear_regression.ipynb) - predict a numeric value from one feature.
3. [Multiple linear regression](Multiple%20Linear%20Regression/Python/multiple_linear_regression.ipynb) - use several features to predict a numeric value.
4. [Logistic regression](Logistic%20Regression/Python/logistic_regression.ipynb) - predict a category, such as yes/no.
5. [K-nearest neighbors](K-Nearest%20Neighbors%20%28K-NN%29/Python/k_nearest_neighbors.ipynb) - classify an example based on nearby examples.
6. [Naive Bayes](Naive%20Bayes/Python/naive_bayes.ipynb) - learn a probabilistic classification method.
7. [Decision trees](Decision%20Tree%20Classification/Python/decision_tree_classification.ipynb) - make predictions using a sequence of feature-based decisions.
8. [Random forests](Random%20Forest%20Classification/Python/random_forest_classification.ipynb) - combine many decision trees.
9. [K-means clustering](Clustering/Section%2024%20-%20K-Means%20Clustering/Python/k_means_clustering.ipynb) - group examples into a chosen number of clusters.
10. [Hierarchical clustering](%20Hierarchical%20Clustering/Python/hierarchical_clustering.ipynb) - build and inspect a hierarchy of clusters.

## Get set up

Install Python 3 and use a virtual environment so the packages for these lessons stay separate from other projects. From the repository folder, run:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install numpy pandas matplotlib scikit-learn scipy statsmodels jupyter
```

On Windows, activate the environment with `.venv\Scripts\activate` instead of the `source` command. Install Python from [python.org](https://www.python.org/downloads/) if it is not already available.

To work through a notebook, start Jupyter from the repository folder:

```bash
jupyter lab
```

Open a lesson's `.ipynb` file in the browser, select the virtual environment as its Python kernel if asked, and run cells from top to bottom. You can also open and run notebooks in VS Code after installing its Python and Jupyter extensions.

To run a standalone script, change into that lesson's `Python` folder and run its `.py` file. For example:

```bash
cd "Decision Tree Classification/Python"
python decision_tree_classification.py
```

## Lessons and data

| Topic | Folder | Included data or materials |
| --- | --- | --- |
| Gradient descent | [`Gradient_discent`](Gradient_discent/) | Notebook and spreadsheet |
| Simple linear regression | [`Simple Linear Regression`](Simple%20Linear%20Regression/) | Salary data |
| Multiple linear regression | [`Multiple Linear Regression`](Multiple%20Linear%20Regression/) | Startup and motor data |
| Logistic regression | [`Logistic Regression`](Logistic%20Regression/) | Social network ads data |
| K-nearest neighbors | [`K-Nearest Neighbors (K-NN)`](K-Nearest%20Neighbors%20%28K-NN%29/) | Social network ads data |
| Naive Bayes | [`Naive Bayes`](Naive%20Bayes/) | Social network ads data and calculation workbook |
| Decision trees | [`Decision Tree Classification`](Decision%20Tree%20Classification/) | Social network ads data and entropy workbook |
| Random forests | [`Random Forest Classification`](Random%20Forest%20Classification/) | Python examples; social network ads data |
| K-means clustering | [`Clustering`](Clustering/) | Mall customers data |
| Hierarchical clustering | [`Hierarchical Clustering`](%20Hierarchical%20Clustering/) | Mall customers data |

CSV files are kept with their related lessons. Open the notebook or script from its lesson folder so relative data paths resolve as expected. The standalone scripts for simple linear regression, multiple linear regression, logistic regression, and K-means currently contain absolute paths from another computer. Replace those paths with the included data files (`Salary_Data.csv`, `50_Startups.csv`, `motor_data.csv`, and `Mall_Customers.csv`, respectively). The `motor_data.csv` file is in the Multiple Linear Regression folder, not the Logistic Regression folder; check that a dataset's columns fit the script before substituting it. The notebooks do not have this known absolute-path issue.

## Case studies and projects

Use the links in [Case_studies_links.docx](Case_studies_links.docx) to find case studies you can explore as independent projects. For each one, define the question, inspect and prepare the data, choose a suitable method from the lessons, evaluate the results, and explain the limits of your conclusions.

## Make the most of each example

- Before running the model, identify the input features and the value or category it is trying to predict. In clustering lessons, look for how the groups are formed instead.
- Run each notebook cell in order and read the code as well as the output. Try changing a feature, model setting, or plot label and observe what changes.
- For prediction tasks, distinguish training data from test data. Evaluate predictions on held-out test data rather than relying only on training accuracy.
- Treat plots and scores as evidence about these particular data, not proof that a model will work equally well on new data.
- If an import fails, confirm the notebook or script is using the environment where you installed the packages.

These are learning examples, not a single packaged application. Some scripts are older teaching drafts and may need small adjustments to run in a different environment; use the notebooks and the included data as your guide.

### Full-Stack Machine Learning Model

The objective of this project is to build a basic machine learning model and create an API around the model that can be hosted on the Internet. 

* Use Iris dataset to build a classification model to predict the type of Iris, based on the leaf characteristics. The Iris dataset is part of the `scikit-learn` library and is where we will access the data from.

* Build one or two classification models using sklearn and turn each to optimize using **grid search**. Use **10-fold cross** validation to ensure that the model is able to generalize well. 

* "Pickle" the model file.

* Load `pkl` file and make a prediction from the saved `pkl` file. 

* Build a flask API that will take in the leaf measurements and make a prediction using the `pkl` file. 

* Once the flask API is built and working on the local machine, we will push the API onto Heroku.

* With a working API that can be called, we will then make a simple front end that will take values in from a form, pass the data to the API, retrieve the result and render the result to the page.

* The final working front end will also be pushed onto Heroku.

---

### Workplan for Front End 

* Create a bootstrap form with four (4) text boxes. These four boxes will correspond to the four leaf characteristics of the Iris sample.

* Also create a submit button on the form.

* Once data is in the form, and the submit button, the app will get the data in the form and create the proper connection string for the API:

	`/prediction?sepallen={}&sepalwid={}&petallen={}&petalwid={}`
	
* Once the API returns the JSON, the app will need to modify the inner HTML and parse the JSON and render the results to the screen. We will need to format the decimal values of the class probabilities for readability once rendered to the screen.

---

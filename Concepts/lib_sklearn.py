from sklearn import linear_model

reg = linear_model.LinearRegression()
reg.fit([[0,0], [1,1], [2,2]], [0,1,2])
reg.coef_




# Ref : https://scikit-learn.org/stable/modules/linear_model.html
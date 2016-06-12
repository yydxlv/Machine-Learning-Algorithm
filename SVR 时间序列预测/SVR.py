from sklearn.svm import SVR

svr_rbf = SVR(kernel='rbf', C=1, gamma=0.5)
# and now train the model
# batch_size should be appropriate to your memory size
# number of epochs should be higher for real world problems
svr_rbf.fit(X_train, y_train)

predicted = model.predict(X_test)
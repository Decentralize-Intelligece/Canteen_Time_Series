print("Canteen..\n")

print("1. Train")
print("2. Predict")
print("3. Learn")
print("4. Exit")

choice = int(input("Enter your choice: "))


# parameters : data_path, canteen_name
def train(data_path, canteen_name):
    # get the data from the data_path
    # load the model
    # train the model
    # save the model
    pass


def predict(last_X_day_data_path, canteen_name):
    # get the data from the last_X_day_data_path
    # load the model
    # predict
    # save the prediction
    # print the prediction
    pass


def learn(canteen_name, savedPrediction, savedRealSales, pathToTheNewModel):
    # load the model
    # load the savedPrediction
    # load the savedRealSales
    # learn
    # save the new model
    pass


if choice == 1:
    print("Training the model...")
    train("data", "canteenC")
elif choice == 2:
    print("Predicting the model...")
    predict("data", "canteenC")
elif choice == 3:
    print("Learning the model...")
    learn("canteenC", "savedPrediction", "savedRealSales", "pathToTheNewModel")
elif choice == 4:
    print("Exiting the program...")
    exit()
else:
    print("Invalid choice")
    exit()

# other processess

# Save each transaction in a file (How this task need to be performed) or X days data in a file
#

# data
# canteenData
# Temp Data - for a week
# In a specific day turn the data into a file and perform the training or learning

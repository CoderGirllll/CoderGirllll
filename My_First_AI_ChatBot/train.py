import numpy
import json, torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from nltk_utils import bag_of_words, tokenize, stem
from model import NeuralNet

with open("My_First_AI_ChatBot\intents.json", 'r') as f:
    intents = json.load(f)

all_words = []
tags = []
xy = []
#Loop through each sentence in our intents patterns
for intents in intents["intents"]:
    tag = intents["tag"]
    #add to tag list
    tags.append(tag)
    for pattern in intents["patterns"]:
        #tokenize each word in the sentence
        w = tokenize(pattern)
        #add to our words list
        all_words.extend(w)
        #add to xy pair
        xy.append((w, tag))

#stem and lower each word
ignore_words = ['?', '.', '!']
all_words = [stem(w) for w in all_words if w not in ignore_words]
#remove duplicates and sort
all_words = sorted(set(all_words))
tags = sorted(set(tags))

print(len(xy), "patterns")
print(len(tags), "tags:", tags)
print(len(all_words), "unique stemmed words:", all_words)

#create training data
X_train = []
Y_train = []
for (pattern_sentence, tag) in xy:
    #X: bag of words for each pattern_sentence
    bag = bag_of_words(pattern_sentence, all_words)
    X_train.append(bag)
    #Y: PyTorch CrossEntropyLoss needs onyl class labels
    label = tags.index(tag)
    Y_train.append(label)

X_train = numpy.array(X_train)
Y_train = numpy.array(Y_train)

#hyper-parameters
num_epochs = 1000
batch_size = 8
learning_rate = 0.001
input_size = len(X_train[0])
hidden_size = 8
output_size = len(tags)
print(input_size, output_size)

class ChatDataset(Dataset):
    def __init__(self):
        self.n_samples = len(X_train)
        self.x_data = X_train
        self.y_data = Y_train

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]
    
    #We can call len(dataset) to return the size
    def __len__(self):
        return self.n_samples
    
dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset,
                          batch_size=batch_size,
                          shuffle=True,
                          num_workers=0)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = NeuralNet(input_size, hidden_size, output_size).to(device)
#loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
#train the model
for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(dtype=torch.long).to(device)
        #forward pass
        outputs = model(words)
        #if y would be one-hot, we must apply
        #labels = torch.max(labels, 1)[1]
        loss = criterion(outputs, labels)
        #backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    if (epoch+1) % 100 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

print(f'final loss: {loss.item():.4f}')
data = {
    "model_state": model.state_dict(),
    "input_size": input_size,
    "hidden_size": hidden_size,
    "output_size": output_size,
    "all_words": all_words,
    "tags": tags
}
FILE = "chatdata.pth"
torch.save(data, FILE)
print(f'training complete. file saved to {FILE}')

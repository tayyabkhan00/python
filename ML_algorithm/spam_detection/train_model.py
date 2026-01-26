import pandas as pd

df = pd.read_csv("/Users/tayyabkhan/python/ML_algorithm/spam_detection/data/spam.csv", encoding="latin-1")
df = df[["v1", "v2"]]
df.columns = ["label", "message"]

df.head(10)

df.info()
df["label"].value_counts()

df[df["label"] == "spam"].head(5)["message"]


import re
import string

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.strip()

df["clean_message"] = df["message"].apply(clean_text)
df.head()

df["label"] = df["label"].map({"ham": 0, "spam": 1})

from sklearn.model_selection import train_test_split

X = df["clean_message"]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(
    stop_words="english",
    max_features=5000
)

X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)


from sklearn.svm import LinearSVC

model = LinearSVC()
model.fit(X_train_tfidf, y_train)


from sklearn.metrics import classification_report, confusion_matrix

y_pred = model.predict(X_test_tfidf)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))


import pickle

pickle.dump(model, open("/Users/tayyabkhan/python/ML_algorithm/spam_detection/model/spam_model.pkl", "wb"))
pickle.dump(tfidf, open("/Users/tayyabkhan/python/ML_algorithm/spam_detection/model/tfidf.pkl", "wb"))

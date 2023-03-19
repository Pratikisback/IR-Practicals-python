import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
corpus = ['this is doc one', 'this is doc two', 'and this is third doc']
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
print("fit transfrom is")
print(X.toarray())

#Till here we transformed the document into index form

df = pd.DataFrame(X.toarray(),columns=vectorizer.get_feature_names_out())
print(df)

alldata = df[(df['this']==1) & (df['is']==1)]
print("indices where both terms are present", alldata.index.tolist())

ordata = df[(df['this']==1) | (df['is']==1)]
print("indices where any of the terms are present", ordata.index.tolist())

notdata = df[(df['and']!=1) ]
print("indices where both terms are present", alldata.index.tolist())
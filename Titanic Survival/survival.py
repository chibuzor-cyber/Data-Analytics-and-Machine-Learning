import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('titanic.csv')

#print(df.head())
#print(df.info())
#print(df.describe())
#print(df.isnull().sum())


#Filling missing "age" with Meadian
#df['Age'].fillna(df['Age'].median(), inplace=True)

#fill missing 'embarked' with mode
#df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

#filling missing 'Cabin' with 'unkown
#df['Cabin'].fillna(df['Cabin'].mode()[0], inplace=True)


#print(df.isnull().sum())

#Univariate analysis
#sns.countplot(x='Sex', data=df, palette='deep')
#plt.title('Gender Distribution on Titanic')
#plt.show()

#Age distribution
#sns.histplot(df['Age'], bins=30, kde=True, color= 'blue')
#plt.title('Age Distribution on Titanic')
#plt.show()

#Gender vs Survival
#sns.countplot(x='Sex', hue='Survived', data=df, palette='deep')
#plt.title('Survival by Gender')
#plt.show()

#Age vs Survival
#sns.boxplot(x='Survived', y='Age', data=df, palette='dark')
#plt.title('Age vs Survival')
#plt.show()


#Correlation Analysis

#titanic_corr = df[['Age', 'Fare', 'Survived']].corr()

#sns.heatmap(titanic_corr, annot=True, cmap='coolwarm')
#plt.title('correlation Heatmap')
#plt.show()

#Feature Engineering
df['Family_size'] = df['SibSp'] + df['Parch'] + 1

#create age group
df['Age_Group'] = pd.cut(df['Age'],
                         bins=[0, 12, 18, 35, 65, 85],
                         labels=['child', 'Teen', 'Young adult', 'Adult', 'Senior'])
df[['Age', 'Age_Group', 'Family_size']].head()
df.head()

#Encoding Categorical Features
titanic_encoded = pd.get_dummies(df, columns=['Sex', 'Pclass', 'Embarked', 'Age_Group'], drop_first=True)
print(titanic_encoded.head())


#IQR Method
Q1 = df['SibSp'].quantile(0.25)
Q3 = df['SibSp'].quantile(0.75)
print('Q1:', Q1)
print('Q3:', Q3)

IQR = Q3 - Q1
print(IQR)

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
print('lower bond:', lower, 'upper bond:', upper)

#Final visualization
plt.figure(figsize=(10, 6))
sns.barplot(x='Age_Group', y='Survived', hue='Sex', palette='Blues', data=df)
plt.title('Survived by Age_Group')
plt.show()

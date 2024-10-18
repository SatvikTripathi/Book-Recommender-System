# Book-Recommender-System
This project is focussed on developing a book recommender system based on two recommender systems:

+ **Popularity-Based Recommender**
+ **Collaborative Filtering Based Recommender**

The model is trained on [book-recommendation-dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset) which contains **1,149,780 ratings** (explicit / implicit) on **271,379 books** by **278,858 users**.

## Popularity-Based Recommender

A popularity-based recommender system is used to suggest the most popular items based on their overall populartiy across users, without considering individual user preferences. In this project, we are displaying **Top 100** most popular books based on their ratings. A popularity-based system does not tailor recommendations to individual user preferences which are helpful in the following scenarios:
+ For New Users
+ Recommending Trending Items
+ Cold Start

![book recommender system_top 100 page](https://github.com/user-attachments/assets/247ca0dc-d70e-418e-8207-4e637f7cb57e)

## Collaborative Filtering Based Recommender

A collaborative filtering based recommender system uses an algorithm that makes predictions about a user's interests by collecting preferences, in this project, ratings, from many other users. And items which are liked by (with high ratings) similar users are recommended to the user.

We have used Item-Based Collaborative Filtering, in which, the system finds items that are similar to those the user has interacted with in the past and recommends them by calculating similarities between items based on the users who have rated or interacted with them.

This system is helpful in the following scenarios:
+ Cold Start Problem
+ Sparsity
+ Scalability

![book recommender system_recommender page](https://github.com/user-attachments/assets/2b4278be-d1a4-402b-80e8-f9e962de8136)


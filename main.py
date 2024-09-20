from book_recommender.recommender import get_book_recommendation

def main():
    print("Welcome to the Book Recommender!")
    user_preferences = input("Please enter your book preferences: ")
    
    recommendation = get_book_recommendation(user_preferences)
    
    if recommendation:
        print("\nBased on your preferences, here's a book recommendation:")
        print(f"Title: {recommendation.title}")
        print(f"Author: {recommendation.author}")
        print(f"Genre: {recommendation.genre}")
        print(f"Published in: {recommendation.publication_year}")
        print(f"\nSummary: {recommendation.summary}")
        print("\nReasons for recommendation:")
        for reason in recommendation.reasons:
            print(f"- {reason}")
    else:
        print("Sorry, we couldn't generate a recommendation at this time.")

if __name__ == "__main__":
    main()
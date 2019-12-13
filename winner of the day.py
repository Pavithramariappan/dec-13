def find_winner_of_the_day(*match_tuple):
    count=match_tuple.count("Team1")
    if count>1:
        print("Team1")
    count=match_tuple.count("Team2")
    if count>1:
        print("Team2")
    count=match_tuple.count("Team3")
    if count>1:
        print("Team3")   
        pass
#Invoke the function with each of the print statements given below
print(find_winner_of_the_day("Team1","Team2","Team1"))
#print(find_winner_of_the_day("Team1","Team2","Team2","Team1","Team2"))

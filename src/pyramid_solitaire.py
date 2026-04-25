#PS 1st CP2 Final - Pyramid Soliaire source code

#import shuffle function
#import csv management functions
#import JSON reader func

#setup function
    #call shuffle function to return a randomized list
    #create 7 lists for each row of the pyramid and put those inside another creating a matrix
    
    #count each iteration of the loop to determine number of cards in each row
    #Loop for every row (7 times)
        #put one card in row one and then 2 cards and row to and so on

    #DISPLAY TABLEU - have each row slightly offsetted
    #output tableu, discard pile (empty), draw pile

#Accessible cards function (tableu list)
    
    #for each row
        #check if there is a row above it
        
        #if there is
            #for each card in current row,
                #save each of the indexes in a dict that is formatted like this: dictname:{top_row_allowable:{card1:[0,1]},second:{card2:[0,1],card3:[1,2]} etc. etc. (see activity diagram for what indexes mean)
    
    #output the dictionary

#valid Combo Function (card1_id,card2_id,list_of_cards)
    #get both of the dictionaries for the cards in the JSON
    
    #if card1[value] + card2[value] == 13:
        #pop those ids out of the tableu add them to the discard pile
    #else:
        #display invalid value error

#Options funcs


#Gameloop (actual game)
    #call setup and save returned values
    #call accessibility function and save the dict
    
    #actual gameloop
        #allow user to click button to choose type of move to do
        #check if tableu is gone
        #if yes
            #leave gameloop
        #else
            #continue
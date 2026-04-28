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

    #put the rest of the cards in the draw pile list

    #DISPLAY TABLEU - have each row slightly offsetted
    #output tableu, discard pile (empty), draw pile, shown draw pile

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

#draw card function (draw pile, shown draw pile)
    #check if draw pile has cards in it
    # if yes
        #remove card from draw pile and add it shown draw pile and display that card face up
    #if no
        #make draw pile equal to shown and then clear shown
        #reverse order of draw pile to represent flipping of pile over

        #remove card from draw pile and add it shown draw pile and display that card face up

#Discard King function (tableu, discard pile, shown draw pile)
    #call accessibility function for accessible cards
    #allow user to select a card that is accessible
    
    #check if the card is a king
    
    #if yes
        # if card is in tableu
            #remove from tableu
        #else
            #remove from draw
        #add to discard pile
    #if no
        #display error message stating that the card selected was not a king


#matching check (card1, card2)
    #use JSON reading to get values of card1 and card2
    #if card1[value] + card2[value] is = 13
        #output True
    #else
        #output false

#Matching inside tableu (tableu, discard pile, shown draw pile)
    #call acessiblility function
    # allow user to select any valid card from tableu
    # allow user to select another card
    # call matching check (card1, card2)
    #if matching check is True
        #remove cards from tableu
        #add cards to discard pile
    #else
        #display invalid match (values)

#matching from draw pile and tableu (tableu, discard pile, shown draw pile)
    #call accessibility function
    # allow user to select a card from tableu   
    # use card from the top of shown draw pile
    # call matching check (tableu card, draw pile card)
    #if matching cards check is True
        #Remove card from tableu
        #remove card from draw pile
        #add both to discard pile
    #else 
        #display invalid match (values)


#Gameloop (setup variables)
    #call setup and save returned values
    #call accessibility function and save the dict
    
    #actual gameloop

        #allow user to click button to choose type of move to do
        #onclick of draw card button
            #call draw cards function
        #onclick of discard king button
            #call draw cards function
        #onclick of matching inside tableu button
            #call corresponding function
        #onclick of matching from draw and tableu
            #call corresponding function
        
        #update display

        #check if tableu is gone
        #if yes
            #leave gameloop
            #save game number and win
        #else
            #continue

        #If user clicks the quit button
            #leave gameloop
            #save game number and lose
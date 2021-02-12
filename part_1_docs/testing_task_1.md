### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

  #missing an __init__ function


  def check_for_ace(self, card):
    #line 22 missing equal sign, should be ==1
    if card.value = 1:
      return True
    #line 25 missing colon after else
    else
      return False
   
  #line 30 spelling mistake, should be def, not dif
  #line 30 comma missing between card1 and card2 in brackets
  dif highest_card(self, card1 card2):
  #lines 32 to 35 should be indented
  if card1.value > card2.value:
  #line 36 should return card1
    return card
  else:
    return card2

#lines 41 to 47 need to be indented
def cards_total(self, cards):
#line 43 total needs to be assigned a value
  total
  for card in cards:
    total += card.value
    #line 47 should have a space after 'of' in the string, the return needs to have the same indentation as the for loop and the total needs to parsed to a string
    return "You have a total of" + total
  
```

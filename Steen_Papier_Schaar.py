#Namen van de spelers:
naam1 = input("Naam speler 1: ")
naam2 = input("Naam speler 2: ")

score1 = 0
score2 = 0 

rondes = int(input("Hoeveel rondes willen jullie spelen?"))

for ronde in range(1, rondes + 1):
#Hun zet:
  zet1 = input(naam1 + " kies uit: steen, papier of schaar:")
  zet2 = input(naam2 + " kies uit: steen, papier of schaar:")
  
  #Als hun keuzes gelijk zijn:
  if zet1 == zet2:
    score2 = int(score2) + 1 
    score1 = int(score1) + 1 
    print("Het is gelijkspel!", naam1, ", je hebt nu:", score1, "punt(en) en", naam2, ", je hebt nu:", score2, "punt(en)")
  
  #Als een keuze of beide keuzes geen optie zijn:
  a_list = ["steen", "papier", "schaar"]
  if zet1 not in a_list or zet2 not in a_list:
    print("Oeps, dit was geen optie, probeer het nog eens.")
  
  #Als het steen tegen papier is:
  if zet1 == "steen" and zet2 == "papier":
    score2 = int(score2) + 1 
    print(naam2, "wint!!", naam2, ", je hebt nu:", score2, "punt(en)")

  #Als het papier tegen steen is:
  if zet1 == "papier" and zet2 == "steen":
    score1 = int(score1) + 1
    print(naam1, ", gefeliciteerd! Je hebt gewonnen!!", naam1, ", je hebt nu:", score1, "punt(en)")
    
  #Als het schaar tegen papier is:
  if zet1 == "schaar" and zet2 == "papier":
    score1 = int(score1) + 1
    print(naam1, ", je hebt", naam2, "verslagen!!", naam1, ", je hebt nu:", score1, "punt(en)")
  
  #Als het papier tegen schaar is:
  if zet1 == "papier" and zet2 == "schaar":
    score2 = int(score2) + 1 
    print(naam2, "Hoera! Je hebt gewonnen!", naam2, ", je hebt nu:", score2, "punt(en)")
  
  #Als het steen tegen schaar is:
  if zet1 == "steen" and zet2 == "schaar":
    score1 = int(score1) + 1 
    print(naam1, "je bent nummer 1!", naam1, ",je hebt nu:", score1, "punt(en)")
  
  #Als het schaar tegen steen is:
  if zet1 == "schaar" and zet2 == "steen":
    score2 = int(score2) + 1 
    print(naam2, "je bent de beste!", naam2, ",je hebt nu:", score2, "punt(en)")

#Als speler2 gewonnen heeft:
if score1 < score2:
  print(naam2, ", je hebt dit spel met", score2, ":", score1, "gewonnen!")

#Als speler 1 gewonnen heeft: 
if score1 > score2:
  print(naam1, ", je hebt dit spel gewonnen met", score1, ":", score2)

#Als het gelijkspel is:
if score1 == score2:
  print("Jullie hebben dit spel beide", score1, "punten gehaald!")
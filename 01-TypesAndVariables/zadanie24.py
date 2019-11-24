# przeliczanie wzrostu na stopy i cale 
cm = 165
template = cm/30.48

feet = int(template)
inch = int((template - feet)*10)

print("Mam " + str(cm) + " cm wzrostu, to jest " + str(feet) + " stóp i " + str(inch) + " cali.")

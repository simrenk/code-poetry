import string

#love letters to the people in my life
def give_love(people):
    print("How is your heart today? Kya haal hain?")
    #family
    if (people == "Papa" or people == "Mama" or people == "Amar Bhai" \
       or people == "Nanu" or people == "Nani" or people == "Dada" or people == "Dadi"):
       print("If the molecules of our blood collided, they would vibrate at the same frequency. \n\
              We are one. \n\
              Thank God we are One.")
    if (people == "Papa" or people == "Mama"):
        print("Thank you for raising me to be strong. I owe everything in me to you")
    if (people == "Amar Bhai"):
        print("I know we don't talk much but I love you, I really do. \n\
                There is something so powerful in you that I don't know how to conceive of it.")
    if (people == "Nanu"):
        print("I think of you as the equal and opposite force on the other side of the world that counteracts me. You make sure I don't float away.\n\
                I will always, always want to be just like you. \n\
                    Thank you for the gentle stoicism, for the love. I am proud to be who I am because of you. ")
    if (people == "Nani"):
        print("You're the most innocent person I know. Thank you for being unadulterated joy.")
    if (people == "Dada"):
        print("I still cry when I think of you sometimes. I dreamt of you in white light the night you died. \n\
                I relayed your message from that night -- Dad knows you love him. \n\
                    You know, I think you completed Amar Bhai with your love. He's still searching without it.\n\
                        But I promise you, we, the Kshetrapals, are still good – I didn't lie to you. Stay where you are, in peace. \n\
                            I wish I had my current brain three years ago. Maybe then I would understand how you were you so soft but so hard at the same time. \n\
                                It would have been a privilege to truly know you.")
    if (people == "Dadi"):
        print("I don't think I can quite fathom how strong you are.\n\
                You etch the art of persistence into the Delhi dust with every one of your 6am walks \n\
                    The Kshetrapal resilience is all you. \n\
                        I am sorry you are alone. I will call more.")
    #chosen family
    elif (people == "David" or people == "Daisy" or people == "Maya" or people == "Kunal" or people == "Sam" or people == "Zachary" or people == "Alexandra" or people == "Daniel" \
        or people == "Chaise" or people == "Christian" or people == "Gage" or people == "Ana" or people == "Charlotte" or people == "Josephine" or people == "Mia"):
        print("Now, you, are my chosen family.")
        if (people == "David"):
            print("Isn't it funny how four more years of college became just one more quarter? \n\
                    Thank you for being my prom date, my best friend, code collaborator extraordinairre \n\
                        Since you always know the answer, answer me this: how am I going to do the next four years without you? \n\
                            I already miss you")
        if (people == "Daisy"):
            print("How are you so free? \n\
                    You are the girl in novels, with the sun always shining in her hair, with the belligerent, awe-inspiring desire to Live with a capital L")
        if (people == "Daniel"):
            print("I don't think you know how much a part of me you are. \n\
                    Sometimes, when my mind wanders, I'm with you in the back of your car (age 17, 18, 20). \n\
                     You're the song I can't get out of my head -- maybe because we keep dancing to it like we keep dancing through time – elusive, undefined. \n\
                         But one day, when we are less than 50 miles apart, I will put flowers in your hair and weep at the softness of it.")
        if (people == "Chaise"):
            print("I will never not be sorry for breaking your heart. \n\
                    But dear God, I hope you know I will still fight for you like I will fight for my boys, like I fight against my alarm clock every morning. \n\
                        You are, by far, the best person I know.")
        if (people == "Christian"):
            print("I know you see me, because in so many ways we are the same. \n\
                    I promise I need you. I promise you are so worthy of love.")
        if (people == "Gage"):
            print("Please stay alive. \n\
                    I want you to meet my future kids. I want to meet your future kids. \n\
                        I'm sorry I said I would never forgive you if you killed yourself. \n\
                            I will. I promise I will. Because I can't pretend that I get it. \n\
                                 But I love you. And I want you around always – for the concerts and all the places we haven't seen yet. \n\
                                     I will carry you on my back if I need to.")
        if (people == "Ana"):
            print("I think you see me the way that I want to be seen. \n\
                Thank you for seeing the good in me and pressing it into all of the gaps in my personality. \n\
                    You make me feel safe. And I love you.")
#pure thoughts only
def nothing_but_love():
    print("I would do anything for you. \n")

#the final solution to all
def run_dance_and_be():
    print("I've been running for a while, but I'll be at The Point 3 minutes after sunset. \n\
            Meet me in the afterglow and help me find the green in the pastel stripes streaking across the sky? \n\
                I swear I'll love you now (as the sun snaps off and you are my only light left) and always. With everything in me.")
#the primary function//the hazy guidelines of my life
def how_to_live(all_i_need):
    my_loved_ones = all_i_need
    for people in my_loved_ones:
        print(people, end='\n')
        give_love(people)
        nothing_but_love()
    run_dance_and_be()

all_i_need = ["Papa", "Mama", "Amar Bhai",
               "Nanu", "Nani", "Dada", "Dadi",
               "David", "Daisy", "Maya", "Kunal", "Sam", "Zachary", "Alexandra", "Daniel",
               "Chaise", "Christian", "Gage", "Ana", "Charlotte", "Josephine", "Mia"]
how_to_live(all_i_need)               

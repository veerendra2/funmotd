#!/usr/bin/python3

all_quotes = {
    "game_of_thrones": [
        [
            {"quote": "Nothing fucks you harder than time.", "character": "Davos Seaworth", "name": "Game of Thrones"},
            {"quote": "What is dead may never die... but kill the bastards anyway.", "character": "Yara", "name": "Game of Thrones"},
            {"quote": "Why are all the gods such vicious cunts? Where's the god of tits and wine?", "character": "Tyrion", "name": "Game of Thrones"},
            {"quote": "It's a shame the throne isn't made out of cocks, they'd have never got him off it.", "character": "Jaime Lannister", "name": "Game of Thrones"},
            {"quote": "I understand that if any more words come pouring out your cunt mouth, I'm gonna have to eat every fucking chicken in this room.", "character": "The Hound", "name": "Game of Thrones"},
        ],
        [
            {"quote": "The man who passes the sentence should swing the sword.", "character": "Ned Stark", "name": "Game of Thrones"},
            {"quote": "The things I do for love.", "character": "Jaime Lannister", "name": "Game of Thrones"},
            {"quote": "When you play the game of thrones, you win or you die.", "character": "Cersei Lannister", "name": "Game of Thrones"},
            {"quote": "I grew up with soldiers. I learned how to die a long time ago.", "character": "Ned Stark", "name": "Game of Thrones"},
            {"quote": "Never forget what you are. The rest of the world will not. Wear it like armour, and it can never be used to hurt you.", "character": "Tyrion Lannister", "name": "Game of Thrones"},
            {"quote": "Everyone is mine to torment.", "character": "Joffrey Lannister", "name": "Game of Thrones"},
            {"quote": "The day will come when you think you are safe and happy, and your joy will turn to ashes in your mouth.", "character": "Tyrion Lannister", "name": "Game of Thrones"},
            {"quote": "The night is dark and full of terrors.", "character": "Melisandre", "name": "Game of Thrones"},
            {"quote": "You know nothing, Jon Snow.", "character": "Ygritte", "name": "Game of Thrones"},
            {"quote": "Night gathers, and now my watch begins", "character": "Various members of the Night's Watch", "name": "Game of Thrones"},
            {"quote": "A Lannister always pays his debts.", "character": "Various Lannisters", "name": "Game of Thrones"},
            {"quote": "Burn them all!", "character": "Aerys II Targaryen", "name": "Game of Thrones"},
            {"quote": "What do we say to the God of death?", "character": "Syrio Forel", "name": "Game of Thrones"},
            {"quote": "There's no cure for being a cunt.", "character": "Bronn", "name": "Game of Thrones"},
            {"quote": "Winter is coming", "character": "Various Starks", "name": "Game of Thrones"},
            {"quote": "That's what I do: I drink and I know things.", "character": "Tyrion Lannister", "name": "Game of Thrones"},
            {"quote": "I am the dragon's daughter, and I swear to you that those who would harm you will die screaming.", "character": "Daenerys Targaryen", "name": "Game of Thrones"},
            {"quote": "A lion does not concern himself with the opinion of sheep.", "character": "Tywin Lannister", "name": "Game of Thrones"},
            {"quote": "Chaos isn't a pit. Chaos is a ladder.", "character": "Littlefinger", "name": "Game of Thrones"},
            {"quote": "Power resides where men believe it resides. It's a trick; a shadow on the wall.", "character": "Varys", "name": "Game of Thrones"},
            {"quote": "If you think this has a happy ending, you haven't been paying attention.", "character": "Ramsay Bolton", "name": "Game of Thrones"},
            {"quote": "If you ever call me sister again, I'll have you strangled in your sleep.", "character": "Cersei Lannister", "name": "Game of Thrones"},
            {"quote": "A girl is Arya Stark of Winterfell. And I'm going home.", "character": "Arya Stark", "name": "Game of Thrones"},
            {"quote": "Any man who must say 'I am the King' is no true King.", "character": "Tywin Lannister", "name": "Game of Thrones"},
            {"quote": "Jaime... my name's Jaime.", "character": "Jaime Lannister", "name": "Game of Thrones"},
            {"quote": "I read it in a book.", "character": "Samwell Tarly", "name": "Game of Thrones"},
            {"quote": "If I fall, don't bring me back.", "character": "Jon Snow", "name": "Game of Thrones"},
            {"quote": "Hold the door!", "character": "Hodor", "name": "Game of Thrones"},
            {"quote": "There's no shame in fear, my father told me, what matters is how we face it.", "character": "Jon Snow", "name": "Game of Thrones"},
            {"quote": "Love is poison. A sweet poison, yes, but it will kill you all the same.", "character": "Cersei Lannister", "name": "Game of Thrones"},
            {"quote": "What good is this, I ask you? He who hurries through life hurries to his grave.", "character": "Davos", "name": "Game of Thrones"},
            {"quote": "Old stories are like old friends, she used to say. You have to visit them from time to time.", "character": "Bran", "name": "Game of Thrones"},
            {"quote": "The greatest fools are ofttimes more clever than the men who laugh at them", "character": "Tyrion", "name": "Game of Thrones"},
            {"quote": "History is a wheel, for the nature of man is fundamentally unchanging.", "character": "Lord Rodrik", "name": "Game of Thrones"},
            {"quote": "Knowledge is a weapon, Jon. Arm yourself well before you ride forth to battle.", "character": "Samwell", "name": "Game of Thrones"},
            {"quote": "Every man should lose a battle in his youth, so he does not lose a war when he is old.", "character": "Victarion Greyjoy", "name": "Game of Thrones"},
            {"quote": "The man is as useless as nipples on a breastplate.", "character": "Cersei Lannister", "name": "Game of Thrones"},
            {"quote": "It's not easy being drunk all the time. If it were easy, everyone would do it.", "character": "Tyrion", "name": "Game of Thrones"},
            {"quote": "Burn them all!", "character": "Aerys II Targaryen", "name": "Game of Thrones"},
            {"quote": "When people ask you what happened here, tell them the North remembers. Tell them winter came for House Frey.", "character": "Arya", "name": "Game of Thrones"},
            {"quote": "There is only one war that matters. The Great War. And it is here.", "character": "Jon Snow", "name": "Game of Thrones"},
            {"quote": "... a mind needs books as a sword needs a whetstone, if it is to keep its edge.", "character": "Tyrion", "name": "Game of Thrones"},
            {"quote": "A mad man sees what he sees.", "character": "Ned Stark", "name": "Game of Thrones"},
            {"quote": "The next time we see each other, we'll talk about your mother. I promise.", "character": "Ned Stark", "name": "Game of Thrones"},
            {"quote": "I've made many mistakes in my life, but that wasn't one of them.", "character": "Ned Stark", "name": "Game of Thrones"},
            {"quote": "I know the truth Jon Arryn died for.", "character": "Ned Stark", "name": "Game of Thrones"},
            {"quote": "You want a whore? Buy one. You want a queen, earn her.", "character": "Cersei", "name": "Game of Thrones"},
            {"quote": "You don't know any other rich girls.", "character": "Arya Stark", "name": "Game of Thrones"},
            {"quote": "Look at you! You're a man!", "character": "Jon Snow", "name": "Game of Thrones"},
            {"quote": "I'm no king, but if I were. I'd knight you ten times over.", "character": "Tormund", "name": "Game of Thrones"}
        ]
    ],
    "friends": [
        [

        ],
        [
            {'quote': 'Pivot! Pivot! Pivot! Pivot! Pivot!', 'character': 'Ross', "name": "Friends"},
            {'quote': "Joey doesn't share food!", 'character': 'Joey', "name": "Friends"},
            {'quote': 'Guys can fake it? Unbelievable! The one thing that\'s ours!', 'character': 'Monica', "name": "Friends"},
            {'quote': "It's a moo point. It's like a cow's opinion; it doesn't matter. It's moo.", 'character': 'Joey', "name": "Friends"},
            {'quote': "Yeah, that's right. I stepped up! She's my friend and she needed help. And if I have to I'd pee on any one of you.", 'character': 'Joey', "name": "Friends"},
            {'quote': "But they don't know that we know they know we know!", 'character': 'Phoebe', "name": "Friends"},
            {'quote': 'This is brand-new information!', 'character': 'Phoebe', "name": "Friends"},
            {'quote': "Phoebe. That's P, as in Phoebe, H as in hoebe, O as in oebe, E as in ebe, B as in bebe, and E as in 'Ello there mate.", 'character': 'Phoebe', "name": "Friends"},
            {'quote': "I'm not so good with the advice. Can I interest you in a sarcastic comment?", 'character': 'Chandler', "name": "Friends"},
            {'quote': 'I got off the plane.', 'character': 'Rachel', "name": "Friends"},
            {'quote': 'How you doin?', 'character': 'Joey', "name": "Friends"},
            {'quote': 'We were on a break!', 'character': 'Ross', "name": "Friends"},
            {'quote': "I grew up in a house with Monica, okay. If you didn't eat fast, you didn't eat.", 'character': 'Ross', "name": "Friends"},
            {'quote': 'Unagi.', 'character': 'Ross', "name": "Friends"},
            {'quote': "Smelly cat, smelly cat, what are they feeding you? Smelly cat, smelly cat, it's not your fault.", 'character': 'Phoebe', "name": "Friends"},
            {'quote': "Just so you know, it's not that common, it doesn't happen to every guy, and it is a big deal!", 'character': 'Rachel', "name": "Friends"},
            {'quote': 'Here come the meat sweats.', 'character': 'Joey', "name": "Friends"},
            {'quote': "Look at me! I'm Chandler! Could I be wearing any more clothes?!", 'character': 'Joey', "name": "Friends"}
        ]
    ],
    "breaking_bad": [
        [
            {"quote": "Jesus! Just grow some fucking balls!", "character": "Walter White", "name": "Breaking Bad"},
            {"quote": "Fuck you! And your eyebrows!", "character": "Walter White", "name": "Breaking Bad"},
            {"quote": "Yeah, bitch! Magnets!", "character": "Jesse Pinkman", "name": "Breaking Bad"},
            {"quote": "You're my free pass... bitch!", "character": "Jesse Pinkman", "name": "Breaking Bad"},
            {"quote": "Fire in the hole, bitch!", "character": "Jesse Pinkman", "name": "Breaking Bad"},
            {"quote": "Bitch!", "character": "Jesse Pinkman", "name": "Breaking Bad"},
            {"quote": "Speak into the mic, bitch.", "character": "Jesse Pinkman", "name": "Breaking Bad"},
            {"quote": "Shut the fuck up and let me die in peace.", "character": "Mike Ehrmantraut", "name": "Breaking Bad"},
            {"quote": "You two suck at peddling meth.", "character": "Saul Goodman", "name": "Breaking Bad"}
        ],
        [
            {"quote": "I am not in danger, Skyler. I AM the danger!", "character": "Walter White", "name": "Breaking Bad"},
            {"quote": "A guy opens his door and gets shot and you think that of me? No. I am the one who knocks!", "character": "Walter White", "name": "Breaking Bad"},
            {"quote": "If that's true, if you don't know who I am, then maybe your best course... would be to tread lightly.", "character": "Walter White", "name": "Breaking Bad"},
            {"quote": "Someone has to protect this family from the man who protects this family.", "character": "Skyler White", "name": "Breaking Bad"},
            {"quote": "Smoking marijuana, eating cheetos, and masturbating do not constitute plans in my book.", "character": "Walter White", "name": "Breaking Bad"},
            {"quote": "Stay out of my territory.", "character": "Walter White", "name": "Breaking Bad"},
            {"quote": "Because I say so.", "character": "Walter White", "name": "Breaking Bad"},
            {"quote": "I'm not in the meth business. I'm in the empire business.", "character": "Walter White", "name": "Breaking Bad"},
            {"quote": "You all know exactly who I am. Say my name.", "character": "Walter White", "name": "Breaking Bad"},
            {"quote": "I watched Jane die. I was there. And I watched her die.","character": "Walter White", "name": "Breaking Bad"},
            {"quote": "I did it for me. I liked it. I was good at it. And... I was really... I was alive.", "character": "Walter White", "name": "Breaking Bad"},
            {"quote": "'Cap'n Cook?' That's not you? Like I said, no one is looking for you.", "character": "Walter White", "name": "Breaking Bad"},
            {"quote": "Do you know how much I make a year? I mean, even if I told you, you wouldn't believe it.", "character": "Walter White", "name": "Breaking Bad"},
            {"quote": "Send him to Belize? I'll send YOU to Belize.", "character": "Walter White", "name": "Breaking Bad"},
            {"quote": "We're done when I say we're done.", "character": "Walter White", "name": "Breaking Bad"},
            {"quote": "So you do have a plan? Yeah, Mr. White! Yeah, science!", "character": "Jesse Pinkman", "name": "Breaking Bad"},
            {"quote": "I'm a criminal, yo.", "character": "Jesse Pinkman", "name": "Breaking Bad"},
            {"quote": "Did you just bring a bomb into a hostpital?", "character": "Jesse Pinkman", "name": "Breaking Bad"},
            {"quote": "Seriously? 'Hello Kitty'?", "character": "Jesse Pinkman", "name": "Breaking Bad"},
            {"quote": "Better call Saul!", "character": "Saul Goodman", "name": "Breaking Bad"},
            {"quote": "You do seem to have a little 'shit creek' action going... You know, FYI, you can buy a paddle.", "character": "Saul Goodman", "name": "Breaking Bad"},
            {"quote": "If I ever get anal polyps, I'll know what to name them.", "character": "Saul Goodman", "name": "Breaking Bad"},
            {"quote": "Clearly, his taste in women is the same as his taste in lawyers.", "character": "Saul Goodman", "name": "Breaking Bad"},
            {"quote": "May his death satisfy you.", "character": "Gustavo Fring", "name": "Breaking Bad"},
            {"quote": "I will kill your wife, I will kill your son, I will kill your infant daughter.", "character": "Gustavo Fring", "name": "Breaking Bad"},
            {"quote": "Everyone sounds like Meryl Streep with a gun to their head.", "character": "Mike Ehrmantraut", "name": "Breaking Bad"},
            {"quote": "You know how they say 'it's been a pleasure'? Well... it hasn't.", "character": "Mike Ehrmantraut", "name": "Breaking Bad"},
            {"quote": "Just because you shot Jesse James doesn't mean you are Jesse James.", "character": "Mike Ehrmantraut", "name": "Breaking Bad"},
            {"quote": "No more half-measures, Walter.", "character": "Mike Ehrmantraut", "name": "Breaking Bad"},
            {"quote": "Keys, scumbag. It's the universal symbol for keys.", "character": "Mike Ehrmantraut", "name": "Breaking Bad"},
            {"quote": "I will put you under the jail.", "character": "Hank Schrader", "name": "Breaking Bad"},
            {"quote": "My name is ASAC Schrader, and you can go fuck yourself.", "character": "Hank Schrader", "name": "Breaking Bad"},
            {"quote": "They're minerals, Marie! Jesus!", "character": "Hank Schrader", "name": "Breaking Bad"},
            {"quote": "Since when do vegans eat fried chicken?", "character": "Hank Schrader", "name": "Breaking Bad"},
            {"quote": "You're the smartest guy I ever met, and you're too stupid to see he made up his mind 10 minutes ago.", "character": "Hank Schrader", "name": "Breaking Bad"},
            {"quote": "All I can do is wait... for the cancer to come back.", "character": "Skyler White", "name": "Breaking Bad"},
            {"quote": "Put me on your magical boat, man, and sail me down your chocolaty river of meth!", "character": "Badger", "name": "Breaking Bad"},
            {"quote": "Buzz buzz buzz", "character": "The fly", "name": "Breaking Bad"},
            {"quote": "The Universe is Random. Not Inevitable. It's simple Chaos.", "character": "Walter White", "name": "Breaking Bad"},
            {"quote": "Sometimes it just feels better not to talk. At All. About Anything. To Anyone.", "character": "Walter White", "name": "Breaking Bad"},
            {"quote": "Name one thing in this world that is non negotiable.", "character": "Walter White", "name": "Breaking Bad"},
            {"quote": "You are not the guy. You're not capable of being the guy. I had a guy but now I don't. You are not the guy.", "character": "Mike Ehrmantraut", "name": "Breaking Bad"},
            {"quote": "just say I know a guy... who knows a guy... who knows another guy.", "character": "Saul Goodman", "name": "Breaking Bad"}
        ]
    ],
    "movies": [
        [

        ],
        [
            {"quote": "... Stop trying to control everything and just let go! LET GO!", "character": "Tyler Durden", "name": "Fight Club"},
            {"quote": "You're not your job, you're not the car you drive, you're not the contents of your wallet..", "character": "Tyler Durden", "name": "Fight Club"},
            {"quote": "We're consumers. We are by-products of a lifestyle obsession...", "character": "Tyler Durden", "name": "Fight Club"},
            {"quote": "We're a generation of men raised by women. I'm wondering if another woman is really the answer we need.", "character": "Tyler Durden", "name": "Fight Club"},
            {"quote": "Hasta la vista, baby.", "character": "Terminator", "name": "Terminator 2"}
        ]
    ],
    "jokes": [
        [

        ],
        [
            {"quote": "Did you hear about the restaurant on the moon? Great food, no atmosphere.", "character": "Unknown", "name": "Unknown"},
            {"quote": "Want to hear a joke about paper? Nevermind it's tearable.", "character": "Unknown", "name": "Unknown"}
        ]
    ]
}
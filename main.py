import random


def randomize_list(list):
    new_list = []
    while len(list) > 0:
        selection = random.choice(list)
        print(selection)
        new_list.append(selection)
        list.remove(selection)
    return new_list


draft_preferences = {
    "Paul": ["Tyson", "Sophie", "Denise", "Yul", "Sarah", "Nick", "Wendell",
             "Michelle", "Jeremy", "Tony", "Ethan", "Sandra", "Parvati", "Ben",
             "Rob", "Adam", "Kim", "Natalie", "Danni", "Amber"],
    "Becky": ["Parvati", "Adam", "Sophie", "Yul", "Nick", "Wendell", "Sarah",
              "Denise", "Michelle", "Jeremy", "Tyson", "Ethan", "Rob",
              "Sandra", "Kim", "Tony", "Ben", "Danni", "Amber", "Natalie"],
    "Tyler": ["Sophie", "Nick", "Wendell", "Michelle", "Adam", "Danni",
              "Denise", "Yul", "Ethan", "Sarah", "Natalie", "Jeremy", "Kim",
              "Tyson", "Ben", "Parvati", "Sandra", "Amber", "Rob", "Tony"],
    "Julia": ["Tyson", "Sophie", "Denise", "Jeremy", "Michelle", "Tony",
              "Wendell", "Nick", "Rob", "Yul", "Kim", "Parvati", "Ben",
              "Sarah", "Sandra", "Ethan", "Adam", "Danni", "Natalie", "Amber"],
    "Jenna": ["Yul", "Sophie", "Tyson", "Wendell", "Natalie", "Jeremy", "Nick",
              "Adam", "Denise", "Ethan", "Tony", "Sarah", "Sandra", "Parvati",
              "Rob", "Kim", "Michelle", "Ben", "Danni", "Amber"]
}


draft_members = ["Paul", "Becky", "Tyler", "Julia", "Jenna"]

draft_order = randomize_list(draft_members)
print(draft_order)

draft = {}

for i in range(1, 4, 1):
    for person in draft_order:
        if person not in draft.keys():
            draft[person] = []
        draftee = draft_preferences[person][0]
        print(f"{person} drafts {draftee} in round {i}!")
        draft[person].append(draftee)
        print(f"{draftee} will now be removed from everyone's draft list.")
        for p in draft_preferences.keys():
            draft_preferences[p].remove(draftee)
        draft_order.reverse()

print(draft)

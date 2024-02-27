"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
            {
        "input": "gazeta publica hoje: breve anuncio de faxina na quermesse",
        "answer": "S"
    },
    {
        "input": "esta frase nao usa todas as letras, estao faltando algumas",
        "answer": "N"
    },
    {
        "input": "abcdefghijlmnopqrstuvxz",
        "answer": "S"
    }
    ]
}

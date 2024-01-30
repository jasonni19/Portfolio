from project import validateInput,website,graph

def test_validateInput():
    assert validateInput("https://etsy.com") == "https://etsy.com"
    assert validateInput("https://roblox.com") == "https://roblox.com"
    assert validateInput("https://youtube.com/") == "https://youtube.com/"
    assert validateInput("moo") == 0
    assert validateInput("youtube.com") == 0
    assert validateInput("") == 0

def test_website():
    assert website("https://youtube.com") == "youtube.com"
    assert website("https://redcross.org") == "redcross.org"
    assert website("http://chess.com") == "chess.com"
    assert website("http://hands4hope.org") == "hands4hope.org"
    assert website("http://www.hands4hope.org") == "hands4hope.org"
    assert website("https://www.wholegraindigital.com/") == "wholegraindigital.com"

def test_graph():
    assert(graph("e")) == "Energy Graph"
    assert(graph("E")) == "Energy Graph"
    assert(graph("c")) == "Carbon Graph"
    assert(graph("C")) == "Carbon Graph"
    assert(graph("b")) == "Both Graphs"
    assert(graph("B")) == "Both Graphs"


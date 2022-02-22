t = """<div class="col-md-4">
            <h5>Track{}</h5>
            <audio controls><source src="/css/IELTS Practice Tests (Peter May)/Test {}/Track No0{}.mp3" type="audio/mpeg"></audio>
        </div>"""

for i in range(10,18):
    print("""<div class="col-md-4">
            <h5>Track{}</h5>
            <audio controls><source src="/css/IELTS Practice Tests (Peter May)/Test 4/Track No{}.mp3" type="audio/mpeg"></audio>
        </div>""".format(i,i))
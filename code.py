#dio html-a
sve = """<p><span class="font6">kjaro </span><span class="font1">- (reg. Dubrovnik) svijetlo, jasno, razumljivo</span></p>
<p><span class="font6">klačinara </span><span class="font1">- (reg.) otpala žbuka sa zida </span><span class="font6">klada </span><span class="font1">- nespretna, pretila, nepokretna osoba;</span></p>
<p><span class="font1">veliko muško spolovilo </span><span class="font6">klada leži </span><span class="font1">- osoba koja pokaže zanimanje za&nbsp;prostitutku na ulici</span></p>
<p><span class="font6">klafrača </span><span class="font1">- žena koja puno brblja, brbljivica, BPK</span></p>"""
#rastepi sve po paragrafima
paragrafi = re.split('<p>', sve)

listaPojmova=[]
#liste u listi - U svakoj je riječ/riječi do </span> glavni pojam
for p in paragrafi:
    list = re.split('<span class="font6">',p)
    listaPojmova.append(list)
listaPojmova


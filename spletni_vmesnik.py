import bottle
import random
from model import Insult, Word, Noun, Adjective

bottle.TEMPLATE_PATH.insert(0, 'C:\\FMF\\UVP\\UVP projektna naloga\\projektna_naloga\\views')

@bottle.get("/")
@bottle.post("/")
def osnovna_stran():
    en = bottle.request.POST.get("en")
    si = bottle.request.POST.get("si")
    if en is not None:
        return bottle.redirect("/en")
    if si is not None:
        return bottle.redirect("/si")
    return bottle.template('osnovna_stran.html')
    

@bottle.get("/en")
@bottle.post("/en")
def choose_difficulty():
    baby = bottle.request.POST.get("baby")
    mean = bottle.request.POST.get("mean")
    any = bottle.request.POST.get("any")
    play_god = bottle.request.POST.get("play_god")
    if baby is not None:
        return bottle.redirect("/baby-mode")
    if mean is not None:
        return bottle.redirect("/hardcore-survival")
    if any is not None:
        return bottle.redirect("/random")
    if play_god is not None:
        Noun.nouns =[]
        Adjective.adjectives = []
        return bottle.redirect("/play-god")
    return bottle.template('choose_difficulty.html')


@bottle.get("/baby-mode")
@bottle.post("/baby-mode")
def baby_mode():
    insult = Insult.generate("en", "baby", "x")
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/baby-mode")
    return bottle.template("baby_mode.html", insult = insult)

@bottle.get("/hardcore-survival")
@bottle.post("/hardcore-survival")
def hardcore_survival():
    insult = Insult.generate("en", "hardcore", "x")
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/hardcore-survival")
    return bottle.template("hardcore_survival.html", insult = insult)

@bottle.get("/random")
@bottle.post("/random")
def no_preference():
    difficulties = ["baby", "hardcore"]
    diff = random.choice(difficulties)
    insult = Insult.generate("en", diff, "x")
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/random")
    return bottle.template("random.html", insult = insult)

@bottle.get("/play-god")
@bottle.post("/play-god")
def play_god():
    adjectives = bottle.request.POST.getunicode("adjective")
    nouns = bottle.request.POST.getunicode("noun")
    generate = bottle.request.POST.getunicode("generate")
    add = bottle.request.POST.getunicode("add")
    if add is not None:
        print("4")
        if adjectives is not None:
            print("1")
            for adj in adjectives.split():
                Adjective(adj, "en", "custom", "x")
        if nouns is not None:
            print("2")
            for n in nouns.split():
                Noun(n, "en", "custom", "x")
    if generate is not None:
        print("3")
        return bottle.redirect("/show-insult")
    return bottle.template("play-god.html", Adjective = Adjective, Noun = Noun)

@bottle.get("/show-insult")
@bottle.post("/show-insult")
def show_insult():
    insult = Insult.generate("en", "custom", "x")
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/show-insult")
    return bottle.template("play-god-2.html", insult = insult)

@bottle.get("/si")
@bottle.post("/si")
def izberi_tezavnost():
    nezaljiva = bottle.request.POST.get("nezaljiva")
    moralno_oporecna = bottle.request.POST.get("moralno_oporecna")
    brez_preference = bottle.request.POST.get("brez_preference")
    samostojno = bottle.request.POST.get("samostojno")
    if nezaljiva is not None:
        return bottle.redirect("/nezaljiva")
    if moralno_oporecna is not None:
        return bottle.redirect("/oporecna")
    if brez_preference is not None:
        return bottle.redirect("/vseeno")
    if samostojno is not None:
        Noun.nouns =[]
        Adjective.adjectives = []
        return bottle.redirect("/samostojno")
    return bottle.template('izberi_tezavnost.html')

@bottle.get("/nezaljiva")
@bottle.post("/nezaljiva")
def otrocje_nezaljiva():
    f = bottle.request.POST.get("ona")
    m = bottle.request.POST.get("on")
    t = bottle.request.POST.get("ono")
    fmt = bottle.request.POST.get("kdorkoli")
    if f is not None:
        return bottle.redirect("/nezaljiva-f")
    if m is not None:
        return bottle.redirect("/nezaljiva-m")
    if t is not None:
        return bottle.redirect("/nezaljiva-t")
    if fmt is not None:
        return bottle.redirect("/nezaljiva-fmt")
    return bottle.template("nezaljiva_izbira_spola.html")

@bottle.get("/nezaljiva-f")
@bottle.post("/nezaljiva-f")
def nezaljiva_f():
    insult = Insult.generate("si", "baby", "f")
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/nezaljiva-f")
    return bottle.template("nezaljiva-f.html", insult = insult)

@bottle.get("/nezaljiva-m")
@bottle.post("/nezaljiva-m")
def nezaljiva_m():
    insult = Insult.generate("si", "baby", "m")
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/nezaljiva-m")
    return bottle.template("nezaljiva-m.html", insult = insult)

@bottle.get("/nezaljiva-t")
@bottle.post("/nezaljiva-t")
def nezaljiva_t():
    insult = Insult.generate("si", "baby", "t")
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/nezaljiva-t")
    return bottle.template("nezaljiva-t.html", insult = insult)

@bottle.get("/nezaljiva-fmt")
@bottle.post("/nezaljiva-fmt")
def nezaljiva_fmt():
    genders = ["f", "m", "t"]
    y = random.choice(genders)
    insult = Insult.generate("si", "baby", y)
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/nezaljiva-fmt")
    return bottle.template("nezaljiva-fmt.html", insult = insult)

@bottle.get("/oporecna")
@bottle.post("/oporecna")
def moralno_oporecna():
    f = bottle.request.POST.get("ona")
    m = bottle.request.POST.get("on")
    t = bottle.request.POST.get("ono")
    fmt = bottle.request.POST.get("kdorkoli")
    if f is not None:
        return bottle.redirect("/oporecna-f")
    if m is not None:
        return bottle.redirect("/oporecna-m")
    if t is not None:
        return bottle.redirect("/oporecna-t")
    if fmt is not None:
        return bottle.redirect("/oporecna-fmt")
    return bottle.template("oporecna_izbira_spola.html")

@bottle.get("/oporecna-f")
@bottle.post("/oporecna-f")
def oporecna_f():
    insult = Insult.generate("si", "hardcore", "f")
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/oporecna-f")
    return bottle.template("oporecna-f.html", insult = insult)

@bottle.get("/oporecna-m")
@bottle.post("/oporecna-m")
def oporecna_m():
    insult = Insult.generate("si", "hardcore", "m")
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/oporecna-m")
    return bottle.template("oporecna-m.html", insult = insult)

@bottle.get("/oporecna-t")
@bottle.post("/oporecna-t")
def oporecna_t():
    insult = Insult.generate("si", "hardcore", "t")
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/oporecna-t")
    return bottle.template("oporecna-t.html", insult = insult)

@bottle.get("/oporecna-fmt")
@bottle.post("/oporecna-fmt")
def oporecna_fmt():
    genders = ["f", "m", "t"]
    y = random.choice(genders)
    insult = Insult.generate("si", "hardcore", y)
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/oporecna-fmt")
    return bottle.template("oporecna-fmt.html", insult = insult)


@bottle.get("/vseeno")
@bottle.post("/vseeno")
def vseeno():
    f = bottle.request.POST.get("ona")
    m = bottle.request.POST.get("on")
    t = bottle.request.POST.get("ono")
    fmt = bottle.request.POST.get("kdorkoli")
    if f is not None:
        return bottle.redirect("/vseeno-f")
    if m is not None:
        return bottle.redirect("/vseeno-m")
    if t is not None:
        return bottle.redirect("/vseeno-t")
    if fmt is not None:
        return bottle.redirect("/vseeno-fmt")
    return bottle.template("vseeno_izbira_spola.html")

@bottle.get("/vseeno-f")
@bottle.post("/vseeno-f")
def vseeno_f():
    difficulties = ["baby", "hardcore"]
    diff = random.choice(difficulties)
    insult = Insult.generate("si", diff, "f")
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/vseeno-f")
    return bottle.template("vseeno-f.html", insult = insult)

@bottle.get("/vseeno-m")
@bottle.post("/vseeno-m")
def vseeno_m():
    difficulties = ["baby", "hardcore"]
    diff = random.choice(difficulties)
    insult = Insult.generate("si", diff, "m")
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/vseeno-m")
    return bottle.template("vseeno-m.html", insult = insult)

@bottle.get("/vseeno-t")
@bottle.post("/vseeno-t")
def vseeno_t():
    difficulties = ["baby", "hardcore"]
    diff = random.choice(difficulties)
    insult = Insult.generate("si", diff, "t")
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/vseeno-t")
    return bottle.template("vseeno-t.html", insult = insult)

@bottle.get("/vseeno-fmt")
@bottle.post("/vseeno-fmt")
def vseeno_fmt():
    difficulties = ["baby", "hardcore"]
    diff = random.choice(difficulties)
    genders = ["f", "m", "t"]
    y = random.choice(genders)
    insult = Insult.generate("si", diff, y)
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/vseeno-fmt")
    return bottle.template("vseeno-fmt.html", insult = insult)

@bottle.get("/samostojno")
@bottle.post("/samostojno")
def samostojno():
    samostalniki = bottle.request.POST.getunicode("samostalnik")
    pridevniki = bottle.request.POST.getunicode("pridevnik")
    gender = bottle.request.POST.get("spol")
    generiraj = bottle.request.POST.get("generiraj")
    if samostalniki is not None:
        if gender is not None:
            for samost in samostalniki.split():
                Noun(samost, "si", "custom", gender)
    if pridevniki is not None:
        if gender is not None:
            for prid in pridevniki.split():
                Adjective(prid, "si", "custom", gender)
    if generiraj is not None:
        return bottle.redirect("/prikazi-insult")
    return bottle.template("samostojno.html", Adjective = Adjective, Noun = Noun)

@bottle.get("/prikazi-insult")
@bottle.post("/prikazi-insult")
def prikazi_insult():
    genders = ["z", "m", "s"]
    gender = random.choice(genders)
    print("5 " + str(gender))
    insult = Insult.generate("si", "custom", gender)
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/prikazi-insult")
    return bottle.template("samostojno2.html", insult = insult)

Word.parse()
bottle.run(reloader=True, debug=True)
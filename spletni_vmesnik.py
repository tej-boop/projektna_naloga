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
        return bottle.redirect("/baby_mode")
    if mean is not None:
        return bottle.redirect("/hardcore-survival")
    if any is not None:
        return bottle.redirect("/random")
    if play_god is not None:
        return bottle.redirect("/play-god")
    return bottle.template('choose_difficulty.html')


@bottle.get("/baby_mode")
def baby_mode():
    insult = Insult.generate("en", "baby", "x")
    return bottle.template("baby_mode.html", insult = insult)

@bottle.get("/hardcore-survival")
def hardcore_survival():
    insult = Insult.generate("en", "hardcore", "x")
    return bottle.template("hardcore_survival.html", insult = insult)

@bottle.get("/random")
def no_preference():
    difficulties = ["baby", "hardcore"]
    diff = random.choice(difficulties)
    insult = Insult.generate("en", diff, "x")
    return bottle.template("random.html", insult = insult)

@bottle.get("/play-god")
@bottle.post("/play-god")
def play_god():
    adjectives = bottle.request.POST.getunicode("adjective")
    nouns = bottle.request.POST.getunicode("noun")
    generate = bottle.request.POST.get("generate")
    if adjectives is not None:
        for adj in adjectives.split():
            Adjective(adj, "en", "custom", "x")
    if nouns is not None:
        for n in nouns.split():
            Noun(n, "en", "custom", "x")
    if generate is not None:
        return bottle.redirect("/show-insult")
    return bottle.template("play-god.html", Adjective = Adjective, Noun = Noun)

@bottle.get("/show-insult")
def show_insult():
    insult = Insult.generate("en", "custom", "x")
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
def nezaljiva_f():
    insult = Insult.generate("si", "baby", "f")
    return bottle.template("nezaljiva-f.html", insult = insult)

@bottle.get("/nezaljiva-m")
def nezaljiva_m():
    insult = Insult.generate("si", "baby", "m")
    return bottle.template("nezaljiva-m.html", insult = insult)

@bottle.get("/nezaljiva-t")
def nezaljiva_t():
    insult = Insult.generate("si", "baby", "t")
    return bottle.template("nezaljiva-t.html", insult = insult)

@bottle.get("/nezaljiva-fmt")
def nezaljiva_fmt():
    genders = ["f", "m", "t"]
    y = random.choice(genders)
    insult = Insult.generate("si", "baby", y)
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
def oporecna_f():
    insult = Insult.generate("si", "hardcore", "f")
    return bottle.template("oporecna-f.html", insult = insult)

@bottle.get("/oporecna-m")
def oporecna_m():
    insult = Insult.generate("si", "hardcore", "m")
    return bottle.template("oporecna-m.html", insult = insult)

@bottle.get("/oporecna-t")
def oporecna_t():
    insult = Insult.generate("si", "hardcore", "t")
    return bottle.template("oporecna-t.html", insult = insult)

@bottle.get("/oporecna-fmt")
def oporecna_fmt():
    genders = ["f", "m", "t"]
    y = random.choice(genders)
    insult = Insult.generate("si", "hardcore", y)
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
def vseeno_f():
    difficulties = ["baby", "hardcore"]
    diff = random.choice(difficulties)
    insult = Insult.generate("si", diff, "f")
    return bottle.template("vseeno-f.html", insult = insult)

@bottle.get("/vseeno-m")
def vseeno_m():
    difficulties = ["baby", "hardcore"]
    diff = random.choice(difficulties)
    insult = Insult.generate("si", diff, "m")
    return bottle.template("vseeno-m.html", insult = insult)

@bottle.get("/vseeno-t")
def vseeno_t():
    difficulties = ["baby", "hardcore"]
    diff = random.choice(difficulties)
    insult = Insult.generate("si", diff, "t")
    return bottle.template("vseeno-t.html", insult = insult)

@bottle.get("/vseeno-fmt")
def vseeno_fmt():
    difficulties = ["baby", "hardcore"]
    diff = random.choice(difficulties)
    genders = ["f", "m", "t"]
    y = random.choice(genders)
    insult = Insult.generate("si", diff, y)
    return bottle.template("vseeno-fmt.html", insult = insult)

@bottle.get("/samostojno")
@bottle.post("/samostojno")
def samostojno():
    samostalniki = bottle.request.POST.getunicode("samostalnik")
    pridevniki = bottle.request.POST.getunicode("pridevnik")
    f = bottle.request.POST.get("ž")
    m = bottle.request.POST.get("m")
    t = bottle.request.POST.get("s")
    generiraj = bottle.request.POST.get("generiraj")
    if samostalniki is not None:
        if f is not None:
            for samost in samostalniki.split():
                Noun(samost, "si", "custom", "f")
        if m is not None:
            for samost in samostalniki.split():
                Noun(samost, "si", "custom", "m")
        if t is not None:
            for samost in samostalniki.split():
                Noun(samost, "si", "custom", "t")
    if pridevniki is not None:
        if f is not None:
            for prid in pridevniki.split():
                Adjective(prid, "si", "custom", "f")
        if m is not None:
            for prid in pridevniki.split():
                Adjective(prid, "si", "custom", "m")
        if t is not None:
            for prid in pridevniki.split():
                Adjective(prid, "si", "custom", "t")
    if generiraj is not None:
        return bottle.redirect("/prikazi-insult")
    return bottle.template("samostojno.html", Adjective = Adjective, Noun = Noun)

@bottle.get("/prikazi-insult")
def prikazi_insult():
    genders = ["f", "m", "t"]
    y = random.choice(genders)
    insult = Insult.generate("si", "custom", y)
    return bottle.template("samostojno2.html", insult = insult)

Word.parse()
bottle.run(reloader=True, debug=True)
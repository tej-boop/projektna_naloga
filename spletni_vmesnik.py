import bottle
import random
import base64
from model import Insult, Word, Noun, Adjective
from datetime import datetime

bottle.TEMPLATE_PATH.insert(0, 'C:\\FMF\\UVP\\UVP projektna naloga\\projektna_naloga\\views')

favourites = {}

@bottle.get("/")
@bottle.post("/")
def osnovna_stran():
    if bottle.request.get_cookie("user"):
        cookie = bottle.request.get_cookie("user")
    else:
        data = str(datetime.now())
        cookie = base64.b64encode(data.encode("utf-8"))
        cookie = str(cookie, "utf-8")
        bottle.response.set_cookie("user", cookie)
    if cookie in favourites.keys():
        pass
    else:
        favourites[cookie] = [None, []]
    en = bottle.request.POST.get("en")
    si = bottle.request.POST.get("si")
    if en is not None:
        return bottle.redirect("/en")
    if si is not None:
        return bottle.redirect("/si")
    return bottle.template('osnovna_stran.html')

@bottle.get("/favourites")
@bottle.post("/favourites")
def favourited_insults():
    if bottle.request.get_cookie("user"):
        cookie = bottle.request.get_cookie("user")
    else:
        data = str(datetime.now())
        cookie = base64.b64encode(data.encode("utf-8"))
        cookie = str(cookie, "utf-8")
        bottle.response.set_cookie("user", cookie)
    if cookie in favourites.keys():
        pass
    else:
        favourites[cookie] = [None, []]
    for i in range(len(favourites[cookie][1])):
        remove = bottle.request.POST.get(str(i))
        if remove is not None:
            favourites[cookie][1].pop(i)
    favourites_list = favourites[cookie][1]
    return bottle.template("favourites.html", favourites_list = list(enumerate(favourites_list)))

@bottle.get("/en")
@bottle.post("/en")
def choose_difficulty():
    if bottle.request.get_cookie("user"):
        cookie = bottle.request.get_cookie("user")
    else:
        data = str(datetime.now())
        cookie = base64.b64encode(data.encode("utf-8"))
        cookie = str(cookie, "utf-8")
        bottle.response.set_cookie("user", cookie)
    if cookie in favourites.keys():
        pass
    else:
        favourites[cookie] = [None, []]
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
    if bottle.request.get_cookie("user"):
        cookie = bottle.request.get_cookie("user")
    else:
        data = str(datetime.now())
        cookie = base64.b64encode(data.encode("utf-8"))
        cookie = str(cookie, "utf-8")
        bottle.response.set_cookie("user", cookie)
    if cookie in favourites.keys():
        pass
    else:
        favourites[cookie] = [None, []]
    favourite = bottle.request.POST.get("favourite")
    if favourite is not None:
        insult = favourites[cookie][0]
        if insult not in favourites[cookie][1]:
            favourites[cookie][1].append(insult)
    else:
        insult = Insult.generate("en", "baby", "x")
        favourites[cookie][0] = insult
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/baby-mode")
    return bottle.template("baby_mode.html", insult = insult)

@bottle.get("/hardcore-survival")
@bottle.post("/hardcore-survival")
def hardcore_survival():
    if bottle.request.get_cookie("user"):
        cookie = bottle.request.get_cookie("user")
    else:
        data = str(datetime.now())
        cookie = base64.b64encode(data.encode("utf-8"))
        cookie = str(cookie, "utf-8")
        bottle.response.set_cookie("user", cookie)
    if cookie in favourites.keys():
        pass
    else:
        favourites[cookie] = [None, []]
    favourite = bottle.request.POST.get("favourite")
    if favourite is not None:
        insult = favourites[cookie][0]
        if insult not in favourites[cookie][1]:
            favourites[cookie][1].append(insult)
    else:
        insult = Insult.generate("en", "hardcore", "x")
        favourites[cookie][0] = insult
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/hardcore-survival")
    return bottle.template("hardcore_survival.html", insult = insult)

@bottle.get("/random")
@bottle.post("/random")
def no_preference():
    if bottle.request.get_cookie("user"):
        cookie = bottle.request.get_cookie("user")
    else:
        data = str(datetime.now())
        cookie = base64.b64encode(data.encode("utf-8"))
        cookie = str(cookie, "utf-8")
        bottle.response.set_cookie("user", cookie)
    if cookie in favourites.keys():
        pass
    else:
        favourites[cookie] = [None, []]
    favourite = bottle.request.POST.get("favourite")
    if favourite is not None:
        insult = favourites[cookie][0]
        if insult not in favourites[cookie][1]:
            favourites[cookie][1].append(insult)
    else:
        difficulties = ["baby", "hardcore"]
        diff = random.choice(difficulties)
        insult = Insult.generate("en", diff, "x")
        favourites[cookie][0] = insult
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/random")
    return bottle.template("random.html", insult = insult)

@bottle.get("/play-god")
@bottle.post("/play-god")
def play_god():
    if bottle.request.get_cookie("user"):
        cookie = bottle.request.get_cookie("user")
    else:
        data = str(datetime.now())
        cookie = base64.b64encode(data.encode("utf-8"))
        cookie = str(cookie, "utf-8")
        bottle.response.set_cookie("user", cookie)
    if cookie in favourites.keys():
        pass
    else:
        favourites[cookie] = [None, []]
    adjectives = bottle.request.POST.getunicode("adjective")
    nouns = bottle.request.POST.getunicode("noun")
    generate = bottle.request.POST.getunicode("generate")
    add = bottle.request.POST.getunicode("add")
    if add is not None:
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
@bottle.post("/show-insult")
def show_insult():
    if bottle.request.get_cookie("user"):
        cookie = bottle.request.get_cookie("user")
    else:
        data = str(datetime.now())
        cookie = base64.b64encode(data.encode("utf-8"))
        cookie = str(cookie, "utf-8")
        bottle.response.set_cookie("user", cookie)
    if cookie in favourites.keys():
        pass
    else:
        favourites[cookie] = [None, []]
    favourite = bottle.request.POST.get("favourite")
    if favourite is not None:
        insult = favourites[cookie][0]
        if insult not in favourites[cookie][1]:
            favourites[cookie][1].append(insult)
    else:
        insult = Insult.generate("en", "custom", "x")
        favourites[cookie][0] = insult
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/show-insult")
    return bottle.template("play-god-2.html", insult = insult)

@bottle.get("/si")
@bottle.post("/si")
def izberi_tezavnost():
    if bottle.request.get_cookie("user"):
        cookie = bottle.request.get_cookie("user")
    else:
        data = str(datetime.now())
        cookie = base64.b64encode(data.encode("utf-8"))
        cookie = str(cookie, "utf-8")
        bottle.response.set_cookie("user", cookie)
    if cookie in favourites.keys():
        pass
    else:
        favourites[cookie] = [None, []]
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
    if bottle.request.get_cookie("user"):
        cookie = bottle.request.get_cookie("user")
    else:
        data = str(datetime.now())
        cookie = base64.b64encode(data.encode("utf-8"))
        cookie = str(cookie, "utf-8")
        bottle.response.set_cookie("user", cookie)
    if cookie in favourites.keys():
        pass
    else:
        favourites[cookie] = [None, []]
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
    if bottle.request.get_cookie("user"):
        cookie = bottle.request.get_cookie("user")
    else:
        data = str(datetime.now())
        cookie = base64.b64encode(data.encode("utf-8"))
        cookie = str(cookie, "utf-8")
        bottle.response.set_cookie("user", cookie)
    if cookie in favourites.keys():
        pass
    else:
        favourites[cookie] = [None, []]
    favourite = bottle.request.POST.get("favourite")
    if favourite is not None:
        insult = favourites[cookie][0]
        if insult not in favourites[cookie][1]:
            favourites[cookie][1].append(insult)
    else:
        insult = Insult.generate("si", "baby", "f")
        favourites[cookie][0] = insult
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/nezaljiva-f")
    return bottle.template("nezaljiva-f.html", insult = insult)

@bottle.get("/nezaljiva-m")
@bottle.post("/nezaljiva-m")
def nezaljiva_m():
    if bottle.request.get_cookie("user"):
        cookie = bottle.request.get_cookie("user")
    else:
        data = str(datetime.now())
        cookie = base64.b64encode(data.encode("utf-8"))
        cookie = str(cookie, "utf-8")
        bottle.response.set_cookie("user", cookie)
    if cookie in favourites.keys():
        pass
    else:
        favourites[cookie] = [None, []]
    favourite = bottle.request.POST.get("favourite")
    if favourite is not None:
        insult = favourites[cookie][0]
        if insult not in favourites[cookie][1]:
            favourites[cookie][1].append(insult)
    else:
        insult = Insult.generate("si", "baby", "m")
        favourites[cookie][0] = insult
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/nezaljiva-m")
    return bottle.template("nezaljiva-m.html", insult = insult)

@bottle.get("/nezaljiva-t")
@bottle.post("/nezaljiva-t")
def nezaljiva_t():
    if bottle.request.get_cookie("user"):
        cookie = bottle.request.get_cookie("user")
    else:
        data = str(datetime.now())
        cookie = base64.b64encode(data.encode("utf-8"))
        cookie = str(cookie, "utf-8")
        bottle.response.set_cookie("user", cookie)
    if cookie in favourites.keys():
        pass
    else:
        favourites[cookie] = [None, []]
    favourite = bottle.request.POST.get("favourite")
    if favourite is not None:
        insult = favourites[cookie][0]
        if insult not in favourites[cookie][1]:
            favourites[cookie][1].append(insult)
    else:
        insult = Insult.generate("si", "baby", "t")
        favourites[cookie][0] = insult
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/nezaljiva-t")
    return bottle.template("nezaljiva-t.html", insult = insult)

@bottle.get("/nezaljiva-fmt")
@bottle.post("/nezaljiva-fmt")
def nezaljiva_fmt():
    if bottle.request.get_cookie("user"):
        cookie = bottle.request.get_cookie("user")
    else:
        data = str(datetime.now())
        cookie = base64.b64encode(data.encode("utf-8"))
        cookie = str(cookie, "utf-8")
        bottle.response.set_cookie("user", cookie)
    if cookie in favourites.keys():
        pass
    else:
        favourites[cookie] = [None, []]
    favourite = bottle.request.POST.get("favourite")
    if favourite is not None:
        insult = favourites[cookie][0]
        if insult not in favourites[cookie][1]:
            favourites[cookie][1].append(insult)
    else:
        genders = ["f", "m", "t"]
        y = random.choice(genders)
        insult = Insult.generate("si", "baby", y)
        favourites[cookie][0] = insult
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/nezaljiva-fmt")
    return bottle.template("nezaljiva-fmt.html", insult = insult)

@bottle.get("/oporecna")
@bottle.post("/oporecna")
def moralno_oporecna():
    if bottle.request.get_cookie("user"):
        cookie = bottle.request.get_cookie("user")
    else:
        data = str(datetime.now())
        cookie = base64.b64encode(data.encode("utf-8"))
        cookie = str(cookie, "utf-8")
        bottle.response.set_cookie("user", cookie)
    if cookie in favourites.keys():
        pass
    else:
        favourites[cookie] = [None, []]
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
    if bottle.request.get_cookie("user"):
        cookie = bottle.request.get_cookie("user")
    else:
        data = str(datetime.now())
        cookie = base64.b64encode(data.encode("utf-8"))
        cookie = str(cookie, "utf-8")
        bottle.response.set_cookie("user", cookie)
    if cookie in favourites.keys():
        pass
    else:
        favourites[cookie] = [None, []]
    favourite = bottle.request.POST.get("favourite")
    if favourite is not None:
        insult = favourites[cookie][0]
        if insult not in favourites[cookie][1]:
            favourites[cookie][1].append(insult)
    else:
        insult = Insult.generate("si", "hardcore", "f")
        favourites[cookie][0] = insult
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/oporecna-f")
    return bottle.template("oporecna-f.html", insult = insult)

@bottle.get("/oporecna-m")
@bottle.post("/oporecna-m")
def oporecna_m():
    if bottle.request.get_cookie("user"):
        cookie = bottle.request.get_cookie("user")
    else:
        data = str(datetime.now())
        cookie = base64.b64encode(data.encode("utf-8"))
        cookie = str(cookie, "utf-8")
        bottle.response.set_cookie("user", cookie)
    if cookie in favourites.keys():
        pass
    else:
        favourites[cookie] = [None, []]
    favourite = bottle.request.POST.get("favourite")
    if favourite is not None:
        insult = favourites[cookie][0]
        if insult not in favourites[cookie][1]:
            favourites[cookie][1].append(insult)
    else:
        insult = Insult.generate("si", "hardcore", "m")
        favourites[cookie][0] = insult
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/oporecna-m")
    return bottle.template("oporecna-m.html", insult = insult)

@bottle.get("/oporecna-t")
@bottle.post("/oporecna-t")
def oporecna_t():
    if bottle.request.get_cookie("user"):
        cookie = bottle.request.get_cookie("user")
    else:
        data = str(datetime.now())
        cookie = base64.b64encode(data.encode("utf-8"))
        cookie = str(cookie, "utf-8")
        bottle.response.set_cookie("user", cookie)
    if cookie in favourites.keys():
        pass
    else:
        favourites[cookie] = [None, []]
    favourite = bottle.request.POST.get("favourite")
    if favourite is not None:
        insult = favourites[cookie][0]
        if insult not in favourites[cookie][1]:
            favourites[cookie][1].append(insult)
    else:
        insult = Insult.generate("si", "hardcore", "t")
        favourites[cookie][0] = insult
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/oporecna-t")
    return bottle.template("oporecna-t.html", insult = insult)

@bottle.get("/oporecna-fmt")
@bottle.post("/oporecna-fmt")
def oporecna_fmt():
    if bottle.request.get_cookie("user"):
        cookie = bottle.request.get_cookie("user")
    else:
        data = str(datetime.now())
        cookie = base64.b64encode(data.encode("utf-8"))
        cookie = str(cookie, "utf-8")
        bottle.response.set_cookie("user", cookie)
    if cookie in favourites.keys():
        pass
    else:
        favourites[cookie] = [None, []]
    favourite = bottle.request.POST.get("favourite")
    if favourite is not None:
        insult = favourites[cookie][0]
        if insult not in favourites[cookie][1]:
            favourites[cookie][1].append(insult)
    else:
        genders = ["f", "m", "t"]
        y = random.choice(genders)
        insult = Insult.generate("si", "hardcore", y)
        favourites[cookie][0] = insult
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/oporecna-fmt")
    return bottle.template("oporecna-fmt.html", insult = insult)


@bottle.get("/vseeno")
@bottle.post("/vseeno")
def vseeno():
    if bottle.request.get_cookie("user"):
        cookie = bottle.request.get_cookie("user")
    else:
        data = str(datetime.now())
        cookie = base64.b64encode(data.encode("utf-8"))
        cookie = str(cookie, "utf-8")
        bottle.response.set_cookie("user", cookie)
    if cookie in favourites.keys():
        pass
    else:
        favourites[cookie] = [None, []]
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
    if bottle.request.get_cookie("user"):
        cookie = bottle.request.get_cookie("user")
    else:
        data = str(datetime.now())
        cookie = base64.b64encode(data.encode("utf-8"))
        cookie = str(cookie, "utf-8")
        bottle.response.set_cookie("user", cookie)
    if cookie in favourites.keys():
        pass
    else:
        favourites[cookie] = [None, []]
    favourite = bottle.request.POST.get("favourite")
    if favourite is not None:
        insult = favourites[cookie][0]
        if insult not in favourites[cookie][1]:
            favourites[cookie][1].append(insult)
    else:
        difficulties = ["baby", "hardcore"]
        diff = random.choice(difficulties)
        insult = Insult.generate("si", diff, "f")
        favourites[cookie][0] = insult
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/vseeno-f")
    return bottle.template("vseeno-f.html", insult = insult)

@bottle.get("/vseeno-m")
@bottle.post("/vseeno-m")
def vseeno_m():
    if bottle.request.get_cookie("user"):
        cookie = bottle.request.get_cookie("user")
    else:
        data = str(datetime.now())
        cookie = base64.b64encode(data.encode("utf-8"))
        cookie = str(cookie, "utf-8")
        bottle.response.set_cookie("user", cookie)
    if cookie in favourites.keys():
        pass
    else:
        favourites[cookie] = [None, []]
    favourite = bottle.request.POST.get("favourite")
    if favourite is not None:
        insult = favourites[cookie][0]
        if insult not in favourites[cookie][1]:
            favourites[cookie][1].append(insult)
    else:
        difficulties = ["baby", "hardcore"]
        diff = random.choice(difficulties)
        insult = Insult.generate("si", diff, "m")
        favourites[cookie][0] = insult
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/vseeno-m")
    return bottle.template("vseeno-m.html", insult = insult)

@bottle.get("/vseeno-t")
@bottle.post("/vseeno-t")
def vseeno_t():
    if bottle.request.get_cookie("user"):
        cookie = bottle.request.get_cookie("user")
    else:
        data = str(datetime.now())
        cookie = base64.b64encode(data.encode("utf-8"))
        cookie = str(cookie, "utf-8")
        bottle.response.set_cookie("user", cookie)
    if cookie in favourites.keys():
        pass
    else:
        favourites[cookie] = [None, []]
    favourite = bottle.request.POST.get("favourite")
    if favourite is not None:
        insult = favourites[cookie][0]
        if insult not in favourites[cookie][1]:
            favourites[cookie][1].append(insult)
    else:
        difficulties = ["baby", "hardcore"]
        diff = random.choice(difficulties)
        insult = Insult.generate("si", diff, "t")
        favourites[cookie][0] = insult
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/vseeno-t")
    return bottle.template("vseeno-t.html", insult = insult)

@bottle.get("/vseeno-fmt")
@bottle.post("/vseeno-fmt")
def vseeno_fmt():
    if bottle.request.get_cookie("user"):
        cookie = bottle.request.get_cookie("user")
    else:
        data = str(datetime.now())
        cookie = base64.b64encode(data.encode("utf-8"))
        cookie = str(cookie, "utf-8")
        bottle.response.set_cookie("user", cookie)
    if cookie in favourites.keys():
        pass
    else:
        favourites[cookie] = [None, []]
    favourite = bottle.request.POST.get("favourite")
    if favourite is not None:
        insult = favourites[cookie][0]
        if insult not in favourites[cookie][1]:
            favourites[cookie][1].append(insult)
    else:
        difficulties = ["baby", "hardcore"]
        diff = random.choice(difficulties)
        genders = ["f", "m", "t"]
        y = random.choice(genders)
        insult = Insult.generate("si", diff, y)
        favourites[cookie][0] = insult
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/vseeno-fmt")
    return bottle.template("vseeno-fmt.html", insult = insult)

@bottle.get("/samostojno")
@bottle.post("/samostojno")
def samostojno():
    if bottle.request.get_cookie("user"):
        cookie = bottle.request.get_cookie("user")
    else:
        data = str(datetime.now())
        cookie = base64.b64encode(data.encode("utf-8"))
        cookie = str(cookie, "utf-8")
        bottle.response.set_cookie("user", cookie)
    if cookie in favourites.keys():
        pass
    else:
        favourites[cookie] = [None, []]
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
    if bottle.request.get_cookie("user"):
        cookie = bottle.request.get_cookie("user")
    else:
        data = str(datetime.now())
        cookie = base64.b64encode(data.encode("utf-8"))
        cookie = str(cookie, "utf-8")
        bottle.response.set_cookie("user", cookie)
    if cookie in favourites.keys():
        pass
    else:
        favourites[cookie] = [None, []]
    favourite = bottle.request.POST.get("favourite")
    if favourite is not None:
        insult = favourites[cookie][0]
        if insult not in favourites[cookie][1]:
            favourites[cookie][1].append(insult)
    else:
        genders = ["z", "m", "s"]
        gender = random.choice(genders)
        insult = Insult.generate("si", "custom", gender)
        favourites[cookie][0] = insult
    refresh = bottle.request.POST.get("refresh")
    if refresh is not None:
        return bottle.redirect("/prikazi-insult")
    return bottle.template("samostojno2.html", insult = insult)

Word.parse()
bottle.run(reloader=True, debug=True)
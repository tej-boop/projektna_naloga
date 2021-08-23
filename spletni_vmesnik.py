import bottle
import model

@bottle.get('/')
def osnovna_stran():
    return bottle.template('osnovna_stran.html')

bottle.run(reloader=True, debug=True)
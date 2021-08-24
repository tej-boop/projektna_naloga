import bottle
import model

bottle.TEMPLATE_PATH.insert(0, 'views')

@bottle.get('/')
def osnovna_stran():
    return bottle.template('osnovna_stran.tpl')

bottle.run(reloader=True, debug=True)
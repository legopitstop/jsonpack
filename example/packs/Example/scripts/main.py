from PIL import Image, ImageTk
from jsonpack import App, Context, Module, Node, Componentable, Eventable
import logging

# Module for handling client-side nodes
resoruce = Module( 'resources', 'default')

# ASSETS NODES

@resoruce.node('/assets/textures/**/*.png', mimetype='image/png')
class Texture(Node):
    traits = ['images']

# DATA NODES
# Module for handling server-side nodes
data = Module( 'data', 'default') 

@data.node('/data/items/**/*.json', mimetype='application/json')
class Item(Node, Componentable, Eventable):
    traits = ['components','events']
    def __init__(self, components:dict, events:dict=None):
        self.components = components
        self.events = events

@Item.component()
def display_name(ctx:Context, text:str):
    return text

@Item.component()
def on_click(ctx:Context, event:str):
    ctx.label.bind('<Button-1>', lambda tk, i=ctx.item, e=event: i.trigger_event(e))
    
@Item.component()
def icon(ctx:Context, texture:Texture.ref): # str should use Texture which will run Texture.validate to make sure the texture exists.
    photo = ctx.app.items['resources']['texture'].get(texture)
    if photo is not None:
        img = ImageTk.PhotoImage(photo.image.resize((64, 64), Image.NEAREST))
        ctx.app.cache.append('images', img)
        return ctx.app.cache.get('images', -1)
    else:
        ctx.logger.warning(f"'{ctx.__file__}' texture '{texture}' could not be found!")
    return None

@data.node('/data/test/**/*.zip', mimetype='application/zip')
class Zipper(Node):
    def on_unload(self, ctx:Context):
        """Close ZIP"""
        self.zip.close()

# EVENTS

@data.event('print')
def _print(ctx:Context, text:str):
    logging.info(text)

# NODES


# ITEM COMPONENTS

def on_enable(ctx: App):
    """Triggers when the pack has been enabled"""
    ctx.logger.info('Example/main.py loaded!')

def on_disable(ctx: App):
    """Triggers when the pack has been disabled"""
    ctx.logger.info('Example/main.py unloaded!')

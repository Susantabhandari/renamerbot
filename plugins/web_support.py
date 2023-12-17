# Don't Remove Credit @Susantabhandari Github
# Subscribe Telegram Channel For Amazing Bot @Susanta_Bhandarii
# Ask Doubt on telegram @lifegrambot

from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("Telegram Subscribe @Susanta_Bhandarii")


async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

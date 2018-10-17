from pyramid.response import Response
from pyramid.view import view_config, view_defaults


@view_defaults(route_name='members')
class MemberViews:
    def __init__(self, request):
        self.request = request
        self.view_name = 'MemberViews'

    @property
    def player_name(self):
        name = self.request.matchdict['name']
        character = self.request.matchdict['character']
        return f"Name: {name}; Character: {character}"

    @view_config(renderer='../templates/members.jinja2')
    def home(self):
        return {'page_title': 'Members List'}

    # Retrieving /members/{name}/{character}
    @view_config(route_name='player', renderer='../templates/player.jinja2')
    def player(self):
        return {'page_title': 'Player View'} 



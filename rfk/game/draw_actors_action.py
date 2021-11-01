from game.action import Action

# TODO: Define the DrawActorsAction class here
class DrawActorsAction(Action):
    def __init__(self, output_service):
        self._output_service = output_service


    def execute(self, cast):
        artifacts = cast["artifact"]
        marquee = cast["marquee"][0] # there's only one
        robot = cast["robot"][0]
        self._output_service.clear_screen()
        self._output_service.draw_actors(artifacts)
        self._output_service.draw_actor(marquee)
        self._output_service.draw_actor(robot)
        self._output_service.flush_buffer()
        pass
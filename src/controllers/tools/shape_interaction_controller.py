from tools.base_tool import Tool


class InteractionController:
    def __init__(self):
        self.active_tool: Tool | None = None

    def set_tool(self, tool: Tool | None):
        
        if self.active_tool:
            self.active_tool.on_deactivate()
        self.active_tool = tool

        if self.active_tool:
            self.active_tool.on_activate()

    def mouse_press(self, pos, button):
        if self.active_tool:
            self.active_tool.on_mouse_press(pos, button)

    def mouse_move(self, pos):
        if self.active_tool:
            self.active_tool.on_mouse_move(pos)

    def mouse_release(self, pos, button):
        if self.active_tool:
            self.active_tool.on_mouse_release(pos, button)

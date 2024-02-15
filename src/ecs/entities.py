class Entity:
    def __init__(self, entity_id):
        self.entity_id = entity_id
        self.components = {}

    def add_component(self, component) :
        self.components[type(component)] = component
    
    def get_component(self, component_type) :
        return self.components.get(component_type)
    
    def remove_component(self, component_type):
        if component_type in self.components:
            del self.components[component_type]
    
    def has_component(self, component_type):
        return component_type in self.components
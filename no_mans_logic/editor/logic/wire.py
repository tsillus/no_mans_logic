from no_mans_logic.editor.model.vector import Vector


class Wire:
    image = ''

    def __init__(self, source: Vector, target: Vector):
        self.source = source
        self.target = target

    def tick(self, signals):
        result = []
        for signal in signals:
            if signal.is_located_at(self.source):
                result.append(signal.propagate_to(self.target))
            elif signal.is_located_at(self.target):
                result.append((signal.propagate_to(self.source)))

        if len(result) <= 1:
            return result

        return [min(result)]

class EventEmitter(object):
  def __init__(self):
    self._eventListeners = {}

  def on(self, eventName, callback):
    self._eventListeners[eventName] = self._eventListeners.get(eventName, []) + [callback]

  def emit(self, eventName, data=None):
    for registeredEventName, events in self._eventListeners.items():
      if registeredEventName == eventName:
        for event in events:
          if data:
            event(data)
          else:
            event()
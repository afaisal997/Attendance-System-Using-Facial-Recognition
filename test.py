from Foundation import NSObject, NSApplicationDelegate

class AppDelegate(NSObject):
    def applicationSupportsSecureRestorableState_(self, app):
        return True

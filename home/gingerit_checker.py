from gingerit.gingerit import GingerIt

class GingeritChecker:
    def __init__(self):
        self.parser = GingerIt()

    def check_grammar(self, text):
        result = self.parser.parse(text)
        return result['corrections']

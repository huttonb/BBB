import bolt
class FireBolt(bolt.Bolt):
    def _init__(self):
        super().__init__("fire", 0, 15)

    def effect(target):
        target.health(-1)
        target.setaflame = True

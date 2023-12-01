class Display:
    def __init__(
        self,
        id,
        car_park,
        message="",
        is_on=False,
    ):
        self.id = id
        self.message = message
        self.is_on = is_on or False
        self.car_park = car_park

    def update(self, data):
        """Update display"""
        for key, value in data.items():
            print(f"{key}:{value}")
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                print(f"Key '{key}' does not exist in Display object.")

    def __str__(self):
        return f"{self.id}: Display is {'is on' if self.is_on else 'if off'}"

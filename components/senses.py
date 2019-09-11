class Senses:
    def __init__(self, alert_threshold, fov_radius=8, fov_radius_dark=0):
        self.alert_threshold=alert_threshold
        self.alertness=0
        self.fov_radius=fov_radius
        self.fov_radius_dark=fov_radius_dark
        # Maybe add scent tracing in the future???
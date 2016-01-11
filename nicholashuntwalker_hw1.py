class Position:
    """
    Take in x, y, and z components of position.
    Assumed units of meters.
    """
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Velocity:
    """
    Take in x, y, and z components of particle velocity.
    Assumed units of meters per second.
    """
    def __init__(self, vx, vy, vz):
        self.vx = vx
        self.vy = vy
        self.vz = vz

class Particle:
    """
    Take in mass (float), position (object), and velocity (object).
    Mass assumed in kg
    """
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.pos = position
        self.vel = velocity

    @staticmethod
    def force(p1, p2, G = 1):
        """
        Calculate and return the gravitational force between
        particles p1 and p2. In order for calculation to
        happen, particles need to have mass and a position object
        as properties.

        Assumed units of Newtons. By default, G is unitless
        """
        del_x = p1.pos.x - p2.pos.x 
        del_y = p1.pos.y - p2.pos.y
        del_z = p1.pos.z - p2.pos.z
        r_sq = del_x ** 2 + del_y ** 2 + del_z ** 2
        return G * p1.mass * p2.mass / r_sq

if __name__ == "__main__":
    Particle1 = Particle(200.0, Position(0., 0., 0.), Velocity(0., 0., 0.))
    Particle2 = Particle(1500.0, Position(3., 4., 5.), Velocity(5., 10., 15.))

    grav_force = Particle1.force(Particle1, Particle2, G=6.67E-11)
    print "Fg =", grav_force, "N"

import math
import geosys
import pytest


class ReferencePoint:
    def __init__(self):
        self.latitude = None
        self.longitude = None
        self.altitude = 0
        self.x = None
        self.y = None
        self.z = None
        self.ids = None


brno = ReferencePoint()
brno.latitude = 49.2002211
brno.longitude = 16.6078411
brno.x = 4001412.65349505
brno.y = 1193469.21673459
brno.z = 4805137.77147738
brno.ids = "test_as_brno"


brno_altitude = ReferencePoint()
brno_altitude.latitude = 49.2002211
brno_altitude.longitude = 16.6078411
brno_altitude.altitude = 1989
brno_altitude.x = 4002658.08446854
brno_altitude.y = 1193840.68142897
brno_altitude.z = 4806643.43965832
brno_altitude.ids = "test_brno_altitude"

null_island = ReferencePoint()
null_island.latitude = 0
null_island.longitude = 0
null_island.x = 6378137
null_island.y = 0
null_island.z = 0
null_island.ids = "test_null_island"


null_island_altitude = ReferencePoint()
null_island_altitude.latitude = 0
null_island_altitude.longitude = 0
null_island_altitude.altitude = 1989
null_island_altitude.x = 6380126
null_island_altitude.y = 0
null_island_altitude.z = 0
null_island_altitude.ids = "test_null_island_altitude"


north_pole = ReferencePoint()
north_pole.latitude = 90
north_pole.longitude = 0
north_pole.x = 3.91849150799252e-10
north_pole.y = 0
north_pole.z = 6356752.31415482
north_pole.ids = "test_north_pole"


north_pole_altitude = ReferencePoint()
north_pole_altitude.latitude = 90
north_pole_altitude.longitude = 0
north_pole_altitude.altitude = 1989
north_pole_altitude.x = 3.91970937901139e-10
north_pole_altitude.y = 0
north_pole_altitude.z = 6358741.31415482
north_pole_altitude.ids = "test_north_pole_altitude"


south_pole = ReferencePoint()
south_pole.latitude = -90
south_pole.longitude = 0
south_pole.x = 3.91849150799252e-10
south_pole.y = 0
south_pole.z = -6356752.31415482
south_pole.ids = "test_south_pole"


south_pole_altitude = ReferencePoint()
south_pole_altitude.latitude = -90
south_pole_altitude.longitude = 0
south_pole_altitude.altitude = 1989
south_pole_altitude.x = 3.91970937901139e-10
south_pole_altitude.y = 0
south_pole_altitude.z = -6358741.31415482
south_pole_altitude.ids = "test_south_pole_altitude"


sydney_altitude = ReferencePoint()
sydney_altitude.latitude = -33.8559799094
sydney_altitude.longitude = 151.20666584
sydney_altitude.altitude = 1989
sydney_altitude.x = -4648075.79053196
sydney_altitude.y = 2554597.1391822
sydney_altitude.z = -3534299.67369454
sydney_altitude.ids = "test_sydney"

meridian180 = ReferencePoint()
meridian180.latitude = 0
meridian180.longitude = 180
meridian180.altitude = 0
meridian180.x = -6378137
meridian180.y = 7.8107070957496e-10
meridian180.z = 0
meridian180.ids = "test_meridian180"

meridian180_altitude = ReferencePoint()
meridian180_altitude.latitude = 0
meridian180_altitude.longitude = 180
meridian180_altitude.altitude = 1989
meridian180_altitude.x = -6380126
meridian180_altitude.y = 7.81314283778735E-10
meridian180_altitude.z = 0
meridian180_altitude.ids = "test_meridian180_altitude"

reference_points = [
    brno,
    brno_altitude,
    null_island,
    null_island_altitude,
    north_pole,
    north_pole_altitude,
    south_pole,
    south_pole_altitude,
    sydney_altitude,
    meridian180,
    meridian180_altitude
]


@pytest.mark.parametrize("reference_point", reference_points, ids=[p.ids for p in reference_points])
def test_convert_to_cartesian(reference_point):
    point = geosys.WSG84.to_cartesian(reference_point.latitude,
                                      reference_point.longitude,
                                      reference_point.altitude)

    tolerance = 0.0001

    assert math.isclose(point.x, reference_point.x, abs_tol=tolerance) == True
    assert math.isclose(point.y, reference_point.y, abs_tol=tolerance) == True
    assert math.isclose(point.z, reference_point.z, abs_tol=tolerance) == True


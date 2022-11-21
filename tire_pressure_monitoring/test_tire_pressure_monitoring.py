import unittest
from unittest.mock import patch

from tire_pressure_monitoring.tire_pressure_monitoring import Alarm


class AlarmTest(unittest.TestCase):

    def test_alarm_is_off_by_default(self):
        alarm = Alarm()
        assert not alarm.is_alarm_on

    @patch("tire_pressure_monitoring.sensor.Sensor.pop_next_pressure_psi_value")
    def test_alarm_is_on_when_below_low_pressure_threshold(self, pop_next_pressure_psi_value):
        pop_next_pressure_psi_value.return_value = 16
        alarm = Alarm()
        alarm.check()
        assert alarm.is_alarm_on

    @patch("tire_pressure_monitoring.sensor.Sensor.pop_next_pressure_psi_value")
    def test_alarm_is_on_when_above_high_pressure_threshold(self, pop_next_pressure_psi_value):
        pop_next_pressure_psi_value.return_value = 22
        alarm = Alarm()
        alarm.check()
        assert alarm.is_alarm_on


    @patch("tire_pressure_monitoring.sensor.Sensor.pop_next_pressure_psi_value")
    def test_alarm_is_off_when_within_range(self, pop_next_pressure_psi_value):
        pop_next_pressure_psi_value.return_value = 19
        alarm = Alarm()
        alarm.check()
        assert not alarm.is_alarm_on

import unittest
from unittest.mock import patch

from telemetry_system.telemetry import *


class TelemetryDiagnosticControlsTest(unittest.TestCase):
    def test_diagnostic_info_default(self):
        diagnostics = TelemetryDiagnostics()
        self.assertEqual("", diagnostics.diagnostic_info)

    def test_check_transmission_raises_exception(self):
        diagnostics = TelemetryDiagnostics()
        self.assertRaises(Exception, diagnostics.check_transmission())
        self.assertTrue("Unable to connect.", str(diagnostics.check_transmission()))


    @patch("telemetry_system.client.TelemetryClient.online_status")
    def test_check_transmission_does_not_raise_exception_when_connect_not_false(self, online_status):
        online_status.return_value = 2
        diagnostics = TelemetryDiagnostics()
        assert diagnostics.check_transmission() is None


    @patch("telemetry_system.client.TelemetryClient.online_status")
    def test_check_transmission_receives_message(self, online_status):
        online_status.return_value = 2
        diagnostics = TelemetryDiagnostics()
        diagnostics.check_transmission()
        assert diagnostics.diagnostic_info != ""


    @patch("telemetry_system.client.TelemetryClient.online_status")
    def test_check_transmission_sends_message(self, online_status):
        online_status.return_value = 2
        client = TelemetryClient()
        diagnostics = TelemetryDiagnostics()
        diagnostics.check_transmission()
        assert client.DIAGNOSTIC_MESSAGE == "AT#UD"


if __name__ == "__main__":
    unittest.main()

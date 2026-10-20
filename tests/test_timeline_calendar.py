import importlib.util
from pathlib import Path
from datetime import date
import unittest
p = Path(__file__).resolve().parents[1] / 'skills/agentic-artefact-project-collaboration/scripts/timeline_calendar.py'
spec = importlib.util.spec_from_file_location('timeline_calendar', p)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class CalendarTests(unittest.TestCase):
    def test_friday_start_stays_in_natural_week(self):
        w = m.calendar_weeks(date(2026, 10, 16), date(2026, 10, 23))
        self.assertEqual(w[0]['dates'], ['2026-10-12', '2026-10-13', '2026-10-14', '2026-10-15', '2026-10-16'])
        self.assertEqual(w[1]['week_start'], '2026-10-19')

    def test_year_boundary_and_weekends(self):
        w = m.calendar_weeks(date(2026, 12, 31), date(2027, 1, 4), True)
        self.assertEqual(w[0]['week_start'], '2026-12-28')
        self.assertEqual(w[0]['dates'][-1], '2027-01-03')
        self.assertEqual(w[1]['week_start'], '2027-01-04')

    def test_invalid_span(self):
        with self.assertRaises(ValueError):
            m.calendar_weeks(date(2026, 10, 20), date(2026, 10, 19))

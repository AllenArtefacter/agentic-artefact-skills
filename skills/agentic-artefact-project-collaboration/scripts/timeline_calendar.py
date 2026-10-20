#!/usr/bin/env python3
"""Emit natural-week date groups for a timeline (no cloud writes)."""
import argparse
import json
from datetime import date, timedelta


def calendar_weeks(start, end, weekends=False):
    if end < start:
        raise ValueError('End must not precede start')
    monday = start - timedelta(days=start.weekday())
    weeks = []
    while monday <= end:
        days = [monday + timedelta(days=i) for i in range(7 if weekends else 5)]
        weeks.append({'week_start': monday.isoformat(),
                      'label': 'Week of ' + monday.isoformat(),
                      'dates': [d.isoformat() for d in days]})
        monday += timedelta(days=7)
    return weeks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--start', type=date.fromisoformat, required=True)
    parser.add_argument('--end', type=date.fromisoformat, required=True)
    parser.add_argument('--include-weekends', action='store_true')
    args = parser.parse_args()
    try:
        weeks = calendar_weeks(args.start, args.end, args.include_weekends)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps({'weeks': weeks}, indent=2))


if __name__ == '__main__':
    main()

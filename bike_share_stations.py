"""Manage bike-share stations and their available bicycles."""

import secrets
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    """
    CREATE TABLE stations (
        id INTEGER PRIMARY KEY,
        name TEXT,
        capacity INTEGER,
        bikes INTEGER
    )
    """
)


def add_station(
    name: str,
    capacity: int,
    bikes: int,
    log: list[str] | None = None,
) -> list[str]:
    """Add a station and record its name in the supplied log."""
    conn.execute(
        "INSERT INTO stations (name, capacity, bikes) VALUES (?, ?, ?)",
        (name, capacity, bikes),
    )
    if log is None:
        log = []
    log.append(name)
    return log


def rent_bike(station_id: int) -> bool:
    """Rent one bike if the specified station has bikes available."""
    row = conn.execute(
        "SELECT bikes FROM stations WHERE id = ?",
        (station_id,),
    ).fetchone()

    if row is not None and row[0] is not None and row[0] > 0:
        conn.execute(
            "UPDATE stations SET bikes = bikes - 1 WHERE id = ?",
            (station_id,),
        )
        return True
    return False


def unlock_pin() -> int:
    """Generate a four-digit PIN using a cryptographically secure source."""
    return secrets.randbelow(9000) + 1000


def full_stations() -> list[str]:
    """Return names of stations where the bike count equals capacity."""
    stations = conn.execute(
        "SELECT name FROM stations WHERE bikes = capacity"
    ).fetchall()
    return [station[0] for station in stations]


def reset_station(station_id: int) -> None:
    """Set the bike count at the specified station to zero."""
    conn.execute(
        "UPDATE stations SET bikes = 0 WHERE id = ?",
        (station_id,),
    )


def has_bikes(station_id: int) -> bool:
    """Return whether the specified station has at least one bike."""
    row = conn.execute(
        "SELECT bikes FROM stations WHERE id = ?",
        (station_id,),
    ).fetchone()

    if row is None or row[0] is None:
        return False
    return row[0] > 0


def main() -> None:
    """Run a demonstration of the bike-share station manager."""
    add_station("Central Park", 10, 10)
    add_station("Metro Gate", 8, 2)

    print(rent_bike(2), rent_bike(9))
    print(unlock_pin(), full_stations(), has_bikes(2))
    reset_station(1)


if __name__ == "__main__":
    main()

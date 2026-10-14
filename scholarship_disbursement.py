"""Manage scholarship awards and track their disbursement status."""

import sqlite3

CONN = sqlite3.connect(":memory:")
CONN.execute(
    """
    CREATE TABLE awards (
        id INTEGER PRIMARY KEY,
        student TEXT,
        scheme TEXT,
        amount INTEGER,
        disbursed INTEGER
    )
    """
)


def grant(student, scheme, amount, audit=None):
    """Create a scholarship award and record the student in the audit list."""
    if audit is None:
        audit = []

    CONN.execute(
        """
        INSERT INTO awards (student, scheme, amount, disbursed)
        VALUES (?, ?, ?, 0)
        """,
        (student, scheme, amount),
    )
    audit.append(student)
    return audit


def disburse(award_id):
    """Disburse an award, or return None if it does not exist."""
    row = CONN.execute(
        "SELECT amount, disbursed FROM awards WHERE id = ?",
        (award_id,),
    ).fetchone()

    if row is not None and row[1] == 0:
        CONN.execute(
            "UPDATE awards SET disbursed = 1 WHERE id = ?",
            (award_id,),
        )
        return row[0]

    return None


def archive():
    """Print a message indicating that the awards are being archived."""
    print("archiving awards")


def by_scheme_count(scheme):
    """Return the number of awards for a scheme."""
    if scheme is None:
        return 0

    return CONN.execute(
        "SELECT COUNT(*) FROM awards WHERE scheme = ?",
        (scheme,),
    ).fetchone()[0]


def main():
    """Run a demonstration of the scholarship disbursement ledger."""
    grant("Ishaan", "Merit", 50000)
    grant("Divya", "Need-based", 75000)

    first_disbursement = disburse(1)
    missing_disbursement = disburse(9)

    disbursed_total = sum(
        amount
        for amount in (first_disbursement, missing_disbursement)
        if amount is not None
    )

    print(first_disbursement, missing_disbursement)
    print(by_scheme_count("Merit"), disbursed_total)
    archive()


if __name__ == "__main__":
    main()

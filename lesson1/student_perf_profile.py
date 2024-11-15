from pathlib import Path

import ydata_profiling

TEMP = Path("/tmp")


def student_performance_report() -> None:
    data = ydata_profiling.load_dataset(TEMP / "student-mat.csv")

    ydata_profiling.generate_report(data, TEMP / "student_perf_report.html")


if __name__ == "__main__":
    student_performance_report()

def generate_monthly_report(attendances):
    """
    ダミーAIレポート生成
    （本番では外部AI APIに差し替え可能）
    """
    if not attendances:
        return "勤怠データがありません。"

    total_days = len(attendances)

    total_hours = 0
    for a in attendances:
        start = a["start_time"]
        end = a["end_time"]

        start_h, start_m = map(int, start.split(":"))
        end_h, end_m = map(int, end.split(":"))

        total_hours += (end_h * 60 + end_m) - (start_h * 60 + start_m)

    total_hours = round(total_hours / 60, 1)

    return (
        f"今月の出勤日数は {total_days} 日でした。\n"
        f"総労働時間は 約 {total_hours} 時間です。\n"
        "全体的に安定した勤務状況です。"
    )

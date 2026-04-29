# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-29 12:55:09 EDT`
Last processed slot: `manage_1300`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$16,772.50`
- Equity: `$16,772.50`
- Realized PnL: `$6,772.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-04-29)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  INTC     option         option INTC260529C00084000     10          2026-04-28         2026-04-29        7.075        8.85 1775.0   25.088339 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
    ZS           84.38               32            1.39              1.32        135.50                65.17            True
  SNPS           95.24               21            2.09              7.06        480.86                50.93            True
  FAST           82.35               17            1.69              0.53         44.45                39.66            True
  WDAY           83.72               43            0.96              0.82        120.83                63.12            True
  ADSK           88.89               27            1.37              2.25        233.89                45.23            True
  CRWD           82.35               34            1.19              3.80        453.36                53.30            True
  CDNS           93.75               32            1.32              3.01        324.04                53.80            True
   CSX           88.46               26            0.71              0.22         45.13                28.77            True
  AVGO           91.89               37            0.59              1.64        399.13                43.25            True
 CMCSA          100.00                8            1.43              0.28         27.53                60.29           False
  CHTR          100.00                2            4.64              5.61        170.61               113.02           False
  ASML           87.50               40            0.13              1.24       1384.03                50.71           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-29T12:55:09.686981-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-29T12:40:11.745307-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-29T12:35:07.057965-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-29T12:30:04.773295-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-29T12:25:04.979686-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-29T12:10:08.034825-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-29T12:05:04.313090-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-29T12:00:06.336773-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-29T11:55:05.214410-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-29T11:40:04.893859-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260429125509)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260429125509)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260429125509)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260429125509)

</details>

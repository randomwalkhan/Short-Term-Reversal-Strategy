# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-29 13:25:10 EDT`
Last processed slot: `manage_1330`

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
    ZS           83.33               30            1.51              1.44        135.45                65.17            True
  CRWD           81.48               27            1.54              4.89        452.89                53.30            True
  FAST           86.67               15            2.03              0.63         44.40                39.66            True
  ADSK           88.89               27            1.36              2.23        233.89                45.23            True
  SNPS           96.00               25            2.00              6.76        480.99                50.93            True
  WDAY           81.58               38            1.39              1.18        120.68                63.12            True
   XEL           95.65               23            0.72              0.40         79.31                20.53            True
  CDNS           93.10               29            1.46              3.33        323.91                53.80            True
   CSX           88.00               25            0.76              0.24         45.13                28.77            True
  UPRO           91.18               34            0.88              0.77        125.36                42.06            True
 CMCSA          100.00                4            1.84              0.36         27.50                60.29           False
  CHTR          100.00                1            5.67              6.87        170.08               113.02           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-29T13:25:10.874925-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-29T13:10:07.449671-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-29T13:05:10.681495-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-29T13:00:11.844514-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-29T12:55:09.686981-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-29T12:40:11.745307-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-29T12:35:07.057965-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-29T12:30:04.773295-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-29T12:25:04.979686-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-29T12:10:08.034825-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260429132510)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260429132510)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260429132510)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260429132510)

</details>

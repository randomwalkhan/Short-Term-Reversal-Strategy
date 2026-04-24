# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-24 14:40:02 EDT`
Last processed slot: `manage_1430`

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

- Cash: `$14,045.50`
- Equity: `$14,045.50`
- Realized PnL: `$4,045.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-04-24)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  NVDA     option         option NVDA260618C00200000      5          2026-04-23         2026-04-24       12.325      14.475 1075.0   17.444219 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FANG          100.00               25            0.71              0.97        195.18                34.00            True
  NFLX           94.87               39            0.58              0.37         92.66                46.09            True
  MRVL           96.97               33            1.00              1.16        165.06                67.12            True
  FAST           88.00               25            1.32              0.42         45.27                38.70            True
   CSX           85.71               21            1.03              0.33         46.04                27.21            True
   WMT           81.82               11            1.93              1.79        131.26                24.33            True
  MSTR           80.95               42            0.75              0.91        172.08                74.46            True
  MDLZ           80.95               21            0.81              0.33         57.57                22.00            True
   APP           83.33               36            1.04              3.30        452.75                77.03            True
  AAPL           82.61               23            1.17              2.25        272.47                25.85            True
   TXN           79.17               24            1.62              3.20        280.86                66.99           False
   ADI           84.62               39            0.33              0.95        403.47                40.58           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-24T14:40:02.156742-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-24T14:35:05.332979-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-24T14:30:02.109645-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-24T14:25:02.113704-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-24T14:10:02.102094-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-24T14:05:04.100469-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-24T14:00:02.276536-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-24T13:55:05.319263-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-24T13:40:02.186193-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-24T13:35:02.128059-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260424144002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260424144002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260424144002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260424144002)

</details>

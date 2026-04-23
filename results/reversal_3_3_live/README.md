# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-23 16:00:04 EDT`
Last processed slot: `manage_1600`

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

- Cash: `$6,808.00`
- Equity: `$13,045.50`
- Realized PnL: `$2,970.50`
- Unrealized PnL: `$75.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  NVDA     option         option NVDA260618C00200000       2026-04-23                   0      5      6162.5                  6237.5        12.32          12.48      198.79        199.83            75.0                   1.22         95.24               21              1.83          41.3           40.45                  33.17              111167.0         4613.0                0.0                      ok
```

## Today's Closed Trades (2026-04-23)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price        pnl  return_pct                   exit_reason
  INTC     option         option INTC260618C00065000      8          2026-04-22         2026-04-23     7.450000    8.675000 980.000000   16.442953  take_profit_day1_hit_at_scan
  ROST      share share_fallback                ROST     26          2026-04-21         2026-04-23   225.914993  226.550003  16.510254    0.281083 share_fallback_retired_in_3_3
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
    MU           83.33               36            1.25              4.26        485.66                79.49            True
  UPRO           90.00               30            1.27              1.12        125.21                53.56            True
  CSCO           81.25               16            1.34              0.84         89.44                27.83            True
  AVGO           91.67               36            0.63              1.87        421.85                44.55            True
  NVDA           92.31               26            1.41              2.00        201.64                33.17            True
  META           68.75               16            2.28             10.77        670.10                51.97           False
  NFLX           97.56               41            0.45              0.29         93.11                46.34           False
  LRCX           72.73               22            2.62              4.87        263.46                67.48           False
  ASML           79.17               24            1.86             18.77       1435.62                53.38           False
   WBD           50.00                2            1.57              0.30         27.20                 7.69           False
  AMZN           85.37               41            0.09              0.17        255.29                33.82           False
  ABNB           88.46               26            1.58              1.60        143.50                37.26           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-23T16:00:04.974935-04:00 manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-23T15:55:05.889210-04:00 manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-23T15:50:06.563469-04:00 manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-23T15:40:01.688489-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-23T15:35:05.849801-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-23T15:30:06.675694-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-23T15:25:05.676765-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-23T15:10:03.835194-04:00  entry_1500 slot_skipped {"reason": "already_processed"}
2026-04-23T15:05:05.649293-04:00  entry_1500 slot_skipped {"reason": "already_processed"}
2026-04-23T15:00:02.837489-04:00  entry_1500 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260423160004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260423160004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260423160004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260423160004)

</details>

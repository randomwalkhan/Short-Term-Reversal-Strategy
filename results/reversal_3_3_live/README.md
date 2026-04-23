# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-23 15:45:05 EDT`
Last processed slot: `manual`

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
- Equity: `$12,945.50`
- Realized PnL: `$2,970.50`
- Unrealized PnL: `$-25.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  NVDA     option         option NVDA260618C00200000       2026-04-23                   0      5      6162.5                  6137.5        12.32          12.28      198.79        199.29           -25.0                  -0.41         95.24               21              1.83          41.3           40.19                  33.17              111167.0         4613.0                0.0                      ok
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
  UPRO           92.59               27            1.62              1.43        125.08                53.56            True
    MU           81.82               33            2.30              7.84        484.12                79.49            True
  CSCO           85.71               21            1.17              0.73         89.48                27.83            True
  AVGO           91.67               36            0.90              2.65        421.51                44.55            True
  NVDA           95.65               23            1.64              2.33        201.50                33.17            True
  ASML           80.95               21            2.44             24.69       1433.08                53.38            True
  KLAC           86.84               38            0.20              2.53       1810.97                51.27           False
  META           72.22               18            2.22             10.48        670.23                51.97           False
  AMAT           86.84               38            0.45              1.27        402.93                55.83           False
   WBD           85.71                7            1.36              0.26         27.22                 7.69           False
  NFLX           97.67               43            0.33              0.22         93.15                46.34           False
  LRCX           68.75               16            3.62              6.72        262.67                67.48           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                                                                                                                                                                                        detail
2026-04-23T15:40:01.688489-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T15:35:05.849801-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T15:30:06.675694-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T15:25:05.676765-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T15:10:03.835194-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T15:05:05.649293-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T15:00:02.837489-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T14:55:05.925620-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T14:50:05.228027-04:00  entry_1500        entry {"allocated_cash": 6162.5, "asset_type": "option", "contract_symbol": "NVDA260618C00200000", "contracts": 5, "entry_option_price": 12.325, "execution_mode": "option", "matched_signals": 21, "option_liquidity_status": "ok", "option_open_interest": 111167.0, "option_spread_pct": 0.41, "option_volume": 4613.0, "success_rate": 95.24, "ticker": "NVDA"}
2026-04-23T14:40:04.065338-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260423154505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260423154505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260423154505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260423154505)

</details>

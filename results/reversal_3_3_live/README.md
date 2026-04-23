# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-23 15:05:05 EDT`
Last processed slot: `entry_1500`

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
- Equity: `$13,070.50`
- Realized PnL: `$2,970.50`
- Unrealized PnL: `$100.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  NVDA     option         option NVDA260618C00200000       2026-04-23                   0      5      6162.5                  6262.5        12.32          12.52      198.79        198.75           100.0                   1.62         95.24               21              1.83          41.3           41.98                  33.17              111167.0         4613.0                0.0                      ok
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
  UPRO           92.86               28            1.52              1.34        125.12                53.56            True
  AMAT           83.87               31            1.06              3.00        402.19                55.83            True
  AVGO           91.67               36            0.61              1.81        421.87                44.55            True
  KLAC           85.71               35            0.93             11.76       1807.02                51.27            True
  CSCO           86.96               23            0.94              0.59         89.55                27.83            True
  ASML           88.24               17            2.72             27.49       1431.88                53.38            True
    MU           81.25               32            2.59              8.84        483.69                79.49            True
  NVDA           95.00               20            1.92              2.72        201.34                33.17            True
  META           68.75               16            2.52             11.89        669.62                51.97           False
   WBD           78.57               14            1.01              0.19         27.25                 7.69           False
  ABNB           87.50               24            1.69              1.70        143.45                37.26           False
  AMZN           85.71               42            0.05              0.08        255.32                33.82           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                                                                                                                                                                                        detail
2026-04-23T15:05:05.649293-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T15:00:02.837489-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T14:55:05.925620-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T14:50:05.228027-04:00  entry_1500        entry {"allocated_cash": 6162.5, "asset_type": "option", "contract_symbol": "NVDA260618C00200000", "contracts": 5, "entry_option_price": 12.325, "execution_mode": "option", "matched_signals": 21, "option_liquidity_status": "ok", "option_open_interest": 111167.0, "option_spread_pct": 0.41, "option_volume": 4613.0, "success_rate": 95.24, "ticker": "NVDA"}
2026-04-23T14:40:04.065338-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T14:35:04.153865-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T14:30:04.173942-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T14:25:01.235972-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T14:10:04.443812-04:00 manage_1400 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T14:05:01.396383-04:00 manage_1400 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260423150505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260423150505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260423150505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260423150505)

</details>

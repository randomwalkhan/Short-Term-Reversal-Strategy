# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-23 16:00:00 EDT`
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

- Cash: `$6,805.01`
- Equity: `$13,005.01`
- Realized PnL: `$2,967.51`
- Unrealized PnL: `$37.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  NVDA     option         option NVDA260618C00200000       2026-04-23                   0      5      6162.5                  6200.0        12.32           12.4      198.79        198.41            37.5                   0.61         95.24               21              1.83          41.3           42.14                  33.17              111167.0         4613.0                0.0                      ok
```

## Today's Closed Trades (2026-04-23)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price        pnl  return_pct                  exit_reason
  INTC     option         option INTC260618C00065000      8          2026-04-22         2026-04-23     7.450000    8.675000 980.000000   16.442953 take_profit_day1_hit_at_scan
  ROST      share share_fallback                ROST     26          2026-04-21         2026-04-23   225.914993  226.434998  13.520111    0.230177        time_exit_at_4pm_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  UPRO           92.59               27            1.81              1.59        125.01                53.56            True
  AMAT           85.71               35            0.87              2.45        402.43                55.83            True
  KLAC           86.49               37            0.61              7.69       1808.77                51.27            True
  AVGO           91.67               36            0.71              2.09        421.76                44.55            True
  CSCO           86.36               22            1.10              0.69         89.50                27.83            True
    MU           81.25               32            2.61              8.91        483.66                79.49            True
  NVDA           94.44               18            2.07              2.94        201.24                33.17            True
  META           73.33               15            2.57             12.12        669.53                51.97           False
  NFLX           97.78               45            0.18              0.12         93.19                46.34           False
  ASML           78.95               19            2.57             26.01       1432.51                53.38           False
   WBD           78.57               14            1.02              0.20         27.25                 7.69           False
  ABNB           87.50               24            1.65              1.67        143.47                37.26           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                                                                                                                                                                                        detail
       2026-04-23T16:00:00-04:00 manage_1600         exit                                                                                                                                                                                              {"asset_type": "share", "contract_symbol": "ROST", "fill_price": 226.435, "pnl": 13.52, "reason": "time_exit_at_4pm_scan", "return_pct": 0.23, "ticker": "ROST"}
2026-04-23T14:55:05.925620-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T14:50:05.228027-04:00  entry_1500        entry {"allocated_cash": 6162.5, "asset_type": "option", "contract_symbol": "NVDA260618C00200000", "contracts": 5, "entry_option_price": 12.325, "execution_mode": "option", "matched_signals": 21, "option_liquidity_status": "ok", "option_open_interest": 111167.0, "option_spread_pct": 0.41, "option_volume": 4613.0, "success_rate": 95.24, "ticker": "NVDA"}
2026-04-23T14:40:04.065338-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T14:35:04.153865-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T14:30:04.173942-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T14:25:01.235972-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T14:10:04.443812-04:00 manage_1400 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T14:05:01.396383-04:00 manage_1400 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T14:00:03.244541-04:00 manage_1400 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260423160000)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260423160000)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260423160000)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260423160000)

</details>

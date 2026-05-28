# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-28 10:05:05 EDT`
Last processed slot: `manage_1000`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$17,884.25`
- Equity: `$30,384.25`
- Realized PnL: `$20,384.25`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-28                   0      4     12500.0                 12500.0        31.25          31.25      419.65         418.9          bid_ask_mid                      31.25                bid_ask_mid                    True             0.0                    0.0         89.19               37              0.52         51.04           51.04                  36.99                2631.0           27.0               0.06                      ok
```

## Today's Closed Trades (2026-05-28)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SNPS     option         option SNPS260717C00500000      2          2026-05-27         2026-05-28        60.05      54.045 -1201.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  CSCO           88.24               17            1.33              1.12        119.19                51.65         0.641          pass              0.340              3.0                           0.201               15.91              0.847                  ok            True                  False
  FTNT          100.00               34            0.93              0.83        127.57                70.83         0.628          pass              0.634              3.6                           0.055                7.69              0.868                  ok            True                  False
    MU           82.76               29            2.27             14.72        922.10               100.84         0.608          pass              0.431             56.6                           0.293               12.91              2.038                  ok            True                  False
  ASML           94.12               34            0.62              6.95       1594.89                53.18         0.576          pass              0.727             44.4                           0.220                0.40              0.543                  ok            True                  False
  SOXL           90.48               21            4.36              6.66        215.13               139.87         0.538          pass              0.598             64.0                           0.330               13.15              2.564                  ok            True                  False
  MNST           89.66               29            0.78              0.49         89.03                49.17         0.536          pass              0.568             43.5                           0.322                3.04              0.252                  ok            True                  False
   XEL           96.15               26            0.79              0.45         80.81                25.49         0.533          pass              0.620             20.0                           0.246                0.56              0.241                  ok            True                  False
  AMAT           83.33               24            1.75              5.49        445.90                50.47         0.529          pass              0.300             21.5                           0.238                0.99              0.356                  ok            True                  False
  INTC           92.86               14            4.27              3.64        120.21                92.16         0.525          pass              0.438              5.5                           0.087               -3.09              0.630                  ok            True                  False
   LIN           84.62               13            1.53              5.43        505.54                20.85         0.514          pass              0.214              6.5                           0.171               -2.56             -0.059                  ok            True                  False
  NXPI           88.89               27            1.26              2.91        327.99                91.24         0.507          pass              0.590             63.0                           0.373                8.94              1.323                  ok            True                  False
   TXN           95.83               24            1.05              2.33        316.45                35.35         0.504          pass              0.665             40.5                           0.208                2.54              0.454                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-05-28T10:05:05.949315-04:00 early_entry_1005          entry {"allocated_cash": 12500.0, "asset_type": "option", "contract_symbol": "AVGO260717C00420000", "contracts": 4, "early_entry_score": 0.738, "entry_mode": "early", "entry_option_price": 31.25, "execution_mode": "option", "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 2631.0, "option_spread_pct": 5.76, "option_volume": 27.0, "success_rate": 89.19, "ticker": "AVGO", "timing_score": 0.427}
2026-05-28T10:05:05.949315-04:00      manage_1000           exit                                                                                                                                                                                                                                                  {"asset_type": "option", "contract_symbol": "SNPS260717C00500000", "fill_price": 54.045, "pnl": -1201.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SNPS"}
2026-05-28T10:00:04.925583-04:00 early_entry_1000  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate"}
2026-05-28T00:00:03.757313-04:00     data_refresh   data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 92}
2026-05-27T15:10:02.000661-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-05-27T15:05:04.292282-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-05-27T15:00:06.354268-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-05-27T14:55:06.489057-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-05-27T14:50:01.720844-04:00       entry_1500  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-27T14:50:01.720844-04:00       entry_1500 timing_overlay                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-27", "training_samples": 5097, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260528100505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260528100505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260528100505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260528100505)

</details>

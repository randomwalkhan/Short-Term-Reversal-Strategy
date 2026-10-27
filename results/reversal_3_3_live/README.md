# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-27 10:00:04 EDT`
Last processed slot: `manage_1000`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
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

- Cash: `$1,421.80`
- Equity: `$142,736.80`
- Realized PnL: `$127,691.80`
- Unrealized PnL: `$5,045.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   EXC     option         option  EXC261218C00045000       2026-10-23                   2    657     72270.0                 75555.0          1.1           1.15       44.42         44.41          bid_ask_mid                       1.15                bid_ask_mid                    True          3285.0                   4.55          80.0               15              0.97         20.09           26.81                  20.91                 278.0           48.0               0.09                      ok
  TEAM     option         option TEAM261218C00230000       2026-10-26                   1     32     64000.0                 65760.0         20.0          20.55      220.60        219.66          bid_ask_mid                      20.55                bid_ask_mid                    True          1760.0                   2.75         100.0               12              3.08         70.90           74.54                  47.89                 302.0           39.0               0.10                      ok
```

## Today's Closed Trades (2026-10-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MDLZ           91.67               12            0.82              0.36         62.82                25.86         0.602          pass              0.481             32.2                           0.500                1.55              0.154                      ok            True                  False
   KHC           85.71               21            1.13              0.20         24.65                34.80         0.561          pass              0.335             17.6                           0.222                9.01              0.994                      ok            True                  False
   KDP           93.33               15            1.24              0.30         34.86                25.67         0.556          pass              0.561             38.7                           0.481                5.80              0.526                      ok            True                  False
  CTSH          100.00               11            2.74              1.33         68.77                46.75         0.555          pass              0.503             13.7                           0.151                9.97              1.239                      ok            True                  False
   PEP           80.95               21            0.75              0.71        135.16                25.06         0.539          pass              0.237             28.0                           0.510                5.61              0.677                      ok            True                  False
  GILD           92.00               25            0.98              1.09        158.22                28.72         0.528          pass              0.613             46.8                           0.567                6.23              0.386                      ok            True                  False
  TEAM          100.00               27            1.68              2.63        222.29                43.78         0.522          pass              0.625             20.0                           0.202                5.59              0.869                      ok            True                  False
   XEL           87.50               24            0.59              0.32         77.72                17.40         0.507          pass              0.421             25.8                           0.221                3.70              0.468                      ok            True                  False
  MSFT           96.15               26            0.66              2.47        531.54                19.60         0.502          pass              0.637             26.6                           0.231               -2.65             -0.234                      ok            True                  False
  VRTX           84.62               26            1.04              3.78        515.87                29.88         0.502          pass              0.384             34.8                           0.372                5.54              0.626                      ok            True                  False
  INTU           84.21               19            2.11              5.03        337.74                38.11         0.502          pass              0.250              9.1                           0.138               10.37              1.072                      ok            True                  False
  TMUS           82.76               29            0.58              0.60        146.67                64.06         0.670          pass              0.402             44.8                           0.331               -4.98             -0.697 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-10-27T10:00:04.985513-04:00 early_entry_1000      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-27T00:00:06.979802-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                            {'saved': 91, 'empty': 2}
2026-10-26T15:10:06.955297-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-26T15:05:03.905393-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-26T15:00:06.230753-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-26T14:55:05.952188-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-10-26T14:50:06.038156-04:00       entry_1500                   entry {"allocated_cash": 64000.0, "asset_type": "option", "contract_symbol": "TEAM261218C00230000", "contracts": 32, "early_entry_score": 0.492, "entry_mode": "regular", "entry_option_price": 20.0, "execution_mode": "option", "matched_signals": 12, "option_liquidity_status": "ok", "option_open_interest": 302.0, "option_spread_pct": 10.0, "option_volume": 39.0, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.514}
2026-10-26T14:50:06.038156-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                {"early_entry_score": 0.565, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 81.0, "option_spread_pct": 22.0, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "KHC", "timing_score": 0.533}
2026-10-26T14:50:06.038156-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                {"early_entry_score": 0.52, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 722.0, "option_spread_pct": 14.29, "option_volume": 6.0, "reason": "no_trade_low_option_liquidity", "ticker": "CTSH", "timing_score": 0.538}
2026-10-26T14:50:06.038156-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-26", "training_samples": 6183, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261027100004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261027100004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261027100004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261027100004)

</details>

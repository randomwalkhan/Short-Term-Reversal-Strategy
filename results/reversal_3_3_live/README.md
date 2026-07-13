# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-13 15:30:06 EDT`
Last processed slot: `manage_1530`

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

- Cash: `$17,620.25`
- Equity: `$27,240.25`
- Realized PnL: `$16,995.25`
- Unrealized PnL: `$245.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  META     option         option META260821C00660000       2026-07-13                   0      2      9375.0                  9620.0        46.88           48.1      660.72        658.33          bid_ask_mid                       48.1                bid_ask_mid                    True           245.0                   2.61         81.82               22              1.27         53.38           56.28                  55.99                7322.0         1343.0               0.02                      ok
```

## Today's Closed Trades (2026-07-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  UPRO           90.00               10            2.55              2.60        145.04                40.56         0.565          pass              0.339              5.3                           0.194                2.65              0.326                                 ok            True                  False
  CSCO           90.00               10            2.00              1.70        120.58                35.64         0.548          pass              0.442             40.1                           0.269                1.38              0.301                                 ok            True                  False
   LIN          100.00               17            1.07              3.98        528.09                20.88         0.530          pass              0.595             31.6                           0.493                2.55              0.049                                 ok            True                  False
  KLAC           72.73               11            4.40              7.13        228.47               110.61         0.632          pass              0.128             19.4                           0.271              -20.49             -2.609 downtrend_blocked_slope_and_streak           False                  False
   KDP           84.62               13            0.90              0.20         31.58                34.17         0.605          pass              0.241             12.3                           0.281               -6.31             -0.695 downtrend_blocked_slope_and_streak           False                  False
    MU           80.00               15            4.84             33.21        965.07               112.95         0.595          pass              0.207             38.1                           0.497              -18.62             -1.885            downtrend_blocked_slope           False                  False
  META           77.78               18            1.63              7.63        665.94                55.99         0.583          pass              0.194             27.4                           0.240               17.01              1.700                                 ok           False                  False
   WDC           92.31               13            5.85             23.84        572.37               121.29         0.578          pass              0.503             32.5                           0.485              -15.85             -1.369            downtrend_blocked_slope           False                  False
   ADI           76.92               13            2.70              7.49        392.44                55.18         0.570          pass              0.124             15.7                           0.248               -1.74             -0.051                                 ok           False                  False
  AMAT           80.00               10            4.77             20.12        593.88                98.14         0.561          pass              0.105             16.3                           0.202              -17.40             -1.960 downtrend_blocked_slope_and_streak           False                  False
  ROST           78.57               14            1.42              2.22        221.93                30.69         0.560          pass              0.088              1.9                           0.214                5.21              0.646                                 ok           False                  False
   TXN           80.00                5            4.15              9.04        307.58                64.14         0.548          pass              0.090             11.7                           0.242                4.57              0.459                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-07-13T15:10:07.483451-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-07-13T15:05:06.913203-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-07-13T15:00:09.058779-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-07-13T14:55:09.246495-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-07-13T14:50:06.804809-04:00       entry_1500              entry {"allocated_cash": 9375.0, "asset_type": "option", "contract_symbol": "META260821C00660000", "contracts": 2, "early_entry_score": 0.317, "entry_mode": "regular", "entry_option_price": 46.875, "execution_mode": "option", "matched_signals": 22, "option_liquidity_status": "ok", "option_open_interest": 7322.0, "option_spread_pct": 2.03, "option_volume": 1343.0, "success_rate": 81.82, "ticker": "META", "timing_score": 0.583}
2026-07-13T14:50:06.804809-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-13", "training_samples": 5399, "window": 5}
2026-07-13T12:00:04.108537-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T11:55:01.971433-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T11:50:06.106391-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T11:35:02.081051-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260713153006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260713153006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260713153006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260713153006)

</details>

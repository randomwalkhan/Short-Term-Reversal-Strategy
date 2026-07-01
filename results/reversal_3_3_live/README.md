# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-01 13:35:01 EDT`
Last processed slot: `manage_1330`

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

- Cash: `$14,720.50`
- Equity: `$29,120.50`
- Realized PnL: `$19,360.50`
- Unrealized PnL: `$-240.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  GILD     option         option GILD260821C00130000       2026-06-29                   2     32     14640.0                 14400.0         4.58            4.5      126.19        126.31          bid_ask_mid                        4.5                bid_ask_mid                    True          -240.0                  -1.64         93.33               15              1.32         33.41           32.81                  29.34                 807.0           40.0               0.08                      ok
```

## Today's Closed Trades (2026-07-01)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   XEL          100.00               11            0.97              0.55         80.07                19.51         0.611          pass              0.529             20.4                           0.319                0.68              0.412                                 ok            True                  False
   EXC           84.62               13            0.90              0.29         46.49                18.60         0.589          pass              0.239             12.5                           0.274               -0.84              0.183                                 ok            True                  False
  AMGN           95.65               23            0.91              2.31        361.13                26.93         0.546          pass              0.607             22.0                           0.206                3.16              0.618                                 ok            True                  False
  AVGO           76.47               17            2.28              6.02        375.17                74.76         0.665          pass              0.148             11.6                           0.333               -1.85             -0.622            downtrend_blocked_slope           False                  False
  QCOM           86.21               29            0.70              0.90        184.40                83.64         0.650          pass              0.567             69.9                           0.465              -14.28             -1.994 downtrend_blocked_slope_and_streak           False                  False
  MCHP           90.91               22            1.91              1.22         90.68                74.43         0.636          pass              0.505             23.5                           0.190               -6.46             -1.001            downtrend_blocked_slope           False                  False
  NXPI           90.91               33            0.23              0.45        280.84                65.46         0.634          pass              0.790             94.3                           0.572               -7.11             -1.127            downtrend_blocked_slope           False                  False
  MPWR           80.95               21            2.73             26.46       1371.02                91.02         0.628          pass              0.245             27.8                           0.223              -10.29             -1.418            downtrend_blocked_slope           False                  False
   ADI           89.29               28            1.06              2.95        395.91                64.06         0.613          pass              0.596             55.8                           0.390               -5.54             -0.929            downtrend_blocked_slope           False                  False
   AEP           75.00               16            0.86              0.82        136.46                19.16         0.548          pass              0.133             12.7                           0.221                4.54              0.783                                 ok           False                  False
  CSCO           96.67               30            1.04              0.85        117.09                44.21         0.527          pass              0.738             50.6                           0.426               -2.78             -0.303 downtrend_blocked_slope_and_streak           False                  False
   HON           77.27               22            0.85              1.34        223.33                42.01         0.521          pass              0.247             38.4                           0.252               -3.27             -0.173                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                 detail
2026-07-01T11:59:52.238657-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-01T11:35:05.893258-04:00 early_entry_1135      early_entry_shadow                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-01T10:59:26.258383-04:00 early_entry_1055      early_entry_shadow                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-01T10:00:05.880743-04:00 early_entry_1000      early_entry_shadow                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-30T17:05:09.028498-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                          {'saved': 93}
2026-06-29T15:10:05.899695-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-06-29T15:05:05.773719-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-06-29T15:00:06.338367-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-06-29T14:55:08.793154-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-06-29T14:50:09.505108-04:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.248, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 22.22, "option_volume": 0.0, "reason": "no_trade_low_option_liquidity", "ticker": "EXC", "timing_score": 0.577}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260701133501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260701133501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260701133501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260701133501)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-01 14:45:07 EDT`
Last processed slot: `manual`

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
- Equity: `$28,080.50`
- Realized PnL: `$19,360.50`
- Unrealized PnL: `$-1,280.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  GILD     option         option GILD260821C00130000       2026-06-29                   2     32     14640.0                 13360.0         4.58           4.18      126.19        125.96          bid_ask_mid                       4.18                bid_ask_mid                    True         -1280.0                  -8.74         93.33               15              1.32         33.41           31.75                  29.34                 807.0           40.0               0.08                      ok
```

## Today's Closed Trades (2026-07-01)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   EXC           84.62               13            0.99              0.32         46.48                18.60         0.581          pass              0.250             16.4                           0.296               -0.92              0.180                                 ok            True                  False
   XEL          100.00               18            0.76              0.43         80.12                19.51         0.575          pass              0.624             37.8                           0.511                0.90              0.421                                 ok            True                  False
   AEP           81.82               11            1.26              1.20        136.29                19.16         0.558          pass              0.174             21.1                           0.332                4.12              0.764                                 ok            True                  False
  AVGO           78.95               19            2.05              5.42        375.43                74.76         0.669          pass              0.188             20.4                           0.391               -1.62             -0.611            downtrend_blocked_slope           False                  False
  NXPI           90.91               33            0.19              0.38        280.87                65.46         0.637          pass              0.793             95.2                           0.672               -7.08             -1.125            downtrend_blocked_slope           False                  False
  QCOM           85.19               27            0.91              1.18        184.28                83.64         0.632          pass              0.497             60.6                           0.312              -14.47             -2.004 downtrend_blocked_slope_and_streak           False                  False
  MCHP           90.91               22            1.98              1.27         90.66                74.43         0.631          pass              0.496             20.6                           0.245               -6.53             -1.005            downtrend_blocked_slope           False                  False
  MPWR           80.00               20            2.90             28.02       1370.35                91.02         0.622          pass              0.200             23.5                           0.239              -10.44             -1.425            downtrend_blocked_slope           False                  False
   ADI           88.00               25            1.27              3.52        395.66                64.06         0.619          pass              0.517             47.2                           0.414               -5.74             -0.938            downtrend_blocked_slope           False                  False
  CSCO           96.67               30            0.97              0.80        117.12                44.21         0.532          pass              0.748             53.8                           0.536               -2.72             -0.300 downtrend_blocked_slope_and_streak           False                  False
   HON           77.27               22            0.83              1.30        223.34                42.01         0.522          pass              0.263             43.6                           0.543               -3.25             -0.172                                 ok           False                  False
  GILD           90.32               31            0.35              0.31        126.21                28.09         0.508          pass              0.607             47.0                           0.333               -1.05              0.068                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260701144507)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260701144507)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260701144507)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260701144507)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-01 12:43:02 EDT`
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
- Equity: `$28,560.50`
- Realized PnL: `$19,360.50`
- Unrealized PnL: `$-800.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  GILD     option         option GILD260821C00130000       2026-06-29                   2     32     14640.0                 13840.0         4.58           4.32      126.19        126.47          bid_ask_mid                       4.32                bid_ask_mid                    True          -800.0                  -5.46         93.33               15              1.32         33.41           31.79                  29.34                 807.0           40.0               0.08                      ok
```

## Today's Closed Trades (2026-07-01)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   XEL          100.00               13            0.87              0.49         80.09                19.51         0.603          pass              0.562             27.1                           0.276                0.79              0.416                                 ok            True                  False
  MRVL          100.00               10            6.51             13.57        292.07               157.45         0.525          pass              0.503             16.9                           0.419               -0.06             -0.457                                 ok            True                  False
  AVGO           71.43               14            2.52              6.66        374.89                74.76         0.664          pass              0.099              2.1                           0.170               -2.10             -0.633            downtrend_blocked_slope           False                  False
  MCHP           92.86               28            1.00              0.64         90.93                74.43         0.659          pass              0.709             60.1                           0.407               -5.58             -0.959            downtrend_blocked_slope           False                  False
  MPWR           83.33               24            2.19             21.16       1373.29                91.02         0.647          pass              0.374             42.3                           0.419               -9.78             -1.392            downtrend_blocked_slope           False                  False
   ADI           90.00               30            0.63              1.74        396.42                64.06         0.630          pass              0.685             73.8                           0.645               -5.13             -0.909            downtrend_blocked_slope           False                  False
   EXC           78.57               14            0.72              0.23         46.52                18.60         0.589          pass              0.143             19.3                           0.233               -0.65              0.192                                 ok           False                  False
  CSCO           96.88               32            0.81              0.66        117.18                44.21         0.529          pass              0.784             61.5                           0.608               -2.56             -0.293 downtrend_blocked_slope_and_streak           False                  False
  NVDA           72.73               22            1.50              2.11        199.19                42.39         0.525          pass              0.296             54.7                           0.651               -4.98             -0.692 downtrend_blocked_slope_and_streak           False                  False
   AEP           78.26               23            0.54              0.52        136.59                19.16         0.521          pass              0.264             41.7                           0.445                4.87              0.797                                 ok           False                  False
  ROST           93.94               33            0.40              0.60        212.59                34.96         0.519          pass              0.782             68.2                           0.651               -9.60             -1.336 downtrend_blocked_slope_and_streak           False                  False
   WDC          100.00                8            6.43             28.76        626.39               116.88         0.514          pass              0.518             22.4                           0.257              -12.25             -1.757            downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260701124302)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260701124302)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260701124302)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260701124302)

</details>

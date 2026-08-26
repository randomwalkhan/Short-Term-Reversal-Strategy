# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-26 10:15:01 EDT`
Last processed slot: `early_entry_1015`

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

- Cash: `$27,460.60`
- Equity: `$54,888.10`
- Realized PnL: `$44,775.60`
- Unrealized PnL: `$112.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX261016C00310000       2026-08-24                   2      9     27315.0                 27427.5        30.35          30.48      310.66        311.22          bid_ask_mid                      30.48                bid_ask_mid                    True           112.5                   0.41          87.5               32              1.06         63.04           63.61                   88.6                 214.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-26)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   KHC     option         option KHC261016C00025000    287          2026-08-25         2026-08-26         1.02       0.918 -2927.4       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  ABNB           93.94               33            0.68              0.90        190.11                61.60         0.649          pass              0.677             28.9                           0.250                5.06              0.506                      ok            True                  False
  SHOP           91.43               35            1.17              1.26        153.34                72.08         0.622          pass              0.670             45.6                           0.389                1.11             -0.128                      ok            True                  False
  REGN          100.00               24            0.94              5.47        831.22                29.20         0.556          pass              0.668             39.6                           0.362                3.60              0.457                      ok            True                  False
   KHC           88.00               25            0.81              0.14         25.26                34.81         0.537          pass              0.610             80.8                           0.693                2.38              0.203                      ok            True                  False
  MELI           97.30               37            0.66              9.18       1993.06                47.50         0.535          pass              0.688             18.0                           0.177                8.51              1.044                      ok            True                  False
  BKNG           96.00               25            1.50              2.24        212.82                35.36         0.517          pass              0.623             23.7                           0.227               -0.79              0.038                      ok            True                  False
  CPRT           86.84               38            0.59              0.14         33.27                43.23         0.502          pass              0.542             40.9                           0.300               14.30              1.398                      ok            True                  False
  MNST           94.12               34            0.43              0.15         48.67               552.32         1.000          pass              0.820             61.2                           0.705                5.53              0.611                      ok           False                  False
  ALNY           87.80               41            0.33              0.55        239.84               130.65         0.841          pass              0.725             77.6                           0.601                6.85              0.684                      ok           False                  False
  SOXL           80.00               35            1.18              0.95        115.26               150.52         0.780          pass              0.412             55.7                           0.378              -19.59             -3.011 downtrend_blocked_slope           False                  False
  DRAM           77.78               36            0.53              0.21         56.15                90.57         0.701          pass              0.441             65.9                           0.422                2.08             -0.143                      ok           False                  False
  INSM           88.89               45            0.55              0.48        123.68               110.58         0.683          pass              0.766             86.8                           0.626               -6.86             -0.449 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                          detail
2026-08-26T10:15:01.106842-04:00 early_entry_1015 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:10:05.242748-04:00 early_entry_1010 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:05:01.196440-04:00 early_entry_1005 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:00:05.932819-04:00 early_entry_1000 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T09:50:01.107222-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "KHC261016C00025000", "fill_price": 0.918, "pnl": -2927.4, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "KHC"}
2026-08-26T00:00:04.646772-04:00     data_refresh       data_refresh                                                                                                                                                                   {'saved': 93}
2026-08-25T15:10:01.918364-04:00       entry_1500       slot_skipped                                                                                                                                                 {"reason": "already_processed"}
2026-08-25T15:05:01.097664-04:00       entry_1500       slot_skipped                                                                                                                                                 {"reason": "already_processed"}
2026-08-25T15:00:03.828348-04:00       entry_1500       slot_skipped                                                                                                                                                 {"reason": "already_processed"}
2026-08-25T14:55:05.864506-04:00       entry_1500       slot_skipped                                                                                                                                                 {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260826101501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260826101501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260826101501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260826101501)

</details>

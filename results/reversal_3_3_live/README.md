# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-17 11:15:01 EDT`
Last processed slot: `early_entry_1115`

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

- Cash: `$13,363.25`
- Equity: `$27,048.25`
- Realized PnL: `$15,985.75`
- Unrealized PnL: `$1,062.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  DRAM     option         option DRAM260717C00069000       2026-06-16                   1     17     12622.5                 13685.0         7.43           8.05       68.52         70.89          bid_ask_mid                       8.05                bid_ask_mid                    True          1062.5                   8.42         90.91               11              3.59         94.78           86.11                 109.99                 846.0          111.0               0.06                      ok
```

## Today's Closed Trades (2026-06-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ           93.33               15            1.11              0.48         61.94                20.23         0.567            pass              0.516             23.3                           0.320                0.64              0.219                                 ok            True                  False
  CTAS           96.43               28            0.80              0.99        176.28                29.79         0.505            pass              0.749             59.4                           0.569                1.14              0.061                                 ok            True                  False
  FAST           93.10               29            0.71              0.23         45.95                20.87         0.500 below_threshold              0.658             44.0                           0.341                2.22              0.053                                 ok            True                  False
    ZS           75.68               37            0.68              0.61        126.97               152.67         0.877            pass              0.479             70.5                           0.594               -5.96             -0.559 downtrend_blocked_slope_and_streak           False                  False
  INTU           80.00               45            0.09              0.17        280.92                99.11         0.712            pass              0.561             96.7                           0.693              -12.85             -1.442 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00                3            1.16              0.19         23.72                25.54         0.691            pass              0.480              3.5                           0.099                5.23              0.802                                 ok           False                  False
   PEP          100.00                4            1.43              1.46        145.49                20.43         0.638            pass              0.519             18.6                           0.277                2.50              0.380                                 ok           False                  False
   CSX          100.00                4            1.58              0.52         46.68                20.12         0.629            pass              0.475              3.9                           0.194                0.04              0.175                                 ok           False                  False
  MCHP           94.59               37            0.04              0.03         95.62                60.62         0.617            pass              0.916             95.1                           0.625               -1.41              0.150                                 ok           False                  False
   XEL          100.00               25            0.16              0.09         78.94                23.22         0.595            pass              0.796             78.7                           0.424                2.02              0.277                                 ok           False                  False
   WMT           73.33               15            1.39              1.18        120.53                34.81         0.589            pass              0.112              6.7                           0.194                5.56              0.478                                 ok           False                  False
  PAYX          100.00               26            0.27              0.19        100.20                31.37         0.587            pass              0.820             84.8                           0.624               -0.77              0.106                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-06-17T11:15:01.940218-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T11:10:02.894138-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T11:05:03.233466-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T11:00:05.904410-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T10:55:04.940733-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T10:50:01.959639-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T10:45:01.979292-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T10:40:01.956283-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T10:35:06.928976-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T10:30:05.890992-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260617111501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260617111501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260617111501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260617111501)

</details>

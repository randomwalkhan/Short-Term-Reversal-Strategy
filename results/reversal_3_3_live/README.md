# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-16 11:05:05 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$65,704.80`
- Equity: `$128,899.80`
- Realized PnL: `$118,734.80`
- Unrealized PnL: `$165.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG261120C00270000       2026-10-15                   1     33     63030.0                 63195.0         19.1          19.15       273.7         273.4          bid_ask_mid                      19.15                bid_ask_mid                    True           165.0                   0.26         81.25               16              2.09         51.04           51.06                  59.82                 446.0           21.0               0.05                      ok
```

## Today's Closed Trades (2026-10-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  META           72.73               11            2.06             10.61        732.17                55.08         0.593            pass              0.096              9.9                           0.245               -0.89              0.057                                 ok           False                  False
   CEG           86.49               37            0.49              0.95        274.59                60.14         0.542            pass              0.610             67.5                           0.389                6.27              0.184                                 ok           False                  False
  QCOM           84.00               25            1.58              1.97        177.56                54.84         0.540            pass              0.401             46.7                           0.404               -5.02             -0.423 downtrend_blocked_slope_and_streak           False                  False
  CSCO           86.67               15            1.40              1.08        109.39                35.07         0.539            pass              0.365             33.3                           0.332               -3.47             -0.391 downtrend_blocked_slope_and_streak           False                  False
  SNPS           60.00                5            3.46             11.32        463.26                53.97         0.536            pass              0.054              0.0                           0.238               -7.75             -0.682 downtrend_blocked_slope_and_streak           False                  False
  PAYX           81.40               43            0.05              0.04        110.76                41.26         0.531            pass              0.552             87.2                           0.584               11.91              1.167                                 ok           False                  False
  MPWR           77.78               27            1.28             11.21       1244.40                56.34         0.524            pass              0.351             61.9                           0.610              -14.35             -1.959            downtrend_blocked_slope           False                  False
  DASH           87.18               39            0.80              1.08        192.59                48.67         0.493 below_threshold              0.434              0.0                           0.210                1.25             -0.029                                 ok           False                  False
   APP           84.38               32            1.69              3.31        277.87                54.48         0.490 below_threshold              0.312              0.0                           0.055                2.36             -0.186                                 ok           False                  False
  CDNS           85.71               28            1.24              2.81        323.17                38.31         0.489 below_threshold              0.368             15.5                           0.215               -8.82             -1.087 downtrend_blocked_slope_and_streak           False                  False
  SHOP           83.33               36            0.81              1.01        177.71                48.01         0.489 below_threshold              0.364             17.5                           0.225               16.72              1.410                                 ok           False                  False
  MSFT           95.24               21            1.06              4.00        537.72                21.00         0.488 below_threshold              0.522              0.0                           0.239                3.13              0.338                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-16T11:05:05.360304-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:00:06.194646-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:55:05.447906-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:50:06.080905-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:45:05.613636-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:40:05.484912-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:35:02.409902-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:30:04.273613-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:25:03.664701-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:20:06.431756-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261016110505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261016110505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261016110505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261016110505)

</details>

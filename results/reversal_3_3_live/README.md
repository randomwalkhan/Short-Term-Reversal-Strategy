# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-07 10:55:05 EDT`
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

- Cash: `$53,034.30`
- Equity: `$104,321.80`
- Realized PnL: `$95,146.80`
- Unrealized PnL: `$-825.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ABNB     option         option ABNB261120C00160000       2026-10-06                   1     55     52112.5                 51287.5         9.48           9.32      160.14         159.1          bid_ask_mid                       9.32                bid_ask_mid                    True          -825.0                  -1.58         83.33               12               2.4         42.26           43.86                  40.56                 310.0           20.0               0.06                      ok
```

## Today's Closed Trades (2026-10-07)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CSCO           80.00               20            0.98              0.80        117.60                34.67         0.566          pass              0.170             15.4                           0.205               10.16              1.085                                 ok            True                  False
  SNPS           81.25               32            0.86              3.03        503.87                54.22         0.556          pass              0.325             29.7                           0.276               21.25              2.322                                 ok            True                  False
  UPRO           91.67               12            2.00              2.19        155.47                30.90         0.547          pass              0.398              6.4                           0.263                1.98              0.296                                 ok            True                  False
   KDP           95.65               23            0.67              0.15         31.07                26.61         0.530          pass              0.662             40.8                           0.420               -1.94             -0.180                                 ok            True                  False
  MPWR           81.25               16            3.26             33.65       1459.27                53.62         0.524          pass              0.189             21.2                           0.317                5.33              0.942                                 ok            True                  False
  DASH           80.95               21            2.15              2.91        192.37                42.81         0.511          pass              0.175              8.5                           0.267                0.10              0.181                                 ok            True                  False
  SHOP           86.11               36            1.13              1.30        163.88                52.70         0.502          pass              0.505             39.4                           0.324               14.22              1.476                                 ok            True                  False
    ZS           93.62               47            0.05              0.08        212.22                73.32         0.618          pass              0.909             94.5                           0.652               -1.08              0.007                                 ok           False                  False
  META           58.33               12            2.05             10.58        734.35                55.45         0.589          pass              0.125             17.5                           0.383               -2.73             -0.332            downtrend_blocked_slope           False                  False
  QCOM           84.00               25            1.46              1.85        180.24                56.22         0.586          pass              0.374             36.2                           0.303               -9.56             -1.051 downtrend_blocked_slope_and_streak           False                  False
   STX           86.84               38            0.20              1.14        805.14                69.91         0.576          pass              0.707             93.4                           0.838              -12.90             -1.262            downtrend_blocked_slope           False                  False
   CEG           80.00                5            3.20              6.73        297.52                58.89         0.571          pass              0.151             31.3                           0.226               10.20              0.948                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-07T10:55:05.731047-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:50:04.594870-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:45:05.752801-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:40:04.683000-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:35:06.455720-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:30:05.764832-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:25:05.803343-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:20:04.740401-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:15:04.665736-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:10:02.695128-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261007105505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261007105505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261007105505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261007105505)

</details>

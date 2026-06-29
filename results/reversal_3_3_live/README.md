# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-29 14:25:06 EDT`
Last processed slot: `manage_1430`

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

- Cash: `$29,360.50`
- Equity: `$29,360.50`
- Realized PnL: `$19,360.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  DRAM           92.00               25            0.97              0.49         71.67               125.47         0.824          pass              0.764             87.1                           0.830                9.49              0.690                                 ok            True                  False
    MU           90.91               33            0.63              4.96       1130.21               130.58         0.758          pass              0.800             93.5                           0.881               14.63              1.179                                 ok            True                   True
   EXC           84.62               13            0.95              0.31         47.27                19.58         0.577          pass              0.251             16.7                           0.235                1.60              0.245                                 ok            True                  False
   KDP          100.00               18            0.67              0.16         33.33                25.91         0.561          pass              0.528              6.2                           0.182                5.37              0.522                                 ok            True                  False
  GILD           93.33               15            1.38              1.24        127.35                29.34         0.559          pass              0.523             26.1                           0.454                1.08              0.083                                 ok            True                  False
  PAYX          100.00               22            0.89              0.62         99.63                33.42         0.539          pass              0.658             41.4                           0.325               -1.60             -0.235                                 ok            True                  False
  PCAR           82.61               23            1.09              0.92        120.29                36.52         0.532          pass              0.339             43.0                           0.565                0.72              0.025                                 ok            True                  False
   HON           66.67                3            3.59              6.11        240.79               250.29         0.998          pass              0.203             34.4                           0.265                6.52              6.019                                 ok           False                  False
   XEL          100.00               21            0.43              0.25         82.12                23.26         0.590          pass              0.687             51.4                           0.520                4.13              0.533                                 ok           False                  False
  ROST           87.50                8            1.95              2.91        212.01                36.17         0.568          pass              0.271              4.8                           0.082              -12.92             -1.296 downtrend_blocked_slope_and_streak           False                  False
  CTAS           62.50                8            1.86              2.23        170.94                30.93         0.562          pass              0.071              5.1                           0.235               -4.29             -0.377            downtrend_blocked_slope           False                  False
   LIN           80.00                5            1.74              6.33        516.91                18.17         0.550          pass              0.144             29.6                           0.429               -2.48             -0.106           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-06-29T12:00:02.850105-04:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:55:01.636700-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:50:05.501340-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:45:01.788217-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:40:06.618174-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:35:03.964780-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:30:02.880420-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:25:02.270662-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:22:12.890748-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:15:24.828732-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260629142506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260629142506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260629142506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260629142506)

</details>

# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-28 10:25:02 EDT`
Last processed slot: `manage_1030`

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

- Cash: `$52,788.10`
- Equity: `$52,788.10`
- Realized PnL: `$42,788.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-28)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MNST           93.10               29            0.51              0.17         46.63               551.83         1.000          pass              0.609             11.1                           0.122               -0.77              0.159                      ok            True                  False
  AMGN          100.00               18            0.83              2.53        435.90                27.65         0.587          pass              0.591             26.3                           0.337                4.98              0.539                      ok            True                  False
  FAST          100.00               12            1.26              0.45         50.94                21.07         0.557          pass              0.482              4.4                           0.090               -1.04             -0.090                      ok            True                  False
  CSCO           83.87               31            1.11              0.87        111.78                41.41         0.535          pass              0.374             25.7                           0.340               -0.69             -0.023                      ok            True                  False
  REGN          100.00               15            1.36              7.72        804.40                24.94         0.522          pass              0.661             58.6                           0.368               -0.73             -0.020                      ok            True                  False
  NVDA           86.67               30            1.17              1.87        227.18                42.92         0.513          pass              0.493             43.6                           0.327                0.07             -0.151                      ok            True                  False
  GILD           95.24               21            1.51              1.57        148.19                26.47         0.503          pass              0.538              4.7                           0.140                5.96              0.637                      ok            True                  False
  INSM           73.33               15            2.42              2.05        120.51               110.68         0.783          pass              0.204             30.8                           0.422               -4.27             -0.593 downtrend_blocked_slope           False                  False
  DRAM           77.78               36            0.26              0.10         56.79                68.22         0.617          pass              0.513             92.8                           0.725               -1.12             -0.227                      ok           False                  False
  MCHP           89.29               28            1.50              0.79         75.15                63.59         0.612          pass              0.507             26.1                           0.236               -5.51             -0.680 downtrend_blocked_slope           False                  False
  SOXL           78.79               33            3.34              2.88        121.82               111.92         0.594          pass              0.324             37.1                           0.320              -17.94             -2.098 downtrend_blocked_slope           False                  False
   MAR           95.12               41            0.03              0.06        353.84                33.75         0.529          pass              0.896             80.9                           0.400               -0.62             -0.031                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-08-28T10:25:02.074094-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:20:02.098332-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:15:03.828658-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:10:03.076583-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:05:04.075473-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:00:04.882804-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T09:20:06.065187-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-27T12:00:04.808984-04:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-27T11:55:06.264052-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-27T11:50:05.715223-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260828102502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260828102502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260828102502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260828102502)

</details>

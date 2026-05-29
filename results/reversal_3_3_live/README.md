# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-29 10:20:01 EDT`
Last processed slot: `manage_1030`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
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

- Cash: `$32,264.25`
- Equity: `$32,264.25`
- Realized PnL: `$22,264.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  CSCO           92.31               26            0.86              0.71        118.33                52.06         0.631            pass              0.610             37.5                           0.238                1.81              0.206                       ok            True                  False
  MDLZ           91.67               12            1.39              0.61         62.13                12.98         0.510            pass              0.495             40.0                           0.362                0.90              0.180                       ok            True                  False
  INSM           72.22               36            0.96              0.73        108.06               111.11         0.775            pass              0.323             24.1                           0.311               -7.17             -0.373  downtrend_blocked_slope           False                  False
   AEP           69.23               13            0.59              0.53        127.53                25.60         0.600            pass              0.163             27.6                           0.277               -1.24              0.105                       ok           False                  False
 GOOGL           90.91               11            1.80              4.92        388.02                41.30         0.542            pass              0.435             27.9                           0.329               -4.48             -0.334  downtrend_blocked_slope           False                  False
  MSTR           85.37               41            0.62              0.66        151.36                63.23         0.512            pass              0.611             72.3                           0.562              -19.40             -1.848  downtrend_blocked_slope           False                  False
  GOOG           88.24               17            1.61              4.35        384.26                41.01         0.503            pass              0.421             34.8                           0.487               -4.35             -0.341  downtrend_blocked_slope           False                  False
  AMGN           91.18               34            0.27              0.64        336.21                27.03         0.498 below_threshold              0.728             73.4                           0.649                0.56              0.283                       ok           False                  False
   PEP           84.21               19            1.25              1.28        145.74                23.56         0.496 below_threshold              0.317             31.7                           0.314               -2.83             -0.274  downtrend_blocked_slope           False                  False
   CSX           71.43               14            1.43              0.46         45.61                23.65         0.488 below_threshold              0.158             27.6                           0.280               -1.67              0.003 downtrend_blocked_streak           False                  False
  SBUX           95.65               23            0.71              0.50        100.54                16.60         0.474 below_threshold              0.766             77.3                           0.612               -5.43             -0.700  downtrend_blocked_slope           False                  False
   ADI           88.24               34            0.57              1.68        418.29                39.51         0.473 below_threshold              0.617             63.4                           0.374               -2.39             -0.085                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                        detail
2026-05-29T10:20:01.218195-04:00 early_entry_1020           entry_skipped                                                                                                                                                                                                        {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-29T10:20:01.218195-04:00 early_entry_1020 entry_candidate_skipped {"early_entry_score": 0.816, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 51.0, "option_spread_pct": 19.35, "option_volume": 80.0, "reason": "no_trade_low_option_liquidity", "ticker": "SNPS", "timing_score": 0.396}
2026-05-29T10:15:06.109113-04:00 early_entry_1015           entry_skipped                                                                                                                                                                                                        {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-29T10:15:06.109113-04:00 early_entry_1015 entry_candidate_skipped       {"early_entry_score": 0.716, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 225.0, "option_spread_pct": 15.24, "option_volume": 10.0, "reason": "no_trade_low_option_liquidity", "ticker": "ALNY", "timing_score": 0.402}
2026-05-29T10:10:01.230925-04:00 early_entry_1010           entry_skipped                                                                                                                                                                                                                                    {"reason": "no_candidate"}
2026-05-29T10:05:04.226067-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                        {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-29T10:05:04.226067-04:00 early_entry_1005 entry_candidate_skipped        {"early_entry_score": 0.776, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 611.0, "option_spread_pct": 26.98, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "GILD", "timing_score": 0.366}
2026-05-29T10:05:04.226067-04:00 early_entry_1005 entry_candidate_skipped {"early_entry_score": 0.817, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 51.0, "option_spread_pct": 15.95, "option_volume": 80.0, "reason": "no_trade_low_option_liquidity", "ticker": "SNPS", "timing_score": 0.397}
2026-05-29T10:00:05.402847-04:00 early_entry_1000           entry_skipped                                                                                                                                                                                                                                    {"reason": "no_candidate"}
2026-05-29T09:20:06.125686-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                 {'saved': 92}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260529102001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260529102001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260529102001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260529102001)

</details>

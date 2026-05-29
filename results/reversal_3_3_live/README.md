# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-29 10:05:04 EDT`
Last processed slot: `manage_1000`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  AMGN           90.48               21            0.86              2.02        335.62                27.03         0.549            pass              0.449             13.8                           0.218               -0.03              0.256                                 ok            True                  False
  INSM           76.74               43            0.19              0.15        108.31               111.11         0.784            pass              0.523             81.6                           0.687               -6.45             -0.338                                 ok           False                  False
  CSCO           92.86               28            0.46              0.38        118.48                52.06         0.644            pass              0.728             66.9                           0.514                2.22              0.224                                 ok           False                  False
   AEP           71.43               14            0.58              0.52        127.54                25.60         0.598            pass              0.125             12.9                           0.156               -1.23              0.106                                 ok           False                  False
  REGN           88.57               35            0.44              1.92        620.70                44.05         0.549            pass              0.623             57.8                           0.337              -13.07             -1.059 downtrend_blocked_slope_and_streak           False                  False
   PEP           90.91               11            1.56              1.60        145.61                23.56         0.540            pass              0.396             14.9                           0.206               -3.13             -0.289            downtrend_blocked_slope           False                  False
   TXN          100.00               31            0.44              0.97        315.53                35.59         0.521            pass              0.678             28.7                           0.208                2.07              0.541                                 ok           False                  False
  SBUX           90.91               11            1.23              0.87        100.38                16.60         0.518            pass              0.531             60.6                           0.318               -5.93             -0.724            downtrend_blocked_slope           False                  False
  MDLZ           85.71                7            1.92              0.84         62.03                12.98         0.505            pass              0.255             17.2                           0.123                0.36              0.156                                 ok           False                  False
 GOOGL           90.00               20            1.43              3.91        388.46                41.30         0.502            pass              0.512             42.8                           0.629               -4.12             -0.317            downtrend_blocked_slope           False                  False
  GOOG           90.48               21            1.29              3.50        384.62                41.01         0.498 below_threshold              0.545             47.5                           0.662               -4.04             -0.326            downtrend_blocked_slope           False                  False
   CSX           62.50                8            1.79              0.57         45.56                23.65         0.497 below_threshold              0.057              2.4                           0.114               -2.03             -0.014           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                        detail
2026-05-29T10:05:04.226067-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                        {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-29T10:05:04.226067-04:00 early_entry_1005 entry_candidate_skipped        {"early_entry_score": 0.776, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 611.0, "option_spread_pct": 26.98, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "GILD", "timing_score": 0.366}
2026-05-29T10:05:04.226067-04:00 early_entry_1005 entry_candidate_skipped {"early_entry_score": 0.817, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 51.0, "option_spread_pct": 15.95, "option_volume": 80.0, "reason": "no_trade_low_option_liquidity", "ticker": "SNPS", "timing_score": 0.397}
2026-05-29T10:00:05.402847-04:00 early_entry_1000           entry_skipped                                                                                                                                                                                                                                    {"reason": "no_candidate"}
2026-05-29T09:20:06.125686-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                 {'saved': 92}
2026-05-28T15:10:10.028312-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-05-28T15:05:04.986129-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-05-28T15:00:06.948836-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-05-28T14:55:06.010831-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-05-28T14:50:05.035990-04:00       entry_1500           entry_skipped                                                                                                                                                                                                                               {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260529100504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260529100504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260529100504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260529100504)

</details>

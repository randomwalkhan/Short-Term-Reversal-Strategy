# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-21 10:55:01 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$28,317.75`
- Equity: `$28,317.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-21)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  SOXL           81.48               27            1.04              1.26        172.66               145.82         0.781          pass              0.434             67.8                           0.434               12.69             -0.489                      ok            True                  False
  INTC           94.74               19            3.37              2.81        117.76               113.85         0.674          pass              0.613             30.7                           0.479                4.86             -0.675                      ok            True                  False
  FTNT          100.00               32            1.09              0.99        129.57                70.74         0.631          pass              0.756             48.6                           0.547               19.09              1.773                      ok            True                  False
  MNST           80.00               25            1.10              0.67         86.59                49.77         0.558          pass              0.391             78.5                           0.414               13.10              0.650                      ok            True                  False
  AMAT           81.82               33            0.83              2.47        425.79                55.19         0.548          pass              0.391             44.7                           0.282                3.09             -0.246                      ok            True                  False
  NVDA           85.00               20            1.85              2.89        222.23                44.60         0.518          pass              0.328             25.5                           0.331                3.71              0.328                      ok            True                  False
  ISRG           84.62               13            2.31              7.26        445.92                35.82         0.508          pass              0.267             24.3                           0.328               -3.27             -0.013                      ok            True                  False
    ZS           85.71               28            1.57              1.92        173.63                63.59         0.507          pass              0.470             48.8                           0.625               12.38              1.847                      ok            True                  False
  AVGO           91.89               37            0.55              1.60        417.07                40.33         0.502          pass              0.701             51.3                           0.284                0.71             -0.162                      ok            True                  False
  CHTR           88.37               43            0.34              0.34        144.46               113.96         0.763          pass              0.746             82.2                           0.648              -10.06             -0.932 downtrend_blocked_slope           False                  False
  INSM           78.57               42            0.22              0.16        107.84               110.82         0.753          pass              0.523             82.6                           0.677                2.55              0.218                      ok           False                  False
  NXPI           75.00               20            2.14              4.65        308.16                91.65         0.698          pass              0.166              9.7                           0.131                4.58              0.245                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                  detail
2026-05-21T10:55:01.033633-04:00 early_entry_1055           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:55:01.033633-04:00 early_entry_1055 entry_candidate_skipped                               {"early_entry_score": 0.684, "option_liquidity_status": "low_volume", "option_open_interest": 225.0, "option_spread_pct": 7.41, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ALNY", "timing_score": 0.396}
2026-05-21T10:55:01.033633-04:00 early_entry_1055 entry_candidate_skipped {"early_entry_score": 0.764, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 81.0, "option_spread_pct": 24.56, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "FAST", "timing_score": 0.481}
2026-05-21T10:50:06.054603-04:00 early_entry_1050           entry_skipped                                                                                                                                                                                                                                              {"reason": "no_candidate"}
2026-05-21T10:45:05.191060-04:00 early_entry_1045           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:45:05.191060-04:00 early_entry_1045 entry_candidate_skipped               {"early_entry_score": 0.778, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 29.0, "option_spread_pct": 9.05, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ADP", "timing_score": 0.528}
2026-05-21T10:40:05.208680-04:00 early_entry_1040           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:40:05.208680-04:00 early_entry_1040 entry_candidate_skipped                {"early_entry_score": 0.75, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 29.0, "option_spread_pct": 9.42, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ADP", "timing_score": 0.528}
2026-05-21T10:35:05.061516-04:00 early_entry_1035           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:35:05.061516-04:00 early_entry_1035 entry_candidate_skipped                   {"early_entry_score": 0.694, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 493.0, "option_spread_pct": 19.05, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "MAR", "timing_score": 0.414}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260521105501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260521105501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260521105501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260521105501)

</details>

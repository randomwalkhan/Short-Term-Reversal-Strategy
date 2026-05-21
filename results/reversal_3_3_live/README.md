# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-21 10:45:05 EDT`
Last processed slot: `early_entry_1045`

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
  INTC           94.74               19            3.09              2.58        117.86               113.85         0.689          pass              0.631             36.4                           0.547                5.16             -0.662                      ok            True                  False
  FTNT          100.00               24            1.44              1.31        129.44                70.74         0.661          pass              0.656             32.3                           0.227               18.67              1.757                      ok            True                  False
  MNST           80.77               26            1.06              0.65         86.60                49.77         0.555          pass              0.420             79.3                           0.418               13.14              0.652                      ok            True                  False
  AMAT           83.33               36            0.58              1.74        426.10                55.19         0.545          pass              0.500             61.1                           0.401                3.34             -0.234                      ok            True                  False
   ADP           93.94               33            0.62              0.95        220.28                38.26         0.528          pass              0.778             66.6                           0.556                2.45              0.451                      ok            True                   True
  NVDA           85.00               20            1.75              2.74        222.30                44.60         0.524          pass              0.341             29.4                           0.314                3.81              0.332                      ok            True                  False
   TXN           91.67               12            2.15              4.59        302.91                69.08         0.514          pass              0.393              5.7                           0.169                4.59              0.477                      ok            True                  False
  ISRG           83.33               12            2.43              7.65        445.75                35.82         0.505          pass              0.213             20.2                           0.281               -3.39             -0.019                      ok            True                  False
  SOXL           84.38               32            0.02              0.02        173.19               145.82         0.807          pass              0.642             99.5                           0.673               13.85             -0.443                      ok           False                  False
  CHTR           90.00               40            0.55              0.56        144.37               113.96         0.769          pass              0.756             70.9                           0.608              -10.25             -0.942 downtrend_blocked_slope           False                  False
  INSM           78.05               41            0.61              0.46        107.71               110.82         0.737          pass              0.427             51.1                           0.441                2.14              0.200                      ok           False                  False
  NXPI           75.00               24            1.34              2.90        308.90                91.65         0.719          pass              0.296             43.6                           0.288                5.44              0.282                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                    detail
2026-05-21T10:45:05.191060-04:00 early_entry_1045           entry_skipped                                                                                                                                                                                                    {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:45:05.191060-04:00 early_entry_1045 entry_candidate_skipped {"early_entry_score": 0.778, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 29.0, "option_spread_pct": 9.05, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ADP", "timing_score": 0.528}
2026-05-21T10:40:05.208680-04:00 early_entry_1040           entry_skipped                                                                                                                                                                                                    {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:40:05.208680-04:00 early_entry_1040 entry_candidate_skipped  {"early_entry_score": 0.75, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 29.0, "option_spread_pct": 9.42, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ADP", "timing_score": 0.528}
2026-05-21T10:35:05.061516-04:00 early_entry_1035           entry_skipped                                                                                                                                                                                                    {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:35:05.061516-04:00 early_entry_1035 entry_candidate_skipped     {"early_entry_score": 0.694, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 493.0, "option_spread_pct": 19.05, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "MAR", "timing_score": 0.414}
2026-05-21T10:35:05.061516-04:00 early_entry_1035 entry_candidate_skipped {"early_entry_score": 0.784, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 29.0, "option_spread_pct": 13.9, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ADP", "timing_score": 0.531}
2026-05-21T10:30:05.185385-04:00 early_entry_1030           entry_skipped                                                                                                                                                                                                    {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:30:05.185385-04:00 early_entry_1030 entry_candidate_skipped     {"early_entry_score": 0.694, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 493.0, "option_spread_pct": 19.05, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "MAR", "timing_score": 0.407}
2026-05-21T10:25:06.196092-04:00 early_entry_1025 entry_candidate_skipped     {"early_entry_score": 0.689, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 493.0, "option_spread_pct": 20.94, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "MAR", "timing_score": 0.405}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260521104505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260521104505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260521104505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260521104505)

</details>

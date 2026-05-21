# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-21 11:25:04 EDT`
Last processed slot: `manage_1130`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  SOXL           81.48               27            1.32              1.60        172.52               145.82         0.769          pass              0.407             59.2                           0.410               12.37             -0.502                  ok            True                  False
  INTC           95.65               23            2.11              1.75        118.21               113.85         0.721          pass              0.729             56.7                           0.803                6.24             -0.616                  ok            True                  False
  QCOM           90.91               33            0.86              1.23        201.98               100.64         0.688          pass              0.706             64.4                           0.351               -0.88             -0.966                  ok            True                  False
  NXPI           81.82               11            3.41              7.40        306.98                91.65         0.678          pass              0.140              5.6                           0.133                3.23              0.186                  ok            True                  False
  FTNT          100.00               28            1.27              1.15        129.51                70.74         0.646          pass              0.705             40.3                           0.331               18.88              1.765                  ok            True                  False
  MNST           81.48               27            0.89              0.54         86.65                49.77         0.561          pass              0.457             82.7                           0.634               13.35              0.660                  ok            True                  False
  PAYX           94.74               19            0.66              0.44         94.73                29.35         0.556          pass              0.721             70.8                           0.542                1.32              0.251                  ok            True                  False
  AMAT           83.33               36            0.60              1.79        426.08                55.19         0.544          pass              0.497             60.0                           0.446                3.33             -0.235                  ok            True                  False
   ADP           94.12               34            0.53              0.81        220.34                38.26         0.527          pass              0.804             71.5                           0.656                2.54              0.455                  ok            True                   True
  NVDA           81.25               16            2.10              3.28        222.06                44.60         0.524          pass              0.172             15.3                           0.300                3.44              0.316                  ok            True                  False
  ISRG           90.91               11            2.49              7.83        445.68                35.82         0.520          pass              0.405             18.4                           0.333               -3.45             -0.022                  ok            True                  False
    ZS           82.35               17            2.63              3.21        173.08                63.59         0.511          pass              0.204             14.5                           0.167               11.18              1.799                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                  detail
2026-05-21T11:25:04.201711-04:00 early_entry_1125           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T11:25:04.201711-04:00 early_entry_1125 entry_candidate_skipped               {"early_entry_score": 0.804, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 29.0, "option_spread_pct": 6.12, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ADP", "timing_score": 0.527}
2026-05-21T11:20:02.110689-04:00 early_entry_1120           entry_skipped                                                                                                                                                                                                                                              {"reason": "no_candidate"}
2026-05-21T11:15:01.031462-04:00 early_entry_1115           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T11:15:01.031462-04:00 early_entry_1115 entry_candidate_skipped                               {"early_entry_score": 0.713, "option_liquidity_status": "low_volume", "option_open_interest": 225.0, "option_spread_pct": 6.82, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ALNY", "timing_score": 0.393}
2026-05-21T11:10:05.158469-04:00 early_entry_1110           entry_skipped                                                                                                                                                                                                                                              {"reason": "no_candidate"}
2026-05-21T11:05:03.180136-04:00 early_entry_1105           entry_skipped                                                                                                                                                                                                                                              {"reason": "no_candidate"}
2026-05-21T11:00:05.229849-04:00 early_entry_1100           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T11:00:05.229849-04:00 early_entry_1100 entry_candidate_skipped                               {"early_entry_score": 0.714, "option_liquidity_status": "low_volume", "option_open_interest": 225.0, "option_spread_pct": 5.21, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ALNY", "timing_score": 0.393}
2026-05-21T10:55:01.033633-04:00 early_entry_1055 entry_candidate_skipped {"early_entry_score": 0.764, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 81.0, "option_spread_pct": 24.56, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "FAST", "timing_score": 0.481}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260521112504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260521112504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260521112504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260521112504)

</details>

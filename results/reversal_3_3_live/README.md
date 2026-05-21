# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-21 11:15:01 EDT`
Last processed slot: `early_entry_1115`

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
  SOXL           81.48               27            1.17              1.42        172.59               145.82         0.775          pass              0.421             63.7                           0.313               12.54             -0.495                      ok            True                  False
  INTC           95.24               21            2.35              1.96        118.12               113.85         0.718          pass              0.700             51.6                           0.732                5.97             -0.628                      ok            True                  False
  QCOM           91.18               34            0.79              1.11        202.03               100.64         0.686          pass              0.730             67.6                           0.371               -0.80             -0.962                      ok            True                  False
  FTNT          100.00               28            1.28              1.16        129.50                70.74         0.646          pass              0.704             39.9                           0.418               18.87              1.765                      ok            True                  False
  PAYX           94.74               19            0.53              0.35         94.77                29.35         0.564          pass              0.740             76.9                           0.640                1.46              0.257                      ok            True                  False
  MNST           80.00               25            1.13              0.69         86.59                49.77         0.557          pass              0.390             78.0                           0.450               13.07              0.649                      ok            True                  False
  AMAT           82.86               35            0.72              2.16        425.92                55.19         0.542          pass              0.452             51.6                           0.332                3.20             -0.241                      ok            True                  False
    ZS           84.21               19            2.27              2.78        173.26                63.59         0.522          pass              0.302             26.0                           0.300               11.58              1.815                      ok            True                  False
  NVDA           84.21               19            1.87              2.93        222.21                44.60         0.522          pass              0.298             24.4                           0.340                3.68              0.326                      ok            True                  False
  ISRG           84.62               13            2.35              7.39        445.86                35.82         0.506          pass              0.262             22.9                           0.395               -3.31             -0.015                      ok            True                  False
  CHTR           90.00               40            0.65              0.66        144.33               113.96         0.764          pass              0.741             65.8                           0.418              -10.34             -0.947 downtrend_blocked_slope           False                  False
  NXPI           73.33               15            3.02              6.55        307.34                91.65         0.667          pass              0.130             10.0                           0.144                3.64              0.204                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                  detail
2026-05-21T11:15:01.031462-04:00 early_entry_1115           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T11:15:01.031462-04:00 early_entry_1115 entry_candidate_skipped                               {"early_entry_score": 0.713, "option_liquidity_status": "low_volume", "option_open_interest": 225.0, "option_spread_pct": 6.82, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ALNY", "timing_score": 0.393}
2026-05-21T11:10:05.158469-04:00 early_entry_1110           entry_skipped                                                                                                                                                                                                                                              {"reason": "no_candidate"}
2026-05-21T11:05:03.180136-04:00 early_entry_1105           entry_skipped                                                                                                                                                                                                                                              {"reason": "no_candidate"}
2026-05-21T11:00:05.229849-04:00 early_entry_1100           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T11:00:05.229849-04:00 early_entry_1100 entry_candidate_skipped                               {"early_entry_score": 0.714, "option_liquidity_status": "low_volume", "option_open_interest": 225.0, "option_spread_pct": 5.21, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ALNY", "timing_score": 0.393}
2026-05-21T10:55:01.033633-04:00 early_entry_1055           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:55:01.033633-04:00 early_entry_1055 entry_candidate_skipped                               {"early_entry_score": 0.684, "option_liquidity_status": "low_volume", "option_open_interest": 225.0, "option_spread_pct": 7.41, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ALNY", "timing_score": 0.396}
2026-05-21T10:55:01.033633-04:00 early_entry_1055 entry_candidate_skipped {"early_entry_score": 0.764, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 81.0, "option_spread_pct": 24.56, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "FAST", "timing_score": 0.481}
2026-05-21T10:50:06.054603-04:00 early_entry_1050           entry_skipped                                                                                                                                                                                                                                              {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260521111501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260521111501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260521111501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260521111501)

</details>

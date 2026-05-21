# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-21 11:10:05 EDT`
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
  SOXL           80.00               25            2.23              2.71        172.04               145.82         0.731          pass              0.265             30.8                           0.200               11.33             -0.545                      ok            True                  False
  INTC           94.74               19            3.07              2.56        117.86               113.85         0.691          pass              0.633             37.0                           0.505                5.19             -0.661                      ok            True                  False
  FTNT          100.00               28            1.27              1.15        129.51                70.74         0.646          pass              0.705             40.3                           0.480               18.88              1.765                      ok            True                  False
  MNST           82.61               23            1.19              0.72         86.57                49.77         0.570          pass              0.444             76.9                           0.418               13.01              0.646                      ok            True                  False
    ZS           85.00               20            2.25              2.75        173.27                63.59         0.518          pass              0.332             26.6                           0.376               11.60              1.816                      ok            True                  False
  ISRG           90.91               11            2.55              8.01        445.60                35.82         0.516          pass              0.398             16.4                           0.301               -3.51             -0.025                      ok            True                  False
  AVGO           92.00               25            1.51              4.41        415.87                40.33         0.515          pass              0.502             10.1                           0.140               -0.27             -0.206                      ok            True                  False
  CHTR           90.00               40            0.58              0.59        144.36               113.96         0.768          pass              0.752             69.5                           0.451              -10.28             -0.943 downtrend_blocked_slope           False                  False
  QCOM           85.71               21            1.76              2.50        201.44               100.64         0.707          pass              0.296              0.0                           0.210               -1.78             -1.007 downtrend_blocked_slope           False                  False
  NXPI           78.57               14            3.14              6.83        307.22                91.65         0.673          pass              0.113              6.2                           0.159                3.51              0.198                      ok           False                  False
 CMCSA           86.67               30            0.48              0.08         24.84                59.59         0.622          pass              0.561             62.5                           0.542               -5.64             -0.369 downtrend_blocked_slope           False                  False
  SBUX          100.00                7            1.88              1.40        105.90                31.64         0.610          pass              0.528             22.3                           0.254                0.82              0.168                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                  detail
2026-05-21T11:10:05.158469-04:00 early_entry_1110           entry_skipped                                                                                                                                                                                                                                              {"reason": "no_candidate"}
2026-05-21T11:05:03.180136-04:00 early_entry_1105           entry_skipped                                                                                                                                                                                                                                              {"reason": "no_candidate"}
2026-05-21T11:00:05.229849-04:00 early_entry_1100           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T11:00:05.229849-04:00 early_entry_1100 entry_candidate_skipped                               {"early_entry_score": 0.714, "option_liquidity_status": "low_volume", "option_open_interest": 225.0, "option_spread_pct": 5.21, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ALNY", "timing_score": 0.393}
2026-05-21T10:55:01.033633-04:00 early_entry_1055           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:55:01.033633-04:00 early_entry_1055 entry_candidate_skipped                               {"early_entry_score": 0.684, "option_liquidity_status": "low_volume", "option_open_interest": 225.0, "option_spread_pct": 7.41, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ALNY", "timing_score": 0.396}
2026-05-21T10:55:01.033633-04:00 early_entry_1055 entry_candidate_skipped {"early_entry_score": 0.764, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 81.0, "option_spread_pct": 24.56, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "FAST", "timing_score": 0.481}
2026-05-21T10:50:06.054603-04:00 early_entry_1050           entry_skipped                                                                                                                                                                                                                                              {"reason": "no_candidate"}
2026-05-21T10:45:05.191060-04:00 early_entry_1045           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:45:05.191060-04:00 early_entry_1045 entry_candidate_skipped               {"early_entry_score": 0.778, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 29.0, "option_spread_pct": 9.05, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ADP", "timing_score": 0.528}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260521111005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260521111005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260521111005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260521111005)

</details>

# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-21 10:35:05 EDT`
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
  INTC           93.75               16            3.50              2.91        117.71               113.85         0.684          pass              0.559             28.2                           0.290                4.73             -0.681                      ok            True                  False
  FTNT          100.00               19            1.72              1.57        129.33                70.74         0.676          pass              0.584             18.9                           0.178               18.33              1.744                      ok            True                  False
  SBUX           92.31               13            1.35              1.01        106.07                31.64         0.591          pass              0.540             44.1                           0.528                1.36              0.193                      ok            True                  False
  MNST           81.48               27            0.98              0.60         86.62                49.77         0.554          pass              0.451             80.8                           0.423               13.24              0.656                      ok            True                  False
   ADP           93.94               33            0.58              0.90        220.31                38.26         0.531          pass              0.784             68.6                           0.716                2.48              0.452                      ok            True                   True
    ZS           82.35               17            2.42              2.96        173.18                63.59         0.524          pass              0.225             21.0                           0.284               11.41              1.808                      ok            True                  False
   TXN           91.67               12            2.01              4.30        303.04                69.08         0.523          pass              0.409             10.7                           0.190                4.73              0.484                      ok            True                  False
  NVDA           81.25               16            2.16              3.37        222.02                44.60         0.520          pass              0.164             13.0                           0.237                3.38              0.313                      ok            True                  False
  ISRG           84.62               13            2.31              7.27        445.91                35.82         0.508          pass              0.266             24.2                           0.354               -3.27             -0.014                      ok            True                  False
  AVGO           91.67               36            0.61              1.77        417.00                40.33         0.505          pass              0.673             46.2                           0.252                0.65             -0.164                      ok            True                  False
  SOXL           83.87               31            0.20              0.24        173.10               145.82         0.803          pass              0.605             93.9                           0.461               13.65             -0.451                      ok           False                  False
  CHTR           88.37               43            0.35              0.36        144.46               113.96         0.762          pass              0.744             81.5                           0.663              -10.07             -0.933 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                    detail
2026-05-21T10:35:05.061516-04:00 early_entry_1035           entry_skipped                                                                                                                                                                                                    {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:35:05.061516-04:00 early_entry_1035 entry_candidate_skipped     {"early_entry_score": 0.694, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 493.0, "option_spread_pct": 19.05, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "MAR", "timing_score": 0.414}
2026-05-21T10:35:05.061516-04:00 early_entry_1035 entry_candidate_skipped {"early_entry_score": 0.784, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 29.0, "option_spread_pct": 13.9, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ADP", "timing_score": 0.531}
2026-05-21T10:30:05.185385-04:00 early_entry_1030           entry_skipped                                                                                                                                                                                                    {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:30:05.185385-04:00 early_entry_1030 entry_candidate_skipped     {"early_entry_score": 0.694, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 493.0, "option_spread_pct": 19.05, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "MAR", "timing_score": 0.407}
2026-05-21T10:25:06.196092-04:00 early_entry_1025           entry_skipped                                                                                                                                                                                                    {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:25:06.196092-04:00 early_entry_1025 entry_candidate_skipped     {"early_entry_score": 0.689, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 493.0, "option_spread_pct": 20.94, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "MAR", "timing_score": 0.405}
2026-05-21T10:25:06.196092-04:00 early_entry_1025 entry_candidate_skipped    {"early_entry_score": 0.717, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 225.0, "option_spread_pct": 22.22, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ALNY", "timing_score": 0.395}
2026-05-21T10:20:05.205283-04:00 early_entry_1020           entry_skipped                                                                                                                                                                                                    {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:20:05.205283-04:00 early_entry_1020 entry_candidate_skipped   {"early_entry_score": 0.687, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 1903.0, "option_spread_pct": 32.26, "option_volume": 14.0, "reason": "no_trade_low_option_liquidity", "ticker": "KDP", "timing_score": 0.459}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260521103505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260521103505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260521103505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260521103505)

</details>

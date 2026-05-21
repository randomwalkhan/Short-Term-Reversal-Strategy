# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-21 11:35:02 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  SOXL           80.77               26            1.72              2.09        172.31               145.82         0.753            pass              0.343             46.7                           0.412               11.91             -0.521                      ok            True                  False
  INTC           95.24               21            2.43              2.02        118.09               113.85         0.714            pass              0.695             50.1                           0.703                5.88             -0.631                      ok            True                  False
  FTNT          100.00               23            1.59              1.45        129.38                70.74         0.659            pass              0.628             25.2                           0.194               18.49              1.750                      ok            True                  False
  SBUX          100.00               10            1.59              1.18        105.99                31.64         0.607            pass              0.564             34.4                           0.443                1.12              0.182                      ok            True                  False
  PAYX           94.44               18            0.75              0.50         94.71                29.35         0.557            pass              0.696             67.1                           0.460                1.23              0.247                      ok            True                  False
  MNST           81.48               27            1.04              0.63         86.61                49.77         0.551            pass              0.447             79.8                           0.568               13.18              0.653                      ok            True                  False
  FAST           94.44               18            1.19              0.36         43.52                21.35         0.527            pass              0.589             32.5                           0.214               -2.71             -0.131                      ok            True                  False
  NVDA           82.35               17            2.05              3.20        222.10                44.60         0.522            pass              0.214             17.5                           0.277                3.50              0.319                      ok            True                  False
  MDLZ           85.71               21            0.97              0.42         61.66                21.23         0.500 below_threshold              0.384             36.2                           0.347               -0.11             -0.011                      ok            True                  False
  CHTR           90.00               40            0.66              0.67        144.32               113.96         0.764            pass              0.739             65.3                           0.384              -10.35             -0.947 downtrend_blocked_slope           False                  False
  NXPI           83.33                6            3.83              8.32        306.58                91.65         0.681            pass              0.175              6.2                           0.170                2.77              0.166                      ok           False                  False
 CMCSA           86.67               30            0.50              0.09         24.84                59.59         0.621            pass              0.556             60.9                           0.579               -5.66             -0.370 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                    detail
2026-05-21T11:35:02.090762-04:00 early_entry_1135           entry_skipped                                                                                                                                                                                                                                {"reason": "no_candidate"}
2026-05-21T11:30:02.245220-04:00 early_entry_1130           entry_skipped                                                                                                                                                                                                                                {"reason": "no_candidate"}
2026-05-21T11:25:04.201711-04:00 early_entry_1125           entry_skipped                                                                                                                                                                                                    {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T11:25:04.201711-04:00 early_entry_1125 entry_candidate_skipped {"early_entry_score": 0.804, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 29.0, "option_spread_pct": 6.12, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ADP", "timing_score": 0.527}
2026-05-21T11:20:02.110689-04:00 early_entry_1120           entry_skipped                                                                                                                                                                                                                                {"reason": "no_candidate"}
2026-05-21T11:15:01.031462-04:00 early_entry_1115           entry_skipped                                                                                                                                                                                                    {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T11:15:01.031462-04:00 early_entry_1115 entry_candidate_skipped                 {"early_entry_score": 0.713, "option_liquidity_status": "low_volume", "option_open_interest": 225.0, "option_spread_pct": 6.82, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ALNY", "timing_score": 0.393}
2026-05-21T11:10:05.158469-04:00 early_entry_1110           entry_skipped                                                                                                                                                                                                                                {"reason": "no_candidate"}
2026-05-21T11:05:03.180136-04:00 early_entry_1105           entry_skipped                                                                                                                                                                                                                                {"reason": "no_candidate"}
2026-05-21T11:00:05.229849-04:00 early_entry_1100           entry_skipped                                                                                                                                                                                                    {"reason": "no_trade_after_option_and_timing_filters"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260521113502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260521113502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260521113502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260521113502)

</details>

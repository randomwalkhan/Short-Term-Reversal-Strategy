# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-03 10:25:05 EDT`
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

- Cash: `$34,571.75`
- Equity: `$34,571.75`
- Realized PnL: `$24,571.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-03)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   TXN     option         option TXN260717C00310000      8          2026-06-03         2026-06-03         22.0        19.8 -1760.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
    MU           81.82               33            0.52              3.84       1062.45               101.17         0.724            pass              0.510             78.6                           0.813               51.50              4.580                      ok            True                  False
  CSCO           95.65               23            0.97              0.87        127.63                53.71         0.624            pass              0.744             65.1                           0.715                9.86              0.911                      ok            True                  False
  MELI           93.55               31            1.14             13.37       1667.10                61.01         0.602            pass              0.681             39.9                           0.603                3.69              0.357                      ok            True                  False
  FTNT          100.00               35            0.96              1.00        148.43                71.83         0.582            pass              0.852             75.7                           0.835               15.51              1.522                      ok            True                   True
  MCHP          100.00               22            1.28              0.87         96.59                44.80         0.530            pass              0.707             58.0                           0.555                4.78              0.373                      ok            True                  False
   ROP           86.67               15            1.88              4.44        334.60                35.89         0.523            pass              0.325             20.6                           0.297                0.38              0.320                      ok            True                  False
  WDAY           84.38               32            1.81              1.88        148.07                75.59         0.521            pass              0.477             53.9                           0.821               13.03              2.124                      ok            True                  False
  CRWD           82.35               17            2.03             10.95        764.26                51.19         0.514            pass              0.286             41.7                           0.718               22.12              2.206                      ok            True                  False
  UPRO           92.31               26            1.25              1.32        150.30                28.22         0.507            pass              0.586             33.6                           0.422                9.03              0.897                      ok            True                  False
  CDNS           88.89               18            2.07              6.02        413.81                43.85         0.501            pass              0.470             43.2                           0.719               20.61              1.855                      ok            True                  False
   ADP           94.12               17            1.92              3.11        229.85                34.09         0.500 below_threshold              0.558             28.2                           0.311                2.86              0.439                      ok            True                  False
    ZS           60.00                5            5.76              5.82        141.66               159.87         0.737            pass              0.093              6.5                           0.194              -22.49             -2.910 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-06-03T10:25:05.972496-04:00 early_entry_1025           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-06-03T10:20:06.156013-04:00 early_entry_1020           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-06-03T10:20:06.156013-04:00      manage_1030                    exit                                                                                                                                                                                                                                                   {"asset_type": "option", "contract_symbol": "TXN260717C00310000", "fill_price": 19.8, "pnl": -1760.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "TXN"}
2026-06-03T10:15:06.039702-04:00 early_entry_1015                   entry {"allocated_cash": 17600.0, "asset_type": "option", "contract_symbol": "TXN260717C00310000", "contracts": 8, "early_entry_score": 0.813, "entry_mode": "early", "entry_option_price": 22.0, "execution_mode": "option", "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 1851.0, "option_spread_pct": 10.0, "option_volume": 30.0, "success_rate": 100.0, "ticker": "TXN", "timing_score": 0.547}
2026-06-03T10:15:06.039702-04:00 early_entry_1015 entry_candidate_skipped                                                                                                                                                                          {"early_entry_score": 0.885, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 771.0, "option_spread_pct": 18.79, "option_volume": 13.0, "reason": "no_trade_low_option_liquidity", "ticker": "FTNT", "timing_score": 0.573}
2026-06-03T10:10:05.039776-04:00 early_entry_1010           entry_skipped                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_trade_after_option_and_timing_filters"}
2026-06-03T10:10:05.039776-04:00 early_entry_1010 entry_candidate_skipped                                                                                                                                                                           {"early_entry_score": 0.848, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 383.0, "option_spread_pct": 21.64, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "FTNT", "timing_score": 0.579}
2026-06-03T10:05:03.196018-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate"}
2026-06-03T10:00:06.995022-04:00 early_entry_1000           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate"}
2026-06-03T09:20:04.119925-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                    {'saved': 92}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260603102505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260603102505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260603102505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260603102505)

</details>

# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-03 10:40:06 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  CSCO           96.15               26            0.70              0.62        127.73                53.71         0.622          pass              0.793             74.9                           0.763               10.16              0.924                      ok            True                  False
  MELI           94.29               35            0.98             11.45       1667.92                61.01         0.586          pass              0.752             48.5                           0.652                3.86              0.364                      ok            True                  False
  FTNT          100.00               35            0.98              1.02        148.42                71.83         0.580          pass              0.850             75.1                           0.650               15.48              1.521                      ok            True                   True
   CEG           80.00               30            1.00              1.90        271.83                55.62         0.539          pass              0.352             55.0                           0.681                3.55             -0.240                      ok            True                  False
  MCHP           96.00               25            0.97              0.66         96.68                44.80         0.525          pass              0.757             68.1                           0.618                5.11              0.387                      ok            True                  False
  CDNS           93.75               16            2.13              6.21        413.73                43.85         0.516          pass              0.583             41.4                           0.657               20.53              1.852                      ok            True                  False
  WDAY           80.77               26            2.48              2.58        147.77                75.59         0.513          pass              0.289             36.8                           0.514               12.25              2.092                      ok            True                  False
   ADP          100.00               15            2.10              3.39        229.73                34.09         0.509          pass              0.549             21.5                           0.355                2.67              0.431                      ok            True                  False
  CRWD           82.35               17            2.17             11.69        763.94                51.19         0.505          pass              0.273             37.8                           0.456               21.94              2.200                      ok            True                  False
  UPRO           92.86               28            1.11              1.17        150.37                28.22         0.503          pass              0.637             41.3                           0.477                9.19              0.903                      ok            True                  False
    ZS           60.00                5            5.90              5.95        141.60               159.87         0.727          pass              0.098              8.6                           0.202              -22.60             -2.916 downtrend_blocked_slope           False                  False
  INTU           70.59               17            3.48              7.84        318.78               101.75         0.632          pass              0.125              5.0                           0.237              -22.21             -1.303 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-06-03T10:40:06.216111-04:00 early_entry_1040           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-06-03T10:35:05.540454-04:00 early_entry_1035           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-06-03T10:30:02.209101-04:00 early_entry_1030           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-06-03T10:25:05.972496-04:00 early_entry_1025           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-06-03T10:20:06.156013-04:00 early_entry_1020           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-06-03T10:20:06.156013-04:00      manage_1030                    exit                                                                                                                                                                                                                                                   {"asset_type": "option", "contract_symbol": "TXN260717C00310000", "fill_price": 19.8, "pnl": -1760.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "TXN"}
2026-06-03T10:15:06.039702-04:00 early_entry_1015                   entry {"allocated_cash": 17600.0, "asset_type": "option", "contract_symbol": "TXN260717C00310000", "contracts": 8, "early_entry_score": 0.813, "entry_mode": "early", "entry_option_price": 22.0, "execution_mode": "option", "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 1851.0, "option_spread_pct": 10.0, "option_volume": 30.0, "success_rate": 100.0, "ticker": "TXN", "timing_score": 0.547}
2026-06-03T10:15:06.039702-04:00 early_entry_1015 entry_candidate_skipped                                                                                                                                                                          {"early_entry_score": 0.885, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 771.0, "option_spread_pct": 18.79, "option_volume": 13.0, "reason": "no_trade_low_option_liquidity", "ticker": "FTNT", "timing_score": 0.573}
2026-06-03T10:10:05.039776-04:00 early_entry_1010           entry_skipped                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_trade_after_option_and_timing_filters"}
2026-06-03T10:10:05.039776-04:00 early_entry_1010 entry_candidate_skipped                                                                                                                                                                           {"early_entry_score": 0.848, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 383.0, "option_spread_pct": 21.64, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "FTNT", "timing_score": 0.579}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260603104006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260603104006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260603104006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260603104006)

</details>

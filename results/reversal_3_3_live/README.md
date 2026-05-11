# Reversal 3.4.1 Live Paper Test

Latest checkpoint (ET): `2026-05-11 09:34:29 EDT`
Last processed slot: `manage_0930`

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
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$32,833.50`
- Equity: `$32,833.50`
- Realized PnL: `$22,833.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-11)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  GOOG           85.00               20            1.43              3.98        395.35                37.66         0.571          pass              0.353             31.9                           0.432               12.29              1.429                      ok            True                  False
   WMT           88.24               17            1.09              0.99        130.00                19.38         0.532          pass              0.341              7.2                           0.246                1.31              0.161                      ok            True                  False
  MSTR           90.62               32            2.36              3.09        186.26                70.10         0.526          pass              0.510              9.1                           0.270                8.26              1.431                      ok            True                  False
  TMUS           85.29               34            0.64              0.87        193.26                36.59         0.522          pass              0.479             41.8                           0.420                5.27              0.281                      ok            True                  False
  FAST           96.00               25            0.91              0.28         44.05                33.60         0.509          pass              0.661             36.8                           0.401               -2.82             -0.152                      ok            True                  False
  ASML           81.82               22            2.28             25.46       1581.11                48.89         0.508          pass              0.259             26.6                           0.473                8.60              1.252                      ok            True                  False
  MDLZ           84.00               25            0.65              0.28         61.43                24.76         0.502          pass              0.481             74.8                           0.562                6.50              0.493                      ok            True                  False
  CHTR           87.50               24            1.85              2.00        154.00               119.48         0.802          pass              0.374              0.0                           0.203              -12.95             -1.181 downtrend_blocked_slope           False                  False
  TEAM           89.36               47            0.21              0.14         91.54               114.36         0.695          pass              0.804             95.1                           0.652               32.05              3.498                      ok           False                  False
  SHOP           85.71               21            2.84              2.19        109.56                82.28         0.611          pass              0.359             24.2                           0.191              -13.57             -1.658 downtrend_blocked_slope           False                  False
  FTNT           95.74               47            0.25              0.20        113.99                70.49         0.578          pass              0.927             89.8                           0.738               32.82              3.101                      ok           False                  False
  GEHC           76.19               42            0.32              0.14         63.41                57.03         0.573          pass              0.459             67.2                           0.376              -10.23             -0.657                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                                                 detail
2026-05-11T09:18:42.943466-04:00 data_refresh data_refresh                                                                                                                                                                          {'saved': 92}
2026-05-08T16:05:06.142170-04:00  manage_1600         exit {"asset_type": "option", "contract_symbol": "TEAM260618C00090000", "fill_price": 9.25, "pnl": 2850.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 19.35, "ticker": "TEAM"}
2026-05-08T16:00:06.094263-04:00  manage_1600 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-08T15:55:02.084715-04:00  manage_1600 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-08T15:40:02.063692-04:00  manage_1530 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-08T15:35:05.923584-04:00  manage_1530 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-08T15:30:06.082521-04:00  manage_1530 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-08T15:25:06.105856-04:00  manage_1530 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-08T15:10:02.102478-04:00   entry_1500 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-08T15:05:03.959571-04:00   entry_1500 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260511093429)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260511093429)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260511093429)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260511093429)

</details>

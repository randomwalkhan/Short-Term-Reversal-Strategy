# Reversal 3.4.1 Live Paper Test

Latest checkpoint (ET): `2026-05-11 09:53:16 EDT`
Last processed slot: `manage_1000`

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
  TEAM           85.29               34            2.15              1.38         91.01               114.36         0.660          pass              0.518             50.4                           0.339               29.49              3.409                      ok            True                  False
  MSTR           89.74               39            0.64              0.84        187.23                70.10         0.574          pass              0.742             77.3                           0.600               10.16              1.510                      ok            True                   True
  GOOG           85.19               27            1.02              2.84        395.83                37.66         0.552          pass              0.461             51.3                           0.636               12.76              1.448                      ok            True                  False
   ADP           89.47               19            1.19              1.77        212.23                34.95         0.544          pass              0.487             39.9                           0.260                6.71              0.470                      ok            True                  False
  TMUS           84.62               26            1.16              1.57        192.96                36.59         0.536          pass              0.336             17.5                           0.221                4.73              0.257                      ok            True                  False
    ZS           83.72               43            0.56              0.60        151.87                58.64         0.527          pass              0.532             60.1                           0.519               12.80              1.416                      ok            True                  False
  FAST           92.86               14            1.63              0.50         43.95                33.60         0.527          pass              0.426              1.4                           0.076               -3.53             -0.186                      ok            True                  False
  MRVL          100.00               23            2.09              2.48        169.07                55.66         0.516          pass              0.701             54.1                           0.777                5.29              0.770                      ok            True                  False
  ASML           84.62               13            3.15             35.05       1577.00                48.89         0.516          pass              0.213              6.1                           0.175                7.64              1.211                      ok            True                  False
   WMT           86.96               23            0.85              0.78        130.10                19.38         0.506          pass              0.426             34.3                           0.301                1.55              0.172                      ok            True                  False
  CHTR           70.00               10            3.40              3.69        153.28               119.48         0.762          pass              0.102              8.5                           0.182              -14.33             -1.253 downtrend_blocked_slope           False                  False
  NXPI           82.50               40            0.05              0.10        294.71                87.07         0.713          pass              0.626             96.0                           0.602               24.37              1.948                      ok           False                  False
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

![Reversal 3.4.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260511095316)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260511095316)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260511095316)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260511095316)

</details>

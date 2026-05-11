# Reversal 3.4.1 Live Paper Test

Latest checkpoint (ET): `2026-05-11 09:47:04 EDT`
Last processed slot: `manual`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  TEAM           86.49               37            1.63              1.04         91.15               114.36         0.672          pass              0.608             62.5                           0.478               30.18              3.433                  ok            True                  False
  MSTR           89.74               39            0.84              1.10        187.12                70.10         0.564          pass              0.720             70.3                           0.554                9.94              1.501                  ok            True                   True
  GOOG           83.33               24            1.14              3.16        395.70                37.66         0.560          pass              0.376             45.9                           0.543               12.63              1.443                  ok            True                  False
  TMUS           86.21               29            0.97              1.31        193.07                36.59         0.535          pass              0.382             12.0                           0.115                4.93              0.266                  ok            True                  False
  MRVL          100.00               23            1.75              2.08        169.24                55.66         0.534          pass              0.725             61.6                           0.796                5.65              0.786                  ok            True                  False
    ZS           82.93               41            0.62              0.66        151.85                58.64         0.534          pass              0.499             55.9                           0.534               12.74              1.414                  ok            True                  False
  FAST           93.33               15            1.49              0.46         43.97                33.60         0.530          pass              0.461              6.4                           0.244               -3.40             -0.179                  ok            True                  False
   ADP           92.00               25            0.89              1.33        212.42                34.95         0.529          pass              0.637             54.8                           0.341                7.03              0.484                  ok            True                  False
  ASML           84.62               13            3.20             35.71       1576.71                48.89         0.513          pass              0.207              4.3                           0.265                7.58              1.209                  ok            True                  False
  ROST           92.86               14            1.28              2.02        224.94                15.75         0.512          pass              0.485             21.3                           0.211               -1.43             -0.065                  ok            True                  False
  WDAY           85.71               35            1.53              1.37        127.24                62.51         0.505          pass              0.460             30.2                           0.266                6.82              0.693                  ok            True                  False
   WMT           86.96               23            0.90              0.83        130.08                19.38         0.503          pass              0.413             30.2                           0.261                1.49              0.169                  ok            True                  False
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

![Reversal 3.4.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260511094704)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260511094704)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260511094704)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260511094704)

</details>

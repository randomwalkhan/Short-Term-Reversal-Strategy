# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-16 10:10:05 EST`
Last processed slot: `manage_1000`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
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

- Cash: `$117,024.80`
- Equity: `$117,024.80`
- Realized PnL: `$107,024.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  QCOM           84.00               25            1.55              1.87        171.67                68.34         0.593          pass              0.387             40.3                           0.347                4.76              0.707                  ok            True                  False
  ISRG           90.62               32            0.79              2.44        442.54                45.74         0.560          pass              0.607             40.4                           0.284                0.74             -0.274                  ok            True                  False
  AAPL           95.83               24            0.65              1.62        355.57                27.52         0.557          pass              0.635             28.6                           0.192                4.70              0.589                  ok            True                  False
   CEG           87.50               32            1.46              2.86        278.55                61.55         0.550          pass              0.514             37.3                           0.312                7.17              1.230                  ok            True                  False
  MSFT           96.77               31            0.67              2.44        522.83                36.51         0.536          pass              0.687             31.2                           0.256                2.62             -0.075                  ok            True                  False
  DXCM           82.05               39            0.69              0.40         83.16                50.11         0.522          pass              0.418             39.2                           0.303               -2.37             -0.406                  ok            True                  False
  ALNY           57.89               19            2.58              2.98        163.76               110.81         0.718          pass              0.155              7.6                           0.071                1.76              0.130                  ok           False                  False
  FTNT           76.00               25            2.14              1.91        126.40                93.31         0.677          pass              0.237             23.0                           0.244               -1.36              0.032                  ok           False                  False
  INTC           63.64               11            6.22              2.60         58.55               143.21         0.665          pass              0.101              9.3                           0.182               -6.70              0.120                  ok           False                  False
  UPRO           80.00                5            3.85              3.73        136.90                68.17         0.586          pass              0.069              3.4                           0.127               -4.29             -0.145                  ok           False                  False
   ADI           83.33                6            3.73             10.40        393.51                66.18         0.572          pass              0.185             13.0                           0.209               -7.20             -0.215                  ok           False                  False
 GOOGL           60.00                5            3.04              6.29        293.08                54.19         0.567          pass              0.069              4.0                           0.164                2.80              0.492                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-11-16T10:10:05.371308-05:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:05:06.161722-05:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:00:04.523594-05:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T09:20:05.612126-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                             {'saved': 91, 'empty': 2}
2026-11-06T16:10:06.061391-05:00      manage_1600               exit                                                                                                                                                                                                                                                      {"asset_type": "option", "contract_symbol": "MDLZ261218C00065000", "fill_price": 2.79, "pnl": -6138.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MDLZ"}
2026-11-06T15:10:05.130683-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-11-06T15:05:05.959531-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-11-06T15:00:05.889317-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-11-06T14:55:04.803922-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-11-06T14:50:04.935495-05:00       entry_1500              entry {"allocated_cash": 61380.0, "asset_type": "option", "contract_symbol": "MDLZ261218C00065000", "contracts": 198, "early_entry_score": 0.675, "entry_mode": "regular", "entry_option_price": 3.1, "execution_mode": "option", "matched_signals": 15, "option_liquidity_status": "ok", "option_open_interest": 3966.0, "option_spread_pct": 6.45, "option_volume": 43.0, "success_rate": 93.33, "ticker": "MDLZ", "timing_score": 0.574}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261116101005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261116101005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261116101005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261116101005)

</details>

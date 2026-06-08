# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-08 12:50:01 EDT`
Last processed slot: `manage_1300`

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

- Cash: `$31,794.75`
- Equity: `$31,794.75`
- Realized PnL: `$21,794.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-08)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TEAM     option         option TEAM260717C00100000     16          2026-06-05         2026-06-08         9.85       8.865 -1576.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  TEAM           94.12               34            1.52              1.06         99.02                86.36         0.631          pass              0.764             54.8                           0.444               14.67              1.812                      ok            True                  False
  PAYX          100.00               11            1.37              0.97        100.12                33.39         0.612          pass              0.557             29.6                           0.254                2.22              0.539                      ok            True                  False
  CRWD           80.00               15            2.35             11.04        666.29                64.90         0.580          pass              0.121              9.9                           0.252                1.08              0.930                      ok            True                  False
  ROST           93.33               30            0.83              1.34        229.80                43.36         0.578          pass              0.592             15.1                           0.222               -2.70             -0.153                      ok            True                  False
  PANW           85.00               20            2.02              3.84        270.40                60.15         0.569          pass              0.341             28.0                           0.294                5.39              1.172                      ok            True                  False
  AMGN           90.00               10            1.24              3.04        348.28                22.27         0.537          pass              0.536             71.7                           0.397                1.75              0.300                      ok            True                  False
  FAST           93.75               16            1.36              0.44         46.60                21.36         0.534          pass              0.501             13.7                           0.186                5.04              0.676                      ok            True                  False
   ADP           96.00               25            1.09              1.77        231.19                32.55         0.521          pass              0.676             41.5                           0.327                1.83              0.591                      ok            True                  False
  CTAS           82.35               17            1.63              2.05        178.97                23.69         0.511          pass              0.183              7.4                           0.212                2.31              0.506                      ok            True                  False
  WDAY           89.19               37            0.87              0.88        143.90                69.97         0.503          pass              0.655             59.8                           0.483               11.62              1.865                      ok            True                  False
    ZS           82.35               34            0.99              0.90        130.39               157.69         0.895          pass              0.485             57.6                           0.458              -29.00             -2.402 downtrend_blocked_slope           False                  False
   TRI           76.92               13            2.52              1.52         85.39                69.04         0.618          pass              0.118             12.1                           0.217               -2.32              0.121                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          detail
2026-06-08T12:35:06.508215-04:00      manage_1230               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"asset_type": "option", "contract_symbol": "TEAM260717C00100000", "fill_price": 8.865, "pnl": -1576.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "TEAM"}
2026-06-08T12:00:05.977560-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:55:06.347594-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:50:04.863668-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:45:02.732022-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:40:03.636153-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:35:06.615496-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:30:04.779379-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:25:01.866024-04:00 early_entry_1125 early_entry_shadow {"contract_symbol": "ADP260717C00230000", "current_drop_pct": 0.52, "early_entry_score": 0.838, "early_reclaim_pct": 72.0, "entry_ask": 9.7, "entry_bid": 7.9, "entry_mode": "early", "entry_option_price": 8.8, "hypothetical_budget": 8805.38, "hypothetical_contracts": 10, "matched_signals": 36, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 263.0, "option_spread_pct": 20.45, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.609, "shadow_only": true, "success_rate": 97.22, "ticker": "ADP", "timing_score": 0.485, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.838, "early_reclaim_pct": 72.0, "matched_signals": 36, "recovery_stability_score": 0.609, "success_rate": 97.22, "ticker": "ADP", "timing_score": 0.485, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-08T11:20:06.683285-04:00 early_entry_1120 early_entry_shadow                           {"contract_symbol": "PANW260717C00270000", "current_drop_pct": 0.8, "early_entry_score": 0.753, "early_reclaim_pct": 71.4, "entry_ask": 18.45, "entry_bid": 17.55, "entry_mode": "early", "entry_option_price": 18.0, "hypothetical_budget": 8805.38, "hypothetical_contracts": 4, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1193.0, "option_spread_pct": 5.0, "option_volume": 196.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.644, "shadow_only": true, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.549, "top_candidates": [{"current_drop_pct": 0.8, "early_entry_score": 0.753, "early_reclaim_pct": 71.4, "matched_signals": 36, "recovery_stability_score": 0.644, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.549, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260608125001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260608125001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260608125001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260608125001)

</details>

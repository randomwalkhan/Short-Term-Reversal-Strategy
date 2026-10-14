# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-14 12:05:06 EDT`
Last processed slot: `manage_1200`

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

- Cash: `$135,462.30`
- Equity: `$135,462.30`
- Realized PnL: `$125,462.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-14)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SNPS     option         option SNPS261120C00500000     28          2026-10-13         2026-10-14         25.4       22.86 -7112.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    ZS           92.59               27            1.96              3.14        227.32                58.33         0.516          pass              0.613             37.4                           0.479               12.42              1.705                                 ok            True                  False
  MSFT          100.00               20            1.22              4.63        541.46                20.68         0.507          pass              0.527              3.1                           0.114                4.67              0.562                                 ok            True                  False
  SNPS           78.57               14            2.05              7.08        491.47                50.26         0.582          pass              0.191             35.3                           0.544               11.37              0.653                                 ok           False                  False
  META           57.14                7            3.23             17.26        755.10                53.30         0.548          pass              0.059              1.3                           0.122                1.75              0.232                                 ok           False                  False
  QCOM           82.35               17            2.57              3.18        175.50                53.60         0.546          pass              0.190              8.8                           0.222               -6.37             -0.643 downtrend_blocked_slope_and_streak           False                  False
  MELI           70.00               10            2.44             31.99       1862.33                40.00         0.538          pass              0.080              8.7                           0.289                5.89              0.976                                 ok           False                  False
  CSCO           93.10               29            0.29              0.23        114.97                34.22         0.537          pass              0.703             57.7                           0.274                7.02              0.667                                 ok           False                  False
   STX           81.48               27            2.47             12.91        741.67                68.64         0.531          pass              0.242             11.9                           0.221              -20.99             -2.516            downtrend_blocked_slope           False                  False
  SHOP           77.78               18            2.20              2.72        175.35                46.81         0.529          pass              0.133              9.0                           0.178               16.41              1.884                                 ok           False                  False
  UPRO          100.00                4            2.87              3.12        154.06                28.27         0.527          pass              0.463              3.5                           0.156                2.70              0.389                                 ok           False                  False
  INTC           85.71               14            3.81              2.74        101.63                67.54         0.525          pass              0.233              0.4                           0.062              -17.75             -2.130 downtrend_blocked_slope_and_streak           False                  False
  MSTR           90.00               10            4.90              5.22        149.94                75.74         0.517          pass              0.333              5.0                           0.185               -5.46             -0.767            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-10-14T12:00:05.972511-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T11:55:04.759815-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "PYPL261120C00055000", "current_drop_pct": 0.51, "early_entry_score": 0.838, "early_reclaim_pct": 64.2, "entry_ask": 3.65, "entry_bid": 3.5, "entry_mode": "early", "entry_option_price": 3.575, "hypothetical_budget": 67731.15, "hypothetical_contracts": 189, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 9142.0, "option_spread_pct": 4.2, "option_volume": 152.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.597, "shadow_only": true, "success_rate": 95.0, "ticker": "PYPL", "timing_score": 0.452, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.838, "early_reclaim_pct": 64.2, "matched_signals": 40, "recovery_stability_score": 0.597, "success_rate": 95.0, "ticker": "PYPL", "timing_score": 0.452, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-14T11:50:06.783855-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T11:45:05.905160-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T11:40:06.200879-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T11:35:06.945849-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T11:30:04.983465-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T11:25:02.806640-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T11:20:05.902505-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T11:15:04.975938-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261014120506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261014120506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261014120506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261014120506)

</details>

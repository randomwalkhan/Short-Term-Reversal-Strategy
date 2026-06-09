# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-09 10:50:06 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$30,222.25`
- Equity: `$30,222.25`
- Realized PnL: `$20,222.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-09)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TEAM     option         option TEAM260717C00100000     17          2026-06-08         2026-06-09         9.25       8.325 -1572.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  DRAM          100.00               15            1.47              0.62         60.25               103.58         0.777          pass              0.521              3.3                           0.090               -1.45             -0.299                                 ok            True                  False
    MU           80.00               25            2.26             15.04        942.83               111.98         0.670          pass              0.207             13.4                           0.232                3.56              0.142                                 ok            True                  False
  PAYX          100.00               17            0.77              0.54         98.69                34.09         0.639          pass              0.672             53.9                           0.318                3.54              0.477                                 ok            True                  False
  TEAM           93.75               32            1.76              1.21         97.37                87.01         0.613          pass              0.710             45.1                           0.288               13.24              0.857                                 ok            True                  False
  PANW           82.35               17            2.22              4.14        264.56                58.75         0.595          pass              0.225             18.5                           0.214                1.43              0.385                                 ok            True                  False
  CDNS           93.33               30            1.08              2.98        392.96                58.79         0.560          pass              0.586             13.6                           0.209                2.16              0.462                                 ok            True                  False
   WMT           86.67               30            0.71              0.59        119.58                36.35         0.536          pass              0.491             42.2                           0.465                0.35              0.104                                 ok            True                  False
   WDC          100.00               19            3.16             11.64        521.94                73.41         0.518          pass              0.536              8.0                           0.181               -2.71             -0.028                                 ok            True                  False
    ZS           71.43               14            3.44              3.11        127.92               157.94         0.867          pass              0.129              5.1                           0.165              -32.39             -1.876            downtrend_blocked_slope           False                  False
  INTU           76.19               21            2.23              4.77        303.47               100.92         0.719          pass              0.204             19.7                           0.131               -1.86             -0.542 downtrend_blocked_slope_and_streak           False                  False
   TRI           88.89               27            0.32              0.19         83.10                69.62         0.697          pass              0.656             78.7                           0.362               -0.97             -0.074                                 ok           False                  False
  CSCO          100.00                3            3.02              2.62        123.03                58.94         0.661          pass              0.466              0.0                           0.083                1.75              0.458                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-06-09T10:50:06.282559-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:45:01.973366-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:40:03.961827-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:35:06.798530-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:30:02.001966-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:25:06.878160-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:20:02.039126-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:15:04.004316-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:10:02.035934-04:00 early_entry_1010 early_entry_shadow   {"contract_symbol": "PANW260717C00270000", "current_drop_pct": 0.7, "early_entry_score": 0.753, "early_reclaim_pct": 74.4, "entry_ask": 13.8, "entry_bid": 12.25, "entry_mode": "early", "entry_option_price": 13.025, "hypothetical_budget": 15111.13, "hypothetical_contracts": 11, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 1240.0, "option_spread_pct": 11.9, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.722, "shadow_only": true, "success_rate": 91.43, "ticker": "PANW", "timing_score": 0.581, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.753, "early_reclaim_pct": 74.4, "matched_signals": 35, "recovery_stability_score": 0.722, "success_rate": 91.43, "ticker": "PANW", "timing_score": 0.581, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-09T10:05:03.054973-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "PANW260717C00270000", "current_drop_pct": 0.65, "early_entry_score": 0.782, "early_reclaim_pct": 76.0, "entry_ask": 14.25, "entry_bid": 12.65, "entry_mode": "early", "entry_option_price": 13.45, "hypothetical_budget": 15111.13, "hypothetical_contracts": 11, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 1240.0, "option_spread_pct": 11.9, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.761, "shadow_only": true, "success_rate": 91.89, "ticker": "PANW", "timing_score": 0.571, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.782, "early_reclaim_pct": 76.0, "matched_signals": 37, "recovery_stability_score": 0.761, "success_rate": 91.89, "ticker": "PANW", "timing_score": 0.571, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260609105006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260609105006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260609105006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260609105006)

</details>

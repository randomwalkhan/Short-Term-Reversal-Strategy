# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-14 11:45:05 EDT`
Last processed slot: `early_entry_1145`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SHOP           80.95               21            1.75              2.17        175.59                46.81         0.539            pass              0.235             27.5                           0.319               16.94              1.904                                 ok            True                  False
    ZS           88.89               18            2.55              4.07        226.91                58.33         0.533            pass              0.400             18.7                           0.168               11.74              1.678                                 ok            True                  False
  MSFT          100.00               21            1.10              4.20        541.65                20.68         0.508            pass              0.550              8.7                           0.214                4.79              0.568                                 ok            True                  False
  SNPS           71.43                7            2.74              9.49        490.44                50.26         0.578            pass              0.098             13.2                           0.215               10.58              0.621                                 ok           False                  False
  META           55.56                9            2.92             15.56        755.83                53.30         0.554            pass              0.071              5.3                           0.176                2.08              0.247                                 ok           False                  False
  QCOM           80.95               21            2.35              2.90        175.62                53.60         0.535            pass              0.190             12.4                           0.227               -6.16             -0.633 downtrend_blocked_slope_and_streak           False                  False
   STX           80.00               25            2.62             13.69        741.33                68.64         0.534            pass              0.170              5.4                           0.167              -21.11             -2.523            downtrend_blocked_slope           False                  False
  MELI           70.00               10            2.59             34.04       1861.45                40.00         0.529            pass              0.061              2.8                           0.242                5.72              0.969                                 ok           False                  False
  UPRO          100.00                4            2.89              3.14        154.05                28.27         0.526            pass              0.461              2.8                           0.220                2.68              0.388                                 ok           False                  False
  MSTR           91.67               12            4.61              4.91        150.08                75.74         0.524            pass              0.397              6.7                           0.198               -5.18             -0.754            downtrend_blocked_slope           False                  False
  INTC           80.95               21            3.18              2.29        101.83                67.54         0.516            pass              0.182             10.4                           0.235              -17.21             -2.100 downtrend_blocked_slope_and_streak           False                  False
  TEAM          100.00               36            1.08              1.57        207.37                43.11         0.492 below_threshold              0.702             26.6                           0.208               14.79              1.368                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-10-14T11:45:05.905160-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T11:40:06.200879-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T11:35:06.945849-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T11:30:04.983465-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T11:25:02.806640-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T11:20:05.902505-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T11:15:04.975938-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T11:10:06.114366-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T11:05:02.794451-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T11:00:06.016976-04:00 early_entry_1100 early_entry_shadow {"contract_symbol": "FAST261120C00050000", "current_drop_pct": 0.52, "early_entry_score": 0.882, "early_reclaim_pct": 93.6, "entry_ask": 2.0, "entry_bid": 1.6, "entry_mode": "early", "entry_option_price": 1.8, "hypothetical_budget": 67731.15, "hypothetical_contracts": 376, "matched_signals": 35, "option_liquidity_status": "wide_spread", "option_open_interest": 3538.0, "option_spread_pct": 22.22, "option_volume": 336.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.934, "shadow_only": true, "success_rate": 97.14, "ticker": "FAST", "timing_score": 0.343, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.882, "early_reclaim_pct": 93.6, "matched_signals": 35, "recovery_stability_score": 0.934, "success_rate": 97.14, "ticker": "FAST", "timing_score": 0.343, "trend_health_status": "ok"}, {"current_drop_pct": 1.13, "early_entry_score": 0.715, "early_reclaim_pct": 64.0, "matched_signals": 35, "recovery_stability_score": 0.731, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.514, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261014114505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261014114505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261014114505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261014114505)

</details>

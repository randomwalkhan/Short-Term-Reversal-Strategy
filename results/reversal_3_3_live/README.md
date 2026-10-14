# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-14 10:45:05 EDT`
Last processed slot: `early_entry_1045`

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
  SHOP           83.33               36            0.73              0.90        176.14                46.81         0.520          pass              0.451             45.8                           0.220               18.17              1.952                                 ok            True                  False
  MSFT           95.65               23            0.96              3.64        541.89                20.68         0.501          pass              0.560              7.6                           0.181                4.94              0.574                                 ok            True                  False
    ZS           91.43               35            1.36              2.18        227.72                58.33         0.500          pass              0.691             56.4                           0.621               13.10              1.733                                 ok            True                  False
  META           63.64               11            2.13             11.38        757.62                53.30         0.601          pass              0.106             13.1                           0.297                2.91              0.284                                 ok           False                  False
  SNPS           75.00               16            1.77              6.14        491.88                50.26         0.585          pass              0.191             30.9                           0.288               11.68              0.666                                 ok           False                  False
  QCOM           82.61               23            1.68              2.08        175.97                53.60         0.569          pass              0.283             23.3                           0.413               -5.52             -0.602 downtrend_blocked_slope_and_streak           False                  False
   STX           81.82               33            1.45              7.60        743.94                68.64         0.554          pass              0.400             47.5                           0.275              -20.17             -2.469            downtrend_blocked_slope           False                  False
  UPRO          100.00                8            2.18              2.37        154.38                28.27         0.549          pass              0.468              4.5                           0.135                3.43              0.421                                 ok           False                  False
 CMCSA           86.67               15            0.60              0.09         20.84                21.61         0.542          pass              0.426             53.7                           0.666               -3.14             -0.353            downtrend_blocked_slope           False                  False
  MSTR           91.67               12            4.46              4.76        150.14                75.74         0.532          pass              0.405              9.2                           0.225               -5.03             -0.747            downtrend_blocked_slope           False                  False
  INTC           85.71               28            2.27              1.63        102.11                67.54         0.530          pass              0.432             35.5                           0.472              -16.43             -2.058 downtrend_blocked_slope_and_streak           False                  False
   WDC           77.14               35            1.21              3.22        379.33                62.57         0.528          pass              0.406             62.3                           0.339              -17.24             -1.994            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-10-14T10:45:05.206630-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T10:40:06.159584-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T10:35:03.750968-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T10:30:05.874859-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T10:25:04.858915-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T10:20:06.339818-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T10:15:04.940444-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T10:10:06.594596-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T10:05:04.809604-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T10:00:05.984655-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "ZS261113C00225000", "current_drop_pct": 0.9, "early_entry_score": 0.75, "early_reclaim_pct": 71.2, "entry_ask": 15.55, "entry_bid": 12.5, "entry_mode": "early", "entry_option_price": 14.025, "hypothetical_budget": 67731.15, "hypothetical_contracts": 48, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 15.0, "option_spread_pct": 21.75, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.846, "shadow_only": true, "success_rate": 91.67, "ticker": "ZS", "timing_score": 0.521, "top_candidates": [{"current_drop_pct": 0.9, "early_entry_score": 0.75, "early_reclaim_pct": 71.2, "matched_signals": 36, "recovery_stability_score": 0.846, "success_rate": 91.67, "ticker": "ZS", "timing_score": 0.521, "trend_health_status": "ok"}, {"current_drop_pct": 1.22, "early_entry_score": 0.682, "early_reclaim_pct": 65.5, "matched_signals": 33, "recovery_stability_score": 0.807, "success_rate": 90.91, "ticker": "FTNT", "timing_score": 0.411, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261014104505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261014104505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261014104505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261014104505)

</details>

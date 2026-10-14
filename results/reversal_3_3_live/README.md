# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-14 10:25:04 EDT`
Last processed slot: `manage_1030`

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
  UPRO          100.00               10            2.05              2.23        154.44                28.27         0.546          pass              0.466              3.9                           0.096                3.57              0.427                                 ok            True                  False
    ZS           90.00               30            1.72              2.75        227.48                58.33         0.509          pass              0.586             45.2                           0.343               12.69              1.716                                 ok            True                  False
  PYPL           92.00               25            1.00              0.39         56.00                25.14         0.509          pass              0.560             29.6                           0.264                5.86              0.673                                 ok            True                  False
  MSFT           96.30               27            0.56              2.11        542.54                20.68         0.503          pass              0.662             32.7                           0.279                5.37              0.593                                 ok            True                  False
  TMUS           89.47               38            0.36              0.39        153.56                58.63         0.597          pass              0.699             66.7                           0.567               -6.08             -0.831            downtrend_blocked_slope           False                  False
  META           63.64               11            2.27             12.12        757.30                53.30         0.594          pass              0.077              3.8                           0.107                2.76              0.277                                 ok           False                  False
  SNPS           78.57               14            2.03              7.04        491.49                50.26         0.587          pass              0.131             15.1                           0.245               11.38              0.654                                 ok           False                  False
   STX           81.82               33            1.16              6.04        744.61                68.64         0.571          pass              0.434             58.2                           0.388              -19.92             -2.455            downtrend_blocked_slope           False                  False
  QCOM           81.82               22            2.09              2.59        175.75                53.60         0.550          pass              0.196              4.3                           0.132               -5.91             -0.621 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           88.89                9            1.08              0.16         20.81                21.61         0.549          pass              0.342             16.7                           0.274               -3.60             -0.375            downtrend_blocked_slope           False                  False
  MSTR           91.67               12            4.48              4.77        150.14                75.74         0.532          pass              0.402              8.0                           0.127               -5.05             -0.747            downtrend_blocked_slope           False                  False
  INTC           84.62               26            2.45              1.76        102.05                67.54         0.531          pass              0.374             30.4                           0.273              -16.58             -2.066 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-10-14T10:25:04.858915-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T10:20:06.339818-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T10:15:04.940444-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T10:10:06.594596-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T10:05:04.809604-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-14T10:00:05.984655-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "ZS261113C00225000", "current_drop_pct": 0.9, "early_entry_score": 0.75, "early_reclaim_pct": 71.2, "entry_ask": 15.55, "entry_bid": 12.5, "entry_mode": "early", "entry_option_price": 14.025, "hypothetical_budget": 67731.15, "hypothetical_contracts": 48, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 15.0, "option_spread_pct": 21.75, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.846, "shadow_only": true, "success_rate": 91.67, "ticker": "ZS", "timing_score": 0.521, "top_candidates": [{"current_drop_pct": 0.9, "early_entry_score": 0.75, "early_reclaim_pct": 71.2, "matched_signals": 36, "recovery_stability_score": 0.846, "success_rate": 91.67, "ticker": "ZS", "timing_score": 0.521, "trend_health_status": "ok"}, {"current_drop_pct": 1.22, "early_entry_score": 0.682, "early_reclaim_pct": 65.5, "matched_signals": 33, "recovery_stability_score": 0.807, "success_rate": 90.91, "ticker": "FTNT", "timing_score": 0.411, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-14T09:50:06.904742-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"asset_type": "option", "contract_symbol": "SNPS261120C00500000", "fill_price": 22.86, "pnl": -7112.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SNPS"}
2026-10-14T00:00:06.708726-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {'saved': 91, 'empty': 2}
2026-10-13T15:10:06.535380-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-10-13T15:05:06.894886-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261014102504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261014102504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261014102504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261014102504)

</details>
